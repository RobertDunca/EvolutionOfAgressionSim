from pprint import pprint
import random
import pandas as pd


class Food:
    def __init__(self):
        self.food_amount = 2
        self.creatures_eating = []


class Creature:
    def __init__(self):
        self.food_count = 0
        
    def choose_food(self, food):
        food.creatures_eating.append(self)
        
    def eat(self):
        pass


class Dove(Creature):
    def __init__(self):
        super().__init__()
 
    def eat(self, food):
        if len(food.creatures_eating) == 1:
            food.food_amount -= 2
            self.food_count += 2
        if len(food.creatures_eating) == 2:
            for creature in food.creatures_eating:
                if creature != self:
                    enemy = creature
            if isinstance(enemy, Dove):
                food.food_amount -= 1
                self.food_count += 1
            elif isinstance(enemy, Hawk):
                food.food_amount -= 0.5
                self.food_count += 0.5
            
    
class Hawk(Creature):
    def __init__(self):
        super().__init__()
    
    def eat(self, food):
        if len(food.creatures_eating) == 1:
            food.food_amount -= 2
            self.food_count += 2
        if len(food.creatures_eating) == 2:
            for creature in food.creatures_eating:
                if creature != self:
                    enemy = creature
            if isinstance(enemy, Dove):
                food.food_amount -= 1.5
                self.food_count += 1.5
            elif isinstance(enemy, Hawk):
                food.food_amount -= 1     
    
  
# CREATE CREATURE POPULATION AND FOOD OBJECTS  
  
def create_creatures(dove_number, hawk_number):
    doves = [Dove() for _ in range(dove_number)]
    hawks = [Hawk() for _ in range(hawk_number)]
    creatures = doves + hawks
    return creatures

def create_food(number):
    food = [Food() for _ in range(number)]  
    return food


# CREATURES EAT RANDOMLY CHOSEN FOOD OBJECTS

def assign_creature_to_food(num_of_doves, num_of_hawks, num_of_food):
    creatures = create_creatures(num_of_doves, num_of_hawks)
    all_food = create_food(num_of_food)
    chosen_food = []
    
    for creature in creatures:
        if not len(all_food):
            break
        food = random.choice(all_food)
        creature.choose_food(food)
        if len(food.creatures_eating) == 2:
            chosen_food.append(food)
            all_food.remove(food)
            
    for food in all_food:
        if len(food.creatures_eating):
            chosen_food.append(food)
            
    return chosen_food

def eat_food(num_of_doves, num_of_hawks, num_of_food):
    chosen_food = assign_creature_to_food(num_of_doves, num_of_hawks, num_of_food)
    creatures = []
    
    for food in chosen_food:
        for creature in food.creatures_eating:
            creature.eat(food)
            creatures.append(creature)
            
    return creatures


# LIVE/REPRODUCE AND SIMULATE THE NEXT GENERATION OF CREATURES

def simulate(generations, num_of_doves, num_of_hawks, num_of_food):
    
    generation_num = [1, ]
    doves = [num_of_doves, ]
    hawks = [num_of_hawks, ]
    
    for generation in range(generations):
        creatures = eat_food(num_of_doves, num_of_hawks, num_of_food)
        next_generation = []
        
        for creature in creatures:
            if isinstance(creature, Dove):
                if creature.food_count == 2:
                    next_generation.append(Dove())
                    next_generation.append(creature)
                elif creature.food_count == 1:
                    next_generation.append(creature)
                elif creature.food_count == 0.5:
                    chance = random.choice([0, 1])
                    if chance:
                        next_generation.append(creature)
            elif isinstance(creature, Hawk):
                if creature.food_count == 2:
                    next_generation.append(Hawk())
                    next_generation.append(creature)
                elif creature.food_count == 1:
                    next_generation.append(creature)
                elif creature.food_count == 1.5:
                    chance = random.choice([0, 1])
                    if chance:
                        next_generation.append(creature)
                        next_generation.append(Hawk())
                    else:
                        next_generation.append(creature)
        
        num_of_doves = len(list(filter(lambda d: isinstance(d, Dove), next_generation)))
        num_of_hawks = len(list(filter(lambda h: isinstance(h, Hawk), next_generation)))
        
        generation_num.append(generation + 2)
        doves.append(num_of_doves)
        hawks.append(num_of_hawks)
        
    data = transform_data(generation_num, doves, hawks)
        
    return data

# TRANSFORM DATA IN A PANDAS DATAFRAME

def transform_data(generation_num, doves, hawks):
    category = ['Dove'] * len(doves) + ['Hawk'] * len(hawks)
    population = doves + hawks
        
    data = pd.DataFrame({'Generation': (generation_num)*2, 
                            'Population': population,
                            'Type': category})
    
    return data

def main():
    simulation = simulate(50, 1, 50, 1000)
    return simulation
        
if __name__ == '__main__':
    main()
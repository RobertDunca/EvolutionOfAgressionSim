This project is simulating the evolution of aggression over multiple generations
- inspired by this YouTube video: https://www.youtube.com/watch?v=YNMkADpvO4w&ab_channel=Primer.

Population:
- the population is formed by two categories: doves and hawks;
- a certain number of doves and/or hawks is chosen at the start of every simulation;
- DOVES are peaceful and HAWKS are aggressive;
- each generation every creature choses a food randomly.

Food:
- at the start of every simulation a certain amount of food is chosen;
- the chosen amount of food remains the same throughout generations;
- every food comes in pairs and it's made of two pieces ;
- eating one piece of food allows a creature to survive to the next generation;
- eating 2 pieces of food allows the creature to survive an reproduce, meaning a new creature will be added to the simulation in the next generation.



Eating and reproducing:

DOVES:
- if a dove chooses a food and there is no other creature choosing the same food, the dove lives to the next generation and it reproduces, so a new dove is added;
- if 2 doves choose the same food, each dove eats one piece and the live to the next generation but they don't reproduce.

HAWKS:
- if a hawk chooses a food and there is no other creature choosing the same food, the hawk lives to the next generation and it reproduces, so a new hawk is added;
- if 2 hawks choose the same food, being aggressive they fight over the food and they also eat one piece of food each, like the doves, but because they fight for it they use all the energy given by the food and they don't live to the next generation.

DOVES and HAWKS:
- if a dove and a hawk choose the same food the hawk eats 1 piece and it also steals half (0,5) a piece from the dove, so the dove only eats half a piece of food;
- because the hawk has one and a half pieces of food it gets to live to the next generation AND it has a 50% chance of reproducing;
- but the dove only has half a piece of food so it only has 50% chance of living to the next generation.



RESULT:
- a population made only of doves which share everything seems to be the most advantageous, the population reaching a certain limit equal to double the amount of food after a few generations and stays there; 
- although hawks seem to have an advantage and being a hawk seems to be the better option, a population made only of hawks is not good overall, the population numbers being lower than half of what the amount of food could sustain;
- adding a single dove to the simulation in a population full of hawks will make the population size double over a few generations and the number of doves and hawks will fluctuate somewhere in the middle.
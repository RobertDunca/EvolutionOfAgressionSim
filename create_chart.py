import altair as alt
from sim import simulate

generations = int(input("How many GENERATIONS do you want the simulation to have? "))
doves = int(input("What should the DOVE population be? "))
hawks = int(input("What should the HAWK population be? "))
foods = int(input("How much FOOD do you want to create? "))

source = simulate(generations, doves, hawks, foods)

chart = alt.Chart(source).mark_area().encode(
    x="Generation:O",
    y="Population:Q",
    color="Type:N"
).properties(
    width=1200,
    height=600
)

chart.save('chart.html')

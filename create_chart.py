import altair as alt
from sim import simulate

generations = 100
doves = 1
hawks = 1
foods = 300

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

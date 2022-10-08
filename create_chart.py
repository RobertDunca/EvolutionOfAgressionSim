import altair as alt
from sim import simulate

source = simulate(100, 1, 100, 200)

chart = alt.Chart(source).mark_area().encode(
    x="Generation:O",
    y="Population:Q",
    color="Type:N"
).properties(
    width=1200,
    height=600
)

chart.save('chart.html')

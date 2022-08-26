from capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Needs to be updated at this section of the code.
df["START_String"] = df["START"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["END_String"] = df["END"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

p = figure(
    x_axis_type="datetime",
    plot_height=100,
    plot_width=500,
    sizing_mode="scale_both",
    title="Motion Graph",
)
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("START: ", "@START_String"), ("END: ", "@END_String")])
p.add_tools(hover)
q = p.quad(left="START", right="END", bottom=0, top=1, color="black", source=cds)

output_file("Graph.html")
show(p)

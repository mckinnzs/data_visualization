
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file

def circle_graph(df, index, list_, unit):
    """Takes a pandas df with an index column and a list of columns (3 to 5 for 
    best results) with float values representing the unit and creates a circle graph"""
    
    """eg circle_graph(survivor_df, 'days lasted', ['15 to 24 y.o.', '25 to 34 y.o.', '35+ y.o.'], '%')"""
    
        #Set the colors of the bars in the bar graph based on "Tableau 20" colors.    
    tableau20 = [ '#1f77b4',  '#2ca02c','#7f7f7f','#8c564b','#d62728', '#bcbd22', '#9edae5','#17becf',
                 '#98df8a','#9467bd','#aec7e8','#c5b0d5', '#c7c7c7']
    width = 800
    height = 800
    inner_radius = 90
    outer_radius = 290
    big_angle = 2.0 * np.pi / (len(df) + 1)
    small_angle = big_angle / (len(list_) *2 + 1)
    p = figure(plot_width=width, plot_height=height, title="", x_axis_type=None, y_axis_type=None,
    x_range=(-420, 420), y_range=(-420, 420), min_border=0, outline_line_color="white")
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    #draw the large wedges
    angles = np.pi/2 - big_angle/2 - df.index.to_series()*big_angle
    p.annular_wedge(0, 0, inner_radius, outer_radius, -big_angle + angles, angles, color='#cfcfcf',)
    
    #find the maximum value for the concentric rings of values
    column_max = list()
    for column in list_:
        column_max.append(max(df[column]))
    label_max = int(max(column_max) + 10 - max(column_max)%10)
    
    #draw the small wedges and labels
    bar_color = {}
    counter = 0
    for column in list_:
        bar_color[column] = tableau20[counter]
        p.annular_wedge(0, 0, inner_radius, 90 + df[column]*(200/float(label_max)),
                -big_angle+angles+(2*counter+1)*small_angle, -big_angle+angles+(2*counter+2)*small_angle,
                color=bar_color[column])
        p.rect([-40, -40, -40], [37-counter*18], width=30, height=13, color=bar_color[column])
        p.text([-15, -15, -15], [37-counter*18], text=[column], text_font_size="9pt", 
               text_align="left", text_baseline="middle")
        counter += 1
    
    #draw the rings and corresponding labels
    labels = np.array(range((label_max+10)/10))*10
    radii = 90 + labels* (200/float(label_max))
    p.circle(0, 0, radius=radii[:-1], fill_color=None, line_color="#E6E6E6")
    p.text(0, radii, [str(z)+str(unit) for z in labels[:-1]], text_font_size="8pt", text_align="center", 
                      text_baseline="middle")
    
    #draw the spokes separating the big wedges
    p.annular_wedge(0, 0, inner_radius-10, outer_radius+10, -big_angle+angles, 
                    -big_angle+angles, color="black")
    
    #draw the labels for the big wedges and angle them correctly
    xr = radii[-1]*np.cos(np.array(-big_angle/2 + angles))
    yr = radii[-1]*np.sin(np.array(-big_angle/2 + angles))   
    label_angle=np.array(-big_angle/2+angles)
    label_angle[label_angle < -np.pi/2] += np.pi   
    p.text(xr, yr, df[index], angle=label_angle, text_font_size="9pt", 
           text_align="center", text_baseline="middle")

    output_file("example.html", title="example.py")
    show(p)

test_df = pd.read_csv(r"C:\Users\Zachery McKinnon\Documents\survivor_demographics_agexdayslasted1.csv")

circle_graph(test_df, 'days_lasted', ('15_to_34', '35_to_54', '55_to_75', '76 to 90'), '%')
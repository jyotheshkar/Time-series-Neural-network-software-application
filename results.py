import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

def create_results(parent_frame):
    # Darken color function
    def darken_color(color, amount=0.5):
        try:
            c = mcolors.cnames[color]
        except KeyError:
            c = color
        c = mcolors.rgb_to_hsv(mcolors.to_rgba(c)[:3])
        c[2] = c[2] * amount
        c = mcolors.hsv_to_rgb(c)
        return c

    # Data to plot
    labels = ['Red Alert', 'Orange Alert', 'Green Alert']
    sizes = [70, 10, 20]
    colors = ['#8B0000', '#8B4513', '#006400']
    dark_colors = [darken_color(color, 0.5) for color in colors]  # Darken the colors by 50%
    explode = (0, 0, 0)  # explode a slice if required

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(3, 3))  # Increased the size of the figure
    fig.patch.set_facecolor('black')  # Set the background color to black
    ax.set_facecolor('black')  # Set the axes background color to black

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    patches, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=dark_colors, autopct='%1.1f%%',
                                       shadow=True, startangle=140, textprops={'color': 'white', 'fontsize': 6})  # Reduced text size

    # Draw the borders between slices
    for i, patch in enumerate(patches):
        theta1, theta2 = patch.theta1, patch.theta2
        center, r = patch.center, patch.r
        x = [center[0], center[0] + r * np.cos(np.radians(theta1))]
        y = [center[1], center[1] + r * np.sin(np.radians(theta1))]
        ax.plot(x, y, color='white', linewidth=1.5)

        x = [center[0], center[0] + r * np.cos(np.radians(theta2))]
        y = [center[1], center[1] + r * np.sin(np.radians(theta2))]
        ax.plot(x, y, color='white', linewidth=1.5)

    # Draw the outer circle of the pie chart
    outer_circle = plt.Circle((0, 0), r, color='white', fill=False, linewidth=2)
    ax.add_artist(outer_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Create a frame for the chart and button
    result_frame = tk.Frame(parent_frame, bg='black')
    result_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Add the pie chart to the Tkinter window
    chart_frame = tk.Frame(result_frame, bg='black')
    chart_frame.grid(row=0, column=0, pady=(0, 5))  # Adjust padding as needed
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)  # A tk.DrawingArea
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Create a frame for the buttons
    button_frame = tk.Frame(result_frame, bg='black')
    button_frame.grid(row=1, column=0)  # Center the button exactly below the pie chart

    # Button configuration for the "Red Alert" button
    red_alert_button = tk.Button(button_frame, text="Red Alert", bg='#450804', fg='white', font=("Helvetica", 12),
                                 width=14, height=2, bd=0, highlightthickness=2, highlightbackground='#FF0000',
                                 activebackground='#5b0000', activeforeground='white')  # Increased size

    # Arrange the button in the frame
    red_alert_button.pack(pady=(0, 0))  # Adjust padding as needed

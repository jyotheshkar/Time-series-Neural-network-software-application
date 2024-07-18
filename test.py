

# ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

# rightgraphmain.py

# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.signal import find_peaks

# # Generate random data ensuring intersections
# np.random.seed(0)
# x = np.arange(0, 100)
# y1 = 0.3 + np.abs(np.cumsum(np.random.randn(100) * 0.5))
# y2 = 0.3 + np.abs(np.cumsum(np.random.randn(100) * 0.4))

# # Force two intersections for demonstration
# y2[20] = y1[20]
# y2[43] = y1[43]

# # Find peaks (local maxima)
# peaks_y1, _ = find_peaks(y1)
# peaks_y2, _ = find_peaks(y2)

# # Create the plot
# fig, ax = plt.subplots()
# fig.patch.set_facecolor('black')  # Set the background color to black
# ax.set_facecolor('black')  # Set the axes background color to black

# # Plot the first line
# ax.plot(x, y1, color='red', label='6774 Activity Levels', linewidth=2)  # Red line for the first data series
# ax.fill_between(x, y1, color='red', alpha=0.3)  # Shaded area under the first line

# # Plot the second line
# ax.plot(x, y2, color='cyan', label='Dairy Herd Activity Levels', linewidth=2)  # Cyan line for the second data series
# ax.fill_between(x, y2, color='cyan', alpha=0.3)  # Shaded area under the second line

# # Create an overlapping area with no color
# overlap = np.minimum(y1, y2)
# ax.fill_between(x, overlap, color='black', alpha=1.0)

# # Add tooltips (scatter points) for the peaks of both lines
# ax.scatter(x[peaks_y1], y1[peaks_y1], color='white', zorder=5, s=8)
# ax.scatter(x[peaks_y2], y2[peaks_y2], color='white', zorder=5, s=8)

# # Customize the axes
# ax.spines['bottom'].set_color('white')
# ax.spines['top'].set_color('white')
# ax.spines['right'].set_color('white')
# ax.spines['left'].set_color('white')

# ax.tick_params(axis='x', colors='white')
# ax.tick_params(axis='y', colors='white')

# # Set the axis labels and title with white color
# ax.set_xlabel('X-axis', color='white')
# ax.set_ylabel('Y-axis', color='white')
# ax.set_title('6774 Activity Levels Vs Dairy Herd Activity Levels', color='white')

# # Add legend at the top right corner with a very dark gray background
# legend = ax.legend(loc='upper right', frameon=True, fontsize=10, labelcolor='white', facecolor='darkgray', edgecolor='white')
# legend.get_frame().set_facecolor('#1a1a1a')  # Darker gray
# legend.get_frame().set_edgecolor('white')

# # Add custom label in the legend
# common_point_patch = plt.Line2D([0], [0], marker='o', color='w', label='Common Activity Level', markerfacecolor='red', markersize=8)
# handles, labels = ax.get_legend_handles_labels()
# handles.append(common_point_patch)
# ax.legend(handles=handles, loc='upper right', frameon=True, fontsize=10, labelcolor='white', facecolor='darkgray', edgecolor='white')

# # Set the y-axis limit to maintain the original range
# ax.set_ylim([0, max(np.max(y1), np.max(y2)) + 1])

# # Remove spacing on the left and right of the line graph
# ax.set_xlim([x[0], x[-1]])

# # Custom tooltip for intersections
# intersection_points = [20, 43]
# for i in intersection_points:
#     ax.scatter(x[i], y1[i], color='red', zorder=6, s=100, edgecolor='white', linewidth=1)

# plt.show()



# ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Function to lighten the colors
def lighten_color(color, amount=0.7):
    try:
        c = mcolors.cnames[color]
    except:
        c = color
    c = mcolors.rgb_to_hsv(mcolors.to_rgba(c)[:3])
    c[2] = c[2] * (1 + amount)
    c = mcolors.hsv_to_rgb(c)
    return c

# Data to plot
labels = ['Red Alert', 'Orange Alert', 'Green Alert']
sizes = [70, 10, 20]
colors = ['#8B0000', '#8B4513', '#006400']
bright_colors = [lighten_color(color, 0.5) for color in colors] # Lighten the colors by 50%
explode = (0, 0, 0)  # explode a slice if required

# Create the pie chart
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')  # Set the background color to black
ax.set_facecolor('black')  # Set the axes background color to black

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
patches, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=bright_colors, autopct='%1.1f%%',
                                   shadow=True, startangle=140, textprops={'color': 'white'})

# Customize the colors with a gradient effect
for patch, color in zip(patches, bright_colors):
    patch.set_edgecolor(color)  # Set the outer edge color
    patch.set_facecolor('none')
    patch.set_linewidth(1.5)
    patch.set_alpha(1)

# Draw thin dividing lines that match segment colors
for i, patch in enumerate(patches):
    theta1, theta2 = patch.theta1, patch.theta2
    x = [0, np.cos(np.radians(theta1))]
    y = [0, np.sin(np.radians(theta1))]
    ax.plot(x, y, color=colors[i], linewidth=0.5)

    x = [0, np.cos(np.radians(theta2))]
    y = [0, np.sin(np.radians(theta2))]
    ax.plot(x, y, color=colors[i], linewidth=0.5)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

plt.show()



# ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????



# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.signal import find_peaks

# # Generate random data with values above 0.3
# np.random.seed(0)
# x = np.arange(0, 100)
# y = 0.3 + np.abs(np.cumsum(np.random.randn(100) * 0.5))  # Generate random data with values above 0.3

# # Find peaks (local maxima)
# peaks, _ = find_peaks(y)

# # Alert lines
# red_line = 5
# orange_line = np.mean(y)
# green_line = 0.3

# # Create the plot
# fig, ax = plt.subplots()
# fig.patch.set_facecolor('black')  # Set the background color to black
# ax.set_facecolor('black')  # Set the axes background color to black

# # Calculate bubble sizes and colors
# bubble_sizes = np.ones(len(peaks)) * 30  # Base bubble size
# colors = []
# for i, peak in enumerate(peaks):
#     if y[peak] > red_line:
#         colors.append('red')
#         bubble_sizes[i] *= 3  # Red bubbles are 3 times larger
#     elif y[peak] > orange_line:
#         colors.append('orange')
#         bubble_sizes[i] *= 2  # Orange bubbles are 2 times larger
#     else:
#         colors.append('green')

# # Scatter plot (bubble chart)
# ax.scatter(x[peaks], y[peaks], s=bubble_sizes, c=colors, alpha=0.6, edgecolor='white', linewidth=1)

# # Customize the axes
# ax.spines['bottom'].set_color('white')
# ax.spines['top'].set_color('white')
# ax.spines['right'].set_color('white')
# ax.spines['left'].set_color('white')

# ax.tick_params(axis='x', colors='white')
# ax.tick_params(axis='y', colors='white')

# # Set the axis labels and title with white color
# ax.set_xlabel('X-axis', color='white')
# ax.set_ylabel('Y-axis', color='white')
# ax.set_title('6774 Activity Levels', color='white')

# # Add three horizontal dotted lines with labels
# ax.axhline(y=red_line, color='red', linestyle='--', linewidth=1, label='Red Alert')  # Red line at y=5
# ax.axhline(y=orange_line, color='orange', linestyle='--', linewidth=1, label='Orange Alert')  # Orange line at mean value
# ax.axhline(y=green_line, color='green', linestyle='--', linewidth=1, label='Green Alert')  # Green line at 0.3

# # Add legend at the top right corner with a very dark gray background
# legend = ax.legend(loc='upper right', frameon=True, fontsize=8, labelcolor='white', facecolor='darkgray', edgecolor='white')
# legend.get_frame().set_facecolor('#2f2f2f')  # Very dark gray
# legend.get_frame().set_edgecolor('white')

# # Set the y-axis limit to maintain the original range
# ax.set_ylim([0, np.max(y) + 1])

# # Remove spacing on the left and right of the white line graph
# ax.set_xlim([x[0], x[-1]])

# plt.show()

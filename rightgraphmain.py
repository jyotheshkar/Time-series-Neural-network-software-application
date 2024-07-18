import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def create_right_plot():
    # Generate random data ensuring intersections
    np.random.seed(0)
    x = np.arange(0, 100)
    y1 = 0.3 + np.abs(np.cumsum(np.random.randn(100) * 0.5))
    y2 = 0.3 + np.abs(np.cumsum(np.random.randn(100) * 0.4))

    # Force two intersections for demonstration
    y2[20] = y1[20]
    y2[43] = y1[43]

    # Find peaks (local maxima)
    peaks_y1, _ = find_peaks(y1)
    peaks_y2, _ = find_peaks(y2)

    # Create the plot
    fig, ax = plt.subplots(figsize=(8.05, 5))  # Increased width by 15%
    fig.patch.set_facecolor('black')  # Set the background color to black
    ax.set_facecolor('black')  # Set the axes background color to black

    # Plot the first line
    ax.plot(x, y1, color='red', label='6774 Activity Levels', linewidth=2)  # Red line for the first data series
    ax.fill_between(x, y1, color='red', alpha=0.3)  # Shaded area under the first line

    # Plot the second line
    ax.plot(x, y2, color='cyan', label='Dairy Herd Activity Levels', linewidth=2)  # Cyan line for the second data series
    ax.fill_between(x, y2, color='cyan', alpha=0.3)  # Shaded area under the second line

    # Create an overlapping area with no color
    overlap = np.minimum(y1, y2)
    ax.fill_between(x, overlap, color='black', alpha=1.0)

    # Add tooltips (scatter points) for the peaks of both lines
    ax.scatter(x[peaks_y1], y1[peaks_y1], color='white', zorder=5, s=8)
    ax.scatter(x[peaks_y2], y2[peaks_y2], color='white', zorder=5, s=8)

    # Customize the axes
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Set the axis labels and title with white color
    ax.set_xlabel('X-axis', color='white')
    ax.set_ylabel('Y-axis', color='white')
    ax.set_title('6774 Activity Levels Vs Dairy Herd Activity Levels', color='white')

    # Add legend at the top right corner with a very dark gray background
    legend = ax.legend(loc='upper right', frameon=True, fontsize=10, labelcolor='white', facecolor='darkgray', edgecolor='white')
    legend.get_frame().set_facecolor('#1a1a1a')  # Darker gray
    legend.get_frame().set_edgecolor('white')

    # Add custom label in the legend
    common_point_patch = plt.Line2D([0], [0], marker='o', color='w', label='Common Activity Level', markerfacecolor='red', markersize=8)
    handles, labels = ax.get_legend_handles_labels()
    handles.append(common_point_patch)
    ax.legend(handles=handles, loc='upper right', frameon=True, fontsize=10, labelcolor='white', facecolor='darkgray', edgecolor='white')

    # Set the y-axis limit to maintain the original range
    ax.set_ylim([0, max(np.max(y1), np.max(y2)) + 1])

    # Remove spacing on the left and right of the line graph
    ax.set_xlim([x[0], x[-1]])

    # Custom tooltip for intersections
    intersection_points = [20, 43]
    for i in intersection_points:
        ax.scatter(x[i], y1[i], color='red', zorder=6, s=100, edgecolor='white', linewidth=1)

    return fig

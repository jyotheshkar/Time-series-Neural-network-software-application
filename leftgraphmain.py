import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def create_plot():
    # Generate random data with values above 0.3
    np.random.seed(0)
    x = np.arange(0, 100)
    y = 0.3 + np.abs(np.cumsum(np.random.randn(100) * 0.5))  # Generate random data with values above 0.3

    # Find peaks (local maxima)
    peaks, _ = find_peaks(y)

    # Alert lines
    red_line = 5
    orange_line = np.mean(y)
    green_line = 0.3

    # Create the plot
    fig, ax = plt.subplots(figsize=(8.05, 5))  # Increased width by 15%
    fig.patch.set_facecolor('black')  # Set the background color to black
    ax.set_facecolor('black')  # Set the axes background color to black

    # Function to segment and plot the line with different colors
    def plot_segments(x, y, threshold, color_above, color_below):
        segments = []
        for i in range(len(y) - 1):
            color = color_above if y[i] > threshold else color_below
            segments.append((x[i:i+2], y[i:i+2], color))
        for seg in segments:
            ax.plot(seg[0], seg[1], color=seg[2])

    # Plot the segments
    plot_segments(x, y, red_line, 'red', 'white')

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
    ax.set_title('6774 Activity Levels', color='white')

    # Add three horizontal dotted lines with labels
    ax.axhline(y=red_line, color='red', linestyle='--', linewidth=1, label='Red Alert')  # Red line at y=5
    ax.axhline(y=orange_line, color='orange', linestyle='--', linewidth=1, label='Orange Alert')  # Orange line at mean value
    ax.axhline(y=green_line, color='green', linestyle='--', linewidth=1, label='Green Alert')  # Green line at 0.3

    # Add tooltips with different colors based on their position
    for peak in peaks:
        if y[peak] > red_line:
            ax.scatter(x[peak], y[peak], color='white', zorder=5)  # White tooltips above red alert line
        elif y[peak] > orange_line:
            ax.scatter(x[peak], y[peak], color='orange', zorder=5)
        elif y[peak] > green_line:
            ax.scatter(x[peak], y[peak], color='green', zorder=5)
        else:
            ax.scatter(x[peak], y[peak], color='red', zorder=5)

    # Add legend at the top right corner with a very dark gray background
    legend = ax.legend(loc='upper right', frameon=True, fontsize=8, labelcolor='white', facecolor='darkgray', edgecolor='white')
    legend.get_frame().set_facecolor('#2f2f2f')  # Very dark gray
    legend.get_frame().set_edgecolor('white')

    # Set the y-axis limit to maintain the original range
    ax.set_ylim([0, np.max(y) + 1])

    # Remove spacing on the left and right of the white line graph
    ax.set_xlim([x[0], x[-1]])

    return fig

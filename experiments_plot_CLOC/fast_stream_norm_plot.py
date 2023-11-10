import matplotlib.pyplot as plt
import random

# Define the names of the lines for each plot
lines_list = [
    ["ER (Delay = 0)", "ER--", "OCL Method"],
    ["ER (Delay = 0)", "ER--", "OCL Method"],
    ["ER (Delay = 0)", "ER--", "OCL Method"],
    ["ER (Delay = 0)", "ER--", "OCL Method"],
    ["ER (Delay = 0)", "ER--", "OCL Method"],
]

titles = [
    "LwF (Delay = 0.33)",
    "RWalk (Delay = 1)",
    "MIR (Delay = 1.5)",
    "PoLRS (Delay = 2)",
    "GSS (Delay = 5)"
]
# Create 5 subplots in a row
fig, axes = plt.subplots(1, 5, figsize=(15, 4))  # 1 row and 5 columns

data = [
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 12.12983, 12.38271, 13.08331, 14.93712, 16.00291, 16.38271, 16.99103, 17.03002, 17.89291],
     [0, 10.87928, 12.63525, 13.89123, 14.91271, 15.24241, 15.98242, 16.10923, 16.73621, 16.92371],
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 10.73621, 11.98930, 12.16091, 13.79391, 14.87881, 15.23153, 16.63813, 16.91384, 17.01310],
     [0, 8.91742, 10.12873, 11.39281, 12.09832, 13.02813, 13.67738, 14.29813, 14.87229, 15.58821]
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 10.29311, 10.75332, 11.16091, 11.79193, 12.28192, 12.63812, 13.19382, 13.93819, 14.39812],
     [0, 7.34353, 8.02934, 9.21243, 9.90238, 10.4312, 10.98201, 11.12932, 11.23976, 11.33982],
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 9.87312, 10.48211, 11.00392, 11.73877, 12.32881, 13.00901, 13.72713, 14.29083, 14.48172],
     [0, 7.02384, 8.45573, 8.72313, 9.29812, 10.78381, 11.01323, 11.78312, 12.22913, 12.47380],
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 6.73621, 8.00129, 9.12931, 9.99329, 10.72821, 11.48911, 12.87281, 13.12873, 13.41738],
     [0, 4.21213, 5.48371, 7.21130, 7.93821, 8.20103, 8.33844, 8.79302, 8.98371, 9.13391],
    ],
]
# Generate random data points for each line in each plot
for i, lines in enumerate(lines_list):
    
    # Define x and y axis ticks
    x_ticks = [0, 3, 6, 9]
    x_tick_labels = ["0", "5k", "10k", "15k"]
    y_ticks = [0, 5, 10, 15, 20]
    
    # Define colors and markers for each line
    colors = ['b', 'g', 'r']
    markers = ['o', 's', 'D']
    
    # Plot each line with its data points using different colors and markers
    for j, line_name in enumerate(lines):
        axes[i].plot(data[i][j], label=line_name, color=colors[j], marker=markers[j])
    
    # Set x and y axis ticks and labels
    axes[i].set_xticks(x_ticks)
    axes[i].set_xticklabels(x_tick_labels)  # Set custom tick labels for the x-axis
    axes[i].set_yticks(y_ticks)
    axes[i].set_xlabel("Time Steps")
    axes[i].set_ylabel("Avg. Online Accuracy (%)" if i == 0 else "")  # Show y-axis label only on the leftmost plot
    
    # Add labels and a legend for each set of lines in each plot
    axes[i].set_title(titles[i])

    # Add grid lines
    axes[i].grid(True)

    # Remove y-axis from non-leftmost plots
    if i != 0:
        axes[i].spines['left'].set_visible(False)

# Set the axis limits to ensure the lower-left corner is at (0, 0)
for ax in axes:
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 20)

# Add a legend that covers the entire figure
handles, labels = axes[2].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', fancybox=True, shadow=True, ncol=3)

# Adjust the layout to prevent overlapping titles
plt.tight_layout()

# Display the plots
plt.show()

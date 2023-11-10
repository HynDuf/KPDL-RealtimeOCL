import matplotlib.pyplot as plt
import random

# Define the names of the lines for each plot
lines_list = [
    ["ER", "ER++", "OCL Method"],
    ["ER", "ER++", "OCL Method"],
    ["ER", "ER++", "OCL Method"],
    ["ER", "ER++", "OCL Method"],
    ["ER", "ER++", "OCL Method"],
]

titles = [
    "LwF (C_S = 1.33)",
    "RWalk (C_S = 2)",
    "MIR (C_S = 2.5)",
    "PoLRS (C_S = 3)",
    "GSS (C_S = 6)"
]
# Create 5 subplots in a row
fig, axes = plt.subplots(1, 5, figsize=(15, 4))  # 1 row and 5 columns

data = [
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 13.12983, 13.78271, 15.08331, 16.93712, 17.00291, 17.38271, 17.99103, 18.53002, 19.89291],
     [0, 11.87928, 13.63525, 14.89123, 15.91271, 16.24241, 16.98242, 17.10923, 17.73621, 17.92371],
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 14.73621, 16.98930, 17.76091, 18.79391, 19.87881, 20.23153, 21.63813, 21.91384, 22.91310],
     [0, 11.91742, 13.52873, 14.99281, 15.79832, 16.32813, 16.99738, 17.99813, 18.47229, 19.58821]
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 15.29311, 16.75332, 17.16091, 18.79193, 19.28192, 20.63812, 21.19382, 22.93819, 23.39812],
     [0, 12.34353, 13.02934, 13.21243, 13.90238, 14.2312, 14.98201, 15.12932, 15.63976, 15.93982],
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 16.87312, 17.48211, 18.00392, 19.73877, 20.32881, 21.00901, 22.72713, 23.29083, 24.48172],
     [0, 12.02384, 13.45573, 14.72313, 15.29812, 16.78381, 17.01323, 17.78312, 18.92913, 19.83380],
    ],
    [
     [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
     [0, 21.73621, 23.00129, 24.12931, 25.99329, 26.72821, 27.48911, 28.87281, 29.12873, 30.41738],
     [0, 8.21213, 10.48371, 12.21130, 13.93821, 14.20103, 15.33844, 16.79302, 16.98371, 17.13391],
    ],
]
# Generate random data points for each line in each plot
for i, lines in enumerate(lines_list):
    
    # Define x and y axis ticks
    x_ticks = [0, 3, 6, 9]
    x_tick_labels = ["0", "5k", "10k", "15k"]
    y_ticks = [0, 5, 10, 15, 20, 25, 30, 35]
    
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
    ax.set_ylim(10, 35)

# Add a legend that covers the entire figure
handles, labels = axes[2].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', fancybox=True, shadow=True, ncol=3)

# Adjust the layout to prevent overlapping titles
plt.tight_layout()

# Display the plots
plt.show()

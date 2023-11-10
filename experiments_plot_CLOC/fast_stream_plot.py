import matplotlib.pyplot as plt
import random

# Define the names of the lines
lines = ["ER", "PoLRS", "ACE", "MIR", "LwF", "GSS", "RWalk"]

# Generate random data points for each line
data = {
    "ER": [0, 12.74937, 13.45948, 14.77933, 15.87221, 16.23773, 16.98327, 17.52931, 18.01983, 18.40921],
    "PoLRS": [0, 7.02384, 8.45573, 8.72313, 9.29812, 10.78381, 11.01323, 11.78312, 12.22913, 12.47380],
    "ACE": [0, 11.68743, 12.39238, 13.10211, 14.92132, 16.01202, 16.53929, 17.19321, 17.32345, 17.98392],
    "MIR": [0, 7.34353, 8.02934, 9.21243, 9.90238, 10.4312, 10.98201, 11.12932, 11.23976, 11.33982],
    "LwF": [0, 10.87928, 12.63525, 13.89123, 14.91271, 15.24241, 15.98242, 16.10923, 16.73621, 16.92371],
    "GSS": [0, 4.21213, 5.48371, 7.21130, 7.93821, 8.20103, 8.33844, 8.79302, 8.98371, 9.13391],
    "RWalk": [0, 8.91742, 10.12873, 11.39281, 12.09832, 13.02813, 13.67738, 14.29813, 14.87229, 15.58821]
}

# Define x and y axis ticks
x_ticks = [0, 3, 6, 9]
x_tick_labels = ["0", "5k", "10k", "15k"]
y_ticks = [0, 5, 10, 15, 20]

# Define colors and markers for each line
colors = ['b', 'c', 'r', 'orange', 'g', 'grey', 'purple']
markers = ['o', 's', 'D', '^', 'v', '<', '>']

# Create a figure and axis
fig, ax = plt.subplots()

# Plot each line with its data points using different colors and markers
for i, line_name in enumerate(lines):
    ax.plot(data[line_name], label=line_name, color=colors[i], marker=markers[i])

# Set x and y axis ticks and labels
ax.set_xticks(x_ticks)
ax.set_xticklabels(x_tick_labels)  # Set custom tick labels for the x-axis
ax.set_yticks(y_ticks)
ax.set_xlabel("Time Steps")
ax.set_ylabel("Avg. Online Accuracy (%)")
ax.grid(True)
ax.set_xlim(0, 9)
ax.set_ylim(0, 20)

# Add labels and a legend below the plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=4)

# Display the plot
plt.show()

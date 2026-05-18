import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
data = pd.read_csv("XYZ.csv")

# Create a figure with five subplots arranged in a grid, with a shared y-axis
fig, axs = plt.subplots(1, 4, sharey=True)


# Define a list of colors for the violin plots
color = ["#599f41", "#c4539d", "#74a6a9", "#f5e802"]
# Loop over the columns of the dataframe
for i, col in enumerate(data.columns):
    # Plot the data in the i-th subplot as a violin plot
    vp = axs[i].violinplot(data[col], showextrema=True, showmedians=True))
    # Set the color of the violin plot
    vp["bodies"][0].set_color(color[i])
    # Set the y-axis limits to 0-100
    axs[i].set_ylim(0, 100)
    # Set the x-axis label to the name of the column
    axs[i].set_xlabel(col)
    # Remove the tick marks from the x-axis
    axs[i].set_xticks([])
    # Set the y-axis tick marks to be at every 10th number
    axs[i].set_yticks(range(0, 101, 10))
    # Set the default font to "Helvetica"
    plt.rcParams["font.family"] = "Helvetica"

# Set the y-axis label to "plddt"
axs[0].set_ylabel("pLDDT per residue of XYZ")

# Save the plot to a png file with a high resolution (900 dpi)
plt.savefig("XYZ_plot.png", dpi=900)

# Show the plot
plt.show()


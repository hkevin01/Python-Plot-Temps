"""
simpletest.py

Example script for map plotting using basemap.
"""

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np


def main():
    """Main function to plot a simple Robinson projection map."""
    # Create a new figure
    plt.figure(figsize=(8, 8))

    # Set up the map projection
    m = Basemap(projection='robin', lon_0=0)

    # Draw coastlines and countries
    m.drawcoastlines()
    m.drawcountries()

    # Fill the continents and lakes
    m.fillcontinents(color='lightgray', lake_color='aqua')
    m.drawmapboundary(fill_color='aqua')

    # Add a title
    plt.title('Robinson Projection')

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()

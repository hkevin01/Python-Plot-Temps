"""
earthquake.py

Processes and visualizes earthquake data from a CSV file using matplotlib and basemap.
"""

# --- Import Libraries ---
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import os

# --- Process Data ---
def get_marker_color(magnitude):
    """Return marker color based on magnitude."""
    if magnitude < 3.0:
        return 'go'
    elif magnitude < 5.0:
        return 'yo'
    else:
        return 'ro'

def main():
    """Main function to process and plot earthquake data."""
    data_file = open('data/earthquake_data.csv', encoding='utf-8')
    lats, lons, magnitudes, timestrings = [], [], [], []
    for index, line in enumerate(data_file.readlines()):
        if index > 0:
            parts = line.split(',')
            lats.append(float(parts[6]))
            lons.append(float(parts[7]))
            magnitudes.append(float(parts[8]))
            timestrings.append(' '.join(parts[4:6]).strip('"'))
    data_file.close()
    # Example plotting code (customize as needed)
    map = Basemap(projection='robin', resolution='l', area_thresh=1000.0,
                  lat_0=0, lon_0=-130)
    map.drawcoastlines()
    map.drawcountries()
    map.bluemarble()
    map.drawmapboundary()
    map.drawmeridians(np.arange(0, 360, 30))
    map.drawparallels(np.arange(-90, 90, 30))
    for lat, lon, mag in zip(lats, lons, magnitudes):
        x, y = map(lon, lat)
        map.plot(x, y, get_marker_color(mag), markersize=mag*2)
    plt.title('Earthquake Data Visualization')
    plt.savefig('docs/earthquake_map.png')

if __name__ == "__main__":
    main()

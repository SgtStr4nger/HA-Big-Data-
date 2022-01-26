# Geographic plotting of data using geopandas

import geopandas as gpd
import matplotlib.pyplot as plt

# Shapefiles:
sfpath_LK = "shapefile/Map2/vg5000_01-01.gk3.shape.ebenen/vg5000_ebenen_0101/VG5000_KRS.shp"

def read_sf (path):
    sf = gpd.read_file(path)
    return sf

def create_map (sf):
    sf.plot()
    plt.show()
    return

create_map(read_sf(sfpath_LK))
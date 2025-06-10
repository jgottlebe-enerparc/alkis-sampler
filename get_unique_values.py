import sys
import geopandas as gpd
import fiona
import numpy as np

path = sys.argv[1]
field = sys.argv[2]

layers = fiona.listlayers(path)
layer = layers[0]

gdf = gpd.read_file(path, layer=layer)

unique_values = gdf[field].unique()
unique_values[unique_values != np.array(None)]
unique_values = sorted(unique_values)

for i, item in enumerate(unique_values):
    if i < 10 or i >= len(unique_values) - 10:
        print(item)
    if i == 10:
        print("...")

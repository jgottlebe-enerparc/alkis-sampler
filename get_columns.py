import sys
import geopandas as gpd
import fiona

path = sys.argv[1]
layers = fiona.listlayers(path)
layer = layers[0]
gdf = gpd.read_file(path, layer=layer)
print(gdf.columns.tolist())



import sys
import geopandas as gpd
import pprint
import copy
import random
import fiona

temp = {
    "land": "",
    "gemarkung": "",
    "gmknr": [""],
    "corridor": "",
    "parcel": "",
    "cadastralid": [""]
}

path = sys.argv[1]

layers = fiona.listlayers(path)
layer = layers[0]

land = sys.argv[2]
field_gemarkung = sys.argv[3]
field_flur = sys.argv[4]
field_flurstueck_zaehler = sys.argv[5]
field_flurstueck_nenner = sys.argv[6]


gdf = gpd.read_file(path, layer=layer)

for i in range(int(sys.argv[7])):
    random_row = gdf.sample(1, random_state=random.randint(0, 999999)).iloc[0]

    template = copy.deepcopy(temp)

    template["land"] = land
    template["gemarkung"] = random_row.get(field_gemarkung, "") or ""
    template["corridor"] = random_row.get(field_flur, "") or ""
    parcel_zaehler = random_row.get(field_flurstueck_zaehler, "") or ""
    parcel_nenner = random_row.get(field_flurstueck_nenner, "") or ""
    template["parcel"] = parcel_zaehler + '/' + parcel_nenner

    pprint.pprint(template)
    print(',')

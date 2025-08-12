#!/usr/bin/env python3
"""
Usage:
    python script.py <path> [<land> <field_gemarkung> <field_flur> <field_flurstueck_zaehler> <field_flurstueck_nenner> <n>]

Arguments:
    <path>                      Path to the GeoPackage or vector file.
    <land>                      Land code or name (used as a fixed value in output).
    <field_gemarkung>           Column name for the "Gemarkung" field.
    <field_flur>                Column name for the "Flur" (corridor) field.
    <field_flurstueck_zaehler>  Column name for the parcel numerator.
    <field_flurstueck_nenner>   Column name for the parcel denominator.
    <n>                         Number of random features to sample.

Behavior:
    - If only <path> is given, the script prints the first layer’s column names.
    - If all arguments are provided, it prints <n> random parcel templates from the file.
"""


def main():

    import sys
    import geopandas as gpd
    import pprint
    import copy
    import random
    import fiona

    # Print usage if no arguments or wrong number
    if len(sys.argv) not in [2, 8]:
        print(__doc__)
        sys.exit(1)

    # Just print columns from the first layer
    if len(sys.argv) == 2:
        path = sys.argv[1]
        layers = fiona.listlayers(path)
        layer = layers[0]
        gdf = gpd.read_file(path, layer=layer)
        print("Available columns:", gdf.columns.tolist())
        sys.exit(0)

    # Full operation mode
    temp = {
        "land": "",
        "gemarkung": "",
        "gmknr": [""],
        "corridor": "",
        "parcel": "",
        "cadastralid": [""]
    }

    path = sys.argv[1]
    land = sys.argv[2]
    field_gemarkung = sys.argv[3]
    field_flur = sys.argv[4]
    field_flurstueck_zaehler = sys.argv[5]
    field_flurstueck_nenner = sys.argv[6]
    n = int(sys.argv[7])

    layers = fiona.listlayers(path)
    layer = layers[0]
    gdf = gpd.read_file(path, layer=layer)

    for _ in range(n):
        random_row = gdf.sample(
            1, random_state=random.randint(0, 999999)).iloc[0]
        template = copy.deepcopy(temp)
        template["land"] = land
        template["gemarkung"] = random_row.get(field_gemarkung, "") or ""
        template["corridor"] = random_row.get(field_flur, "") or ""
        parcel_zaehler = random_row.get(field_flurstueck_zaehler, "") or ""
        parcel_nenner = random_row.get(field_flurstueck_nenner, "") or ""
        template["parcel"] = f"{
            parcel_zaehler}/{parcel_nenner}" if parcel_nenner else parcel_zaehler
        pprint.pprint(template)
        print(',')

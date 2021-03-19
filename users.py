#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import geopandas as gpd
import geoplot as gplt
import contextily as cx
import matplotlib.pyplot as plt
# import rtree

path = "assignment_data/"
signal_path = path + "sample_data"
signals = []

print("Reading data from csv files")
for i, filei in enumerate(os.listdir(signal_path)):
    signals.append(pd.read_csv(signal_path + "/" + filei))
    
print("Joining DataFrames together")
signal = pd.concat(signals)
signal["date"] = pd.to_datetime(signal.utc_timestamp, unit = "ms").map(pd.Timestamp.date)
gsignal = gpd.GeoDataFrame(signal, geometry = gpd.points_from_xy(signal.lon, signal.lat))
gsignal.crs = "EPSG:4326"

west, south, east, north = (
    13.05,
    52.35,
    13.79,
    52.65
    )

img, ext = cx.bounds2img(west,
                         south,
                         east,
                         north,
                         ll=True,
                         source=cx.providers.Stamen.TonerLite,
                         zoom = 12
                        )

img, ext = cx.warp_tiles(img, ext, "EPSG:4326")


f, ax = plt.subplots(1, figsize=(9, 9))
plt.imshow(img, extent=ext)
gplt.kdeplot(gsignal[gsignal.device_id == 8704], ax = ax, cmap = "Reds", shade=True, shade_lowest=False)

plt.savefig("users.png", bbox_inches = "tight")


#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
# import rtree

path = "assignment_data/"

print("Loading store locations")
stores = pd.read_csv(path + "stores.csv")
stores["geometry"] = gpd.GeoSeries.from_wkt(stores.wkt)
gstores = gpd.GeoDataFrame(stores)
gstore_centroids = gstores.copy()
gstore_centroids.geometry = gstores["geometry"].centroid
gstores.crs = "EPSG:4326"
gstore_centroids.crs = "EPSG:4326"

import contextily as cx
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

f, ax = plt.subplots(1, figsize=(9, 9))
ax.imshow(img, extent=ext)
gstores.to_crs(epsg=3857).plot(ax = ax, color = "red", zorder = 3)
gstore_centroids.to_crs(epsg=3857).plot(ax = ax, color = "red", zorder = 2)

plt.savefig("stores.png")


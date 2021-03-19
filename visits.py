#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import geopandas
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
gsignal = geopandas.GeoDataFrame(signal, geometry = geopandas.points_from_xy(signal.lon, signal.lat))

print("Loading store locations")
stores = pd.read_csv(path + "stores.csv")
stores["geometry"] = geopandas.GeoSeries.from_wkt(stores.wkt)
gstores = geopandas.GeoDataFrame(stores)

print("Loading affinities and joining them to signal DataFrame")
affinities = os.listdir(path + "affinities")
for i in affinities:
    aff_id = np.genfromtxt(path + "affinities/" + i)
    gsignal[i] = np.where(gsignal["device_id"].isin(aff_id), 1, 0)

print("Filtering visited stores")
visits = geopandas.sjoin(gsignal, gstores, op = "within", how = "inner").reset_index()
visits = visits.drop(["index", "index_right", "utc_timestamp", "wkt", "geometry", "lat", "lon"], axis = 1)

vis_mod = visits.drop_duplicates(subset = ["store_id", "date", "device_id"])
tmp = visits.value_counts(subset = ["store_id", "date", "device_id"])
tmp.name = "total_signals"
vis_mod = vis_mod.join(tmp, on = ["store_id", "date", "device_id"])

vis_mod = vis_mod.drop(columns = "device_id")
tmp = vis_mod.value_counts(subset = ["store_id", "store_name", "date"])
tmp.name = "unique_visits"
vis_mod = vis_mod.groupby(["store_id", "store_name", "date"]).sum()
vis_mod = vis_mod.join(tmp, on = ["store_id", "store_name", "date"]).reset_index()

# Read columns in example, to rearrange the DataFrame column order
example = pd.read_csv(path + "example.csv")

vis_mod = vis_mod.reindex(columns = example.columns)
vis_mod.to_csv("output.csv")


fig = plt.figure(figsize = (8,6))
data = vis_mod.groupby(["date"]).sum().reset_index()
plt.plot(data.date, data.unique_visits)
plt.xlabel("Date (YYYY-MM-DD)")
plt.xticks(data.date, rotation = 45)
plt.ylabel("Unique visits in all stores")

plt.savefig("visits.png", bbox_inches = "tight")

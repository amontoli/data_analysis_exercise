# data_analysis_exercise

The set of users' data used for obtaining these results is that contained in `assignment_data/sample_data`. In order to run the different Python3 scripts in this folder, it is necessary to installed the `numpy`, `matplotlib`, `pandas`, `geopandas`, `geoplot`, `contextily` and `rtree` modules.
After having changed the permissions with `chmod +x script.py`, the scripts can be launched as `./script.py` 

The results to the assignments of the exercise are the following:

1. The script generating the file storing all information about the store visits by date and affinity profile of store visitors is `visits.py`. The output of this script can be found in `output.csv`.

2. The trend of unique visits of all visitors in all the stores can be obtained with the `visits.py` script. The output is the `visits.png` file: 

![Visits trend](https://github.com/amontoli/data_analysis_exercise/blob/main/visits.png)

A weekly trend can be easly noticed in the plot: the peaks are reached on Saturdays, while on Sundays there is a sudden drop of visits. This is most likely because stores are closed on Sunday.

3. With the `users.py` script it is possible to visualise the GPS data of a single user as a heatmap. In `users.png` I show you as an example the GPS data of a the user with `device_id = 8704`:

![GPS data](https://github.com/amontoli/data_analysis_exercise/blob/main/users.png)

There are two clear spots on the map: these are most likely the two places where this person spends most of his/her time, which could be his/her home and his/her workplace.

4. Finally, with the `stores.py` it is possible to produce the plot `stores.png`, in which the stores in the data files are shown.

![Stores](https://github.com/amontoli/data_analysis_exercise/blob/main/stores.png)

There seems to be no clear trends in the store distributions. The only thing I can notice is that the stores seem to be close to main roads.

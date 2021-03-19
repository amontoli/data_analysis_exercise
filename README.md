# data_analysis_exercise

The data used for obtaining these results is that contained in `assignment_data/sample_data`. In order to run the different Python 3 scripts in this folder, it is necessary to have installed the `numpy`, `matplotlib`, `pandas`, `geopandas`, `geoplot`, `contextily` and `rtree` modules.

The results to the assignments of the exercise are the following:
1. The script generating the file storing all information about the store visitation by date and affinity profile of store visitors is `visits.py`. The output of this script can be found in `output.csv`.
2. The trend of unique visits of all visitors in all the stores can be obtained with the `visits.py` script. The output is the `visits.png` file: 
![Visits trend](https://github.com/amontoli/data_analysis_exercise/blob/main/visits.png) A weekly trend can be easly noticed in the plot: the peaks are reached during Saturdays, while on Sundays there is a sudden drop of visits. This is most likely because stores are closed on Sunday.

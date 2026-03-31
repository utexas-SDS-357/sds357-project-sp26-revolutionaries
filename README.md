[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MFzEnxem)

### Project Overview
This project analyzes traffic crashes and police stops in Nashville, Tennessee to understand spatial and temporal patterns in traffic risk and enforcement. The focus is to evaluate whether police activity aligns with high-risk crash locations and peak time periods. The analysis combines geospatial techniques, exploratory data analysis, and logistic regression modeling to produce actionable insights for traffic safety planning.

### Original Datasets
* **Original SOPP Dataset (Nashville, TN):** <https://openpolicing.stanford.edu/data/>
* **Original Crash Datasets:** <https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/>
  * For each year between the decade (2009 - 2019), we merged annual datasets to one crash dataset which we compare with our original SOPP (stop dataset). 
* **Nashville, TN Parcel Dataset:** <https://koordinates.com/layer/97210-nashville-tennessee-parcels/>
  * We filtered our SOPP dataset to include only coordinate points within the boundary provided from the parcel dataset, in order to verify that all points are actually in the city of Nashville.
* **Nashville, TN Precinct Data** <https://data.nashville.gov/datasets/police-precinct-boundaries/explore?location=36.185836%2C-86.787004%2C9>
  *  We used this boundary data to create a precinct column in both our crash and police stop datasets. 

### Cleaned Datasets (For the purposes of modeling)
* `crash_df.csv`: A merged dataset of all the accident files from 2009 - 2019 filtered to only include fatal crashes that occured in Nashville, TN.
* `crash_inflated.csv`: A derived dataset from `crash_df.csv` that includes additional variables for the purposes of Logistic Regression modeling
* `crash_df_3_8.csv`: A merged dataset of all the accident files from 2009 - 2019 filtered to only include fatal crashes that occured in Nashville, TN. Also, there is a zoning assignment for each data point determined for the K-Means Clustering Algorithm applied.
* `sopp_df_3_8.csv` (Google Drive): A derived dataset from `sopp_df.csv` that limits our data points to only 'moving traffic violation' and 'seatbelt violation' as the reasoning for stop. Also, there is a zoning assignment for each data point determined for the K-Means Clustering Algorithm applied. 
* `sopp_inflated.csv`: A derived dataset from `sopp_df_3_8.csv` (Google Drive). Includes additional variables for the purposes of Logistic Regression modeling (time_segment, precinct).

### Notebooks
* `data_cleaning_pipeline.ipynb`: A notebook containing the data cleaning pipeline. Includes the merging of data from the crash datasets, the utilization of the Nashville Parcel Dataset to find police stop points actually in the city of Nashville, and K-Means clustering assigning zones. 
* `crash_heatmap.ipynb` - Crash density heatmap
* `sopp_heatmap.ipynb` - Policing stop density heatmap
* `prelim_temporal_EDA.ipynb` - Preliminary exploratory data analysis where we take a look at the distribution of crashes and police stops by data of the week and hour.
* `Midterm_SOPP_LogisticReg.ipynb` - Logistic regression results performed on `sopp_inflated.csv`
* `SOPP_LOGREG_Visualization.ipynb` - Logistic regression results performed on `sopp_inflated.csv` with included visualization of odds ratios.
* `crash_model.ipynb` - Logistic regression results performed on `crash_df.csv`
* `crash_data_setup.ipynb` - Pipeline for creating `crash_inflated.csv` from `crash_df.csv`
* `sopp_data_setup.ipynb` - Pipeline for creating `sopp_inflated.csv` from `sopp_df_3_8.csv`

### Data Cleaning Pipeline
* **All Necessary Datasets:** [Google Drive Folder](https://drive.google.com/drive/folders/1xy11tw09H_1_WdMzF8wrdNhjIrVrgalV?usp=drive_link)

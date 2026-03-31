[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MFzEnxem)

### Original Datasets
* **Original SOPP Dataset (Nashville, TN):** <https://openpolicing.stanford.edu/data/>
* **Original Crash Datasets:** <https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/>
  * For each year between the decade (2009 - 2019), we merged annual datasets to one crash dataset which we compare with our original SOPP (stop dataset). 
* **Nashville, TN Parcel Dataset:** <https://koordinates.com/layer/97210-nashville-tennessee-parcels/>
  * We filtered our SOPP dataset to include only coordinate points within the boundary provided from the parcel dataset, in order to verify that all points are actually in the city of Nashville.

### Cleaned Datasets (For the purposes of modeling)
* `crash_df_3_8.csv`: A merged dataset of all the accident files from 2009 - 2019 filtered to only include fatal crashes that occured in Nashville, TN. Also, there is a zoning assignment for each data point determined for the K-Means Clustering Algorithm applied.
* `sopp_df_3_8.csv`: A derived dataset from "sopp_df.csv" that limits our data points to only 'moving traffic violation' and 'seatbelt violation' as the reasoning for stop. Also, there is a zoning assignment for each data point determined for the K-Means CLustering Algorithm applied. 
* `sopp_inflated.csv`: A derived dataset from `sopp_df_3_8.csv` (Google Drive). Includes additional variables for the purposes of Logistic Regression modeling (time_segment, precinct).

### Data Cleaning Pipeline
* **All Necessary Datasets:** [Google Drive Folder](https://drive.google.com/drive/folders/1xy11tw09H_1_WdMzF8wrdNhjIrVrgalV?usp=drive_link)

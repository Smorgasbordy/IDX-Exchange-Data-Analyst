# IDX Exchange - Data Analyst Internship

This repository contains the code that I wrote during my Fall 2026 IDX Exchange Data Analyst Internship.
This internship focuses on cleaning, analyzing, and visualizing MLS real estate data using Python, Pandas, and Tableau.

## Week One: Monthly Dataset Aggregation
Week One focuses on combining the monthly listing and sold datasets into two large aggregate datasets for easier analysis.

### Tasks:
* Load monthly data for the listings and sold datasets.
* Aggregate monthly data into complete "listings" and "sold" datasets.
* Filter the datasets to PropertyType == "Residential" only.
* Compute row counts after every change.
* Create a new csv for both of the filtered and aggregated "listings" and "sold" datasets.
* Deliverable: IDX_DA_Week_1.ipynb

## Week Two: Dataset Structuring and Validation
Week Two was about investigating the structure of the dataset, with a focus on understanding distributions of key features.

### Tasks:
* Calculate count and percentage of null data in each column.
* Flag and handle columns with over 90% missing values.
* Create visualizations of key numeric features: ClosePrice, ListPrice, OriginalListPrice, LivingArea, LotSizeAcres, BedroomsTotal, BathroomsTotalInteger, DaysOnMarket, and YearBuilt.
* Flag outliers for later handling.
* Deliverable: IDX_DA_Week_2.ipynb

## Week Three: Mortgage Rate Enrichment
During week three I began some very basic feature engineering by combining the MLS dataset with mortgage rate information
from the Federal Reserve Economic Data (FRED).

### Tasks:
* Fetch the MORTGAGE30US series from FRED.
* Resample the week-based FRED data to monthly, so that it can be merged with the month-based MLS data.
* Create a common key between the datasets and merge them.
* Verify the merge was successful.
* Deliverable: IDX_DA_Week_3.ipynb

## Weeks Four-Five: Data Cleaning and Preparation
Weeks four and five focused on more aggressive cleaning of the dataset. The objective was to handle all null values, as well as
identify and remove data entry errors.

### Tasks:
* Remove redundant or irrelevant columns.
* Handle missing values by dropping them, imputing them, or flagging them with "Unknown."
* Remove impossible values indicative of entry errors (such as a zipcode of 00000 or a ClosePrice of -$100).
* Deliverable: IDX_DA_Week_4-5.ipynb

## Week Six: Feature Engineering and Market Metrics
This week was about engineering key market features. Once these features were created, segment analysis was performed so that property selling trends could be analyzed across several features. Additionally, improve school district information was joined with the MLS data.

### Tasks:
* Create the market metric features: OriginPriceRatio, PriceRatio, PricePerSquareFoot, YearMonth, ListToContract, and ContractToClose.
* Use property longitude and latitude to join the MLS data with the California School District Areas 2024-25 dataset (https://data.ca.gov/@california-department-of-education/california-school-district-areas-2024-25).
* Using the new metrics, perform segment analysis on PropertySubType, CountyOrParish, MLSAreaMajor, ListOfficeName, and BuyerOfficeName.

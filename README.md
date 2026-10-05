# IDX Exchange - Data Analyst Internship

This repository contains the code that I wrote during my Fall 2026 IDX Exchange Data Analyst Internship.
This internship focuses on cleaning, analyzing, and visualizing MLS real estate data using Python, Pandas, and Tableau.

## Week One:
Week One focuses on combining the monthly listing and sold datasets into two large aggregate datasets for easier analysis.

### Tasks:
* Load monthly data for the listings and sold datasets.
* Aggregate monthly data into complete "listings" and "sold" datasets.
* Filter the datasets to PropertyType == "Residential" only.
* Compute row counts after every change.
* Create a new csv for both of the filtered and aggregated "listings" and "sold" datasets.

## Weeks Two - Three:
Weeks Two and Three are about investigating the structure of the dataset, with a focus on understanding distributions of key features.

### Tasks:
* Calculate count and percentage of null data in each column.
* Flag and handle columns with over 90% missing values.
* Create visualizations of key numeric features: ClosePrice, ListPrice, OriginalListPrice, LivingArea, LotSizeAcres, BedroomsTotal, BathroomsTotalInteger, DaysOnMarket, and YearBuilt.
* Flag outliers for later handling.

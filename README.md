# Data Cleaning – Customer Personality Analysis

This project performs data cleaning and preprocessing using **Pandas** on the Customer Personality Analysis dataset (from Kaggle).

## Files

- `marketing_campaign.csv`: Original dataset (tab-separated).
- `preprocessing.py`: Python script that handles all preprocessing steps.
- `marketing_campaign_cleaned.csv`: Cleaned version of the dataset.
- `README.md`: This file.

## Steps Performed

✅ Removed duplicates  
✅ Dropped rows with missing `income`  
✅ Standardized column names  
✅ Standardized text values (`education`, `marital_status`)  
✅ Converted `dt_customer` to datetime format  
✅ Exported cleaned dataset


## Dataset Link
[Customer Personality Analysis – Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis?resource=download)


---

Run the script with:

```bash
python preprocessing.py

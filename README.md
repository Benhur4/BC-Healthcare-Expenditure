# Predicting Canadian Provincial Healthcare Expenditures

This project forecasts changes in per-capita healthcare expenditure across Canadian provinces using historical healthcare spending and demographic data from CIHI and Statistics Canada.

It was completed as a term paper for **ECON 484: Applied Machine Learning Economics** (Spring 2025, SFU).

## Key Features

- **Data sources**:  
  - [CIHI National Health Expenditure Trends](https://www.cihi.ca/en/national-health-expenditure-trends)  
  - [Statistics Canada Demographics](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000501)

- **Objective**:  
  Predict next-year change in per-capita healthcare spending for policy planning and fiscal sustainability analysis.

- **Models considered**:  
  - Linear Regression (OLS)  
  - Random Forest  
  - XGBoost

- **Best model**:  
  Random Forest with tuned hyperparameters (`mtry = 6`, `ntree = 200`), validated via stratified 10-fold cross-validation.

- **Performance**:  
  Final holdout MSE: 11.94

## Usage

The main analysis is in `Term_301558625.Rmd`. To run this project:

1. Open the RMarkdown file in RStudio.
2. Ensure required libraries are installed: `randomForest`, `xgboost`, `tidyverse`, etc.
3. Knit to HTML or PDF for output.

## Disclaimer

Note: The CIHI and Statistics Canada data used here should be obtained directly from their official sources for any further work or redistribution.

---

## License

This project is shared under the MIT License. See `LICENSE` file for details.


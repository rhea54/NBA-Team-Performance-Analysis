# NBA-Team-Performance-Analysis

## Project Overview

This project aims to identify and analyze the key factors that influence the number of wins for NBA teams. By leveraging historical data and applying various regression models, we pinpoint the most significant predictors of team success and provide actionable insights. This analysis helps in understanding the critical metrics that drive success in NBA basketball.


## Project Steps

1. **Data Collection**: Fetching NBA team performance data using the `nba_api` library.
2. **Data Preparation**: Cleaning the data, handling missing values, and generating additional features such as 2-point percentage and dummy variables for teams and seasons.
3. **Exploratory Data Analysis (EDA)**: Visualizing the data distribution and relationships between variables.
4. **Modeling**: Training Ridge, Lasso, and ElasticNet regression models and evaluating their performance using R-squared values.
5. **Results Interpretation**: Identifying the most impactful features and understanding their influence on team performance.

## Notebooks

- `01_data_collection.ipynb`: Notebook for data collection from the NBA API.
- `02_data_preparation.ipynb`: Notebook for data cleaning and feature engineering.
- `03_exploratory_data_analysis.ipynb`: Notebook for EDA and visualizations.
- `04_modeling.ipynb`: Notebook for model training and evaluation.
- `05_results_interpretation.ipynb`: Notebook for interpreting the model results and identifying significant features.

## Scripts

- `data_collection.py`: Script for fetching data from the NBA API.
- `data_preparation.py`: Script for preparing the data.
- `modeling.py`: Script for training and evaluating regression models.
- `utils.py`: Utility functions used across various scripts.

## Visualizations

- `distribution_of_wins.png`: Histogram showing the distribution of wins across NBA teams.
- `fg_pct_vs_wins.png`: Scatter plot showing the relationship between field goal percentage and wins.
- `correlation_heatmap.png`: Heatmap showing the correlation coefficients between different performance metrics.
- `top_10_features.png`: Bar chart showing the top 10 features by coefficient value from the ElasticNet model.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/NBA-Team-Performance-Analysis.git
    cd NBA-Team-Performance-Analysis
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Data Collection**:
    - Run the data collection script to fetch data from the NBA API:
      ```bash
      python scripts/data_collection.py
      ```

2. **Data Preparation**:
    - Run the data preparation script to clean and process the data:
      ```bash
      python scripts/data_preparation.py
      ```

3. **Modeling**:
    - Run the modeling script to train regression models and save the results:
      ```bash
      python scripts/modeling.py
      ```

4. **Results Interpretation**:
    - Run the utils script to display and save the top features:
      ```bash
      python scripts/utils.py
      ```

## Results

The analysis identifies key metrics such as field goal percentage (FG_PCT), three-point percentage (FG3_PCT), defensive rebounds (DREB), steals (STL), and turnovers (TOV) as significant predictors of team success. ElasticNet regression outperformed other models with an R-squared value of 98.55%, highlighting its effectiveness in handling multicollinearity and performing feature selection.

### Key Findings
1. **Shooting Efficiency**: Both FG_PCT and FG3_PCT are strong positive predictors of team success, highlighting the importance of efficient shooting.
2. **Rebounding and Defense**: Defensive rebounds (DREB) and total rebounds (REB), along with steals (STL), are crucial for winning games, emphasizing the role of defense.
3. **Turnovers**: The negative impact of turnovers (TOV) on wins underscores the need to minimize mistakes and maintain possession.
4. **Non-linear Effects**: Polynomial terms like STL^2 and SEASON_2022-23^2 show that some relationships are not purely linear, indicating more complex dynamics in performance metrics.
5. **Team and Season-Specific Variations**: Dummy variables for specific teams and seasons capture unique effects that might not be generalizable but are significant for those particular cases.

## Acknowledgments

- Thanks to the NBA API developers for providing an accessible interface to NBA data.
- Inspired by the data science community for continuous learning and sharing of knowledge.

#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

def prepare_data(df):
    """
    Prepare the NBA data for analysis by selecting relevant columns and creating new features.

    Parameters:
    df (pd.DataFrame): DataFrame containing raw NBA data.

    Returns:
    pd.DataFrame: DataFrame with relevant features and dummy variables.
    """
    relevant_columns = ['TEAM_ID', 'SEASON', 'FG3A', 'FG3M', 'FG3_PCT', 'FG_PCT', 'W', 'FGA', 'FGM', 'FTA', 'FTM', 
                        'REB', 'AST', 'TOV', 'DREB', 'BLK', 'STL']
    df = df[relevant_columns].copy()

    # Convert percentages to human-readable format
    df['FG3_PCT'] = df['FG3_PCT'] * 100
    df['FG_PCT'] = df['FG_PCT'] * 100

    # Calculate 2-point percentage (2P_PCT)
    df['2P_PCT'] = (df['FGM'] - df['FG3M']) / (df['FGA'] - df['FG3A']) * 100

    # Create dummy variables for teams and seasons
    df = pd.get_dummies(df, columns=['TEAM_ID', 'SEASON'], drop_first=True)

    return df

def main():
    raw_data = pd.read_csv('data/raw/raw_data.csv')
    prepared_data = prepare_data(raw_data)
    prepared_data.to_csv('data/processed/prepared_data.csv', index=False)
    print("Data preparation completed. Prepared data saved to data/processed/prepared_data.csv")

if __name__ == "__main__":
    main()


# In[ ]:





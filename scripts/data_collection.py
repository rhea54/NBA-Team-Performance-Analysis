#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats

def fetch_nba_data(seasons):
    """
    Fetch NBA data for the given seasons from the NBA API.

    Parameters:
    seasons (list): List of seasons to fetch data for.

    Returns:
    pd.DataFrame: Concatenated DataFrame of all seasons.
    """
    league_stats_df_list = []
    for season in seasons:
        league_stats = leaguedashteamstats.LeagueDashTeamStats(season=season, measure_type_detailed_defense='Base')
        league_stats_df = league_stats.get_data_frames()[0]
        league_stats_df['SEASON'] = season  # Add season information
        league_stats_df_list.append(league_stats_df)
    return pd.concat(league_stats_df_list, ignore_index=True)

def main():
    seasons = ['2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18', '2016-17', '2015-16', '2014-15']
    raw_data = fetch_nba_data(seasons)
    raw_data.to_csv('data/raw/raw_data.csv', index=False)
    print("Data collection completed. Raw data saved to data/raw/raw_data.csv")

if __name__ == "__main__":
    main()


# In[ ]:





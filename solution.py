import numpy as np
import pandas as pd

def load_players(file_path):
    return pd.read_csv("C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\cricket_players_analysis\\data\\players.csv")

def load_matches(file_path):
    return pd.read_csv("C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\cricket_players_analysis\\data\\matches.csv")

def merge_players_matches(players_df, matches_df):
    return pd.merge(players_df, matches_df, on="PlayerID")

def total_runs_per_team(merged_df):
    return merged_df.groupby('Team')['Runs'].sum().reset_index()

def calculate_strike_rate(merged_df):
    return merged_df.assign(StrikeRate=(merged_df['Runs'] / merged_df['Balls']) * 100)[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]

def runs_agg_per_player(merged_df):
    return merged_df.groupby(['PlayerID', 'Name'])['Runs'].agg(['mean', 'min', 'max']).reset_index()[['PlayerID', 'Name', 'mean', 'min', 'max']]

def avg_age_by_role(players_df):
    return players_df.groupby('Role')['Age'].mean().reset_index()

def total_matches_per_player(matches_df):

    # Step 1: Get counts (index: PlayerID, column: count)
    counts = matches_df.groupby("PlayerID").size().reset_index(name="MatchCount")
    return counts

    # Step 2: Rename columns explicitly and cleanly
    counts = counts.rename(columns={'MatchID': 'MatchCount'})

    # Ensure columns are in correct order
    counts = counts[['PlayerID', 'TotalMatches']]
    return counts

    max_wickets = merged_df['Wickets'].max()
    return merged_df.loc[merged_df['Wickets'] == max_wickets, ['PlayerID', 'Name', 'Wickets']]

def top_wicket_takers(merged_df):
    wickets = merged_df.groupby(["PlayerID", "Name"], as_index=False)["Wickets"].sum()
    top3 = wickets.sort_values("Wickets", ascending=False).head(3)
    return top3

def avg_strike_rate_per_team(merged_df):
    df = merged_df.copy()
    df["StrikeRate"] = (df["Runs"] / df["Balls"]) * 100
    result = df.groupby("Team", as_index=False)["StrikeRate"].mean()
    return result

def catch_to_match_ratio(merged_df):
    catches = merged_df.groupby("PlayerID", as_index=False)["Catches"].sum()
    matches = merged_df.groupby("PlayerID").size().reset_index(name="MatchCount")
    merged = pd.merge(catches, matches, on="PlayerID")
    merged["CatchToMatchRatio"] = merged["Catches"] / merged["MatchCount"]
    result = merged[["PlayerID", "CatchToMatchRatio"]] 
    return result 






import os
import pandas as pd

from pprint import pprint
from pandas import DataFrame
from pandas.api.types import is_numeric_dtype, is_string_dtype


def get_unique_champs_from_df(df: DataFrame, columns: list[str]) -> list[int]:
    """Given a DataFrame containing champions and a list of relevant columns,
    extract the unique champions in the dataframe.

    Args:
        df (DataFrame): A DataFrame containing champions.
        columns (list[str]): A list of relevant columns in said DataFrame containing champions.

    Returns:
        set[int]: A list containing the unique champions (as ids) in the dataframe.
    """

    cols = df[columns]
    flattened = cols.to_numpy().flatten().tolist()

    return list(set(flattened))


def create_id_champ_map(
    src: str = "../data/ChampionTbl.csv", reverse_map=False
) -> dict[int, str]:
    """Create a dictionary that maps ids to champion names using a CSV file.

    Args:
        src (str, optional): A path to the CSV file. Defaults to "../data/ChapionTbl.csv".

    Returns:
        dict[int, str]: A dictionary containing id to champion mappings.
    """
    csv = pd.read_csv(src)
    mapping = {}

    if len(csv.columns) != 2:
        raise ValueError(
            "The CSV file should contain only two columns: [id] | [champion_name].\n"
            + f"Columns: {csv.columns}"
        )

    if not is_numeric_dtype(csv[csv.columns[0]].dtype):
        raise ValueError(
            f"Invalid Type: The first column in the CSV file should be an id.\n"
            + f"Type: {type(csv.iloc[0].dtype)}"
        )

    if not is_string_dtype(csv[csv.columns[1]].dtype):
        raise ValueError(
            "Invalid Type: The second column in the CSV file should be a string corresponding"
            + "to the champion name.\n"
            + f"Type: {type(csv.iloc[1].dtype)}"
        )

    for idx, row in csv.iterrows():
        id = row.iloc[0]
        champ = row.iloc[1]

        if reverse_map:
            mapping[champ] = id
        else:
            mapping[id] = champ

    return mapping


def get_win_counts(df: DataFrame, columns: list[str]) -> tuple[int, int]:
    """Takes a DataFrame containing the wins for the red team and blue teams and returns the counts
    for each team as a tuple.

    Input Format:
    - 1st Index -> Red Team
    - 2nd Index -> Blue Team

    Answer format will be the same.

    Args:
            df (DataFrame): The DataFrame containing the wins for each team.
            columns (list[str]): A list of strings containing the names of the columns that contain the wins for each team.

    Returns:
            tuple[int, int]: A tuple containing the counts for the wins on the red team and blue team respectively.
    """

    wins = df[columns]

    if len(columns) != 2:
        raise ValueError(
            "Invalid Number of Columns: There should be exactly two columns.\n"
            + f"Columns: {columns}"
        )

    wins = df[columns]
    red_team_value_counts = wins[columns[0]].value_counts()

    red_team_wins = red_team_value_counts[1]
    blue_team_wins = red_team_value_counts[0]

    return (red_team_wins, blue_team_wins)

import os
import pandas as pd

from pprint import pprint
from pandas import DataFrame
from pandas.api.types import is_numeric_dtype, is_string_dtype

from sklearn.preprocessing import MultiLabelBinarizer


RANK_COLORS = {
    "Iron": "#51484a",
    "Bronze": "#a35869",
    "Silver": "#989ea3",
    "Gold": "#f1ac46",
    "Platinum": "#15bdd8",
    "Emerald": "#33c4b3",
    "Diamond": "#3543cc",
    "Master": "#9d1357",
    "Grandmaster": "#c34017",
    "Challenger": "#f0af31",
}

RANK_ORDER = [
    "Iron",
    "Bronze",
    "Silver",
    "Gold",
    "Platinum",
    "Emerald",
    "Diamond",
    "Master",
    "Grandmaster",
    "Challenger",
]


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


def create_one_hot_encoding(
    df: DataFrame,
    blue_champ_cols: list[str],
    red_champ_cols: list[str],
    champs: list[int],
    names=False,
) -> DataFrame:
    """Given a DataFrame containing rows of matches and a list of champions, create a
    one-hot encoding for the champions in the dataframe.

    Args:
        df (DataFrame): A DataFrame containing rows of matches.
        blue_champ_cols (list[str]): The names of the columns containing the champions on the blue team.
        red_champ_cols (list[str]): The names of the columns containing the champions on the red team.
        champs (list[int]): A list of ids corresponding to unique champions in the dataset.

    Returns:
        DataFrame: A new DataFrame containing a one-hot encoding for the champions in all matches..
    """

    blue_champ_cols_values = df[blue_champ_cols].values.tolist()
    red_champ_cols_values = df[red_champ_cols].values.tolist()
    other_cols = df.drop(columns=red_champ_cols + blue_champ_cols)

    binarizer = MultiLabelBinarizer(classes=champs)

    ohe_blue_champs_cols = pd.DataFrame(
        binarizer.fit_transform(blue_champ_cols_values), columns=champs, index=df.index
    )

    ohe_red_champs_cols = pd.DataFrame(
        binarizer.fit_transform(red_champ_cols_values), columns=champs, index=df.index
    )

    # Create difference encoding: positive if champion is on blue team, negative if on red team
    champ_diff = ohe_blue_champs_cols - ohe_red_champs_cols

    stacked = pd.concat(
        [champ_diff, other_cols], axis=1, join="inner"
    )

    if names:
        stacked = stacked.rename(columns=create_id_champ_map())

    return stacked

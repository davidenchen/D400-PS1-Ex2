import pandas as pd
from typing import List


def keep_countries(df: pd.DataFrame, countries: List[str]) -> pd.DataFrame:
    try:
        return df[df["Country Name"].isin(countries)]
    except IndexError:
        raise IndexError("Country Name not in data frame columns")


def drop_cols(df: pd.DataFrame, cols_to_drop: List[str]) -> pd.DataFrame:
    return df.drop(cols_to_drop, axis=1)


def reshape_long(df: pd.DataFrame, id_vars: str,
                 var_name: str, value_name: str) -> pd.DataFrame:
    return df.melt(id_vars, var_name=var_name, value_name=value_name)

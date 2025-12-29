import pandas as pd

def get_unique_sort(_df: pd.DataFrame, _str: str) -> pd.DataFrame:
    new_df = _df[_str].unique()
    new_df.sort()
    return new_df

def sort_dict(_dict: dict, _reverse: bool=True) -> dict:
    sorted_dict = {k: v for k, v in sorted(_dict.items(), key=lambda item: item[1], reverse=_reverse)}
    return sorted_dict

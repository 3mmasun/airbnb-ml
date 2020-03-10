import pandas as pd

def drop_rows_occurs_less_than(df, columnName, low_bound):
    counts = df[columnName].value_counts()
    to_remove = counts[counts <= low_bound].index
    new_df = df[~df[columnName].isin(to_remove)]
    return new_df


def drop_rows_with_values(df, columnName, values):
    new_df = df[~df[columnName].isin(values)]
    print(new_df)
    return new_df

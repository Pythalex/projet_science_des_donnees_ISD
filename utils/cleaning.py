import numpy as np

def print_conflictual_information(df):
    """
    Print conflictual information as multiple rows of the same day but with different number
    of confirmed cases according to each source.
    """

    for d in df["date"].unique():
        s = df[np.logical_and(df["maille_code"] == "FRA", df["date"] == d)]["cas_confirmes"].dropna()
        if s.size > 1:
            if s.drop_duplicates().size > 1:
                print(d)
                print(s)


def keep_only_france(df):
    """
    Returns dataframe with only rows concerning whole france
    """
    return df[df["maille_code"] == "FRA"]


def drop_NA_confirmed_cases(df):
    """
    Returns a dataframe where rows with N/A confirmed cases have been dropped
    """
    return df.drop(df[df["cas_confirmes"].isna()].index)


def keep_only_first_row_by_date(df):
    """
    Keep only one row for each unique date, keep the first that occurs.
    """
    return df.groupby("date", as_index=False).first()


def interpolate_nan(df, feature):
    """
    replaces nan in given feature by linear interpolation
    """
    col = df[feature]
    nan_index = np.where(col.isna())
    xp = np.setdiff1d(col.index, nan_index)
    yp = col[xp]
    interp = np.interp(nan_index, xp, yp)

    df_copy = df.copy()

    for num, idx in enumerate(nan_index):
        df_copy.loc[idx, feature] = interp[num]
        
    return df_copy
import pandas as pd

ALLOWED_BASELINES = [
    "load_lag_1h",
    "load_lag_24h",
    "load_roll_24h",
    "load_roll_7d",
]


def naive_model_load(
    test_df: pd.DataFrame, predictor_col: str = "load_lag_1h"
) -> pd.Series:
    """
    Predicts the target variable using one of the allowed baseline predictor columns.

    Parameters
    ----------
    test_df : pd.DataFrame
        Test dataset containing the predictor column.
    predictor_col : str, optional
        Name of the predictor column to use for prediction.
        Must be one of: 'load_lag_1h', 'load_lag_24h', 'load_roll_24h', 'load_roll_7d'.

    Returns
    -------
    pd.Series
        Series of predictions based on the selected baseline predictor.

    Raises
    ------
    ValueError
        If the predictor column is not one of the allowed options or not present in the DataFrame.
    """
    if predictor_col not in ALLOWED_BASELINES:
        raise ValueError(
            f"Invalid predictor_col '{predictor_col}'. Must be one of: {ALLOWED_BASELINES}"
        )
    if predictor_col not in test_df.columns:
        raise ValueError(f"Column '{predictor_col}' not found in test_df.")

    return test_df[predictor_col].copy()


def mean_model(
    train_df: pd.DataFrame, test_df: pd.DataFrame, target: str = "total_load_actual"
) -> pd.Series:
    """
    Generate constant predictions using the mean of the target variable from the training set.

    This is a simple baseline model that ignores all temporal structure
    and predicts the same average value for every timestamp in the test set.

    Parameters
    ----------
    train_df : pd.DataFrame
        Training dataset used to compute the mean of the target variable.
    test_df : pd.DataFrame
        Test dataset used to determine the length and index of the predictions.
    target : str, optional
        Name of the target variable. Default is "total_load_actual".

    Returns
    -------
    pd.Series
        Predicted values as a constant series equal to the training mean.
    """
    mean_value = train_df[target].mean()
    return pd.Series([mean_value] * len(test_df), index=test_df.index)

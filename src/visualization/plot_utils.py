import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Union


def set_plot_style() -> None:
    """Sets a unified visual style for all plots in the project."""
    sns.set_theme(style="whitegrid", palette="Set2")
    plt.rcParams.update(
        {
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 10,
            "figure.figsize": (10, 6),
            "axes.grid": True,
            "grid.alpha": 0.3,
        }
    )


def plot_predictions(
    y_true: Union[pd.Series, np.ndarray],
    y_pred: Union[pd.Series, np.ndarray],
    title: str = "Predictions vs Actual",
    label: str = "Model",
    n: int = 168,
) -> None:
    """
    Plots the actual vs predicted values for a given number of time steps.
    """
    set_plot_style()
    y_true_arr = np.asarray(y_true)
    y_pred_arr = np.asarray(y_pred)

    plt.plot(y_true_arr[:n], label="Actual", color="black")
    plt.plot(y_pred_arr[:n], label=label, linestyle="--", color="royalblue")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Load (MW)")
    plt.legend()
    plt.tight_layout()
    plt.show()

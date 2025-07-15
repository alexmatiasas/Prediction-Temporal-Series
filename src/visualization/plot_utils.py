import matplotlib.pyplot as plt
import seaborn as sns

# General plot style settings
def set_plot_style():
    """Sets a unified visual style for all plots in the project."""
    sns.set_theme(style="whitegrid", palette="Set2")
    plt.rcParams.update({
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "figure.figsize": (10, 6),
        "axes.grid": True,
        "grid.alpha": 0.3,
    })

# Real vs predicted plots
def plot_predictions(y_true, y_pred, title="Predictions vs Actual", label="Model", n=168):
    """
    Plots the actual vs predicted values for a given number of time steps.
    
    Parameters:
        y_true (array-like): True target values.
        y_pred (array-like): Predicted values.
        title (str): Plot title.
        label (str): Label for predicted line.
        n (int): Number of points to show (default: 168 → 7 days hourly).
    """
    set_plot_style()
    plt.plot(y_true[:n].values, label="Actual", color="black")
    plt.plot(y_pred[:n], label=label, linestyle="--", color="royalblue")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Load (MW)")
    plt.legend()
    plt.tight_layout()
    plt.show()
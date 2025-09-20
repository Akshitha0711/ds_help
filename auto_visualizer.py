import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional

def auto_visualize(df: pd.DataFrame, plot_type: str = 'auto'):
    if plot_type == 'heatmap':
        return plot_correlation_heatmap(df)

    for col in df.columns:
        fig, ax = plt.subplots(figsize=(6, 4))
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(df[col].dropna(), kde=True, ax=ax)
        else:
            sns.countplot(x=df[col], ax=ax, order=df[col].value_counts().index)
        ax.set_title(f"{col}")
        plt.show()

def plot_correlation_heatmap(df: pd.DataFrame, method: str = 'pearson'):
    corr = df.corr(method=method, numeric_only=True)
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()

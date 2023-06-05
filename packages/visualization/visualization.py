import ast
import base64
import io
from typing import Counter
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

colors = sns.color_palette('Blues_d')[0:6]
matplotlib.rcParams['figure.facecolor'] = 'white'

# taken from the example project
def fig_to_base64(fig):
    """
    Convert the figure to base64 string

    Parameters
    ----------
    fig: `matplotlib.figure`

    Returns
    -------
    `str` The img HTML tag in base64 format.
    """
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    img_data = base64.b64encode(img.getvalue()).decode('utf-8')

    return f'<img src="data:image/png;base64, {img_data}">'


def plot_salary_estimate(data: pd.DataFrame, store_file=False) -> str:
    fig = plt.figure(figsize=(15, 6))
    data["Salary"].value_counts().plot(kind='bar')
    plt.xticks(rotation=90)
    plt.title("Salary Estimate Distribution")

    if(store_file):
        plt.savefig("/result/salary_estimate.png",
                    dpi=300, bbox_inches="tight")
    return fig_to_base64(fig)

def plot_box_adjusted_by_loc(data: pd.DataFrame, store_file=False) -> str:
    unique_locations = data["Location"].unique()
    num_loc = len(unique_locations)

    colors = plt.cm.get_cmap('Set3', num_loc)
    fig, ax = plt.subplots(figsize=(12, 6))
    boxplot = ax.boxplot([data[data["Location"] == loc]["Adjusted salary"] for loc in unique_locations], patch_artist=True)

    # Assign a different color to each boxplot
    for patch, color in zip(boxplot['boxes'], colors(range(num_loc))):
        patch.set_facecolor(color)

    ax.set_title("Adjusted salary by location")
    ax.set_ylabel("Adjusted salary")
    ax.set_xlabel("Location")
    ax.set_xticklabels(unique_locations, rotation=90)
    if(store_file):
        plt.savefig("/result/adjusted_salary_by_loc.png",
                    dpi=300, bbox_inches="tight")
    return fig_to_base64(fig)

def plot_average_per_column(df, col, col2, color):
    avg = {}
    for i in df[col].unique():
        if i != "Not Available" and i != "Unknown":
            avg[i] = df[df[col] == i][col2].mean()
    
    # sort the dictionary by value
    avg = dict(sorted(avg.items(), key=lambda item: item[1], reverse=True))

    fig = plt.figure(figsize=(12, 6))
    plt.bar(avg.keys(), avg.values(), color=color)
    plt.title("Average " + col2 + " per " + col + "")
    plt.xlabel(col)
    plt.xticks(rotation=90)
    plt.ylabel("Average " + col2)
    return fig

def plot_average_rating_by_loc(data: pd.DataFrame, store_file=False) -> str:
    avg_rating_per_loc = plot_average_per_column(data, "Location", "Rating", colors[0])

    if(store_file):
        plt.savefig("/result/average_rating_per_loc.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_rating_per_loc)

def plot_average_rating_by_industry(data: pd.DataFrame, store_file=False) -> str:
    avg_rating_ownership = plot_average_per_column(data, "Type of ownership", "Rating", colors[1])

    if(store_file):
        plt.savefig("/result/average_rating_per_industry.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_rating_ownership)

def plot_average_adjusted_salary_by_loc(data: pd.DataFrame, store_file=False) -> str:
    avg_adjusted_salary_per_loc = plot_average_per_column(data, "Location", "Adjusted salary", colors[4])

    if(store_file):
        plt.savefig("/result/average_adjusted_salary_per_loc.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_adjusted_salary_per_loc)

def plot_average_adjusted_salary_by_industry(data: pd.DataFrame, store_file=False) -> str:
    avg_adjusted_salary_per_ownership = plot_average_per_column(data, "Type of ownership", "Adjusted salary", colors[5])

    if(store_file):
        plt.savefig("/result/average_adjusted_salary_per_industry.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_adjusted_salary_per_ownership)

def plot_average_combined_rank_per_location(data: pd.DataFrame, store_file=False) -> str:
    avg_combined_rank_per_loc = plot_average_per_column(data, "Location", "Combined rank", colors[2])

    if(store_file):
        plt.savefig("/result/average_combined_rank_per_loc.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_combined_rank_per_loc)

def plot_adjutsed_and_rank(data: pd.DataFrame, store_file=False) -> str:
    df = data[['Adjusted salary', 'Combined rank']]
    plt.figure(figsize=(15, 6))
    plt.scatter(df['Adjusted salary'], df['Combined rank'])
    plt.title("Adjusted salary vs Combined rank")
    plt.xlabel("Adjusted salary")
    plt.ylabel("Combined rank")
    
    if(store_file):
        plt.savefig("/result/adjusted_salary_vs_combined_rank.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(plt)

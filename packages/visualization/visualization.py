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
    data["Salary Estimate"].value_counts().plot(kind='bar')
    plt.xticks(rotation=90)
    plt.title("Salary Estimate Distribution")

    if(store_file):
        plt.savefig("/result/salary_estimate.png",
                    dpi=300, bbox_inches="tight")
    return fig_to_base64(fig)

def plot_box_adjusted_by_state(data: pd.DataFrame, store_file=False) -> str:
    data = data[data["State"].isin(["NY", "CA", "FL", "IL", "TX", "PA", "NC", "WA", "CO"])]
    unique_states = data["State"].unique()
    num_states = len(unique_states)


    colors = plt.cm.get_cmap('Set3', num_states)
    fig, ax = plt.subplots(figsize=(12, 6))
    boxplot = ax.boxplot([data[data["State"] == state]["Adjusted salary"] for state in unique_states], patch_artist=True)

    # Assign a different color to each boxplot
    for patch, color in zip(boxplot['boxes'], colors(range(num_states))):
        patch.set_facecolor(color)

    ax.set_title("Adjusted salary by state")
    ax.set_ylabel("Adjusted salary")
    ax.set_xlabel("State")
    ax.set_xticklabels(unique_states)
    if(store_file):
        plt.savefig("/result/adjusted_salary_by_state.png",
                    dpi=300, bbox_inches="tight")
    return fig_to_base64(fig)

# get the average rating for each state
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

def plot_average_rating_by_state(data: pd.DataFrame, store_file=False) -> str:
    avg_rating_per_state = plot_average_per_column(data, "State", "Rating", colors[0])

    if(store_file):
        plt.savefig("/result/average_rating_per_state.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_rating_per_state)

def plot_average_rating_by_industry(data: pd.DataFrame, store_file=False) -> str:
    avg_rating_ownership = plot_average_per_column(data, "Type of ownership", "Rating", colors[1])

    if(store_file):
        plt.savefig("/result/average_rating_per_industry.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_rating_ownership)

def plot_average_salary_by_state(data: pd.DataFrame, store_file=False) -> str:
    avg_salary_per_state = plot_average_per_column(data, "State", "Salary", colors[2])

    if(store_file):
        plt.savefig("/result/average_salary_per_state.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_salary_per_state)
    
def plot_average_salary_by_industry(data: pd.DataFrame, store_file=False) -> str:
    avg_salary_ownership = plot_average_per_column(data, "Type of ownership", "Salary", colors[3])

    if(store_file):
        plt.savefig("/result/average_salary_per_industry.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_salary_ownership)

def plot_average_adjusted_salary_by_state(data: pd.DataFrame, store_file=False) -> str:
    avg_adjusted_salary_per_state = plot_average_per_column(data, "State", "Adjusted salary", colors[4])

    if(store_file):
        plt.savefig("/result/average_adjusted_salary_per_state.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_adjusted_salary_per_state)

def plot_average_adjusted_salary_by_industry(data: pd.DataFrame, store_file=False) -> str:
    avg_adjusted_salary_per_ownership = plot_average_per_column(data, "Type of ownership", "Adjusted salary", colors[5])

    if(store_file):
        plt.savefig("/result/average_adjusted_salary_per_industry.png",
                    dpi=300, bbox_inches="tight")
        
    return fig_to_base64(avg_adjusted_salary_per_ownership)

def generate_salary_estimate_plot(
        filepath_dataset: str) -> str:

    data_analyst_jobs = pd.read_csv(filepath_dataset)

    plot_salary_estimate(data_analyst_jobs, True)

    return "salary_estimate.png"

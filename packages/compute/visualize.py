#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io

def visualize(df):
    meandf = df.groupby('Location').mean()
    generate_salary_barplot(meandf)
    # generate_coli_barplot(meandf)
    # generate_adjusted_salary_barplot(meandf)    
    # generate_salary_boxplot(df, meandf)
    # generate_adjusted_salary_boxplot(df)
    return "TODO: RETURN PLOT IN STDOUT"

def generate_salary_barplot(df: pd.DataFrame, store_file=False, return_base64=False) -> str:
    fig = plt.figure(figsize=(20, 10))
    plt.xticks(rotation=90)
    plt.title('Average Salary by Location')
    plt.xlabel('Location')
    plt.ylabel('Salary')
    sns.barplot(x=df.index, y=df['Salary'], order=df.sort_values('Salary', ascending=False).index)
    if(store_file):
        plt.savefig("/result/salary_barplot.png",
                    dpi=300, bbox_inches="tight")
    if(return_base64):
        return fig_to_base64(fig)
    else:
        return "salary_barplot.png"


# def generate_coli_barplot(df: pd.DataFrame, store_file=False) -> str:
#     plt.figure(figsize=(20, 10))
#     plt.xticks(rotation=90)
#     plt.title('Average Cost of Living Index by Location (lower is better)')
#     plt.xlabel('Location')
#     plt.ylabel('Cost of Living Index')
#     sns.barplot(x=df.index, y=df['Cost of Living Index'], order=df.sort_values('Cost of Living Index', ascending=True).index)
#     plt.savefig('coli_barplot.png')

# def generate_adjusted_salary_barplot(df: pd.DataFrame, store_file=False) -> str:
#     plt.figure(figsize=(20, 10))
#     plt.xticks(rotation=90)
#     plt.title('Average Adjusted Salary by Location')
#     plt.xlabel('Location')
#     plt.ylabel('Adjusted Salary')
#     sns.barplot(x=df.index, y=df['Adjusted salary'], order=df.sort_values('Adjusted salary', ascending=False).index)
#     plt.savefig('adjusted_salary_barplot.png')

# def generate_salary_boxplot(df, meandf):
#     plt.figure(figsize=(20, 10))
#     plt.xticks(rotation=90)
#     plt.title('Salary by Location')
#     plt.xlabel('Location')
#     plt.ylabel('Salary')
#     sns.boxplot(x=df['Location'], y=df['Salary'], order=df.sort_values(ascending=False).index)
#     plt.savefig('salary_boxplot.png')

# def generate_adjusted_salary_boxplot(df, meandf):
#     plt.figure(figsize=(20, 10))
#     plt.xticks(rotation=90)
#     plt.title('Adjusted Salary by Location')
#     plt.xlabel('Location')
#     plt.ylabel('Adjusted Salary')
#     sns.boxplot(x=df['Location'], y=df['Adjusted salary'], order=meandf.sort_values('Adjusted salary', ascending=False).index)
#     plt.savefig('adjusted_salary_boxplot.png')

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
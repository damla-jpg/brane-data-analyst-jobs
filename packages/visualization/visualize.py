#!/usr/bin/python3
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def visualize():
    # !!! TODO: Find a way to get turn the input into a datafram
    df = json.loads(os.environ['INPUT'])
    meandf = df.groupby('Location').mean()
    generate_salary_barplot(meandf)
    generate_coli_barplot(meandf)
    generate_adjusted_salary_barplot(meandf)    
    generate_salary_boxplot(df, meandf)
    generate_adjusted_salary_boxplot(df)
    return "TODO: RETURN PLOT IN STDOUT"

def generate_salary_barplot(df):
    plt.figure(figsize=(20, 10))
    plt.xticks(rotation=90)
    plt.title('Average Salary by Location')
    plt.xlabel('Location')
    plt.ylabel('Salary')
    sns.barplot(x=df.index, y=df['Salary'], order=df.sort_values('Salary', ascending=False).index)
    # plt.savefig('salary_barplot.png')

def generate_coli_barplot(df):
    plt.figure(figsize=(20, 10))
    plt.xticks(rotation=90)
    plt.title('Average Cost of Living Index by Location (lower is better)')
    plt.xlabel('Location')
    plt.ylabel('Cost of Living Index')
    sns.barplot(x=df.index, y=df['Cost of Living Index'], order=df.sort_values('Cost of Living Index', ascending=True).index)
    # plt.savefig('coli_barplot.png')

def generate_adjusted_salary_barplot(df):
    plt.figure(figsize=(20, 10))
    plt.xticks(rotation=90)
    plt.title('Average Adjusted Salary by Location')
    plt.xlabel('Location')
    plt.ylabel('Adjusted Salary')
    sns.barplot(x=df.index, y=df['Adjusted salary'], order=df.sort_values('Adjusted salary', ascending=False).index)
    # plt.savefig('adjusted_salary_barplot.png')

def generate_salary_boxplot(df, meandf):
    plt.figure(figsize=(20, 10))
    plt.xticks(rotation=90)
    plt.title('Salary by Location')
    plt.xlabel('Location')
    plt.ylabel('Salary')
    sns.boxplot(x=df['Location'], y=df['Salary'], order=df.sort_values(ascending=False).index)
    # plt.savefig('salary_boxplot.png')

def generate_adjusted_salary_boxplot(df, meandf):
    plt.figure(figsize=(20, 10))
    plt.xticks(rotation=90)
    plt.title('Adjusted Salary by Location')
    plt.xlabel('Location')
    plt.ylabel('Adjusted Salary')
    sns.boxplot(x=df['Location'], y=df['Adjusted salary'], order=meandf.sort_values('Adjusted salary', ascending=False).index)
    # plt.savefig('adjusted_salary_boxplot.png')
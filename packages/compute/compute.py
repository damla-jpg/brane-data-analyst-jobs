#!/usr/bin/python3

import pandas as pd
import numpy as np
import json
import os
import sys

def compute():
    pd.options.mode.chained_assignment = None
    dataset = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/dataset.csv")
    coli = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/coli.csv")

    dataset = clean_data(dataset)

    dataset['State'] = dataset['Location'].apply(get_state)
    dataset['City'] = dataset['Location'].apply(lambda x: x.split(',')[0])
    
    dataset = dataset.merge(coli, how='left', left_on=['City', 'State'], right_on=['City', 'State'])
    dataset['Salary'] = dataset['Salary Estimate'].apply(get_salary_range)

    dataset = account_for_coli(dataset)

    output = dataset[['Location', 'Salary', 'Cost of Living Index', 'Adjusted salary']]
    return output

# generic data cleaning
def clean_data(df):
    df.drop(df.columns[0], axis=1, inplace=True)
    df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
    df.fillna("Not Available", inplace=True)
    df["Company Name"] = df["Company Name"].apply(lambda x: x.split('\n')[0])
    df["Size"] = df["Size"].apply(lambda x: x.split('employees')[0])
    df["Size"] = df["Size"].apply(lambda x: x.replace(" to ", "-"))
    df["Type of ownership"] = df["Type of ownership"].apply(lambda x: "Unknown" if x == "-1" else x)
    return df

# helper function for data cleaning to extract the state
def get_state(x):
    if x.count(',') > 1:
        return x.split(', ')[2]
    else:
        return x.split(', ')[1]

# convert salary range to concrete number we can work with
def get_salary_range(x):
    if x == '-1':
        return -1
    range_salary = x.split('-')
    n1 = range_salary[0].replace('$', '').replace('K', '').replace(' ', '')
    n2 = range_salary[1].replace('$', '').replace('K', '').replace(' ', '')
    
    range_salary = np.arange(int(n1), int(n2)+1, 1)
    range_salary = np.median(range_salary) * 1000
    return range_salary

def account_for_coli(df):
    df = df[df['Cost of Living Index'].notna()]
    df['Cost of Living Index'] = df['Cost of Living Index'] / 100

    # make a new column, salary adjusted for cost of living
    df['Adjusted salary'] = df['Salary'] / df['Cost of Living Index']
    df['Adjusted salary'] = df['Adjusted salary'].astype(int)
    return df
#!/usr/bin/python3

import pandas as pd
import numpy as np
import json
import os


def compute(data_path):
    pd.options.mode.chained_assignment = None
    dataset = pd.read_csv(f"{data_path}/dataset.csv")
    coli = pd.read_csv(f"{data_path}/coli.csv")
    us_sdr = pd.read_csv(f"{data_path}/us_sdr.csv")

    # dataset = clean_data(dataset)

    dataset['State'] = dataset['Location'].apply(get_state)
    dataset['City'] = dataset['Location'].apply(lambda x: x.split(',')[0])
    
    dataset = dataset.merge(coli, how='left', left_on=['City', 'State'], right_on=['City', 'State'])
    dataset['Salary'] = dataset['Salary Estimate'].apply(get_salary_range)

    dataset = account_for_coli(dataset)

    dataset = dataset.merge(us_sdr[['abbrv', 'overall_score']], how='left', left_on='State', right_on='abbrv')
    dataset = account_for_sdr(dataset)

    dataset = dataset[['Location', 'Type of ownership', 'Rating', 'Salary', 'Cost of Living Index', 'Adjusted salary', 'Combined rank']]

    new_path = '/result/dataset.csv'
    dataset.to_csv(new_path)
    return new_path

# generic data cleaning
def clean_data(df_path):
    df = pd.read_csv(f'{df_path}/dataset.csv')
    coli = pd.read_csv(f"{df_path}/coli.csv")
    us_sdr = pd.read_csv(f"{df_path}/us_sdr.csv")

    coli.to_csv('/result/coli.csv')
    us_sdr.to_csv('/result/us_sdr.csv')

    df.drop(df.columns[0], axis=1, inplace=True)
    df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
    df.fillna("Not Available", inplace=True)
    df["Company Name"] = df["Company Name"].apply(lambda x: x.split('\n')[0])
    df["Size"] = df["Size"].apply(lambda x: x.split('employees')[0])
    df["Size"] = df["Size"].apply(lambda x: x.replace(" to ", "-"))
    df["Type of ownership"] = df["Type of ownership"].apply(lambda x: "Unknown" if x == "-1" else x)

    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

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

def account_for_sdr(df):
    df['Adjusted salary rank'] = df['Adjusted salary'].rank(ascending=True)

    df['Adjusted salary rank'] = df['Adjusted salary rank'] / df['Adjusted salary rank'].max()
    
    df['overall_score'] = df['overall_score'] / 100
    
    df['Combined rank'] = 0.5* df['Adjusted salary rank'] + 0.5*df['overall_score']

    df = df.sort_values(by=['Combined rank'], ascending=True)
    return df
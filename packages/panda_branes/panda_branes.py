#!/usr/bin/python3

import pandas as pd
import numpy as np
import json
import os


'''Sample function to test the package'''
def hello_world():
    print('output: "Hello, World!"')


'''--------------------DATA EXPLORATION FUNCTIONS--------------------'''

def shape(data_path: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    shape = df.shape
    print(f'output: "{str(shape)}"')
    return shape

def dtypes(data_path: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    dtypes = df.dtypes
    print(f'output: "{str(dtypes)}"')
    return dtypes

def columns(data_path: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    columns = df.columns.tolist()
    print(f'output: "{str(columns)}"')
    return columns

def index(data_path: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    index = df.index.tolist()
    print(f'output: "{str(index)}"')
    return index

def describe(data_path: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    print(f'output: "{str(df.describe())}"')
    return df.describe()

def head(data_path: str, n: int):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    print(f'output: "{str(df.head(n))}"')
    return df.head(n)

def tail(data_path: str, n: int):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    print(f'output: "{str(df.tail(n))}"')
    return df.tail(n)

def loc(data_path: str, row: int, column: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    print(f'output: "{str(df.loc[row, column])}"')
    return df

def iloc(data_path: str, row: int, column: int):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    print(f'output: "{str(df.iloc[row, column])}"')
    return df

def describe_column(data_path: str, column_name: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    column = df[column_name]
    print(f'output: "{str(column.describe())}"')
    return column.describe()

def get_row(data_path: str, row: int):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    index = df.loc[row].tolist()
    print(f'output: "{str(index)}"')
    return index

def get_column(data_path: str, column_name: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    column = df[column_name].tolist()
    print(f'output: "{str(column)}"')
    return column

def get_column_value_counts(data_path: str, column_name: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    column = df[column_name]
    print(f'output: "{str(column.value_counts())}"')
    return column.value_counts()

def query(data_path: str, query: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    query_result = df.query(query)
    print(f'output: "{str(query_result)}"')
    return query_result

'''-------------------------------------------------------------------------------------'''




'''--------------------DATA MANIPULATION FUNCTIONS--------------------------------------'''

### Sorting functions.
def sort_index(data_path: str, axis: int, ascending: bool):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.sort_index(axis=axis, ascending=ascending)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def sort_values(data_path: str, by: str, axis: int, ascending: bool):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.sort_values(by=by, axis=axis, ascending=ascending)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path


### Cleaning functions.
def drop_row(data_path: str, row: int):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.drop(index=row)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def drop_column(data_path: str, column_name: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.drop(columns=column_name)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def drop_duplicates(data_path: str, keep: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.drop_duplicates(keep=keep)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def dropna(data_path: str, axis: int):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.dropna(axis=axis)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def fillna(data_path: str, value: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.fillna(value=value)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def replace(data_path: str, old_value: str, new_value: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.replace(to_replace=old_value, value=new_value)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

### Column manipulation functions.
def cast_column(data_path: str, column_name: str, dtype: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df[column_name] = df[column_name].astype(dtype)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def rename_column(data_path: str, old_column_name: str, new_column_name: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.rename(columns={old_column_name: new_column_name})
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
# (I actually didn't know this function existed)
def query_and_save(data_path: str, query: str):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    df = df.query(query)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

'''-------------------------------------------------------------------------------------'''




'''--------------------MULTI-DATASET FUNCTIONS------------------------------------------'''
def concat(data_path: str, other_data_path: str, axis: int):
    df1 = pd.read_csv(f'{data_path}/dataset.csv')
    df2 = pd.read_csv(f'{other_data_path}/dataset.csv')
    df = pd.concat([df1, df2], axis=axis)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

def merge(data_path: str, other_data_path: str, on: str, how: str):
    df1 = pd.read_csv(f'{data_path}/dataset.csv')
    df2 = pd.read_csv(f'{other_data_path}/dataset.csv')
    df = pd.merge(df1, df2, on=on, how=how)
    new_path = '/result/dataset.csv'
    df.to_csv(new_path)
    return new_path

'''-------------------------------------------------------------------------------------'''

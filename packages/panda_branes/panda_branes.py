#!/usr/bin/python3

import pandas as pd
import numpy as np
import json
import os


def hello_world(input):
    print(f'output: "Hello, {input}!"')
    

def get_columns(data_path):
    df = pd.read_csv(f'{data_path}/dataset.csv')
    columns = df.columns.tolist()
    print(f'output: "{str(columns)}"')
    return columns
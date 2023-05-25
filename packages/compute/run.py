#!/usr/bin/python3

import json
import os
import pandas as pd
import sys

def give_row(dataset_path: str, row: int):
  df = pd.read_csv(f"{dataset_path}/dataset.csv")
  print(f'output: "{df.head(row).tail(1)}"')
  return


def main():
  command = sys.argv[1]

  if command == "first_row":
    df = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/dataset.csv")
    print(f'output:"first: {df.head(1)}"')
    return

  if command == "second_row":
    df = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/dataset.csv")
    print(f'output: "second: {df.head(2).tail(1)}"')
    return
  

if __name__ == '__main__':
  main()

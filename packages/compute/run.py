#!/usr/bin/python3

import compute

import json
import os
import sys

def run_action(cmd, filepath):
  return {
    "clean_data": compute.clean_data,
    "hihi": compute.hihi
  }[cmd](filepath)


def main():
  command = sys.argv[1]

  if command == "compute":
    # dataset = compute.compute()
    # !!! TODO: Find a way to output the dataframe as text in a way we can decode it in visualize.py (base64?)
    return "IT WORKS!"

  filepath_out = run_action(command, json.loads(os.environ['FILEPATH']))
  # if command == "second_row":
  #   df = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/dataset.csv")
  #   print(f'output: "second: {df.head(2).tail(1)}"')
  #   return
  

if __name__ == '__main__':
  main()

#!/usr/bin/python3

import compute

import json
import os
import sys

def run_action(cmd, filepath):
  return {
    "clean_data": compute.clean_data,
  }[cmd](filepath)


def main():
  command = sys.argv[1]

  if command == "process_data":
    dataset = compute.compute(f"{json.loads(os.environ['FILEPATH_DATA'])}/dataset.csv", f"{json.loads(os.environ['FILEPATH_COLI'])}")
    # !!! TODO: Find a way to output the dataframe as text in a way we can decode it in visualize.py (base64?)
    return

  run_action(command, json.loads(os.environ['FILEPATH']))
  

if __name__ == '__main__':
  main()

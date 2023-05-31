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
    dataset = compute.compute(f"{json.loads(os.environ['FILEPATH_DATA'])}", f"{json.loads(os.environ['FILEPATH_COLI'])}")
    return

  run_action(command, json.loads(os.environ['FILEPATH']))
  

if __name__ == '__main__':
  main()

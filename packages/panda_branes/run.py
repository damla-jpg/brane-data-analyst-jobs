#!/usr/bin/python3

import panda_branes

import json
import os
import sys

def run_action_two_parameters(cmd, filepath, parameter1):
  return {
    "get_column": panda_branes.get_column,
    "describe_column": panda_branes.describe_column,
    "get_column_value_counts": panda_branes.get_column_value_counts,
  }[cmd](filepath, parameter1)


def main():
  command = sys.argv[1]

  if command == "hello_world":
    panda_branes.hello_world()
    return

  elif command == "get_column":
    out = panda_branes.get_column(f"{json.loads(os.environ['FILEPATH_DATA'])}", f"{json.loads(os.environ['COLUMN_NAME'])}")
    return

  f_out = run_action_two_parameters(command, json.loads(os.environ['FILEPATH']), json.loads(os.environ['PARAMETER1']))


if __name__ == '__main__':
  main()

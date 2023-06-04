#!/usr/bin/python3

import panda_branes

import json
import os
import sys


def run_action(cmd, filepath):
  return {
    "get_columns": panda_branes.get_columns,
  }[cmd](filepath)


def main():
  command = sys.argv[1]

  if command == "hello_world":
    # pandabranes.hello_world(json.loads(os.environ['FILEPATH']))
    print(f'output: "Hello, World!"')
    return

  f_out = run_action(command, json.loads(os.environ['FILEPATH']))


if __name__ == '__main__':
  main()

#!/usr/bin/python3

'''
Entry point for the pandas_branes package.

This package adapts a small part of the pandas library to work with Brane.
'''

import panda_branes

import json
import os
import sys


def convert_parameters(parameters):
  '''
  Utility function
  Converts the parameters from strings to their respective types.

  NOTE: Does not work for lists or dictionaries.
  '''
  if parameters == None:
    return None
  
  for i in range(len(parameters)):

    # Booleans
    if parameters[i] == "True":
      parameters[i] = True
    elif parameters[i] == "False":
      parameters[i] = False

    # Integers
    elif parameters[i].isdigit():
      parameters[i] = int(parameters[i])

    # Floats
    elif parameters[i].replace('.', '', 1).isdigit():
      parameters[i] = float(parameters[i])

    # Lists
    elif parameters[i][0] == '[' and parameters[i][-1] == ']':
      parameters[i] = parameters[i][1:-1].split(', ')

    # Dictionaries
    elif parameters[i][0] == '{' and parameters[i][-1] == '}':
      parameters[i] = json.loads(parameters[i])

    # Strings
    else:
      parameters[i] = str(parameters[i])
      
  return parameters


def run_action(cmd, filepath, *parameters):
  '''
  Runs the action specified by the command.

  Parameters:
    cmd (str): The command to run.
    filepath (str): The filepath to the file to run the command on.
    parameters (list): The parameters to pass to the command. (can be empty)
  '''
  func = getattr(panda_branes, cmd)
  return func(filepath, *parameters)


def main():
  command = sys.argv[1]

  if command == "hello_world":
    panda_branes.hello_world()
    return

  if 'PARAMETERS' in os.environ:
    params_str = json.loads(os.environ['PARAMETERS'])
    params = convert_parameters(params_str)

    run_action(command, json.loads(os.environ['FILEPATH']), *params)
    return
  
  run_action(command, json.loads(os.environ['FILEPATH']))


if __name__ == '__main__':
  main()

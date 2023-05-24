import json
import pandas as pd
import sys


def main():
  command = sys.argv[1]

  if command == "first_row":
    df = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/dataset.csv")
    print(f'output:"{df.head(1)}"')
    return

  if command == "second_row":
    df = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/dataset.csv")
    return df.head(2)

if __name__ == '__main__':
  main()

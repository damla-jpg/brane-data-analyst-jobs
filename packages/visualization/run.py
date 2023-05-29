#!/usr/bin/python3
import sys
import visualize

def main():
  command = sys.argv[1]

  if command == "visualize":
    visualize.visualize()
    print(f'output:')
    return

  # if command == "second_row":
  #   df = pd.read_csv(f"{json.loads(os.environ['FILEPATH'])}/dataset.csv")
  #   print(f'output: "second: {df.head(2).tail(1)}"')
  #   return
  

if __name__ == '__main__':
  main()

import os
import sys

def main():
  if len(sys.argv) != 2:
    print('Wrong number of command line arguments')
    return
  filepath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + sys.argv[1]
  if not os.path.isfile(filepath):
    print('file path is not a file.')
    return

  outfile = open(filepath + '.n', 'w')
  with open(filepath) as file:
    for line in file:
      if line.strip()[:5] == 'array':
        line = line.replace('array(', '')
        line = line.replace(', ', ' => ', 1)
        line = line.replace(')', '')
      outfile.write(line)

  outfile.close()

if __name__ == '__main__':
  main()

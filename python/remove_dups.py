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
    urls = list()
    for line in file:
      if line not in urls:
        urls.append(line)

  i = 0
  for url in urls:
    outfile.write(url)
    if i % 10 == 0:
      outfile.write('\n')
    i = i + 1

  outfile.close()

if __name__ == '__main__':
  main()

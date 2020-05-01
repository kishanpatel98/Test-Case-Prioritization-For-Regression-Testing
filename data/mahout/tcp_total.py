import subprocess
import sys
import ast
from collections import defaultdict


def main(argv):

    d = defaultdict(list)

    with open(str(sys.argv[1])) as fp, open('mahout-total-result.txt', 'w') as outfile:
        for line in fp:
            k, v = line[: line.index('):')+1], ast.literal_eval(line[line.index(':[') + 1:])
            d[k] += v

    #print(d)
        res = ''
        for x in sorted(d.keys(), key=lambda k: len(d[k]), reverse=True):
            res += x + ' ' + str(len(d[x])) + '\n'
        outfile.writelines(res)
    fp.close()
    outfile.close()

    arr = [];
    with open("faultsformatted.txt") as input:
        for line in input:
            #print(line)
            arr.append(line.strip())

    input.close();

    #print(str(arr))

    print(d.keys())

    #print(sum)


main(str(sys.argv[1]))

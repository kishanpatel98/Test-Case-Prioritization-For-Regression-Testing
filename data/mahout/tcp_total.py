import subprocess
import sys
import ast
from collections import defaultdict


def main(argv):

    d = defaultdict(list)
    with open(str(sys.argv[1])) as fp:
        for line in fp:
            k, v = line[: line.index('():') - 1], ast.literal_eval(line[line.index(':[') + 1:])
            d[k].append(v)

    print(dict(d))

main(str(sys.argv[1]))

import subprocess
import sys
import re

def main(argv):

    with open("output.txt", "w+") as output:
        subprocess.call(['java', '-jar', 'javacg-0.1-SNAPSHOT-static.jar', str(sys.argv[1])], stdout=output)
    output.close()

    match = "test"
    with open("output.txt") as input, open('filtered.txt', 'w') as newfile:
        for line in input:
            if ("test" in line and "C:" not in line):
                newfile.write(line)
    input.close()
    newfile.close()

    d = {}
    with open("filtered.txt") as input:
        for line in input:
            (key, val) = line.strip().split(" ")
            if str(key) in d:
                d[str(key)].append(val)
            else:
                d[str(key)] = [val]

    keys = []
    for key in d:
        keys.append(key)

    keys.sort()

    input.close()

    with open('mahout-coverage.txt', 'w') as outfile:
        for key in keys:
            #outfile.writelines(key.split('.')[-1] + "\n")
            outfile.writelines('{}:{}'.format(key, d[key]) + "\n")
            #outfile.writelines('{}:{}'.format(key.split('.')[-1], d[key]) + "\n")
    outfile.close()

main(str(sys.argv[1]))

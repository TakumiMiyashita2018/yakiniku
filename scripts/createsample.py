import sys

file_name = sys.argv

with open(file_name[1], "r") as file:
    with open(file_name[2], "w") as sample:
        for i in range(200):
            line = file.readline()
            sample.write(line)

import sys

file_name = sys.argv

with open(file_name[1], "w") as w:
    for i in range(2, len(file_name)):
        with open(file_name[i], 'r') as file:
            line = file.readline()
            while(line):
                w.write(line)
                line = file.readline()

import sys
import json

file_name = sys.argv

with open(file_name[1], "w") as w:
    with open(file_name[2], 'r') as file:
        line = file.readline()
        while(line):
            f_tmp = json.loads(line)
            del f_tmp["histogram"]
            del f_tmp["byteentropy"]
            json.dump(f_tmp, w)
            w.write("\n")
            line = file.readline()

import json
import sys
import tool

file_name = sys.argv

with open(file_name[2], 'w') as w:
    with open(file_name[1], 'r') as r:
        line = r.readline()
        f_tmp = json.loads(line)
        f_benign = tool.sortDictValue(f_tmp)
        line = r.readline()
        f_tmp = json.loads(line)
        f_maricious = tool.sortDictValue(f_tmp)

    for i in range(10):
        w.write(f_benign[i] + '\n')
    for i in range(10):
        w.write(f_maricious[i] + '\n')

#for i in range(10):
#    print(f_benign[i])

#for i in range(10):
#    print(f_maricious[i])

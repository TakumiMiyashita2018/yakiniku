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

    w.write('benign\n')
    for i in range(1,11):
        w.write(f_benign[i] + '\n')
    w.write('maricious\n')
    for i in range(1, 11):
        w.write(f_maricious[i] + '\n')

#print('benign: \n')
#for i in range(10):
#    print(f_benign[i])

#print('benign: \n')
#for i in range(10):
#    print(f_maricious[i])

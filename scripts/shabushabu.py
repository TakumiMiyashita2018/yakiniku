import sys
import json

file_name = sys.argv
a_benign = [0 for i in range(256)]
a_maricious = [0 for i in range(256)]
n_benign = n_maricious = 0

for i in range(3, len(file_name)):
    with open(file_name[i], 'r') as data:
        line = data.readline()
        while line:
            f_tmp = json.loads(line)
            l_tmp = f_tmp["average"]
            if f_tmp["label"]:
                for j in range(256):
                    a_maricious[j] = a_maricious[j] + (l_tmp[j] * f_tmp["number"])
                    n_maricious = n_maricious + f_tmp["number"]
            else :
                for j in range(256):
                    a_benign[j] = a_benign[j] + (l_tmp[j] * f_tmp["number"])
                    n_benign = n_benign + f_tmp["number"]
            line = data.readline()

for i in range(256):
    a_benign[i] = a_benign[i] / n_benign
    a_maricious[i] = a_maricious[i] / n_maricious

with open(file_name[1], 'w') as b:
    with open(file_name[2], 'w') as m:
        for i in range(256):
            b.write(str(a_benign[i]) + '\n')
            m.write(str(a_maricious[i]) + '\n')

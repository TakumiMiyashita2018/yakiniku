import sys
import tool
import json

file_name = sys.argv
n_benign = n_maricious = n_unlabeled = 0
l_benign = []
l_maricious = []

with open(file_name[1], 'w') as sample:
    for i in range(3, len(file_name)):
        with open(file_name[i], 'r') as file:
            line = file.readline()
            while line:
                f_tmp = json.loads(line)
                l_tmp = tool.normalization(f_tmp)
                if f_tmp["label"] == 0:
                    if l_benign:
                        for i in range(len(f_tmp["histogram"])):
                            l_benign[i] += l_tmp[i]
                    else:
                        l_benign += l_tmp
                    n_benign += 1
                elif f_tmp["label"] == 1:
                    if l_maricious:
                        for i in range(len(f_tmp["histogram"])):
                            l_maricious[i] += l_tmp[i]
                    else:
                        l_maricious += l_tmp
                    n_maricious += 1
                else:
                    n_unlabeled += 1
                json.dump({"normalized": l_tmp, "label": f_tmp["label"]}, sample)
                sample.write("\n")
                line = file.readline()

for i in range(len(l_benign)):
    l_benign[i] /= n_benign
for i in range(len(l_maricious)):
    l_maricious[i] /= n_maricious

benign = {
        "average": l_benign,
        "label": 0,
        "number": n_benign
}
maricious = {
        "average": l_maricious,
        "label": 1,
        "number": n_maricious
}

with open(file_name[2], "w") as file:
    json.dump(benign, file)
    file.write("\n")
    json.dump(maricious, file)

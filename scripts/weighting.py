import sys
import json
import tool

file_name = sys.argv

with open(file_name[1], "r") as v:
    line = v.readline()
    v_benign = json.loads(line)["variance"]
    line = v.readline()
    v_maricious = json.loads(line)["variance"]

with open(file_name[2], "r") as a:
    line = a.readline()
    a_benign = json.loads(line)["average"]
    line = a.readline()
    a_maricious = json.loads(line)["average"]

w_benign = []
w_maricious = []

for v in v_benign:
    w = v
    w_benign.append(v)

for v in v_maricious:
    w = v
    w_maricious.append(v)

dict = {"a_b": a_benign,
        "a_m": a_maricious,
        "w_b": w_benign,
        "w_m": w_maricious}

c_right = c_wrong = 0

with open(file_name[3], "r") as test:
    line = test.readline()
    while line:
        specimen = json.loads(line)
        n_specimen = tool.normalization(specimen)
        judge = tool.compare(dict, n_specimen)
        if judge:
            if specimen["label"] == 0:
                c_right += 1
            else:
                c_wrong += 1
        else:
            if specimen["label"] == 1:
                c_right += 1
            else:
                c_wrong += 1
        line = test.readline()

c_all = c_right + c_wrong
ratio = (c_right / c_all) * 100
print("{0} right answers, {1} wrong answers, {2}% right answer ratio.".format(c_right, c_wrong, ratio))

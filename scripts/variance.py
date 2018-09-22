import sys
import json
import statistics as ss
import tool

file_name = sys.argv

with open(file_name[1], "r") as ave:
    line = ave.readline()
    benign = json.loads(line)
    line = ave.readline()
    maricious = json.loads(line)
    l_benign = benign["average"]
    n_benign = benign["number"]
    l_maricious = maricious["average"]
    n_maricious = maricious["number"]

v_benign = [0.0 for i in range(len(l_benign))]
v_maricious = [0.0 for i in range(len(l_maricious))]
ll_benign = [[] for i in range(256)]
ll_maricious = [[] for i in range(256)]


with open(file_name[2], "r") as sample:
    line = sample.readline()

    while line:
        d_tmp = json.loads(line)
        l_sample = d_tmp["normalized"]
        if d_tmp["label"] == 0:
            for i in range(len(l_sample)):
                ll_benign[i].append(l_sample[i])
        elif d_tmp["label"] == 1:
            for i in range(len(l_sample)):
                ll_maricious[i].append(l_sample[i])
        line = sample.readline()

for i in range(256):
    v_benign[i] = ss.pvariance(ll_benign[i]) * (10 ** 5)
    v_maricious[i] = ss.pvariance(ll_maricious[i]) * (10 ** 5)

with open(file_name[3], "w") as v:
    json.dump({"variance": v_benign, "label": benign["label"]}, v)
    v.write("\n")
    json.dump({"variance": v_maricious, "label": maricious["label"]}, v)

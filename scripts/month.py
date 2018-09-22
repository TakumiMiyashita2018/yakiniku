import sys
import json

file_name = sys.argv
t_list = []

with open(file_name[1], "r") as file:
    line = file.readline()
    while line:
        l_tmp = json.loads(line)
        t_list.append(l_tmp["appeared"])
        line = file.readline()

t_list.sort()
median = t_list[len(t_list) // 2]

print("oldest:{0}, latest:{1}, median:{2}".format(t_list[0], t_list[-1], median))

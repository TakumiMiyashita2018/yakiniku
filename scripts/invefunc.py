import sys
import json
import bisect

file_name = sys.argv
f_benign = {"imports": {}, "exports": {}}
f_maricious = {"imports": {}, "exports": {}}

with open(file_name[1], 'r') as file:
    line = file.readline()
    while line:
        f_tmp = json.loads(line)
        i_dict = f_tmp["imports"]
        e_list = f_tmp["exports"]

        if f_tmp["label"] == 0:
            for list in i_dict.values():
                for item in list:
                    if item in f_benign["imports"]:
                        f_benign["imports"][item] = f_benign["imports"][item] + 1
                    else:
                        f_benign["imports"][item] = 1
#            for item in e_list:
#                if item in f_benign["exports"]:
#                    f_benign["exports"][item] = f_benign["exports"][item] + 1
#                else:
#                    f_benign["exports"][item] = 1

        if f_tmp["label"] == 1:
            for list in i_dict.values():
                for item in list:
                    if item in f_maricious["imports"]:
                        f_maricious["imports"][item] = f_maricious["imports"][item] + 1
                    else:
                        f_maricious["imports"][item] = 1
#            for item in e_list:
#                if item in f_maricious["exports"]:
#                    f_maricious["exports"][item] = f_maricious["exports"][item] + 1
#                else:
#                    f_maricious["exports"][item] = 1

        line = file.readline()

with open(file_name[2], 'w') as out:
    json.dump(f_benign['imports'], out)
    out.write("\n")
    json.dump(f_maricious['imports'], out)

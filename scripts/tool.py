def normalization(dict):
    sum = 0.0
    list = dict["histogram"]

    for num in list:
        sum += num

    for i in range(len(list)):
        list[i] /= sum

    return list

def sortDictValue(dict):
    ans = []
    for k, v in sorted(dict.items(), key = lambda x: -x[1]):
        ans.append(str(k) + ": " + str(v))
    return ans

def compare(dict, l_test):
    s_benign = s_maricious = 0

    for i in range(256):
        score = ((dict["a_b"][i] - l_test[i]) ** 2) * dict["w_b"][i]
        s_benign += score
        score = ((dict["a_m"][i] - l_test[i]) ** 2) * dict["w_m"][i]
        s_maricious += score

    if s_benign > s_maricious:
        return False
    else:
        return True

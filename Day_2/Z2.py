import re


def isSafe(niz):
    safe_vr = []
    i = 0
    while not safe_vr:
        if (niz[i] - niz[i+1]) > 0:
            safe_vr = [1, 2, 3]
        elif (niz[i] - niz[i+1]) < 0:
            safe_vr = [-1, -2, -3]
        i += 1
        # print(i)
        if i > len(niz)-2:
            break
    else:
        for j in range(1, len(niz)):
            if niz[j-1] - niz[j] not in safe_vr:
                break
        else:
            return True
        return False
    return False

input_list = open('input.txt', 'r').readlines()

safe_br = 0
for line in input_list:
    input_niz = re.sub('\n', '', line).split()
    # print(input_niz)
    input_niz = [int(num) for num in input_niz]
    # print(input_niz)
    ok = False
    for i in range(len(input_niz)):
        tmp_niz = input_niz.copy()
        del tmp_niz[i]

        # print(i)
        # print('A:', input_niz)
        # print('B:', tmp_niz)

        if isSafe(tmp_niz):
            safe_br += 1
            break
    # break
    # if isSafe(niz):
    #     safe_br += 1

print(safe_br)

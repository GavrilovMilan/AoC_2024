import re


def isSafe(niz):
    safe_vr = []
    i = 0
    # moze sa sorted
    while not safe_vr:
        if niz[i] - niz[i+1] > 0:
            safe_vr = [1, 2, 3]
        elif niz[i] - niz[i+1] < 0:
            safe_vr = [-1, -2, -3]
        i += 1

    for i in range(1, len(niz)):
        if niz[i-1] - niz[i] not in safe_vr:
            break
    else:
        return True
    return False


input_list = open('input.txt', 'r').readlines()

safe_br = 0
for line in input_list:
    niz = re.sub('\n', '', line).split()
    # print(niz)
    niz = [int(num) for num in niz]
    # print(niz)
    if isSafe(niz):
        safe_br += 1

print(safe_br)

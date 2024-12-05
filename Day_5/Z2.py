import re


def getWrong(update):
    for j in rules:
        l, d = j.split('|')[0], j.split('|')[1].split('\n')[0]
        pl = update.find(l)
        pd = update.find(d)
        if pl == -1 or pd == -1:
            continue
        elif pl > pd:
            global wrong_updates
            wrong_updates.append(update)
            break



def getMiddle(update):
    update = re.sub('\n', '', update)
    update = update.split(',')
    flag = True
    while flag:
        br = False
        for j in rules:
            l, d = j.split('|')[0], j.split('|')[1].split('\n')[0]
            pl = update.index(l) if l in update else -1
            pd = update.index(d) if d in update else -1
            if pl == -1 or pd == -1:
                continue
            elif pl > pd:
                tmp = update[pl]
                update[pl] = update[pd]
                update[pd] = tmp
                br = True
            if br:
                break
        else:
            flag = False

    return int(update[int(len(update) / 2)])


input_list = open('input.txt', 'r').readlines()
# print(input_list)

rules = []
updates = []
wrong_updates = []
for i in input_list:
    if '|' in i:
        rules.append(i)
    elif i != '\n':
        updates.append(i)

for i in updates:
    getWrong(i)

res = 0
for i in wrong_updates:
    res += getMiddle(i)

print(res)



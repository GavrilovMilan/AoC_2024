def getMiddle(update):
    for j in rules:
        l, d = j.split('|')[0], j.split('|')[1].split('\n')[0]
        pl = update.find(l)
        pd = update.find(d)
        if pl == -1 or pd == -1:
            continue
        elif pl > pd:
            break
    else:
        middle = int(update.split(',')[int(len(update.split(','))/2)])
        return middle
    return 0

input_list = open('input.txt', 'r').readlines()
# print(input_list)

rules = []
updates = []
for i in input_list:
    if '|' in i:
        rules.append(i)
    elif i != '\n':
        updates.append(i)

res = 0
for i in updates:
    res += getMiddle(i)

print(res)



import re


input_string = open('input.txt', 'r').read()
# print(input_string)

filtered = re.findall('mul\\([0-9]{1,3},[0-9]{1,3}\\)', input_string)
# print(filtered)

sum = 0
for i in filtered:
    a = i.split(',')[0][4:]
    b = i.split(',')[1][:-1]
    # print(a, b)
    sum += int(a) * int(b)

print(sum)
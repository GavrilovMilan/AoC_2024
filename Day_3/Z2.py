import re

input_string = open('input.txt', 'r').read()
input_string = re.sub('\n', '', input_string)

filtered_list = re.sub('do\\(\\)', '\ndo()', input_string).split('\n')
print(filtered_list)

filtered = ''
for i in filtered_list:
    filtered += i.split('don\'t()')[0]
filtered = re.findall('mul\\([0-9]{1,3},[0-9]{1,3}\\)', filtered)

sum = 0
for i in filtered:
    a = i.split(',')[0][4:]
    b = i.split(',')[1][:-1]
    # print(a, b)
    sum += int(a) * int(b)

print(sum)
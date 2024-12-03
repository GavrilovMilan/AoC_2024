import re

input_file = open('input.txt', 'r')
lista = input_file.readlines()

lista1 = []
lista2 = []

for str in lista:
    str = re.sub('\n', '', str)

    lista1.append(str.split()[0])
    lista2.append(str.split()[1])


lista1.sort()
lista2.sort()
res = 0

for str in lista1:
    br_pojavljivanja = lista2.count(str)
    # print(f'{str} : {br_pojavljivanja}')
    res += int(str) * br_pojavljivanja


print(res)

import re

input_file = open('input.txt', 'r')
lista = input_file.readlines()

lista1 = []
lista2 = []
distance = []

for str in lista:
    str = re.sub('\n', '', str)

    lista1.append(str.split()[0])
    lista2.append(str.split()[1])


lista1.sort()
lista2.sort()

for i in range(len(lista1)):
    distance.append(int(lista1[i]) - int(lista2[i]) if int(lista1[i]) > int(lista2[i]) else int(lista2[i]) - int(lista1[i]))

res = 0
for br in distance:
    res += br

print(res)
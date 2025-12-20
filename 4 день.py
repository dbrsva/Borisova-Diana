"""import csv

with open("/Users/iluvdii/Downloads/36031.csv", "r") as f:
    n = csv.reader(f)
    n = list(csv.reader(f))
    l = []
    for i in range(len(n)):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)

        print(l)"""
from itertools import repeat

#робот
"""
import csv

with open("/Users/iluvdii/Desktop/задачи/36031.csv", "r") as f:
    n = list(csv.reader(f))
    Coins = []
    for i in range(len(n)):
        a = n[i][0].split(';')
        a = [int(el) for el in a]
        Coins.append(a)

Coins.reverse()
for i in range(len(Coins)):
    Coins[i].reverse()

N = len(Coins)
M = len(Coins[0])

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            Coins[i][j] += Coins[i][j - 1]
        elif j == 0:
            Coins[i][j] += Coins[i - 1][j]
        else:
            Coins[i][j] += max(Coins[i - 1][j], Coins[i][j - 1])

print("Максимум монет:", Coins[N - 1][M - 1])

i = 0
j = 0

while i < N - 1 or j < M - 1:
    if i == N - 1:
        j += 1
        print("влево")
    elif j == M - 1:
        i += 1
        print("вверх")
    elif Coins[i][j + 1] >= Coins[i + 1][j]:
        j += 1
        print("влево")
    else:
        i += 1
        print("вверх")
"""
#1 задание
"""
import csv

with open("/Users/iluvdii/Downloads/DropMeFiles_v0zPU/59778.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    count = 0


    for i in range(len(n)- 1):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i].count(l[i][j]) == 4:
                repeat = l[i][j]
                x = []
                for j in range(len(l[i])):
                    if l[i][j] not in x and l[i][j] != repeat:
                        x.append(l[i][j])
                summa_repeat = 4 * repeat
                average_sum = sum(x) / 3
                if average_sum > summa_repeat:
                    count += 1
    print(count//4)
"""
#2 задание

import csv
with open("/Users/iluvdii/Downloads/DropMeFiles_v0zPU/29666.csv", "r") as f:
    fi = csv.reader(f, delimiter=";")
    l = []
    for i in fi:
        a = i[0].replace(",", ".")
        l.append(float(a))

max_sum = 0
for i in range(len(l)):
    j_max = l[i]
    for j in range(i + 1, len(l)):
        if l[j] < l[j - 1]:
            j_max += l[j]
        else:
            break
    if max_sum < j_max:
        max_sum = j_max
print(max_sum)















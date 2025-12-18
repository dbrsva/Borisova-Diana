#1
"""with open ("/Users/iluvdii/Desktop/задачи/39762.txt", "r") as f:
    n = f.readlines()
    n = [int(el) for el in n]
    print(n)

count = 0
max_sum = 0

for i in range(len(n) - 1):
    a = n[i]
    b = n[i+1]

    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        count += 1
        if a + b > max_sum:
            max_sum = a + b

print(count, max_sum)"""
#3
with open("/Users/iluvdii/Desktop/задачи/40992.txt", "r") as f:
    n = [int(el) for el in f]

nechet_sum = 0
nechet_count = 0

for x in n:
    if x % 2 != 0:
        nechet_sum += x
        nechet_count += 1

srednee = nechet_sum/nechet_count

max_sum = 0
count = 0

for i in range(len(n) - 1):
    a = n[i]
    b = n[i+1]

    if (a % 5 == 0 or b % 5 == 0) and (a < srednee or b < srednee):
        count += 1
        if a + b > max_sum:
            max_sum += a + b
print (count, max_sum)







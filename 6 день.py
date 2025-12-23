#1
"""def function(x, y):
    if x > 12:
        return 0
    if x == 12:
        if y:
            return 1
        else:
            return 0

    if x == 10:
        y = True

    return function(x + 1, y) + function(x + 2, y) + function(x * 2, y)


print(function(3, False))
"""
#2
"""
def function(x):
    if x > 27:
        return 0
    if x == 26:
        return 0
    if x == 27:
        return 1

    return function(x + 1)+ function(2 * x + 1)

print(function(1))
"""
#3
"""def function(x, y):
    if x > 18:
        return 0
    if x == 14:
        return 0
    if x == 18:
        if y:
            return 1
        else:
            return 0

    if x == 9:
        y = True

    return function(x + 1, y) + function(x + 2, y)
print(function(2, False))"""

#обработка символьных строк

#1
"""
with open ("27686.txt", "r") as f:
    text = f.read().strip()

max_len = 0
current_len = 0

for c in text:
    if c == 'X':
        current_len += 1
        if current_len > max_len:
            max_len = current_len
        else:
            current_len = 0
print(max_len)
"""

#2
"""with open ("36037.txt", "r") as f:
    text = f.read().strip()
max_len = 0
current_len = 0
a = ""

for c in text:
    a += c
    current_len += 1

    if len(a) > 4:
        a = a[:1]

    if 'XZZY' in a:
        current_len = 0
        a = ""

    if current_len > max_len:
        max_len = current_len

print(max_len)"""

#3
with open("46982.txt", "r") as f:
    text = f.read().strip()
    n = len(text)

count = 0
i = 0

while i < n:






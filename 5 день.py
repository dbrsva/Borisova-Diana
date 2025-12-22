#факториал
"""
n = int(input())
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return 1

print(factorial(n))
"""

#2
"""
def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for char in string:
        if char not in vowels:
            result += char
    return result
n = input()
print(remove_vowels(n))
"""

#3
"""
def pascals(n):
    if n == 1:
        return [1]
    prev = pascals(n-1)
    row = [1]
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i-1])
    row.append(1)
    return row

n = int(input())
print(pascals(n))
"""







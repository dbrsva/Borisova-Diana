#1
"""def f(arr):
    n = len(arr)
    if n == 0:
        return 0
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    a = max(dp)
    return a
posled = [6, 2, 5, 4, 2, 5, 6]
a = f(posled)
print(a)
print(len(posled) - a)
"""
#2
"""def f(a):
    if len(a) <= 1:
        return len(a)
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            b = a[:i] + a[i + 1:]
            c = a[:i + 1] + a[i + 2:]
            return max(f(b), f(c))
    return len(a)


n = int(input())
a = list(map(int, input().split()))

print(f(a))"""

#3
def reverse_number(n):
    return int(str(n)[::-1])

def count_k(K):
    count = 0
    for Y in range(1, K):
        if Y + reverse_number(Y) == K:
            count += 1
    return count
K = 1050
result = count_k(K)
print(f"Количество {K}-удивительных чисел:", result)







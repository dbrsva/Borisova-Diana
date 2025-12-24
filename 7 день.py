#1
"""def task1():
    digits = "0123456789ABCDE"

    for i in digits:
        a = int("123" + i + "5", 15)
        b = int("1" + i + "233", 15)
        s = a + b

        if s % 14 == 0:
            return s // 14
print(task1())"""

#2
"""def task2():
    digits = "0123456789ABCDEF"  

    num1 = "AB267D1"
    num2 = "F024A89"
    max_digit = max(max(int(c, 16) if c.isdigit() else ord(c) - ord('A') + 10 for c in num1),
                    max(int(c, 16) if c.isdigit() else ord(c) - ord('A') + 10 for c in num2))
    p = max_digit + 1
    while True:
        try:
            a = int(num1, p)
            b = int(num2, p)
        except ValueError:
            p += 1
            continue
        s = a + b
        if s % (p - 1) == 0:
            return p
        p += 1
print(task2())"""

#3
"""def task3():
    digits = "0123456789ABCDE"  
    for i in digits:
        num1 = i + "B09"  
        num2 = i + "8E8"  

        a = int(num1, 17)
        b = int(num2, 15)
        s = a + b
        if s % 155 == 0:
            return s // 155
print(task3())
"""
#4
"""def task4():
    x = 0
    y = 0
    min_result = 0

    while y < 8:
        while x < 8:
            s = int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)

            if s % 117 == 0:
                     min_result = s // 117

            x += 1
        x = 0
        y += 1
    return min_result
print(task4())"""

#5









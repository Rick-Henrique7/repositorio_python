def factorial(n):
    fat = 1
    if n == 0:
        return 1
    while n > 1:
        fat *= n
        n-=1
    return fat

print(factorial(6020))

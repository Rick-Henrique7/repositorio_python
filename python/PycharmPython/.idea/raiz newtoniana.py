def sqrt_newton(n, epsilon=0.001):
    p = (n - 2) / 2
    while True:
        p_squared = p * p
        difference = abs(p_squared - n)
        if difference <= epsilon:
            break
        p = (p + (n / p)) / 2
    return p

# Testando a função com n = 1
print(sqrt_newton(6))

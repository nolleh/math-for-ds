def factorial(n):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

def coeff(n, k):
    return factorial(n) / factorial(n - k) * factorial(k)

def binomial_distribution(n, k, p):
    return coeff(n, k) * p ** k * (1- p) ** (n-k)

n = 10
p = 0.9

for k in range(n + 1):
    probability = binomial_distribution(k, n, p)
    print("{0} - {1}".format(k, probability))


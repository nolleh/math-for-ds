from scipy.stats import binom

def factorial(n):
    f = 1
    for i in range(2, n +1):
        f *= i
    return f

def coeff(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))

def binomial_distribution(n, k, p):
    return coeff(n, k) * (p ** k) * (1- p) ** (n-k)

n = 10
p = 0.9

for k in range(n + 1):
    prob = binom.pmf(k, n, p)
    probability = binomial_distribution(n, k, p)
    print("{0} - {1},{2}".format(k, prob, probability))


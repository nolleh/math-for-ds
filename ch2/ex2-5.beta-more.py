from scipy.stats import betas

a = 30
b = 6
p = 1 - beta.cdf(0.9, a, b)

print(p)

sample = [90, 80, 63, 87]
weights = [0.2, 0.2, 0.2, 0.4]

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)

weights2 = [1.0, 1.0, 1.0, 2.0]
weighted_mean2 = sum(s * w for s,w in zip(sample, weights2)) / sum(weights2)

print(weighted_mean, weighted_mean2)


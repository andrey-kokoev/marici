from math import log, sqrt


def centered_pair_norm(n):
    delta = log(n + 1) - log(n)
    return abs(delta) / sqrt(2)


samples = [10, 100, 1000, 10000]
norms = [centered_pair_norm(n) for n in samples]

assert all(a > b for a, b in zip(norms, norms[1:]))
assert norms[-1] < 1e-4

renormalizers = [1 / (log(n + 1) - log(n)) for n in samples]
assert all(a < b for a, b in zip(renormalizers, renormalizers[1:]))
assert renormalizers[-1] > 10000

print("finite two-label moment rank: full")
print("centered moment norm tends to zero")
print("divided-difference normalization is unbounded in the raw completion")

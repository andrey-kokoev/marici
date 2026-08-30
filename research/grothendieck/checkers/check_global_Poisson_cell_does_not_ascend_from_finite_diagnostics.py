#!/usr/bin/env python3
"""Exact witnesses to cutoff leakage and sampling nonfactorization."""


def matmul(left, right):
    rows = len(left)
    inner = len(right)
    cols = len(right[0])
    return [
        [sum(left[i][k] * right[k][j] for k in range(inner))
         for j in range(cols)]
        for i in range(rows)
    ]


# A minimal Fourier-like involution exchanging one retained and one omitted
# source coordinate.
fourier = ((0, 0, 1), (0, 1, 0), (1, 0, 0))
cutoff = ((1, 0, 0), (0, 1, 0), (0, 0, 0))
complement = ((0, 0, 0), (0, 0, 0), (0, 0, 1))
leakage = matmul(matmul(cutoff, fourier), complement)
assert any(value != 0 for row in leakage for value in row)

# One sampled coordinate cannot reconstruct an independent Poisson-sensitive
# gap coordinate.
gap_variation = (0, 1)
sample = gap_variation[0]
poisson_sensitive = gap_variation[1]
assert sample == 0
assert poisson_sensitive != 0

print("finite_cutoff_Fourier_leakage=nonzero")
print("prime_sampling_to_Poisson_factorization=impossible")
print("required_direction=global_cell_then_observer_descent")


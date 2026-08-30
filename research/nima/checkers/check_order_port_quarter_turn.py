from fractions import Fraction

S = ((0, -1), (1, 0))
u = (Fraction(1), Fraction(1))
v = (Fraction(-1), Fraction(1))


def apply(matrix, vector):
    return tuple(sum(a * b for a, b in zip(row, vector)) for row in matrix)


assert apply(S, u) == v
assert apply(S, v) == tuple(-x for x in u)
assert apply(S, apply(S, u)) == tuple(-x for x in u)

rho_values = [Fraction(9, 10), Fraction(99, 100), Fraction(999, 1000)]
contrast_eigenvalues = [1 - rho for rho in rho_values]
mean_eigenvalues = [1 + rho for rho in rho_values]

assert all(a > b for a, b in zip(contrast_eigenvalues, contrast_eigenvalues[1:]))
assert all(value > 1 for value in mean_eigenvalues)

print("order operator squares to minus identity")
print("order operator maps mean to contrast with gap-independent strength")
print("positive-window contrast eigenvalue collapses independently")

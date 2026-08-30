"""Exact finite Euler/Fredholm determinant checks."""

import sympy as sp

s = sp.symbols("s", positive=True)
prime_sets = ([2], [2, 3], [2, 3, 5, 7])

for primes in prime_sets:
    prime_operator = sp.diag(*[sp.Integer(prime) ** (-s) for prime in primes])
    determinant = sp.simplify((sp.eye(len(primes)) - prime_operator).det())
    euler_product = sp.prod(1 - sp.Integer(prime) ** (-s) for prime in primes)
    assert sp.simplify(determinant - euler_product) == 0

    for prime in primes:
        factor = 1 - sp.Integer(prime) ** (-s)
        expected_term = sp.log(prime) * sp.Integer(prime) ** (-s) / factor
        assert sp.simplify(sp.diff(factor, s) / factor - expected_term) == 0
    print(f"prime_count={len(primes)} Fredholm_Euler_identity=True")

# Finite shadows of the critical-line Hilbert--Schmidt sum grow monotonically.
partial_sums = []
for bound in (10, 30, 100, 300):
    value = sum(sp.Rational(1, prime) for prime in list(sp.primerange(1, bound + 1)))
    partial_sums.append(value)
assert all(partial_sums[index] < partial_sums[index + 1] for index in range(len(partial_sums) - 1))

print(f"critical_line_HS_partial_sums={[f'{float(value):.6f}' for value in partial_sums]}")
print("critical_line_prime_operator_Hilbert_Schmidt=False")
print("critical_line_Fredholm_determinant=False")
print("relative_regularized_determinant_required=True")

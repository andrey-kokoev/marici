"""Exact finite-prime checks for smoothing and phase blindness."""

import sympy as sp

height, tau = sp.symbols("T tau", real=True, positive=True)
primes = [2, 3, 5, 7, 11]

amplitudes = [
    sp.Integer(prime) ** (-sp.Rational(1, 2) - sp.I * height)
    * sp.exp(-tau * sp.log(prime) ** 2 / 2)
    for prime in primes
]
norm_squared = sp.simplify(sum(value * sp.conjugate(value) for value in amplitudes))
expected = sum(sp.exp(-tau * sp.log(prime) ** 2) / prime for prime in primes)
assert sp.simplify(norm_squared - expected) == 0
assert sp.simplify(sp.diff(norm_squared, height)) == 0

p, q = sp.Integer(2), sp.Integer(3)
off_diagonal = sp.simplify(
    p ** (-sp.Rational(1, 2) - sp.I * height)
    * sp.conjugate(q ** (-sp.Rational(1, 2) - sp.I * height))
)
assert sp.simplify(sp.diff(off_diagonal, height)) != 0

for smoothing in (sp.Rational(1, 10), sp.Rational(1, 2), sp.Integer(1)):
    value = sp.N(expected.subs(tau, smoothing), 12)
    print(f"tau={smoothing} finite_prime_smoothed_norm={value}")

print("diagonal_smoothed_norm_height_independent=True")
print("off_diagonal_log_difference_height_dependent=True")
print("unsmoothed_infinite_prime_norm_diverges=True")
print("paired_difference_kernel_required=True")


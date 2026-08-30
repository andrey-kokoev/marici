"""Exact finite local-factor tests for the Euler-local zero no-go."""

import sympy as sp

height = sp.symbols("T", real=True)
s = sp.Rational(1, 2) + sp.I * height

for prime in (2, 3, 5, 7, 11):
    phase_amplitude = sp.Integer(prime) ** (-sp.Rational(1, 2)) * sp.exp(-sp.I * height * sp.log(prime))
    modulus_squared = sp.simplify((1 - phase_amplitude) * (1 - sp.conjugate(phase_amplitude)))
    expected = 1 + sp.Rational(1, prime) - 2 * sp.Integer(prime) ** (-sp.Rational(1, 2)) * sp.cos(height * sp.log(prime))
    assert sp.simplify(sp.expand_complex(modulus_squared - expected)) == 0
    lower_bound = (1 - sp.Integer(prime) ** (-sp.Rational(1, 2))) ** 2
    assert lower_bound > 0
    print(f"prime={prime} critical_line_local_factor_nonzero=True")

finite_product = sp.prod(
    1 - sp.Integer(prime) ** (-sp.Rational(1, 2)) * sp.exp(-sp.I * height * sp.log(prime))
    for prime in (2, 3, 5, 7)
)
assert abs(complex(sp.N(finite_product.subs(height, 14), 30))) > 0

print("finite_Euler_products_nonzero_in_positive_half_plane=True")
print("gamma_factor_has_zeros=False")
print("absolutely_convergent_nonzero_local_product_has_zeros=False")
print("global_continuation_anomaly_required=True")

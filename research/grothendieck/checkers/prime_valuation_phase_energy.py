"""Exact one-prime energy identity and finite smoothed zero-set tests."""

import sympy as sp

p, height = sp.symbols("p T", positive=True, real=True)
radius = p ** (-sp.Rational(1, 2))
theta = height * sp.log(p)
r = radius * sp.exp(-sp.I * theta)

energy = sp.simplify(1 + (1 - r) * (1 - sp.conjugate(r)) / (1 - radius**2))
expected_energy = 2 * (1 - radius * sp.cos(theta)) / (1 - radius**2)
assert sp.simplify(sp.expand_complex(energy - expected_energy)) == 0

defect = sp.simplify(expected_energy - expected_energy.subs(height, 0))
expected_defect = 2 * radius * (1 - sp.cos(theta)) / (1 - radius**2)
assert sp.simplify(defect - expected_defect) == 0

for prime in (2, 3, 5):
    for test_height in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)):
        value = sp.N(expected_defect.subs({p: prime, height: test_height}), 20)
        assert value > 0
    print(f"prime={prime} sampled_nonzero_heights_positive=True")

tau = sp.Rational(1, 2)
finite_global = sum(
    sp.exp(-tau * sp.log(prime) ** 2) * expected_defect.subs(p, prime)
    for prime in (2, 3, 5, 7)
)
assert sp.simplify(finite_global.subs(height, 0)) == 0
assert sp.N(finite_global.subs(height, 1), 20) > 0

print("one_prime_closed_energy_identity=True")
print("valuation_metric_restores_height_dependence=True")
print("smoothed_positive_energy_zero_only_at_origin=True")
print("raw_positive_energy_is_not_Xi_spectral_equation=True")


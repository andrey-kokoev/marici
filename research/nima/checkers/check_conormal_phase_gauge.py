from fractions import Fraction
import json
from pathlib import Path


ComplexQ = tuple[Fraction, Fraction]


def add(z: ComplexQ, w: ComplexQ) -> ComplexQ:
    return z[0] + w[0], z[1] + w[1]


def mul(z: ComplexQ, w: ComplexQ) -> ComplexQ:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def div(z: ComplexQ, w: ComplexQ) -> ComplexQ:
    norm = w[0] * w[0] + w[1] * w[1]
    return (
        (z[0] * w[0] + z[1] * w[1]) / norm,
        (z[1] * w[0] - z[0] * w[1]) / norm,
    )


def phase_jet(value: ComplexQ, derivative: ComplexQ) -> ComplexQ:
    # i times the imaginary part of derivative/value.
    logarithmic = div(derivative, value)
    return Fraction(0), logarithmic[1]


one = (Fraction(1), Fraction(0))
psi = one
psi_prime = (Fraction(0), Fraction(1))
f = one
f_prime = (Fraction(0), Fraction(2))

product = mul(f, psi)
product_prime = add(mul(f_prime, psi), mul(f, psi_prime))

j_psi = phase_jet(psi, psi_prime)
j_f = phase_jet(f, f_prime)
j_product = phase_jet(product, product_prime)

assert j_psi == (0, 1)
assert j_f == (0, 2)
assert j_product == add(j_psi, j_f) == (0, 3)

# Positive-real scaling and constant phase have zero phase gradient.
positive_real = (Fraction(3), Fraction(0))
positive_real_prime = (Fraction(5), Fraction(0))
constant_phase = (Fraction(0), Fraction(2))
constant_phase_prime = (Fraction(0), Fraction(0))

assert phase_jet(positive_real, positive_real_prime) == (0, 0)
assert phase_jet(constant_phase, constant_phase_prime) == (0, 0)

result = {
    "schema": "marici.nima.conormal-phase-gauge.v1",
    "status": "pass",
    "base_phase_jet": [str(x) for x in j_psi],
    "gauge_shift": [str(x) for x in j_f],
    "rescaled_phase_jet": [str(x) for x in j_product],
    "cocycle_identity": j_product == add(j_psi, j_f),
    "harmless_rescalings": ["positive-real", "constant-phase"],
}

output = Path(__file__).parents[1] / "results" / "conormal-phase-gauge.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

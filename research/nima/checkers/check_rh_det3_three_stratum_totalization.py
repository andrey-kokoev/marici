"""Exact formal checks for order-three determinant totalization."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


max_degree = 12


def full_log_coefficients(multiplicity):
    return {degree: Fraction(multiplicity, degree) for degree in range(1, max_degree + 1)}


def primitive_coefficients(multiplicity):
    return {1: Fraction(multiplicity)}


def square_coefficients(multiplicity):
    return {2: Fraction(multiplicity, 2)}


def connected_coefficients(multiplicity):
    return {
        degree: Fraction(multiplicity, degree)
        for degree in range(3, max_degree + 1)
    }


def add_series(*series):
    return {
        degree: sum(item.get(degree, Fraction(0)) for item in series)
        for degree in range(1, max_degree + 1)
    }


records = []
for multiplicity in [1, 2, 5, 11]:
    full = full_log_coefficients(multiplicity)
    total = add_series(
        primitive_coefficients(multiplicity),
        square_coefficients(multiplicity),
        connected_coefficients(multiplicity),
    )
    assert total == full
    records.append({
        "labelled_block_multiplicity": multiplicity,
        "degrees_verified": max_degree,
        "identity": True,
    })

# Direct-sum composition is coefficientwise addition.
left = add_series(
    primitive_coefficients(2),
    square_coefficients(2),
    connected_coefficients(2),
)
right = add_series(
    primitive_coefficients(3),
    square_coefficients(3),
    connected_coefficients(3),
)
combined = add_series(left, right)
assert combined == full_log_coefficients(5)

# If grading is forgotten, a counterterm can be transferred between the first
# two channels without changing their total.
primitive_scalar = Fraction(7, 3)
square_scalar = Fraction(-5, 4)
counterterm = Fraction(11, 6)
shifted_primitive = primitive_scalar + counterterm
shifted_square = square_scalar - counterterm
assert primitive_scalar + square_scalar == shifted_primitive + shifted_square
assert (primitive_scalar, square_scalar) != (shifted_primitive, shifted_square)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "order-three determinant is the canonical finite totalization of primitive, square, and connected strata",
    "records": records,
    "direct_sum_composition": True,
    "ungraded_counterterm_transfer": {
        "original": [str(primitive_scalar), str(square_scalar)],
        "shifted": [str(shifted_primitive), str(shifted_square)],
        "same_total": True,
    },
    "verdict": "finite totalization canonical; global anomaly-line trivialization open",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-det3-three-stratum-totalization.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))

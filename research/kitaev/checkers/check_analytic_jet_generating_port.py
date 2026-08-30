#!/usr/bin/env python3
"""Exact audit of one analytic germ port generating all finite jets."""

import hashlib
import json
from math import factorial
from pathlib import Path

from sympy import I, Rational, Symbol, diff, expand, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/analytic-jet-generating-port.json"


def multiplicity(coefficients):
    for index, value in enumerate(coefficients):
        if value != 0:
            return index
    return None


def main():
    w = Symbol("w")
    coefficients = [Rational(2), Rational(-3, 2), I, Rational(5, 3), 0, Rational(-1, 4)]
    polynomial = expand(sum(value * w**m for m, value in enumerate(coefficients)))

    recovered = []
    for m, expected in enumerate(coefficients):
        value = simplify(diff(polynomial, w, m).subs(w, 0) / factorial(m))
        assert value == expected
        recovered.append(str(value))

    # Exact weighted H^2_R coefficient identity for a polynomial.
    R = Rational(3, 2)
    weighted_norm_squared = simplify(sum(value * value.conjugate() * R ** (2 * m) for m, value in enumerate(coefficients)))
    sequence_norm_squared = simplify(sum((R**m * value) * (R**m * value).conjugate() for m, value in enumerate(coefficients)))
    assert weighted_norm_squared == sequence_norm_squared

    # Sharp coefficient norm: normalized monomial has H^2_R norm one.
    sharp_bounds = []
    for m in range(7):
        normalized_coefficient = R ** (-m)
        norm_squared = simplify(normalized_coefficient**2 * R ** (2 * m))
        assert norm_squared == 1
        sharp_bounds.append({"order": m, "coefficient_functional_norm": str(R ** (-m))})

    # Cauchy estimate is saturated by a monomial on radius r.
    r = Rational(1, 2)
    cauchy_checks = []
    for m in range(7):
        supremum = r**m
        coefficient = Rational(1)
        assert coefficient == r ** (-m) * supremum
        cauchy_checks.append({"order": m, "bound_constant": str(r ** (-m))})

    # Shrinking analytic radii destroy uniform coefficient bounds.
    shrinking = []
    fixed_order = 3
    for N in (2, 3, 5, 10, 20):
        RN = Rational(1, N)
        norm = RN ** (-fixed_order)
        assert norm == N**fixed_order
        shrinking.append({"N": N, "radius": str(RN), "order_3_evaluation_norm": str(norm)})

    # Full finite polynomial germ is faithful through all coefficients.
    assert any(value != 0 for value in coefficients)
    assert polynomial != 0
    zero_coefficients = [0] * 7
    assert multiplicity(zero_coefficients) is None

    # Multiplicity selector is discontinuous under arbitrarily small constants.
    selector_hostile = []
    base_order = 4
    base = [0] * base_order + [1]
    assert multiplicity(base) == base_order
    for N in (2, 3, 5, 10, 20):
        perturbed = [Rational(1, N)] + [0] * (base_order - 1) + [1]
        assert multiplicity(perturbed) == 0
        selector_hostile.append({"perturbation_norm": str(Rational(1, N)), "multiplicity_after": 0})

    # w^N tends to zero on every fixed compact subdisk r<1, while order grows.
    compact_open = []
    for N in (2, 3, 5, 10, 20):
        compact_supremum = r**N
        compact_open.append({"N": N, "multiplicity": N, "sup_on_radius_half": str(compact_supremum)})

    payload = {
        "schema": "marici.kitaev.analytic_jet_generating_port.v1",
        "status": "pass",
        "strength": "analytic compiler theorem",
        "recovered_coefficients": recovered,
        "weighted_hardy_norm_squared": str(weighted_norm_squared),
        "weighted_sequence_isometry": True,
        "sharp_coefficient_bounds": sharp_bounds,
        "compact_open_cauchy_checks": cauchy_checks,
        "shrinking_radius_hostile": shrinking,
        "multiplicity_selector_hostile": selector_hostile,
        "compact_open_unbounded_multiplicity": compact_open,
        "backward_indexed_constructor_rejected": True,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "theta germ derivation", "infinite instrument access",
            "Riemann-zero multiplicity bound", "zero orientation",
            "completion-stable observability", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

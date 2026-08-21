#!/usr/bin/env python3
"""Hostile test of n-fold substrate maps against two physical selections."""

import json
from pathlib import Path


N_MAX = 12

# Memory: scaling the linear difference plane by n induces graded pullback.
memory_checks = 0
for n in range(N_MAX + 1):
    for a in range(-8, 9):
        for b in range(-8, 9):
            q2 = a * a - a * b + b * b
            q3 = a * b * (a - b)
            scaled_q2 = (n * a) ** 2 - (n * a) * (n * b) + (n * b) ** 2
            scaled_q3 = (n * a) * (n * b) * (n * a - n * b)
            assert scaled_q2 == n**2 * q2
            assert scaled_q3 == n**3 * q3
            memory_checks += 2

# Cosmology: n-fold addition on the exponent-two deck group is parity.
# The quotient difference map is natural, but the identity-idempotent
# selection delta_0 is not: every even n sends every difference to zero.
quotient_naturality_checks = 0
selection_passes = []
selection_failures = []
for n in range(N_MAX + 1):
    multiplier = n % 2
    failures = 0
    for g in range(32):
        for h in range(32):
            lhs_difference = (multiplier * g) ^ (multiplier * h)
            rhs_difference = multiplier * (g ^ h)
            assert lhs_difference == rhs_difference
            quotient_naturality_checks += 1

            original_selection = int((g ^ h) == 0)
            repeated_selection = int(rhs_difference == 0)
            if original_selection != repeated_selection:
                failures += 1
    if failures:
        selection_failures.append({"n": n, "failures": failures})
    else:
        selection_passes.append(n)

assert selection_passes == [n for n in range(N_MAX + 1) if n % 2 == 1]
assert all(row["failures"] == 992 for row in selection_failures)

# Multiplicative composition [m] o [n] = [mn] remains valid in both models.
monoid_law_checks = 0
for m in range(N_MAX + 1):
    for n in range(N_MAX + 1):
        assert (m % 2) * (n % 2) == ((m * n) % 2)
        monoid_law_checks += 1

result = {
    "schema": "marici.nima.readout_arithmetic_naturality.v1",
    "n_range": [0, N_MAX],
    "memory": {
        "operation": "linear scaling [n] on the memory plane",
        "pullback": "q2 -> n^2 q2; q3 -> n^3 q3",
        "checks": memory_checks,
        "graded_naturality": True,
    },
    "cosmology": {
        "operation_tested": "n-fold addition on G=(C2)^5",
        "difference_quotient_natural": True,
        "quotient_checks": quotient_naturality_checks,
        "physical_selection_natural_for_n": selection_passes,
        "physical_selection_failures": selection_failures,
        "even_n_failure_reason": "[n] sends every deck difference to zero, so delta_0 becomes the constant-one function",
    },
    "multiplicative_monoid_law_checks": monoid_law_checks,
    "common_physical_arithmetic_action": False,
    "conclusion": "formal n-fold substrate maps do not automatically define selection-compatible physical constructors",
    "passed": True,
}
out = Path(__file__).with_name("results") / "readout-arithmetic-naturality.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))


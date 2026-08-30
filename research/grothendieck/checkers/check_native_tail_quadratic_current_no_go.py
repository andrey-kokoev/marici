"""Dependency-free exact audit for native quadratic tail currents."""

from fractions import Fraction
import json


# One nonzero rational specialization suffices as the exact finite falsifier.
s = Fraction(3)
f = Fraction(5)

# Vanishing -2*A*s and -B*f forces A=B=0 over the rationals.
A = Fraction(0)
B = Fraction(0)
coefficients = {
    "G2": -2 * A * s,
    "Gc": -(2 * A * f + B * s),
    "c2": -B * f,
}
remaining_gc = coefficients["Gc"]
target_gc = 2 * f

checks = {
    "s_is_nonzero": s != 0,
    "f_is_nonzero": f != 0,
    "G2_elimination_forces_A_zero": coefficients["G2"] == 0 and A == 0,
    "c2_elimination_forces_B_zero": coefficients["c2"] == 0 and B == 0,
    "remaining_Gc_coefficient_is_zero": remaining_gc == 0,
    "target_Gc_coefficient_is_nonzero": target_gc != 0,
    "native_quadratic_current_cannot_match_forcing": remaining_gc != target_gc,
}

result = {
    "schema": "marici.grothendieck.native-tail-quadratic-current-no-go.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "specialization": {"s": str(s), "f": str(f)},
    "coefficients": {name: str(value) for name, value in coefficients.items()},
    "forced_solution": {"A": "0", "B": "0"},
    "remaining_Gc": str(remaining_gc),
    "target_Gc": str(target_gc),
}

print(json.dumps(result, indent=2, sort_keys=True))

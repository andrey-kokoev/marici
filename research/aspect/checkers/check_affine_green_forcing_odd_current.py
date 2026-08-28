import json
from pathlib import Path

import sympy as sp


ell, eta, z, f = sp.symbols("ell eta z f", positive=True)
a = sp.Rational(1, 2) + z
b = sp.Rational(1, 2) - z


def decay(length):
    return sp.diag(sp.exp(-a * length), sp.exp(-b * length))


def reservoir(length):
    return sp.Matrix([
        f * (1 - sp.exp(-a * length)) / a,
        f * (1 - sp.exp(-b * length)) / b,
    ])


def affine(length):
    d = decay(length)
    r = reservoir(length)
    return sp.Matrix([
        [d[0, 0], 0, -r[0]],
        [0, d[1, 1], -r[1]],
        [0, 0, 1],
    ])


cocycle = sp.simplify(reservoir(ell + eta) - decay(eta) * reservoir(ell) - reservoir(eta))
composition = (affine(eta) * affine(ell) - affine(ell + eta)).applyfunc(sp.simplify)
odd_current = sp.simplify(-(sp.Matrix([[1, -1]]) * reservoir(ell))[0])
odd_series = sp.series(odd_current, ell, 0, 4)
normalized_limit = sp.simplify(sp.limit(odd_current / (1 - sp.exp(-ell)), ell, 0))

checks = {
    "forcing_reservoir_is_a_cocycle": cocycle == sp.zeros(2, 1),
    "affine_interval_composition": composition == sp.zeros(3, 3),
    "odd_current_vanishes_on_reciprocal_seam": sp.simplify(odd_current.subs(z, 0)) == 0,
    "odd_current_is_reciprocal_odd": sp.simplify(odd_current.subs(z, -z) + odd_current) == 0,
    "leading_odd_leakage_is_f_z_ell_squared": sp.simplify(sp.limit(odd_current / ell**2, ell, 0) - f * z) == 0,
    "vacuum_normalized_leakage_vanishes_archimedeanly": normalized_limit == 0,
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "odd_current": str(odd_current),
    "odd_current_series": str(odd_series),
    "vacuum_normalized_archimedean_limit": str(normalized_limit),
}

out = Path(__file__).resolve().parents[1] / "results" / "affine_green_forcing_odd_current.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

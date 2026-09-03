from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/quarter-shift-normalized-localizer-v1.json")


def sampled_matrix(function: sp.Expr, variable: sp.Symbol, t: sp.Symbol, h: sp.Symbol, size: int) -> sp.Matrix:
    return sp.Matrix(size, size, lambda i, j: function.subs(variable, t + (i + j) * h))


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    s, t, h, lam = sp.symbols("s t h lam", positive=True, real=True)
    c = sp.Rational(1, 4)

    endpoint = sp.exp(c * s)
    remainder = 2 * sp.exp(-lam * s)
    H = endpoint + remainder
    F = sp.simplify(sp.exp(-c * s) * H)
    assert sp.simplify(F - (1 + 2 * sp.exp(-s * (lam + c)))) == 0

    size = 3
    M_H_t = sampled_matrix(H, s, t, h, size)
    M_H_th = sampled_matrix(H, s, t + h, h, size)
    M_F_t = sampled_matrix(F, s, t, h, size)
    M_F_th = sampled_matrix(F, s, t + h, h, size)
    D = sp.diag(*(sp.exp(-i * c * h) for i in range(size)))

    expected_M_F = sp.exp(-c * t) * D * M_H_t * D
    assert sp.simplify(M_F_t - expected_M_F) == sp.zeros(size)

    L_F = sp.simplify(M_F_t - M_F_th)
    expected_L_F = sp.exp(-c * t) * D * (M_H_t - sp.exp(-c * h) * M_H_th) * D
    assert sp.simplify(L_F - expected_L_F) == sp.zeros(size)

    endpoint_F = sp.simplify(sp.exp(-c * s) * endpoint)
    assert endpoint_F == 1
    assert sampled_matrix(endpoint_F, s, t, h, size) - sampled_matrix(endpoint_F, s, t + h, h, size) == sp.zeros(size)

    raw_localizer = sp.simplify(M_H_t - M_H_th)
    assert sp.simplify(raw_localizer - L_F) != sp.zeros(size)
    q = sp.exp(-c * h)
    sharp_L_F = sp.simplify(q * M_F_t - M_F_th)
    expected_sharp = sp.exp(-c * t) * q * D * raw_localizer * D
    assert sp.simplify(sharp_L_F - expected_sharp) == sp.zeros(size)
    endpoint_matrix = sampled_matrix(endpoint_F, s, t, h, size)
    sharp_endpoint = sp.simplify(q * endpoint_matrix - endpoint_matrix)
    assert sharp_endpoint != sp.zeros(size)

    # The normalized positive atom has a direct localizer Gram factor.
    y = sp.exp(-(lam + c) * h)
    v = sp.Matrix([y**i for i in range(size)])
    atom_localizer = sp.simplify(L_F)
    expected_atom_localizer = 2 * sp.exp(-(lam + c) * t) * (1 - y) * v * v.T
    assert sp.simplify(atom_localizer - expected_atom_localizer) == sp.zeros(size)

    status = contract["status"]
    assert status["normalized_remainder_cone"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.quarter-shift-normalized-localizer-check.v1",
        "status":"normalization_congruence_verified",
        "spectral_quarter_shift":True,
        "hankel_congruence":True,
        "localizer_congruence":True,
        "weak_endpoint_localizer_cancels":True,
        "sharp_endpoint_localizer_survives":True,
        "sharp_localizer_raw_congruence":True,
        "raw_and_weak_normalized_localizers_differ":True,
        "positive_atom_normalized_factor":True,
        "source_RH_normalization_reverified":False,
        "normalized_remainder_cone":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

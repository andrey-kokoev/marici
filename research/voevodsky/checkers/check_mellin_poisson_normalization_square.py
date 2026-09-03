from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/mellin-poisson-normalization-square-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    q, s = sp.symbols("q s")
    a = s / 2

    # Under integration by parts, D contributes -a and D^2 contributes a^2.
    multiplier = 2 * a**2 - a
    assert sp.simplify(multiplier - s * (s - 1) / 2) == 0

    # L kills the two polar asymptotic modes.
    constant = sp.Integer(1)
    reciprocal_mode = sp.exp(-q / 2)
    L = lambda expression: 2 * sp.diff(expression, q, 2) + sp.diff(expression, q)
    assert L(constant) == 0
    assert sp.simplify(L(reciprocal_mode)) == 0

    # From h(-q)=exp(q/2)h(q), derive (Lh)(-q)=exp(q/2)(Lh)(q).
    h = sp.Function("h")(q)
    h_minus = sp.exp(q / 2) * h
    L_at_minus = 2 * sp.diff(h_minus, q, 2) - sp.diff(h_minus, q)
    assert sp.simplify(L_at_minus - sp.exp(q / 2) * L(h)) == 0

    # Phi=exp(q/4)Lh is therefore even.
    transformed_phi_minus = sp.exp(-q / 4) * L_at_minus
    phi_plus = sp.exp(q / 4) * L(h)
    assert sp.simplify(transformed_phi_minus - phi_plus) == 0

    w = sp.symbols("w")
    centered_kernel = sp.exp(w * q / 2)
    assert centered_kernel.subs(w, -w) == centered_kernel.subs(q, -q)

    status = contract["status"]
    assert status["positivity_implication_for_zeros"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.mellin-poisson-normalization-square-check.v1",
        "status":"normalization_square_symbolically_verified",
        "operator_multiplier_is_xi_factor":True,
        "constant_polar_mode_annihilated":True,
        "reciprocal_polar_mode_annihilated":True,
        "completed_source_even":True,
        "centered_reciprocal_naturality":True,
        "positivity_to_zero_localization":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

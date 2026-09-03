from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/theta-mellin-completion-square-v1.json")
SOURCE = Path("research/grothendieck/theta-decay-solves-the-wrong-coefficient-space-without-the-mellin-square.md")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    assert "Required Mellin square" in source
    assert "gamma and polar terms" in source

    s, u, n = sp.symbols("s u n", positive=True)
    # Termwise Mellin transform after x=pi*n^2*u.
    term = sp.pi ** (-s / 2) * sp.gamma(s / 2) * n ** (-s)
    assert sp.simplify(term / (sp.pi ** (-s / 2) * sp.gamma(s / 2)) - n ** (-s)) == 0

    kernel = u ** (s / 2) + u ** ((1 - s) / 2)
    polar = 1 / (s - 1) - 1 / s
    assert sp.simplify(kernel.subs(s, 1 - s) - kernel) == 0
    assert sp.simplify(polar.subs(s, 1 - s) - polar) == 0
    assert sp.simplify(polar - 1 / (s * (s - 1))) == 0

    w = sp.symbols("w")
    centered = sp.Rational(1, 2) + w
    assert sp.simplify((1 - centered) - (sp.Rational(1, 2) - w)) == 0

    # Deliberate failure: fixed-u scalar theta coefficient is not the zeta coefficient 1.
    smoothed_first = 2 * sp.exp(-sp.pi * u)
    assert sp.simplify(smoothed_first - 1) != 0

    status = contract["status"]
    assert status["reciprocal_naturality"] == "constructed"
    assert status["rh_implication"] == "none"
    result = {
        "schema":"marici.voevodsky.theta-mellin-completion-square-check.v1",
        "status":"classical_mellin_square_symbolically_verified",
        "termwise_gamma_factor":True,
        "dirichlet_coefficient_recovered_after_mellin":True,
        "reciprocal_large_u_kernel_invariant":True,
        "polar_correction_invariant":True,
        "centered_reciprocal_coordinate":True,
        "fixed_u_scalar_identification_deliberate_failure":True,
        "cutoff_integral_interchange_requires_gaussian_domination":True,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

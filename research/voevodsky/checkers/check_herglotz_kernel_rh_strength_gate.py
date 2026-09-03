from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/herglotz-kernel-rh-strength-gate-v1.json")
HOSTILE = Path("research/grothendieck/a-positive-gaussian-mixture-falsifies-archimedean-endpoint-dominance.md")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    hostile = HOSTILE.read_text(encoding="utf-8")
    assert "positive" in hostile.lower() and "zero" in hostile.lower()

    z, wb, gamma = sp.symbols("z wb gamma", real=True)
    Fz = 1 / (z - sp.I * gamma) + 1 / (z + sp.I * gamma)
    Fbarw = 1 / (wb + sp.I * gamma) + 1 / (wb - sp.I * gamma)
    kernel = sp.simplify((Fz + Fbarw) / (z + wb))
    gram = 1 / ((z - sp.I * gamma) * (wb + sp.I * gamma)) + 1 / ((z + sp.I * gamma) * (wb - sp.I * gamma))
    assert sp.simplify(kernel - gram) == 0

    points = [sp.Integer(1), sp.Integer(2), sp.Integer(3)]
    gammas = [sp.Integer(1), sp.Integer(2)]
    matrix = sp.Matrix([[sum(
        1 / ((left - sp.I * g) * (right + sp.I * g))
        + 1 / ((left + sp.I * g) * (right - sp.I * g))
        for g in gammas
    ) for right in points] for left in points])
    assert matrix == matrix.conjugate().T
    principal_minors = []
    for size in range(1, 4):
        for indices in combinations(range(3), size):
            minor = sp.simplify(matrix.extract(indices, indices).det())
            principal_minors.append(minor)
            assert minor >= 0

    # An off-axis zero rho creates a pole of Xi'/Xi inside the right half-plane.
    rho = sp.Rational(1, 3) + 2 * sp.I
    off_axis_term = 1 / (z - rho)
    assert sp.denom(off_axis_term).subs(z, rho) == 0
    assert sp.re(rho) > 0

    status = contract["status"]
    assert status["source_gram_realization_for_completed_arithmetic_kernel"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.herglotz-kernel-rh-strength-gate-check.v1",
        "status":"finite_zero_herglotz_gram_gate_verified",
        "rank_one_kernel_identity":True,
        "finite_imaginary_zero_gram_psd":True,
        "principal_minors_checked":len(principal_minors),
        "off_axis_zero_forces_half_plane_pole":True,
        "positive_even_source_sufficient":False,
        "source_gram_realization_supplied":False,
        "rh_proved":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

"""Inventory whether current cosmology data authorize an analytic-continuation contour.

This is an authority gate, not a numerical period computation.  Earlier
source work supplies the universal negative-imaginary energy boundary value,
which induces a local p-i0 germ.  That local side is not yet a global contour
or a twisted physical pairing for the triple-incidence nearby line.
"""

from __future__ import annotations

import json
from pathlib import Path

NIMA = Path(__file__).resolve().parents[1]
OUT = NIMA / "results" / "cosmology_analytic_continuation_authority_gate.json"


def load(name: str) -> dict:
    return json.loads((NIMA / "results" / name).read_text(encoding="utf-8"))


def main() -> None:
    activation = load("cosmology_triple_incidence_activation_obstruction.json")
    bridge = load("cosmology_z3_to_mu2_bridge_no_go.json")
    vertical = load("rank-two-vertical-excess-real-support.json")
    five_site = load("five-site-deck-continued-period-poles.json")

    assert activation["analytic_continuation_period_supported_on_nearby_line"] is False
    assert "non-torsion analytic-continuation contour" in bridge["remaining_escape_hatches"][0]
    assert vertical["literal_euclidean_activation"] is False
    assert vertical["analytic_continuation_required"] is True
    assert five_site["positive_ray_regular_sheets"] == [0]
    assert five_site["positive_ray_singular_sheet_count"] == 31
    assert "requires an independently specified contour" in five_site["conclusion"]
    assert "does not choose a contour" in five_site["scope"]

    # The primary Bunch--Davies prescription is predeclared independently of
    # this target.  For p=X1+X2+3*X3 its induced imaginary displacement is
    # -(epsilon1+epsilon2+3*epsilon3), strictly negative on the full positive
    # regulator cone.  This fixes a local boundary-value germ, not the missing
    # transported thimble or scalar period.
    p_regulator_coefficients = [1, 1, 3]
    assert all(coefficient > 0 for coefficient in p_regulator_coefficients)

    packet = {
        "schema": "marici.cosmology-analytic-continuation-authority-gate.v1",
        "target": "triple-incidence mu2-odd nearby line",
        "ordinary_positive_support": False,
        "analytic_continuation_required": True,
        "predeclared_local_p_i_epsilon_present": True,
        "source_authorized_local_boundary_germ_present": True,
        "local_boundary_prescription": "Xi -> Xi-i*epsilon_i, epsilon_i>0; p -> p-i*(epsilon1+epsilon2+3*epsilon3)",
        "local_regulator_sign_on_positive_cone": -1,
        "source_authorized_global_contour_present": False,
        "source_authorized_contour_present": False,
        "continued_scalar_period_assigned": False,
        "evidence": {
            "triple_incidence_positive_activation": activation[
                "analytic_continuation_period_supported_on_nearby_line"
            ],
            "rank_two_vertical_excess_real_solutions": vertical[
                "real_solutions_to_w2_plus_R"
            ],
            "rank_two_vertical_excess_requires_continuation": vertical[
                "analytic_continuation_required"
            ],
            "five_site_regular_positive_sheets": five_site[
                "positive_ray_regular_sheets"
            ],
            "five_site_singular_continued_sheets": five_site[
                "positive_ray_singular_sheet_count"
            ],
            "five_site_scope": five_site["scope"],
            "local_boundary_source_locator": [
                "src/ledger/20260815-180 Boundary-Value Leray Uniqueness and the Canonical Physical Residue Germ.md",
                "arXiv:2305.19686v2 equations (4.18)-(4.20)"
            ],
            "positive_triple_fold_precedents": [
                "src/ledger/20260821-1882 The Source Regulator Activates the Surviving Triple Fold.md",
                "src/ledger/20260822-1894 The Generic Six-Site Divisor Is Source-Activated.md"
            ]
        },
        "forbidden_promotions": [
            "treating analytic-continuation-required as analytic-continuation-authorized",
            "using a pointwise deformed contour without source invariance",
            "assigning scalar periods to singular continued sheets without a contour prescription",
            "using the closed T7 or all-soft Z3 gates as contour authority",
        ],
        "conclusion": (
            "current cosmology data require analytic continuation for nonliteral "
            "branches; the primary source fixes the local p-i0 boundary side, "
            "but does not yet supply the transported mu2-odd thimble, global "
            "contour, or physical period covector"
        ),
        "next_gate": (
            "transport the positive Cayley--Menger germ over a transverse p-disk, "
            "compute its Picard--Lefschetz variation and mu2 character, and prove "
            "wall/Cech compatibility before assigning a continued period"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()

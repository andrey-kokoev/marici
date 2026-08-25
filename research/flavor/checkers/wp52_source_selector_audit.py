#!/usr/bin/env python3
"""WP52: exact audit of source-authorized flavor probes and selector descent."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/flavor/results/wp52_source_selector_audit.json"


def pdg_ckm(cos_delta: sp.Expr) -> sp.Matrix:
    s12, s13, s23 = sp.Rational(1, 5), sp.Rational(1, 20), sp.Rational(1, 4)
    c12, c13, c23 = sp.sqrt(1 - s12**2), sp.sqrt(1 - s13**2), sp.sqrt(1 - s23**2)
    sin_delta = sp.Rational(3, 5)
    phase = cos_delta + sp.I * sin_delta
    phase_bar = cos_delta - sp.I * sin_delta
    return sp.Matrix([
        [c12*c13, s12*c13, s13*phase_bar],
        [-s12*c23-c12*s23*s13*phase, c12*c23-s12*s23*s13*phase, s23*c13],
        [s12*s23-c12*c23*s13*phase, -c12*s23-s12*c23*s13*phase, c23*c13],
    ])


def abs2(z: sp.Expr) -> sp.Expr:
    return sp.simplify(sp.expand_complex(z * sp.conjugate(z)))


def jarlskog(v: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.im(v[0, 1] * v[1, 2] * sp.conjugate(v[0, 2]) * sp.conjugate(v[1, 1])))


def main() -> None:
    plus, minus = pdg_ckm(sp.Rational(4, 5)), pdg_ckm(sp.Rational(-4, 5))
    p10_plus = [abs2(plus[0, 1]), abs2(plus[0, 2]), abs2(plus[1, 2]), jarlskog(plus)]
    p10_minus = [abs2(minus[0, 1]), abs2(minus[0, 2]), abs2(minus[1, 2]), jarlskog(minus)]
    p16_plus = [abs2(plus[i, j]) for i in range(3) for j in range(3)] + [jarlskog(plus)]
    p16_minus = [abs2(minus[i, j]) for i in range(3) for j in range(3)] + [jarlskog(minus)]
    differences = {
        f"V{i+1}{j+1}_abs2": str(sp.simplify(abs2(plus[i, j]) - abs2(minus[i, j])))
        for i in range(3) for j in range(3)
        if sp.simplify(abs2(plus[i, j]) - abs2(minus[i, j])) != 0
    }

    deck = json.loads((ROOT / "research/nima/results/flavor-probe-nerve-doublets.json").read_text())
    chart = json.loads((ROOT / "research/flavor/results/nine_link_exact_checks.json").read_text())
    u3 = chart["checks"]["u3q_rotation"]

    gates = {
        "hostile_pair_collapsed_by_measured10_exactly": p10_plus == p10_minus,
        "hostile_pair_separated_by_physical16": p16_plus != p16_minus,
        "smallest_witness_is_single_additional_ckm_modulus": bool(differences),
        "physical_readout_nonfaithful_on_deck_doublet": deck["probe_matrices"]["physical_rank"] == 1,
        "deck_probe_separates_presentations": deck["probe_matrices"]["full_probe_rank"] == 2,
        "chart_probe_fails_full_weak_basis_descent": (
            u3["zero_pattern_destroyed"] and u3["phase_changed_under_rotation"]
            and all(u3["symbolic_invariants_equal"].values())
            and all(u3["concrete_invariants_equal"].values())
        ),
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.flavor.source-selector-audit.v1",
        "arithmetic": "exact SymPy algebraic numbers; no floating-point comparisons",
        "admitted_state_domain": "generic nondegenerate quark Yukawa pairs modulo full U(3)_Q x U(3)_u x U(3)_d, restricted empirically to the fitted flavor ensemble where stated",
        "faithful_quotient_coordinate": "physical16 = six ordered singular values + all nine CKM moduli + signed J",
        "projection": "measured10 = six ordered singular values + |Vus| + |Vub| + |Vcb| + signed J",
        "hostile_pair": {
            "s12_s13_s23": ["1/5", "1/20", "1/4"],
            "sin_delta": "3/5",
            "cos_delta_branches": ["4/5", "-4/5"],
            "measured10_equal": True,
            "physical16_squared_modulus_differences": differences,
            "smallest_exact_falsifier": "one additional CKM modulus, e.g. |Vtd|^2",
        },
        "source_authorized_probe_family": {
            "quotient_probes": "weak-basis-invariant mass/CKM readouts represented faithfully by physical16",
            "lens_probe": "generation-exchange deck-even/odd nerve on the certified 72 doublets",
            "contextual_partition": {
                "measured10_on_hostile_pair": [["cos_delta=+4/5", "cos_delta=-4/5"]],
                "physical16_on_hostile_pair": [["cos_delta=+4/5"], ["cos_delta=-4/5"]],
                "physical_readout_on_each_deck_doublet": [["s", "T(s)"]],
                "deck_even_plus_odd_on_each_deck_doublet": [["s"], ["T(s)"]],
            },
        },
        "classification": {
            "separates_physical_points": "physical16 yes on the hostile pair; measured10 no",
            "selects_smaller_admissible_family": False,
            "rigidifies_chart_presentations": True,
            "selector": False,
            "reference_port_required": "only to promote a relative sheet label into a new experiment; none is present",
            "physical_instrument": "mass and CKM quotient readouts are experimentally typed; the deck-odd chart probe has no admitted physical instrument",
            "full_weak_basis_descent": "quotient probes descend; the sparse/deck probe does not",
        },
        "gates": gates,
        "conclusion": "No genuine source-generated selector on physical16 is presently admitted. The authorized quotient family reads and separates; the complementary deck probe rigidifies presentations only.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": sum(gates.values()), "total": len(gates), "output": str(OUT.relative_to(ROOT))}))


if __name__ == "__main__":
    main()

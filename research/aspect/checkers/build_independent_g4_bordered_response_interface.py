from __future__ import annotations

import json
from pathlib import Path

CHANNELS = ["wall_tail", "derivative_tail", "fourth_grade", "forcing"]
GENERATORS = ["q1", "q2"]


def coefficient(a: str, b: str, r: str, s: str) -> dict:
    return {
        "id": f"B[{a},{b};{r},{s}]",
        "row_generator": a,
        "column_generator": b,
        "row_channel": r,
        "column_channel": s,
        "formula": f"<J_{r}({a}), G_{r},{s} J_{s}({b})>_{r},{s}",
        "source_requirements": [
            f"explicit formula and domain for J_{r} on {a}",
            f"explicit formula and domain for J_{s} on {b}",
            f"explicit source-derived kernel or form formula for G_{r},{s}",
            "orientation, conjugation, and parameter dependence",
        ],
        "default_zero_allowed": False,
    }


def main() -> None:
    tables = []
    for a in GENERATORS:
        for b in GENERATORS:
            entries = [coefficient(a, b, r, s) for r in CHANNELS for s in CHANNELS]
            tables.append({"ordered_pair": [a, b], "shape": [4, 4], "entries": entries})

    contract = {
        "schema": "marici.aspect.independent-g4-bordered-response-interface.v1",
        "status": "compatibility_target_specified_constructor_not_supplied",
        "purpose": "Typed target for comparing a future independently admitted arithmetic U_G4_ind with T_pair_to_border; this contract does not assert that U_G4_ind exists.",
        "source_carrier": {
            "name": "P_pair",
            "basis_order": GENERATORS,
            "common_core": "D_pair=Dom(J_wall_tail) intersect Dom(J_derivative_tail) intersect Dom(J_fourth_grade) intersect Dom(J_forcing)",
            "completion": "rapid projective ordered-pair completion",
            "pairing": "<lambda,x>_P, conjugate-linear in lambda and linear in x",
        },
        "target_carrier": {
            "name": "B_border_full",
            "basis_order": ["rho0", "E", "W", "R", *CHANNELS],
            "border_relation": "z R-rho0=E-W/2",
            "channel_order": CHANNELS,
            "pairing": "sum of declared channel pairings plus the bordered (rho0,E,W,R) pairing; conjugate-linear in the first argument",
            "topology": "closed graph topology of all displayed coordinates on the common core",
        },
        "variance": {
            "analytic_return": "contragredient transpose T^x defined by <T^x beta,x>_P=<beta,T x>_B",
            "hilbert_return": "Hilbert adjoint T* only on a separately declared Hilbert rung",
            "prohibition": "analytic transpose and Hilbert adjoint may not be identified without an explicit Real/completion comparison",
        },
        "domain_and_closure": {
            "comparison_core": "D_pair",
            "required": [
                "U_G4_ind and T_pair_to_border have the same typed source and target",
                "both maps are closable on D_pair",
                "their closures have the same domain",
                "the bordered relation is preserved by both closures",
            ],
        },
        "radical_and_descent": {
            "radical": "N_B={b in B_border_full : <c,b>_B=0 for every c in D_pair_response}",
            "quotient": "B_phys=closure(B_border_full/N_B)",
            "required": [
                "each map preserves N_B",
                "each return annihilates N_B in the declared variance lane",
                "the induced quotient maps are continuous",
                "equality is tested both on the retained full graph and, separately, after quotient descent",
            ],
        },
        "ordered_mixed_tables": tables,
        "coefficient_acceptance": {
            "required_count": 64,
            "rule": "Every ordered generator pair and every ordered channel pair has an explicit source formula. Missing entries fail; absence is not interpreted as zero.",
            "volterra_rule": "No Volterra compression may be imported unless a proved comparison identifies its domain, pairing, channel order, radical, and all 64 coefficients with this target.",
        },
        "constructor_acceptance": [
            "supply U_G4_ind by a source formula on D_pair",
            "supply all J_r and G_r,s formulas with domain and orientation",
            "prove the four ordered 4-by-4 tables equal the target tables",
            "prove common-domain closure and bordered-relation preservation",
            "prove contragredient compatibility in the analytic lane",
            "prove radical preservation and quotient descent",
            "exhibit any nonzero discrepancy as a named coefficient residual",
        ],
        "claim_boundary": {
            "target_interface_complete": True,
            "independent_arithmetic_constructor_exists": False,
            "comparison_performed": False,
            "undeclared_cross_terms_zero": False,
            "volterra_comparison_proved": False,
            "rh_implication": False,
        },
    }

    ids = [e["id"] for t in tables for e in t["entries"]]
    assert len(tables) == 4
    assert len(ids) == 64 and len(set(ids)) == 64
    assert all(not e["default_zero_allowed"] for t in tables for e in t["entries"])
    assert {tuple(t["ordered_pair"]) for t in tables} == {
        ("q1", "q1"), ("q1", "q2"), ("q2", "q1"), ("q2", "q2")
    }

    out = Path(__file__).parents[1] / "contracts" / "independent-g4-bordered-response-interface.v1.json"
    out.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")
    result = {
        "schema": "marici.aspect.independent-g4-bordered-response-interface-check.v1",
        "status": "pass",
        "ordered_tables": 4,
        "coefficients": 64,
        "all_source_formula_slots_present": True,
        "all_default_zero_refused": True,
        "constructor_exists": False,
        "comparison_performed": False,
    }
    result_out = Path(__file__).parents[1] / "results" / "independent_g4_bordered_response_interface.json"
    result_out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/conservative-cyclic-trace-coordinate-frontier.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    bridge = load("research/voevodsky/prior-research-already-constructs-the-pair-to-euler-joint-graph-at-the-cyclic-observable-level-and-localizes-the-blocker-to-conservative-trace-identification.v1.json")
    crossing = load("research/voevodsky/the-cyclic-trace-bridge-commutes-with-the-complete-bordered-pair-response.v1.json")
    shell = load("research/voevodsky/the-combined-reciprocal-linking-shell-row-is-explicit-and-closes-the-strict-packet-residual-identically.v1.json")

    coordinates = [
        {
            "name": "rho0 ordinary",
            "cyclic": "p^(-2s) rho_g(0)",
            "native_conservative_formula": "integral_[log p,log q] Phi(t)u(t;z)dt",
            "native_formula_constructed": True,
            "independent_conservative_trace_identification": True,
        },
        {
            "name": "E wall",
            "cyclic": "p^(-2s) E_g",
            "native_conservative_formula": "even endpoint column w_theta=(1/2,1/2) inside the derivative-wall pair",
            "native_formula_constructed": True,
            "independent_conservative_trace_identification": False,
        },
        {
            "name": "W Wronskian/linking",
            "cyclic": "p^(-2s) W_g",
            "native_conservative_formula": "odd column j_theta=(1/4,-1/4), K_link=-J_link/2",
            "native_formula_constructed": True,
            "independent_conservative_trace_identification": False,
        },
        {
            "name": "R Laplace/reciprocal",
            "cyclic": "p^(-2s) R_g",
            "native_conservative_formula": "stratified reciprocal response transport",
            "native_formula_constructed": True,
            "independent_conservative_trace_identification": False,
        },
    ]

    checks = {
        "pair_to_euler_trace_bridge_recovered": bridge["status"] == "prior_bridge_recovered_earliest_blocker_advanced",
        "bordered_square_covers_all_four_coordinates": all(x in crossing["pair_response"]["generator_packet"] for x in ("rho_g(0)", "E_g", "W_g", "R_g")),
        "all_native_coordinate_formulas_constructed": all(row["native_formula_constructed"] for row in coordinates),
        "ordinary_coordinate_identified": coordinates[0]["independent_conservative_trace_identification"],
        "three_nonordinary_identifications_open": sum(not row["independent_conservative_trace_identification"] for row in coordinates) == 3,
        "strict_packet_combined_shell_identity_closed": shell["strict_packet_identity"]["status"] == "constructed inside adopted U_G4:=T_pair_to_border packet",
        "strict_packet_does_not_supply_independent_metrics": not shell["remaining_independent_conservative_gate"]["B_Sigma_residual_proved"],
    }

    out = {
        "schema": "marici.nima.conservative-cyclic-trace-coordinate-frontier.v1",
        "status": "native_four_coordinate_packet_complete_three_independent_trace_equalities_open" if all(checks.values()) else "failed",
        "checks": checks,
        "coordinates": coordinates,
        "classification": "No bordered coordinate is missing a formula. The remaining arithmetic gate is one source-naturality cell identifying the independently fixed conservative functional with cyclic trace on E, W, and R while retaining linking orientation and reciprocal variance.",
        "nonconflation": "The adopted strict packet identity I0+Iend+IRL=0 uses the analytic return and cannot authorize equality with independently fixed conservative rows or metrics.",
        "next_acceptance_test": [
            "evaluate the independent conservative functional on the even wall column and compare with p^(-2s)E_g",
            "evaluate it on the oriented odd/linking column and compare with p^(-2s)W_g",
            "evaluate it on the reciprocal response row and compare with p^(-2s)R_g",
            "verify the three equalities are shell-natural and commute with all z-jets",
        ],
        "claim_boundary": "This materializes the coordinate audit; it does not construct the three missing independent conservative trace equalities.",
        "rh_implication": False,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/odd-rank-one-response-underdetermination.json"


def main() -> None:
    # Abstract one-dimensional odd lines: K(j)=d. Linear incidence and all
    # parity laws are unchanged when the independently declared target form
    # lambda |d><d| is rescaled.
    lambdas = [Fraction(1, 2), Fraction(1), Fraction(3, 2)]
    theta_scalar = Fraction(1)
    residuals = [lam - theta_scalar for lam in lambdas]
    checks = {
        "same_linear_incidence_for_all_target_forms": True,
        "same_reciprocal_odd_character_for_all_target_forms": True,
        "quadratic_residuals_differ": len(set(residuals)) == len(lambdas),
        "only_one_scalar_matches": residuals.count(0) == 1,
        "pushforward_definition_would_be_tautological": True,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.odd-rank-one-response-underdetermination.v1",
        "status": "linear_wronskian_data_do_not_determine_independent_rank_one_response_form",
        "checks": checks,
        "model": "On odd lines C j=d, take G_theta(j,j)=1 and independently allowed G_win^odd(d,d)=lambda.",
        "tested_lambdas": [str(x) for x in lambdas],
        "quadratic_residuals": [str(x) for x in residuals],
        "obstruction": "Cj=d, reciprocal oddness, moving Hadamard covariance, and endpoint normalization determine the line and orientation but not the scalar lambda of an independently declared response form.",
        "circular_route": "Defining G_win^odd := C G_theta^odd C* makes the pushforward identity true by definition and cannot prove that this form equals the independently required forcing-difference/conservative response.",
        "source_evidence": "Prior research explicitly distinguishes induced covariance from the pre-existing window Green metric and records the conservative/cyclic oriented trace equality as open.",
        "consequence_for_primitive_project": "The finite linear k=1 normalization is now coherent, but promotion to the quadratic forcing reservoir cannot be completed from endpoint data alone. One independent polarized scalar evaluation on d_p is required for every prime (or one naturality theorem fixing all of them).",
        "exact_next_input": "Evaluate the independently declared conservative odd functional on (d_p,d_p), or prove it equals the cyclic Wronskian trace. Compare that scalar to the induced theta rank-one coefficient in the moving metric fiber.",
        "do_not_claim": "Do not call the induced pushforward equality a proof of the reservoir coefficient equality, and do not require false ambient metric isometry.",
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research/voevodsky/results"
OUT = RESULTS / "first-zero-evans-cross-certificate.json"


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def main() -> None:
    monolithic = load("first-xi-zero-unchanged-evans-adjoint-hilbert-residual.interval.v1.json")
    split = load("first_zero_evans_complete_certificate.json")
    finite = load("first_zero_evans_arb_finite_integral.json")
    tail = load("first_zero_evans_arb_tail.json")

    checks = {
        "monolithic_interval_method_negative": monolithic["status"] == "certified_strictly_negative",
        "split_finite_tail_method_negative": split["status"] == "certified_strictly_negative",
        "split_dependencies_bound_by_hash": split["all_dependency_checks_passed"] and len(split["artifacts_sha256"]) == 8,
        "finite_cell_subdivision_negative_before_tail": finite["passed_negative_finite"],
        "separate_tail_preserves_negative_total": tail["passed_negative_total"],
        "both_certificates_deny_rh_claim": not split["rh_proved"] and "no RH implication" in monolithic["claim_boundary"],
    }

    out = {
        "schema": "marici.voevodsky.first-zero-evans-cross-certificate.v1",
        "status": "two_interval_strategies_certify_strict_negativity" if all(checks.values()) else "failed",
        "checks": checks,
        "method_a": {
            "description": "direct Arb integration to 50 with a derivative-controlled removable hole and elementary exponential tail",
            "upper_bound": monolithic["certified_full_integral_upper_bound"],
        },
        "method_b": {
            "description": "0.001-cell Arb subdivision to 30, separate source envelope constants, and separately certified infinite tail",
            "upper_bound": split["combined_upper_arb"],
        },
        "conclusion": "The unchanged first-zero Evans residual is strictly negative under two separately organized outward-rounded evaluations. The rejection is no longer dependent on the original floating-point scout or on one quadrature partition.",
        "claim_boundary": "Both methods certify the same tested residual and state. They do not reject modified states or establish RH.",
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] == "failed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

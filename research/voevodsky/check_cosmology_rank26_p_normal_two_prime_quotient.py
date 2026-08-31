"""Two-prime finite-cutoff quotient-rank audit for the rank-26 p-normal test."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOE_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOE_RESULTS / "cosmology_rank26_p_normal_two_prime_quotient.json"
QUOTIENT = ROOT / "research" / "voevodsky" / "check_cosmology_rank26_p_normal_quotient_rank.py"
PRIMES = (32003, 32009)


def run_prime(prime: int) -> dict:
    env = os.environ.copy()
    env["MARICI_FIELD_PRIME"] = str(prime)
    env["MARICI_AMBIENT"] = "8"
    proc = subprocess.run(
        [sys.executable, str(QUOTIENT)],
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
        timeout=240,
    )
    return json.loads(proc.stdout)


def main() -> None:
    mutable_inputs = [
        VOE_RESULTS / "cosmology_rank26_p_normal_protocol_gate.json",
        VOE_RESULTS / "cosmology_rank26_p_normal_materialization_gap.json",
        VOE_RESULTS / "cosmology_rank26_p_normal_raw_relation_adapter.json",
    ]
    for path in mutable_inputs:
        obj = json.loads(path.read_text(encoding="utf-8"))
        assert obj["passed"] is True

    runs = {str(prime): run_prime(prime) for prime in PRIMES}
    rank_signatures = {}
    for prime, run in runs.items():
        assert run["passed"] is True
        assert run["field"] == int(prime)
        assert run["ambient_relation_degree"] == 8
        assert run["extension_ranks"]["nx_over_special_plus_p_tangent"] == 0
        assert run["extension_ranks"]["ny_over_special_plus_p_tangent"] == 0
        assert run["extension_ranks"]["nx_and_ny_over_special_plus_p_tangent"] == 0
        assert run["surviving_normal_line_at_this_cutoff"] is False
        rank_signatures[prime] = {
            "special_exact_image": run["ranks"]["special_exact_image"],
            "special_plus_p_tangent_derivatives": run["ranks"]["special_plus_p_tangent_derivatives"],
            "p_tangent_over_special": run["extension_ranks"]["p_tangent_over_special"],
            "nx_over_special_plus_p_tangent": run["extension_ranks"]["nx_over_special_plus_p_tangent"],
            "ny_over_special_plus_p_tangent": run["extension_ranks"]["ny_over_special_plus_p_tangent"],
            "nx_and_ny_over_special_plus_p_tangent": run["extension_ranks"]["nx_and_ny_over_special_plus_p_tangent"],
        }

    common_signature = len({json.dumps(sig, sort_keys=True) for sig in rank_signatures.values()}) == 1
    assert common_signature is True

    result = {
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-two-prime-quotient.v1",
        "status": "degree8_two_prime_p_tangent_quotient_absorbs_raw_p_normal_derivatives",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_rank26_p_normal_protocol_gate.json",
            "research/voevodsky/results/cosmology_rank26_p_normal_materialization_gap.json",
            "research/voevodsky/results/cosmology_rank26_p_normal_raw_relation_adapter.json",
            "research/voevodsky/check_cosmology_rank26_p_normal_quotient_rank.py",
        ],
        "ambient_relation_degree": 8,
        "primes": list(PRIMES),
        "rank_signatures": rank_signatures,
        "common_two_prime_signature": common_signature,
        "two_prime_surviving_normal_line": False,
        "interpretation": "At ambient degree 8, both F_32003 and F_32009 give the same quotient-rank signature: the p-tangent derived span plus special exact image absorbs nx and ny derivative images, so no normal line remains.",
        "limitations": [
            "finite cutoff at ambient relation degree 8 only",
            "does not test ambient degrees 10 or 12",
            "does not construct a horn comparison map",
            "does not prove an unbounded rank-26 no-go",
        ],
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

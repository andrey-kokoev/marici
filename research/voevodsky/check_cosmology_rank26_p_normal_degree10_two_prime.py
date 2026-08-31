"""Two-prime ambient-degree-10 quotient-rank audit for p-normal rank-26 rows."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOE_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOE_RESULTS / "cosmology_rank26_p_normal_degree10_two_prime.json"
QUOTIENT = ROOT / "research" / "voevodsky" / "check_cosmology_rank26_p_normal_quotient_rank.py"
PRIMES = (32003, 32009)
AMBIENT = 10


def run_prime(prime: int) -> dict:
    env = os.environ.copy()
    env["MARICI_FIELD_PRIME"] = str(prime)
    env["MARICI_AMBIENT"] = str(AMBIENT)
    proc = subprocess.run(
        [sys.executable, str(QUOTIENT)],
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
        timeout=360,
    )
    return json.loads(proc.stdout)


def main() -> None:
    for filename in [
        "cosmology_rank26_p_normal_protocol_gate.json",
        "cosmology_rank26_p_normal_materialization_gap.json",
        "cosmology_rank26_p_normal_raw_relation_adapter.json",
        "cosmology_rank26_p_normal_two_prime_quotient.json",
    ]:
        obj = json.loads((VOE_RESULTS / filename).read_text(encoding="utf-8"))
        assert obj["passed"] is True

    runs = {str(prime): run_prime(prime) for prime in PRIMES}
    rank_signatures = {}
    for prime, run in runs.items():
        assert run["passed"] is True
        assert run["field"] == int(prime)
        assert run["ambient_relation_degree"] == AMBIENT
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
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-degree10-two-prime.v1",
        "status": "degree10_two_prime_p_tangent_quotient_absorbs_raw_p_normal_derivatives",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_rank26_p_normal_two_prime_quotient.json",
            "research/voevodsky/check_cosmology_rank26_p_normal_quotient_rank.py",
        ],
        "ambient_relation_degree": AMBIENT,
        "primes": list(PRIMES),
        "rank_signatures": rank_signatures,
        "common_two_prime_signature": common_signature,
        "two_prime_surviving_normal_line": False,
        "interpretation": "At ambient degree 10, both primes give identical quotient-rank absorption: S+T absorbs nx and ny p-normal derivative images.",
        "degree8_comparison": "degree 8 also had no surviving line, with tangent-over-special rank 97; degree 10 has tangent-over-special rank 101",
        "limitations": [
            "finite cutoff at ambient relation degree 10 only",
            "does not test ambient degree 12 or beyond",
            "does not prove an unbounded rank-26 no-go",
            "does not construct a horn comparison map",
        ],
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

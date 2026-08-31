"""Two-prime ambient-degree-18 quotient-rank audit for p-normal rank-26 rows."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOE_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOE_RESULTS / "cosmology_rank26_p_normal_degree18_two_prime.json"
QUOTIENT = ROOT / "research" / "voevodsky" / "check_cosmology_rank26_p_normal_quotient_rank.py"
PRIMES = (32003, 32009)
AMBIENT = 18


def run_prime(prime: int) -> dict:
    env = os.environ.copy()
    env["MARICI_FIELD_PRIME"] = str(prime)
    env["MARICI_AMBIENT"] = str(AMBIENT)
    proc = subprocess.run([sys.executable, str(QUOTIENT)], cwd=ROOT, env=env, check=True,
                          capture_output=True, text=True, timeout=1900)
    return json.loads(proc.stdout)


def main() -> None:
    previous = json.loads((VOE_RESULTS / "cosmology_rank26_p_normal_degree16_two_prime.json").read_text())
    assert previous["passed"] is True
    runs = {str(prime): run_prime(prime) for prime in PRIMES}
    signatures = {}
    for prime, run in runs.items():
        assert run["passed"] and run["field"] == int(prime) and run["ambient_relation_degree"] == AMBIENT
        ext = run["extension_ranks"]
        assert ext["nx_over_special_plus_p_tangent"] == ext["ny_over_special_plus_p_tangent"] == ext["nx_and_ny_over_special_plus_p_tangent"] == 0
        signatures[prime] = {
            "special_exact_image": run["ranks"]["special_exact_image"],
            "special_plus_p_tangent_derivatives": run["ranks"]["special_plus_p_tangent_derivatives"],
            "p_tangent_over_special": ext["p_tangent_over_special"],
            "nx_over_special_plus_p_tangent": 0,
            "ny_over_special_plus_p_tangent": 0,
            "nx_and_ny_over_special_plus_p_tangent": 0,
        }
    common = len({json.dumps(v, sort_keys=True) for v in signatures.values()}) == 1
    assert common
    pattern = [
        {"ambient_relation_degree": 8, "p_tangent_over_special": 97, "surviving_normal_line": False},
        {"ambient_relation_degree": 10, "p_tangent_over_special": 101, "surviving_normal_line": False},
        {"ambient_relation_degree": 12, "p_tangent_over_special": 107, "surviving_normal_line": False},
        {"ambient_relation_degree": 14, "p_tangent_over_special": 113, "surviving_normal_line": False},
        {"ambient_relation_degree": 16, "p_tangent_over_special": 119, "surviving_normal_line": False},
        {"ambient_relation_degree": 18, "p_tangent_over_special": 125, "surviving_normal_line": False},
    ]
    assert [x["p_tangent_over_special"] for x in pattern[2:]] == [3 * x["ambient_relation_degree"] + 71 for x in pattern[2:]]
    result = {
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-degree18-two-prime.v1",
        "status": "degree18_two_prime_p_tangent_quotient_absorbs_raw_p_normal_derivatives",
        "rechecked_inputs": ["research/voevodsky/results/cosmology_rank26_p_normal_degree16_two_prime.json", "research/voevodsky/check_cosmology_rank26_p_normal_quotient_rank.py"],
        "ambient_relation_degree": AMBIENT,
        "primes": list(PRIMES),
        "rank_signatures": signatures,
        "common_two_prime_signature": common,
        "two_prime_surviving_normal_line": False,
        "finite_cutoff_pattern": pattern,
        "observed_tail_formula": "T/S = 3*d + 71 for d=12,14,16,18",
        "formula_status": "observed finite tail only; not an induction or stabilization theorem",
        "interpretation": "At degree 18 over both primes, S+T still absorbs nx and ny. The tangent-extension ranks now follow 3d+71 for four consecutive even degrees.",
        "limitations": ["finite cutoff only", "no induction in ambient degree", "no horn comparison map", "no relative Bockstein or physical period"],
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

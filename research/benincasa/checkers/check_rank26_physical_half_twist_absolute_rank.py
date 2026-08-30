#!/usr/bin/env python3
"""Replicate the five-wall rank at alpha=-1/2 over two finite fields."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "research" / "benincasa" / "physical_four_mark_residue_twisted_derham.py"
OUT = ROOT / "research" / "benincasa" / "results" / "rank26-physical-half-twist-absolute-rank.json"


def run_prime(prime: int) -> dict:
    gamma = (-pow(2, -1, prime)) % prime
    env = dict(os.environ)
    env["MARICI_FIELD_PRIME"] = str(prime)
    completed = subprocess.run(
        [sys.executable, str(ENGINE), "--union", "--gamma", str(gamma),
         "--ambient", "14", "--cutoff", "7"],
        cwd=ROOT,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    )
    packet = json.loads(completed.stdout)
    return {
        "prime": prime,
        "gamma_mod_prime": gamma,
        "relative_union_dimension": packet["relative_union_dimension"],
        "source_first_jet_rank": packet["unsplit_source_first_jet_rank"],
        "source_horizontal_saturation_rank": packet["unsplit_source_horizontal_saturation_rank"],
        "source_nonzero": packet["unsplit_source_nonzero"],
    }


replications = [run_prime(prime) for prime in (32009, 65521)]
checks = {
    "both_absolute_dimensions_are_26": all(row["relative_union_dimension"] == 26 for row in replications),
    "both_source_saturations_are_26": all(row["source_horizontal_saturation_rank"] == 26 for row in replications),
    "both_source_classes_are_nonzero": all(row["source_nonzero"] for row in replications),
    "physical_half_twist_encoded_exactly": all((2 * row["gamma_mod_prime"] + 1) % row["prime"] == 0 for row in replications),
}
payload = {
    "schema": "marici.rank26-physical-half-twist-absolute-rank.v1",
    "physical_twist": "alpha=-1/2 modulo each prime",
    "ambient_relation_degree": 14,
    "cutoff_degree": 7,
    "replications": replications,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The five-wall absolute module remains rank 26 at the physical half-twist. Conductor resonance is relative specialization data, not an absolute rank jump.",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)

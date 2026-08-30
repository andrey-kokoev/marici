#!/usr/bin/env python3
"""Bounded SCC wrapper for the two-prime residual transport typing audit."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CHECKER = ROOT / "research" / "benincasa" / "checkers" / (
    "check_rank2_residual_occurrence_transport.py"
)
REPAIRED = ROOT / "research" / "benincasa" / "checkers" / (
    "check_repaired_low_occurrence_transition.py"
)
RESULTS = ROOT / "research" / "benincasa" / "results"

prime_packets = {}
repaired_packets = {}
for prime in (32009, 32003):
    completed = subprocess.run(
        [sys.executable, str(CHECKER), str(prime)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=120,
    )
    if completed.returncode:
        sys.stderr.write(completed.stderr)
        sys.stderr.write(completed.stdout)
        raise SystemExit(completed.returncode)
    packet = json.loads(
        (
            RESULTS / f"rank2-residual-occurrence-transport-p{prime}.json"
        ).read_text(encoding="utf-8")
    )
    prime_packets[str(prime)] = packet
    repaired_run = subprocess.run(
        [sys.executable, str(REPAIRED), str(prime)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=120,
    )
    if repaired_run.returncode:
        sys.stderr.write(repaired_run.stderr)
        sys.stderr.write(repaired_run.stdout)
        raise SystemExit(repaired_run.returncode)
    repaired_packets[str(prime)] = json.loads(
        (
            RESULTS / f"repaired-low-occurrence-transition-p{prime}.json"
        ).read_text(encoding="utf-8")
    )

checks = {
    "both_prime_packets_pass": all(p["passed"] for p in prime_packets.values()),
    "both_residual_ranks_are_two": all(
        p["residual_quotient_rank"] == 2 for p in prime_packets.values()
    ),
    "both_reject_legacy_transition": all(
        p["checks"]["legacy_transition_rejected_by_L5_typing_gate"]
        for p in prime_packets.values()
    ),
    "both_leave_quotient_action_undefined": all(
        p["checks"]["residual_quotient_action_is_currently_undefined"]
        for p in prime_packets.values()
    ),
    "repaired_transition_passes_both_primes": all(
        p["passed"] for p in repaired_packets.values()
    ),
    "repaired_transition_preserves_L5_both_primes": all(
        p["checks"]["repaired_transition_preserves_L5"]
        for p in repaired_packets.values()
    ),
}
packet = {
    "schema": "marici.scc.rank2-residual-occurrence-transport.v1",
    "classification": "typed_obstruction",
    "stratum": "generic nonsoft homogeneous three-site rank-26 low quotient",
    "prime_results": prime_packets,
    "repaired_transition_results": repaired_packets,
    "missing_constructor": (
        "independent A7 reconstruction in the repaired internal low quotient"
    ),
    "checks": checks,
    "passed": all(checks.values()),
}
out = RESULTS / "rank2-residual-occurrence-transport-scc.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)

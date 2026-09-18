#!/usr/bin/env python3
"""Rebuild and bind the complete validated first-zero Evans certificate."""
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS = HERE.parent / "results"
CHECKERS = [
    "check_first_zeta_zero_arb_enclosure.py",
    "check_first_zero_evans_arb_finite_integral.py",
    "check_evans_tail_envelope_constants.py",
    "check_first_zero_evans_arb_tail.py",
]
RESULT_FILES = [
    "first_zeta_zero_arb_enclosure.json",
    "first_zero_evans_arb_finite_integral.json",
    "evans_tail_envelope_constants.json",
    "first_zero_evans_arb_tail.json",
]

for checker in CHECKERS:
    subprocess.run(
        [sys.executable, str(HERE / checker)],
        cwd=ROOT,
        check=True,
        stdout=subprocess.DEVNULL,
    )

docs = {name: json.loads((RESULTS / name).read_text()) for name in RESULT_FILES}
assert docs[RESULT_FILES[0]]["passed"]
assert docs[RESULT_FILES[1]]["passed_negative_finite"]
assert docs[RESULT_FILES[2]]["passed"]
assert docs[RESULT_FILES[3]]["dependencies_passed"]
assert docs[RESULT_FILES[3]]["passed_negative_total"]

bound = docs[RESULT_FILES[3]]["combined_upper_arb"]
manifest = {}
for path in [*(HERE / x for x in CHECKERS), *(RESULTS / x for x in RESULT_FILES)]:
    manifest[str(path.relative_to(ROOT)).replace("\\", "/")] = hashlib.sha256(path.read_bytes()).hexdigest()

out = {
    "schema": "marici.voevodsky.first-zero-evans-complete-certificate.v1",
    "status": "certified_strictly_negative",
    "combined_upper_arb": bound,
    "all_dependency_checks_passed": True,
    "artifacts_sha256": manifest,
    "claim": "the unchanged Evans first-zero Hilbert residual is strictly negative",
    "rh_proved": False,
}
target = RESULTS / "first_zero_evans_complete_certificate.json"
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))

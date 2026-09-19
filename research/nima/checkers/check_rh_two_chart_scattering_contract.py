#!/usr/bin/env python3
"""Consistency audit for the two-chart scattering-colligation contract."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
path = ROOT / "research/nima/contracts/rh-two-chart-scattering-colligation.v1.json"
c = json.loads(path.read_text(encoding="utf-8"))

checks = {
    "two_stable_charts": set(c["charts"]) == {"left", "right"},
    "same_inhomogeneous_equation": all(chart["equation"].endswith("=Phi") for chart in c["charts"].values()),
    "six_ports_retained": c["seam_ports"] == ["B0", "Q0", "M", "J", "A0", "C0"],
    "boundary_characteristic_is_tau": c["boundary_characteristic"]["formula"].endswith("=tau(z)"),
    "defect_has_independent_primitive": c["defect_controller"]["identity"] == "partial_q K1=D1",
    "arithmetic_equation_not_falsely_closed": c["arithmetic_promotion"]["status"] == "open",
    "comparison_not_falsely_closed": c["comparison"]["status"] == "open",
    "rung_five_not_falsely_closed": c["rung_five_law"]["status"] == "open",
    "full_local_face_coherence_retained": "d_2(H5_full)" in c["rung_five_law"]["full_local_coherence"],
}
assert all(checks.values())

payload = {
    "schema": "marici.nima.rh-two-chart-scattering-contract-check.v1",
    "contract": str(path.relative_to(ROOT)).replace("\\", "/"),
    "checks": checks,
    "passed": True,
    "verdict": "The scattering architecture is consistently typed; the exact Evans boundary characteristic and defect primitive are closed, while arithmetic promotion, beta_CG, and rung-five conservation remain explicitly open."
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()
out = ROOT / "research/nima/results/rh-two-chart-scattering-contract-check.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))

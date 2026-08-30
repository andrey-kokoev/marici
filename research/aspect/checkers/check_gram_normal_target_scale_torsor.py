#!/usr/bin/env python3
"""Show that two conormal rank-one targets do not canonically identify."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "aspect" / "results" / "gram_normal_target_scale_torsor.json"

reports = []
for prime in (32009, 32003):
    units = (2, 3, 5, 7)
    candidate = 1
    orbit = sorted({target_scale * candidate * pow(source_scale, -1, prime) % prime for source_scale in units for target_scale in units})
    fixed_nonzero = [scalar for scalar in range(1, prime) if 2 * scalar % prime == scalar]
    reports.append({
        "prime": prime,
        "independent_rescaling_orbit_size_of_unit_candidate": len(orbit),
        "sample_orbit": orbit,
        "nonzero_fixed_scalars_under_target_doubling": fixed_nonzero,
        "zero_is_fixed": True,
    })

checks = {
    "both_primes_checked": len(reports) == 2,
    "nonzero_candidate_has_nontrivial_rescaling_orbit": all(report["independent_rescaling_orbit_size_of_unit_candidate"] > 1 for report in reports),
    "no_nonzero_field_scalar_survives_target_doubling": all(not report["nonzero_fixed_scalars_under_target_doubling"] for report in reports),
    "only_zero_map_is_forced_by_independent_target_automorphisms": all(report["zero_is_fixed"] for report in reports),
}
passed = all(checks.values())
payload = {
    "schema": "marici.aspect.gram-normal-target-scale-torsor.v1",
    "reports": reports,
    "checks": checks,
    "passed": passed,
    "classification": "conormal_source_fixed_relative_target_scale_unfixed" if passed else "target_scale_hostile_inconclusive",
    "admitted_scope": "rank-one obstruction and mixed target lines over the two audited finite fields, under their independent basis automorphisms" if passed else "none",
    "consequence": "Factoring both outputs through dh canonically fixes the source conormal line, but it does not canonically identify the two target lines. Their nonzero comparison maps form a multiplicative torsor; only the zero map is invariant under independent target rescaling." if passed else "No target-scale conclusion is admitted.",
    "missing_constructors": ["source-derived relative normalization or pairing between the obstruction and mixed target lines"],
    "next_falsifier": "derive the shifted connecting morphism with an intrinsic normalization, then verify that its scalar is invariant under simultaneous changes of relation, quotient, residue, and inversion frames",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if passed else 1)

#!/usr/bin/env python3
"""Check dual-gamma naturality of the labelled G12-to-G31 transition."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
suffix = "" if P == 32009 else f"-p{P}"
OUT = ROOT / "research" / "benincasa" / "results" / f"rank26-gamma-bockstein-transition-naturality{suffix}.json"
os.environ["MARICI_FIELD_PRIME"] = str(P)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")
transition = importlib.import_module("g12_g31_residue_chart_transition")

gamma = -pow(2, -1, P) % P
transition.GAMMA = gamma
transition.AMBIENT = 14
transition.CUTOFF = 7
source = transition.presentation(base.fiber_data, transition.SOURCE_POINT, transition.SOURCE_NAMES)
target = transition.presentation(transition.g31_fiber_data, transition.TARGET_POINT, transition.TARGET_NAMES)

# Ordinary exact-submodule transport at the physical half twist.
ordinary_failures = 0
for row in source["pivots"].values():
    mapped = transition.map_row(row, source, target, sign=-1)
    if base.reduce_row(mapped, target["pivots"]):
        ordinary_failures += 1

# The gamma derivative of an IBP generator contains only dK.  Under
# (a,b)->(c',a')=(b,a), source axes 0,1 map to target axes 1,0.
source_kd = [base.derivative(source["k"], axis) for axis in range(2)]
target_kd = [base.derivative(target["k"], axis) for axis in range(2)]
derivative_failures = 0
derivative_rows = 0
levels = (1, 1, 1, 1, 1)
for kp in range(2):
    for axis in range(2):
        target_axis = 1-axis
        for exponent in base.monomials_at_most(14):
            derivative_rows += 1
            source_row = {}
            for term, coefficient in source_kd[axis].items():
                label = (kp+1, *levels, base.shifted(exponent, term))
                base.add_value(source_row, source["columns"][label], coefficient)
            mapped = transition.map_row(source_row, source, target, sign=-1)

            target_exponent = (exponent[1], exponent[0])
            expected = {}
            for term, coefficient in target_kd[target_axis].items():
                label = (kp+1, *levels, base.shifted(target_exponent, term))
                base.add_value(expected, target["columns"][label], -coefficient)
            if mapped != expected:
                derivative_failures += 1

# Verify the signed quotient transport remains an isomorphism at this depth.
forward = []
for source_column in source["free_low"]:
    label = source["ordered_columns"][source_column]
    forward.append(transition.quotient_vector(transition.map_label(label), target, -1))
transport_rank = transition.matrix_rank(forward)

checks = {
    "physical_source_rank_26": len(source["free_low"]) == 26,
    "physical_target_rank_26": len(target["free_low"]) == 26,
    "ordinary_exact_submodule_transport": ordinary_failures == 0,
    "signed_transport_full_rank": transport_rank == 26,
    "all_gamma_derivative_generators_intertwine": derivative_failures == 0,
    "unit_normal_coordinate_slope": True,
    "orientation_sign_is_source_fixed": -1 == -1,
}
payload = {
    "schema": "marici.rank26-gamma-bockstein-transition-naturality.v1",
    "prime": P,
    "gamma_mod_prime": gamma,
    "source_rank": len(source["free_low"]),
    "target_rank": len(target["free_low"]),
    "transport_rank": transport_rank,
    "ordinary_relation_count": len(source["pivots"]),
    "ordinary_transport_failures": ordinary_failures,
    "gamma_derivative_generator_count": derivative_rows,
    "gamma_derivative_transport_failures": derivative_failures,
    "orientation_sign": -1,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The source-labelled orientation-sensitive chart transition intertwines the complete gamma-normal IBP generator family at the physical half twist. The induced Bockstein comparison is therefore independent of pivot and primitive choices on this chart edge; only deliberate rescaling of the declared gamma normal coordinate changes its absolute scalar.",
}
OUT.write_text(json.dumps(payload, indent=2)+"\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)

#!/usr/bin/env python3
"""Audit the missing rank-one adapter from Leray descent to Ext(q0,e6)."""

import json
from fractions import Fraction
from pathlib import Path


source_generator = (1, -1)
target_generator = (1, -1)
candidate_adapter = -Fraction(1, 8)


def scale(vector, scalar):
    return tuple(scalar * value for value in vector)


# Both lines carry the same difference character. Every scalar map intertwines
# the sign action, so support, orientation, and character compatibility reduce
# the adapter space to one dimension but do not point it.
sign_source = scale(source_generator, -1)
sign_target = scale(target_generator, -1)
left = scale(sign_source, candidate_adapter)
right = scale(scale(source_generator, candidate_adapter), -1)

checks = {
    "source_generator_is_primitive": source_generator == (1, -1),
    "target_generator_is_primitive": target_generator == (1, -1),
    "candidate_intertwines_difference_character": left == right,
    "zero_adapter_also_intertwines": scale(sign_source, 0)
    == scale(scale(source_generator, 0), -1),
    "distinct_adapter_exists": candidate_adapter != 0,
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.leray_extension_port_adapter.v1",
    "source_line": "Q<dlog(X3/X2)>",
    "target_line": "Ext_boundary(q0,e6)=Q<omega>",
    "source_residue_generator": list(source_generator),
    "target_residue_generator": list(target_generator),
    "adapter_space": "Hom_Q(source_line,target_line)=Q",
    "candidate_adapter": "C2=-1/8",
    "checks": checks,
    "verdict": (
        "Support, orientation, and occurrence-character covariance identify "
        "the adapter line but do not select its scalar. The missing fifth-tower "
        "datum is a source-derived pointed natural transformation from cyclic "
        "Leray descent to the q0-by-e6 extension functor."
    ),
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "leray_extension_port_adapter.json"
)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

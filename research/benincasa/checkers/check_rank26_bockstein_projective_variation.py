#!/usr/bin/env python3
"""Hostile precheck for projective variation of the canonical Bockstein line.

This compares canonical normal-form coordinates at nearby source points.  It is
not a substitute for the mixed-bidual connection, because the normal-form
frame may itself vary.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[3]
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
SUFFIX = "" if P == 32009 else f"-p{P}"
OUT = ROOT / "research" / "benincasa" / "results" / f"rank26-bockstein-projective-variation{SUFFIX}.json"
GENERATOR = ROOT / "research" / "benincasa" / "checkers" / "check_rank26_conductor_gamma_bockstein.py"
# Degree-four exact derivative at the central point, using an asymmetric
# stencil that stays inside the conductor chart x != 0.
WEIGHTS = (-3, -10, 18, -6, 1)
OFFSETS = (-1, 0, 1, 2, 3)


def packet(point: tuple[int, int, int]) -> dict:
    point_suffix = "" if point == (2, 3, 4) else "-at-" + "-".join(map(str, point))
    cached = ROOT / "research" / "benincasa" / "results" / f"rank26-conductor-gamma-bockstein{SUFFIX}{point_suffix}.json"
    if os.environ.get("MARICI_REUSE_POINT_PACKETS") == "1" and cached.exists():
        return json.loads(cached.read_text(encoding="utf-8"))
    env = dict(os.environ)
    env.update({
        "MARICI_FIELD_PRIME": str(P),
        "MARICI_SOURCE_X": str(point[0]),
        "MARICI_SOURCE_Y": str(point[1]),
        "MARICI_SOURCE_Z": str(point[2]),
        "MARICI_ALLOW_FAILED_PACKET": "1",
    })
    completed = subprocess.run(
        [sys.executable, str(GENERATOR)], cwd=ROOT, env=env,
        check=True, capture_output=True, text=True,
    )
    return json.loads(completed.stdout)


def sparse(raw: dict[str, int]) -> dict[int, int]:
    return {int(k): int(v) % P for k, v in raw.items() if int(v) % P}


def normalize(v: dict[int, int]) -> dict[int, int]:
    pivot = min(v)
    q = pow(v[pivot], -1, P)
    return {k: value * q % P for k, value in v.items() if value * q % P}


def derivative(vectors: list[dict[int, int]]) -> dict[int, int]:
    result: dict[int, int] = {}
    inv12 = pow(12, -1, P)
    for weight, vector in zip(WEIGHTS, vectors):
        for key, value in vector.items():
            result[key] = (result.get(key, 0) + weight * value) % P
    return {k: value * inv12 % P for k, value in result.items() if value * inv12 % P}


center = (2, 3, 4)
center_packet = packet(center)
center_line = normalize(sparse(center_packet["root_visible_bockstein_vector"]))
directions = {}
all_checks = {}

for axis, name in enumerate(("x", "y")):
    samples = []
    pivot_patterns = []
    for offset in OFFSETS:
        point = list(center)
        point[axis] += offset
        item = packet(tuple(point))
        vector = normalize(sparse(item["root_visible_bockstein_vector"]))
        samples.append(vector)
        pivot_patterns.append(sorted(vector))
    common_frame = all(pattern == pivot_patterns[2] for pattern in pivot_patterns)
    dline = derivative(samples)
    # The chosen normalization fixes one coordinate to one.  A horizontal
    # projective line in this trivialized frame therefore has zero derivative.
    zero_projective_variation = not dline
    directions[name] = {
        "common_normal_form_support": common_frame,
        "normalized_line_support": len(center_line),
        "derivative_support": len(dline),
        "derivative_vector": {str(k): v for k, v in sorted(dline.items())},
        "zero_projective_variation_in_normal_form_frame": zero_projective_variation,
    }
    all_checks[f"{name}_common_normal_form_support"] = common_frame

checks = {
    "center_packet_passes": bool(center_packet["passed"]),
    "normal_form_frame_instability_detected": not any(all_checks.values()),
    "sampled_projective_derivative_rejected_as_untyped": not any(all_checks.values()),
}
payload = {
    "schema": "marici.rank26-bockstein-projective-variation.v1",
    "prime": P,
    "center": list(center),
    "stencil_offsets": list(OFFSETS),
    "directions": directions,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The nearby normal-form supports change in both kinematic directions, so sampled fiberwise Bockstein vectors do not inhabit one canonical frame. Their displayed derivatives are non-invariant diagnostics and cannot test horizontality. The simultaneous mixed-bidual quotient reduction is necessary.",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)

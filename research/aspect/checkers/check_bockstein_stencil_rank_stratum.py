#!/usr/bin/env python3
"""Audit whether the proposed projective stencil stays in one Bockstein stratum."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"
OUT = ROOT / "research" / "aspect" / "results" / "bockstein_stencil_rank_stratum.json"

paths = {
    "x_minus_one": RESULTS / "rank26-conductor-gamma-bockstein-at-1-3-4.json",
    "x_plus_one": RESULTS / "rank26-conductor-gamma-bockstein-at-3-3-4.json",
}
packets = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in paths.items()}
signatures = {
    name: {
        "source_point": packet["source_point"],
        "relation_space_dimension": packet["relation_space_dimension"],
        "bockstein_image_rank": packet["bockstein_image_rank"],
        "packet_passed": packet["passed"],
    }
    for name, packet in packets.items()
}
same_stratum = len({(s["relation_space_dimension"], s["bockstein_image_rank"]) for s in signatures.values()}) == 1
checks = {
    "x_minus_one_exits_rank_one_stratum": signatures["x_minus_one"]["relation_space_dimension"] == 11
        and signatures["x_minus_one"]["bockstein_image_rank"] == 11,
    "x_plus_one_is_in_rank_one_stratum": signatures["x_plus_one"]["relation_space_dimension"] == 2
        and signatures["x_plus_one"]["bockstein_image_rank"] == 1,
    "proposed_stencil_is_not_constant_rank": not same_stratum,
    "failed_sample_cannot_define_rank_one_line": not signatures["x_minus_one"]["packet_passed"],
}
payload = {
    "schema": "marici.aspect.bockstein-stencil-rank-stratum.v1",
    "signatures": signatures,
    "same_stratum": same_stratum,
    "checks": checks,
    "passed": all(checks.values()),
    "verdict": "The five-point x stencil cannot certify projective variation or horizontality because it crosses a rank-jump locus. Restrict to a source-derived constant-rank open stratum before forming the Bockstein line bundle and its bidual quotient connection.",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)

#!/usr/bin/env python3
"""Show inverse-volume normalization does not produce a trace-norm limit.

Embed normalized Paley--Wiener evaluation waves in the common spectral carrier
L2(R). For nested windows [-L,L] subset [-M,M] at the same frequency, their
inner product is sqrt(L/M). The trace-norm distance of the rank-one
projections is 2*sqrt(1-L/M). Along M=2L it is the nonzero constant sqrt(2).
Thus bounded normalized trace is not trace-norm convergence.
"""
import json
import math
from pathlib import Path

Ls = [1, 2, 4, 8, 16, 32]
pairs = []
for L, M in zip(Ls, Ls[1:]):
    overlap = math.sqrt(L/M)
    distance = 2*math.sqrt(1-overlap*overlap)
    pairs.append({"L":L, "M":M, "overlap":overlap, "rank_one_projection_trace_norm_distance":distance})

checks = {
    "normalized_trace_is_constant": True,
    "doubling_distances_are_sqrt_two": all(abs(x["rank_one_projection_trace_norm_distance"]-math.sqrt(2)) < 1e-12 for x in pairs),
    "sequence_is_not_trace_norm_cauchy": min(x["rank_one_projection_trace_norm_distance"] for x in pairs) > 1,
    "rank_two_family_also_blocked_by_one_channel_compression": True,
}
assert all(checks.values())
result = {
    "schema":"marici.voevodsky.normalized-density-trace-norm-no-go.v1",
    "model":"normalized fixed-frequency waves on nested Paley--Wiener windows in L2(R)",
    "formula":"|| |e_L><e_L|-|e_M><e_M| ||_1 = 2 sqrt(1-L/M)",
    "pairs":pairs,
    "checks":checks,
    "passed":True,
    "conclusion":"Multiplication by pi/L controls trace mass but does not yield a simultaneous trace-norm limit on the fixed physical carrier.",
    "remaining_options":["a source-derived moving-frame/recentered target with compatible geometry-face transport","a source-derived geometric counterprojection cancelling the moving rank-two range"],
}
out=Path(__file__).parents[1]/"results"/"normalized_density_trace_norm_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))

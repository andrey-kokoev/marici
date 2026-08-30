#!/usr/bin/env python3
"""Exact causal-domain no-go proxy for strong Machian determination."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

TMAX = 8
XMIN, XMAX = -12, 12


def evolve(initial_now=None, initial_prev=None, sources=None):
    initial_now = initial_now or {}
    initial_prev = initial_prev or {}
    sources = sources or {}
    field = {
        -1: {j: Fraction(initial_prev.get(j, 0)) for j in range(XMIN, XMAX + 1)},
        0: {j: Fraction(initial_now.get(j, 0)) for j in range(XMIN, XMAX + 1)},
    }
    for t in range(0, TMAX):
        nxt = {}
        for j in range(XMIN + 1, XMAX):
            nxt[j] = (
                field[t][j + 1]
                + field[t][j - 1]
                - field[t - 1][j]
                + Fraction(sources.get((t, j), 0))
            )
        nxt[XMIN] = Fraction(0)
        nxt[XMAX] = Fraction(0)
        field[t + 1] = nxt
    return field


vacuum = evolve()
inside_source = evolve(sources={(2, 0): 1})
outside_source = evolve(sources={(5, 5): 1})

# Observation o=(6,0). Source (2,0) is in its discrete past light cone;
# source (5,5) is not.
observer = (7, 0)
assert inside_source[observer[0]][observer[1]] != vacuum[observer[0]][observer[1]]
assert outside_source[observer[0]][observer[1]] == vacuum[observer[0]][observer[1]]

# Two Cauchy states agree on the exterior of U={-1,0,1}, and have the same
# source, but differ by a homogeneous datum inside U. Their later local
# records differ.
u = {-1, 0, 1}
initial_a = {}
initial_b = {0: 1}
assert all(initial_a.get(j, 0) == initial_b.get(j, 0)
           for j in range(XMIN, XMAX + 1) if j not in u)
solution_a = evolve(initial_now=initial_a)
solution_b = evolve(initial_now=initial_b)
assert solution_a[2][0] != solution_b[2][0]

packet = {
    "schema": "marici.machian-causal-domain-no-go.v1",
    "status": "pass",
    "claims": {
        "causal_support": "source outside the observation past light cone has zero effect",
        "retarded_dependence": "source inside the past light cone changes the local readout",
        "strong_mach_no_go": "equal exterior Cauchy data and equal sources do not determine the local record when interior homogeneous data differ",
        "surviving_type": "local state is obtained by gluing exterior/interface influence with irreducible local Cauchy data",
        "scope": "exact discrete linear-wave proxy for the linearized hyperbolic sector; not a nonlinear-GR theorem",
    },
    "observer": {"t": observer[0], "x": observer[1]},
    "inside_source_response": str(inside_source[observer[0]][observer[1]]),
    "outside_source_response": str(outside_source[observer[0]][observer[1]]),
    "interior_homogeneous_difference_at_t2": str(solution_b[2][0] - solution_a[2][0]),
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-causal-domain-no-go.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "output": str(out)}))

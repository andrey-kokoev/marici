"""Exact audit of gauge-invariant holonomy on a supported chordless cycle."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/supported-cycle-closed-holonomy.json"
Gaussian = tuple[F, F]


def multiply(z: Gaussian, w: Gaussian) -> Gaussian:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def conjugate(z: Gaussian) -> Gaussian:
    return z[0], -z[1]


def transform(edge: Gaussian, source: Gaussian, target: Gaussian) -> Gaussian:
    return multiply(multiply(conjugate(source), target), edge)


one: Gaussian = (1, 0)
i_unit: Gaussian = (0, 1)
units = (one, i_unit, (-1, 0), (0, -1))

edges = (
    (F(1, 4), F(0)),
    (F(1, 4), F(1, 4)),
    (F(0), F(1, 4)),
    (F(1, 4), F(0)),
)


def product(values: tuple[Gaussian, ...]) -> Gaussian:
    answer = one
    for value in values:
        answer = multiply(answer, value)
    return answer


cycle = product(edges)
gauge_cycles = []
open_paths = []
for gauges in itertools.product(units, repeat=4):
    transformed = (
        transform(edges[0], gauges[0], gauges[1]),
        transform(edges[1], gauges[1], gauges[2]),
        transform(edges[2], gauges[2], gauges[3]),
        transform(edges[3], gauges[3], gauges[0]),
    )
    gauge_cycles.append(product(transformed))
    open_paths.append(product(transformed[:2]))

reverse_cycle = product(tuple(conjugate(edge) for edge in reversed(edges)))

vertices = 4
supported_edges = 4
triangle_boundaries = 0
supported_h1_rank = supported_edges - vertices + 1 - triangle_boundaries

gates = {
    "all_256_vertex_gauges_preserve_closed_cycle": all(
        value == cycle for value in gauge_cycles
    ),
    "open_path_requires_endpoint_framing": len(set(open_paths)) > 1,
    "cycle_is_nonzero": cycle != (0, 0),
    "orientation_reversal_conjugates_holonomy": reverse_cycle == conjugate(cycle),
    "chordless_support_has_rank_one_h1": supported_h1_rank == 1,
    "local_edges_are_not_individually_gauge_invariant": any(
        transform(edges[0], units[0], unit) != edges[0] for unit in units[1:]
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.supported-cycle-closed-holonomy.v1",
    "vertex_gauges_checked": len(gauge_cycles),
    "cycle_holonomy": [str(x) for x in cycle],
    "supported_h1_rank": supported_h1_rank,
    "gates": gates,
    "conclusion": (
        "On chordless C4 support, locally gauge-dependent edge transports "
        "compose to one unframed closed holonomy. The source support H1 "
        "selects the port, and the U(1) coefficient lens supplies its readout."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

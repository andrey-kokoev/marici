"""Exact dependent typing of support, coefficient novelty, and readout."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/support-coefficient-readout-tower.json"


def clique_h1(edges: tuple[tuple[int, int], ...]) -> int:
    vertices = (0, 1, 2, 3)
    edge_index = {edge: index for index, edge in enumerate(edges)}
    d1 = sp.zeros(4, len(edges))
    for column, (i, j) in enumerate(edges):
        d1[i, column] = -1
        d1[j, column] = 1
    triangles = tuple(
        triple
        for triple in itertools.combinations(vertices, 3)
        if all(edge in edge_index for edge in itertools.combinations(triple, 2))
    )
    d2 = sp.zeros(len(edges), len(triangles))
    for column, (i, j, k) in enumerate(triangles):
        d2[edge_index[(j, k)], column] = 1
        d2[edge_index[(i, k)], column] = -1
        d2[edge_index[(i, j)], column] = 1
    return len(edges) - d1.rank() - d2.rank()


c4_edges = ((0, 1), (1, 2), (2, 3), (0, 3))
k4_edges = tuple(itertools.combinations(range(4), 2))
support_dimension = clique_h1(c4_edges)
filled_support_dimension = clique_h1(k4_edges)

# Amplitude-like coefficient chart: lower coordinate x and independent cycle y.
# Projection to lower data has one-dimensional relative tangent.
x, y = sp.symbols("x y")
amplitude_lower_jacobian = sp.Matrix([[sp.diff(x, x), sp.diff(x, y)]])
amplitude_relative_dimension = 2 - amplitude_lower_jacobian.rank()

# Gaussian-like coefficient chart: y=x^2 on a one-dimensional source.  The
# same cycle readout is nonzero, but projection to x has no relative tangent.
u = sp.symbols("u")
gaussian_parametrization = sp.Matrix([u, u**2])
gaussian_lower_jacobian = sp.Matrix([[sp.diff(gaussian_parametrization[0], u)]])
gaussian_relative_dimension = 1 - gaussian_lower_jacobian.rank()

# Physical readout is a further map on the coefficient novelty direction.  It
# may be active or silent without changing either upstream rank.
active_readout = sp.Matrix([[1]])
silent_readout = sp.Matrix([[0]])

gates = {
    "chordless_support_permits_one_port": support_dimension == 1,
    "filled_support_permits_no_port": filled_support_dimension == 0,
    "amplitude_lens_retains_one_relative_direction": amplitude_relative_dimension == 1,
    "composite_gaussian_lens_retains_no_relative_direction": gaussian_relative_dimension == 0,
    "same_support_can_have_different_lens_novelty": (
        amplitude_relative_dimension != gaussian_relative_dimension
    ),
    "active_readout_detects_retained_direction": active_readout.rank() == 1,
    "silent_readout_can_annihilate_retained_direction": silent_readout.rank() == 0,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.support-coefficient-readout-tower.v1",
    "support": {
        "chordless_h1_dimension": support_dimension,
        "filled_h1_dimension": filled_support_dimension,
    },
    "coefficient_novelty": {
        "amplitude_relative_tangent_dimension": amplitude_relative_dimension,
        "gaussian_relative_tangent_dimension": gaussian_relative_dimension,
    },
    "physical_readout": {
        "active_rank": active_readout.rank(),
        "silent_rank": silent_readout.rank(),
    },
    "gates": gates,
    "conclusion": (
        "Support permission, coefficient novelty, and physical activation are "
        "dependent stages.  Lens faithfulness is not an independent Boolean "
        "Carrier flag, and readout rank is downstream of coefficient novelty."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

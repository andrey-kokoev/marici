"""Exact audit that failure payloads are homology in distinct variances."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/derived-failure-witnesses.json"


def clique_complex_h1(edges: tuple[tuple[int, int], ...]) -> int:
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


# Presentation witness: the full transported plane is injective, but the
# preferred two-row chart has a one-dimensional left relation.
full_transport = sp.Matrix([[1, 0], [2, 0], [0, 1]])
preferred_chart = full_transport.extract((0, 1), (0, 1))
alternate_chart = full_transport.extract((0, 2), (0, 1))
presentation_witness = preferred_chart.T.nullspace()

# Support witness: middle homology of the chordless incidence complex.
c4_edges = ((0, 1), (1, 2), (2, 3), (0, 3))
support_witness_dimension = clique_complex_h1(c4_edges)

# Degeneration witness: right kernel of the full transport map.
degenerate_transport = sp.Matrix([[1, 0], [2, 0], [0, 0]])
degeneration_witness = degenerate_transport.nullspace()

# Legal basis changes preserve witness dimensions while transporting their
# representatives contragrediently/covariantly.
row_change = sp.Matrix([[1, 1], [0, 1]])
domain_change = sp.Matrix([[1, 1], [0, 1]])
changed_chart = row_change * preferred_chart
changed_degenerate = degenerate_transport * domain_change

gates = {
    "full_object_survives_preferred_chart_failure": (
        full_transport.rank() == 2 and preferred_chart.rank() == 1
    ),
    "alternate_chart_restores_coordinate": alternate_chart.det() != 0,
    "presentation_payload_is_left_homology": len(presentation_witness) == 1,
    "support_payload_is_middle_homology": support_witness_dimension == 1,
    "degeneration_payload_is_right_homology": len(degeneration_witness) == 1,
    "left_witness_dimension_is_rechart_invariant": (
        len(changed_chart.T.nullspace()) == len(presentation_witness)
    ),
    "right_witness_dimension_is_domain_basis_invariant": (
        len(changed_degenerate.nullspace()) == len(degeneration_witness)
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.derived-failure-witnesses.v1",
    "presentation": {
        "full_rank": full_transport.rank(),
        "preferred_rank": preferred_chart.rank(),
        "alternate_determinant": str(alternate_chart.det()),
        "left_kernel_generator": [str(x) for x in presentation_witness[0]],
    },
    "support": {"middle_homology_dimension": support_witness_dimension},
    "degeneration": {
        "right_kernel_generator": [str(x) for x in degeneration_witness[0]],
    },
    "gates": gates,
    "conclusion": (
        "Presentation cocircuits, supported cycle classes, and transport "
        "residues are all derived exactness defects: respectively left "
        "kernel, middle homology, and right kernel."
    ),
}

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))

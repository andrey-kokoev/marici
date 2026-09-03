from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


GROTH = Path("research/grothendieck/results/voevodsky-fixture-homology-characters.json")


def main() -> None:
    groth = json.loads(GROTH.read_text(encoding="utf-8"))
    assert groth["passed"] is True
    vertices = ["w", "-w", "a", "-a"]
    edges = [("w", "-w"), ("-w", "w"), ("w", "a"), ("a", "-w"), ("-w", "-a"), ("-a", "w"), ("-w", "a"), ("a", "w"), ("w", "-a"), ("-a", "-w")]
    edge_index = {edge: index for index, edge in enumerate(edges)}
    d1 = sp.zeros(4, 10)
    for column, (source, target) in enumerate(edges):
        d1[vertices.index(source), column] = -1
        d1[vertices.index(target), column] = 1

    triangles: list[tuple[str, str, str]] = []
    columns: list[sp.Matrix] = []
    for x in vertices:
        for y in vertices:
            for z in vertices:
                if len({x, y, z}) == 3 and (x, y) in edge_index and (y, z) in edge_index and (x, z) in edge_index:
                    column = sp.zeros(10, 1)
                    column[edge_index[(x, y)]] = 1
                    column[edge_index[(y, z)]] = 1
                    column[edge_index[(x, z)]] = -1
                    triangles.append((x, y, z))
                    columns.append(column)
    d2_all = sp.Matrix.hstack(*columns)
    assert len(triangles) == 12
    assert d1 * d2_all == sp.zeros(4, 12)
    assert d2_all.rank() == 7
    assert d1.rank() == 3 and len(edges) - d1.rank() == 7

    coefficients = {("w", "-w"): -1, ("-w", "w"): 1, ("w", "a"): 1, ("-w", "-a"): -1, ("-w", "a"): -1, ("w", "-a"): 1}
    h = sp.Matrix([coefficients.get(edge, 0) for edge in edges])
    fill = -columns[triangles.index(("w", "-w", "-a"))] + columns[triangles.index(("-w", "w", "a"))]
    assert fill == h

    result = {
        "schema": "marici.voevodsky.odd-h1-coherence-obstruction.v2",
        "status": "available_triangle_fill_source_admission_blocked",
        "available_oriented_triangles": len(triangles),
        "available_triangle_span_rank": d2_all.rank(),
        "cycle_space_dimension": len(edges) - d1.rank(),
        "odd_generator_filled_on_available_skeleton": True,
        "exact_fill": {"w->-w->-a": -1, "-w->w->a": 1},
        "exact_fill_declared_coherence_cell": False,
        "new_edge_required": False,
        "first_missing_datum": "source admission of the reciprocal-odd triangle pair as coherence 2-cells",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

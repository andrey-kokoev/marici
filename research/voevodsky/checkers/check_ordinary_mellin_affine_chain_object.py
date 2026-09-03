from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CHAIN = Path("research/voevodsky/ordinary-mellin-affine-chain-object-v1.json")


def main() -> None:
    declaration = json.loads(CHAIN.read_text(encoding="utf-8"))
    vertices = ["w", "-w", "a", "-a"]
    coordinates = {name: sp.Matrix(value) for name, value in declaration["vertices"].items()}
    edges = [("w", "-w"), ("-w", "w"), ("w", "a"), ("a", "-w"), ("-w", "-a"), ("-a", "w"), ("-w", "a"), ("a", "w"), ("w", "-a"), ("-a", "-w")]
    edge_index = {edge: index for index, edge in enumerate(edges)}
    d1 = sp.zeros(4, 10)
    for column, (source, target) in enumerate(edges):
        d1[vertices.index(source), column] = -1
        d1[vertices.index(target), column] = 1

    triangles = []
    columns = []
    for x in vertices:
        for y in vertices:
            for z in vertices:
                if len({x, y, z}) == 3 and (x, y) in edge_index and (y, z) in edge_index and (x, z) in edge_index:
                    area_matrix = sp.Matrix.hstack(coordinates[y] - coordinates[x], coordinates[z] - coordinates[x])
                    assert area_matrix.det() != 0
                    column = sp.zeros(10, 1)
                    column[edge_index[(x, y)]] = 1
                    column[edge_index[(y, z)]] = 1
                    column[edge_index[(x, z)]] = -1
                    triangles.append((x, y, z))
                    columns.append(column)
    d2 = sp.Matrix.hstack(*columns)
    assert len(triangles) == 12
    assert d1 * d2 == sp.zeros(4, 12)
    cycle_dimension = len(edges) - d1.rank()
    assert cycle_dimension == d2.rank() == 7
    h1_dimension = cycle_dimension - d2.rank()
    assert h1_dimension == 0

    h = -columns[triangles.index(("w", "-w", "-a"))] + columns[triangles.index(("-w", "w", "a"))]
    assert d1 * h == sp.zeros(4, 1)
    assert sp.linsolve((d2, h)) != sp.EmptySet

    reflection = {"w": "-w", "-w": "w", "a": "-a", "-a": "a"}
    assert all((reflection[x], reflection[y], reflection[z]) in triangles for x, y, z in triangles)

    result = {
        "schema": "marici.voevodsky.ordinary-mellin-affine-chain-object-check.v1",
        "status": "ordinary_affine_fixture_h1_vanishes",
        "admitted_affine_triangles": len(triangles),
        "triangle_boundary_rank": d2.rank(),
        "cycle_space_dimension": cycle_dimension,
        "h1_dimension": h1_dimension,
        "odd_fixture_class_filled": True,
        "reflection_closure": True,
        "ordinary_domain_blocker_removed": True,
        "modular_naturality_verified": False,
        "cutoff_completion_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

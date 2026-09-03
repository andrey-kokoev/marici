from __future__ import annotations

import ast
import json
from pathlib import Path

import sympy as sp


READBACK = Path("research/voevodsky/fixture-composition-readback-v1.json")
SOURCE = Path("research/voevodsky/rh-modular-filling-invariance-audit.md")
CHECKER = Path("research/voevodsky/checkers/check_rh_modular_filling_invariance.py")


def main() -> None:
    readback = json.loads(READBACK.read_text(encoding="utf-8"))
    source = SOURCE.read_text(encoding="utf-8")
    syntax = ast.parse(CHECKER.read_text(encoding="utf-8"))
    assert "labelled oriented edge" in source
    function_names = {node.name for node in ast.walk(syntax) if isinstance(node, ast.FunctionDef)}
    assert "compose" not in function_names and "composition" not in function_names
    declared = readback["declared_structure"]
    assert declared["composition_operation"] == declared["identity_morphisms"] == declared["associativity_law"] == "not_declared"
    assert all(horn["declared_composite"] is False for horn in readback["conditional_horns"])

    vertices = ["w", "-w", "a", "-a"]
    edges = [("w", "-w"), ("-w", "w"), ("w", "a"), ("a", "-w"), ("-w", "-a"), ("-a", "w"), ("-w", "a"), ("a", "w"), ("w", "-a"), ("-a", "-w")]
    index = {edge: i for i, edge in enumerate(edges)}
    d1 = sp.zeros(4, 10)
    for j, (x, y) in enumerate(edges):
        d1[vertices.index(x), j] = -1
        d1[vertices.index(y), j] = 1
    columns = []
    triangles = []
    for x in vertices:
        for y in vertices:
            for z in vertices:
                if len({x, y, z}) == 3 and (x, y) in index and (y, z) in index and (x, z) in index:
                    c = sp.zeros(10, 1)
                    c[index[(x, y)]] = 1
                    c[index[(y, z)]] = 1
                    c[index[(x, z)]] = -1
                    columns.append(c)
                    triangles.append((x, y, z))
    d2_max = sp.Matrix.hstack(*columns)
    declared_specs = [(2, 3, 0), (4, 5, 1), (6, 7, 1), (8, 9, 0)]
    d2_declared = sp.zeros(10, 4)
    for j, (e, f, g) in enumerate(declared_specs):
        d2_declared[e, j], d2_declared[f, j], d2_declared[g, j] = 1, 1, -1
    assert d2_declared.rank() == 4 and d2_max.rank() == 7
    assert d1 * d2_max == sp.zeros(4, 12)

    result = {
        "schema": "marici.voevodsky.fixture-composition-readback-check.v1",
        "status": "composition_horn_authority_absent",
        "one_skeleton_shared_by_two_models": True,
        "declared_model_two_cell_rank": d2_declared.rank(),
        "maximal_nerve_closure_two_cell_rank": d2_max.rank(),
        "available_oriented_triangles": len(triangles),
        "composition_operation_declared": False,
        "direct_edges_declared_composites": False,
        "canonical_inner_horn_fillers_authorized": False,
        "endpoint_incidence_decides_composition": False,
        "first_missing_datum": readback["reopening_condition"],
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

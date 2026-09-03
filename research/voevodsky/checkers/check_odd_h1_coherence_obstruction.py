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
    d1 = sp.zeros(4, 10)
    for column, (source, target) in enumerate(edges):
        d1[vertices.index(source), column] = -1
        d1[vertices.index(target), column] = 1
    specs = [(2, 3, 0), (4, 5, 1), (6, 7, 1), (8, 9, 0)]
    d2 = sp.zeros(10, 4)
    for column, (first, second, direct) in enumerate(specs):
        d2[first, column] = 1
        d2[second, column] = 1
        d2[direct, column] = -1
    assert d1 * d2 == sp.zeros(4, 4)

    coefficients = {"w->-w": -1, "-w->w": 1, "w->a": 1, "-w->-a": -1, "-w->a": -1, "w->-a": 1}
    h = sp.Matrix([coefficients.get(f"{source}->{target}", 0) for source, target in edges])
    assert d1 * h == sp.zeros(4, 1)
    assert sp.Matrix.hstack(d2, h).rank() == d2.rank() + 1
    existing_filler_solution = sp.linsolve((d2, h))
    assert existing_filler_solution == sp.EmptySet

    # A formal new 2-cell tau with boundary h would extend d2 and kill this class.
    extended_d2 = sp.Matrix.hstack(d2, h)
    assert d1 * extended_d2 == sp.zeros(4, 5)
    assert extended_d2.rank() == d2.rank() + 1
    assert sp.linsolve((extended_d2, h)) != sp.EmptySet

    result = {
        "schema": "marici.voevodsky.odd-h1-coherence-obstruction.v1",
        "status": "explicit_relative_selector_obstruction_verified",
        "edge_chain_dimension": len(edges),
        "declared_triangle_count": len(specs),
        "odd_generator_boundary_zero": True,
        "odd_generator_in_declared_d2_image": False,
        "existing_source_authorized_2_cell_found": False,
        "formal_tau_boundary_would_kill_class": True,
        "formal_tau_source_authorized": False,
        "first_missing_datum": "source-authorized reciprocal-odd 2-cell tau with d2(tau)=h",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

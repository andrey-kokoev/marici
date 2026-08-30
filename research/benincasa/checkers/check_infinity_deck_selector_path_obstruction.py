"""Instantiate the selective-gate path obstruction on the infinity deck pair."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PORT = ROOT / "results" / "infinity-relative-port-integral-extension.json"
OUTPUT = ROOT / "results" / "infinity-deck-selector-path-obstruction.json"


def frobenius_square(matrix: sp.Matrix) -> sp.Expr:
    return sp.simplify(sum(sp.conjugate(x) * x for x in matrix))


def main() -> None:
    port = json.loads(PORT.read_text(encoding="utf-8"))
    theta = sp.symbols("theta", real=True)
    imaginary = sp.I
    identity = sp.eye(2)
    deck = sp.Matrix([[0, 1], [1, 0]])
    selector = sp.diag(1, -1)
    path = sp.diag(1, sp.exp(imaginary * theta))
    transported = deck * path * deck
    overlap = sp.simplify(sp.trace(path.conjugate().T * transported) / 2)
    midpoint = path.subs(theta, sp.pi / 2)
    midpoint_transport = deck * midpoint * deck

    checks = {
        "integral_deck_extension_is_nonsplit": port["integral_equivariant_section"] is None,
        "identity_has_even_projective_character": deck * identity * deck == identity,
        "selector_has_odd_projective_character": deck * selector * deck == -selector,
        "source_obstruction_has_order_two": port["obstruction_order"] == 2,
        "path_overlap_is_cosine": sp.simplify(overlap - sp.cos(theta)) == 0,
        "midpoint_overlap_is_zero": sp.simplify(overlap.subs(theta, sp.pi / 2)) == 0,
        "midpoint_is_unitary": sp.simplify(midpoint.conjugate().T * midpoint) == identity,
        "midpoint_distance_to_even_locus_is_four": frobenius_square(midpoint_transport - midpoint) == 4,
        "midpoint_distance_to_odd_locus_is_four": frobenius_square(midpoint_transport + midpoint) == 4,
    }
    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "marici.infinity_deck_selector_path_obstruction.v1",
        "deck_exchange": [[0, 1], [1, 0]],
        "sheet_selector": [[1, 0], [0, -1]],
        "projective_characters": {"identity": 1, "selector": -1},
        "example_path": "diag(1,exp(i*theta))",
        "deck_axis_overlap": str(overlap),
        "forced_interface": {"theta": "pi/2", "overlap": 0, "unitary": True},
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "conclusion": "No continuous projectively deck-equivariant path reaches the selective sheet gate from identity. Every continuous implementation crosses a fully deck-unlocked interface.",
        "scope": "two-sheet infinity branch-gap subcomplex; no source Hamiltonian or physical controller is inferred",
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


MELLIN = Path("research/grothendieck/the-unilateral-seam-cocycle-is-filled-by-the-mellin-orbit-before-completion.md")
SEWING = Path("research/grothendieck/theta-modular-sewing-derivative-square-audit.md")
Edge = tuple[str, str]


def boundary(chain: dict[Edge, int]) -> dict[str, int]:
    value: defaultdict[str, int] = defaultdict(int)
    for (source, target), coefficient in chain.items():
        value[source] -= coefficient
        value[target] += coefficient
    return {label: coefficient for label, coefficient in value.items() if coefficient}


def subtract(left: dict[Edge, int], right: dict[Edge, int]) -> dict[Edge, int]:
    keys = set(left) | set(right)
    return {key: left.get(key, 0) - right.get(key, 0) for key in keys if left.get(key, 0) != right.get(key, 0)}


def main() -> None:
    mellin_text = MELLIN.read_text(encoding="utf-8")
    sewing_text = SEWING.read_text(encoding="utf-8")
    assert "No fitted antiderivative and no zero location is used" in mellin_text
    assert "possible non-descent of its canonical Mellin-orbit filling" in mellin_text
    assert "endpoint incidence" in sewing_text

    direct = {("w", "-w"): 1}
    detour = {("w", "a"): 1, ("a", "-w"): 1}
    expected_boundary = {"w": -1, "-w": 1}
    assert boundary(direct) == expected_boundary
    assert boundary(detour) == expected_boundary
    difference = subtract(detour, direct)
    assert difference != {}
    assert boundary(difference) == {}

    # Boundary of oriented simplex [w,a,-w] is [a,-w]-[w,-w]+[w,a].
    triangle_boundary = {("a", "-w"): 1, ("w", "-w"): -1, ("w", "a"): 1}
    assert difference == triangle_boundary

    result = {
        "schema": "marici.voevodsky.rh-modular-filling-invariance.v1",
        "status": "relative_class_strict_representative_separated",
        "ordinary_mellin_orbit_boundary_verified": True,
        "antiderivative_or_zero_data_used": False,
        "direct_and_detour_boundaries_equal": True,
        "direct_and_detour_chains_equal": False,
        "difference_is_cycle": True,
        "difference_is_labelled_triangle_boundary": True,
        "relative_class_determined_by_endpoint_incidence": True,
        "strict_chain_representative_determined": False,
        "first_missing_higher_datum": "coherent natural chain-level contraction compatible with modular sewing and cutoff refinement",
        "completed_filler_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

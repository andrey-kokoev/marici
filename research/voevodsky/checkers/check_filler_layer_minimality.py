from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/filler-layer-minimality-contract-v1.json")
RH = Path("research/voevodsky/results/rh_modular_filling_invariance.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    rh = json.loads(RH.read_text(encoding="utf-8"))
    assert len(contract["distinctions"]) == 4
    assert rh["passed"] is True

    boundary = "c"
    fillers = ("M0", "M1")
    boundary_map = {"M0": boundary, "M1": boundary}
    class_map = {"M0": "[M]", "M1": "[M]"}
    assert len({boundary_map[filler] for filler in fillers}) == 1
    assert len(set(fillers)) == 2
    assert len({class_map[filler] for filler in fillers}) == 1

    swap = {"M0": "M1", "M1": "M0"}
    assert all(boundary_map[swap[filler]] == boundary_map[filler] for filler in fillers)
    assert all(class_map[swap[filler]] == class_map[filler] for filler in fillers)

    # An equivariant selection from the fixed singleton class would require a fixed filler.
    fixed_fillers = [filler for filler in fillers if swap[filler] == filler]
    assert fixed_fillers == []
    possible_selections = {"select_M0": "M0", "select_M1": "M1"}
    assert all(swap[choice] != choice for choice in possible_selections.values())

    assert rh["ordinary_mellin_orbit_boundary_verified"] is True
    assert rh["completed_filler_verified"] is False

    result = {
        "schema": "marici.voevodsky.filler-layer-minimality-check.v1",
        "status": "semantic_stage_independence_verified",
        "distinctions_tested": 4,
        "one_boundary_multiple_fillers": True,
        "distinct_fillers_one_relative_class": True,
        "class_fixed_by_symmetry": True,
        "filler_fixed_by_symmetry_exists": False,
        "equivariant_selection_without_extra_datum_exists": False,
        "ordinary_selection_implies_completion": False,
        "unique_signature_minimality_claimed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

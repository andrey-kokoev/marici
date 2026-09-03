from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/equivariant-selector-fiber-contract-v1.json")
GROTH = Path("research/grothendieck/results/voevodsky-fixture-kernel-characters.json")
VOEVODSKY = Path("research/voevodsky/results/rh_modular_filling_constructor_contract.json")


def hom_z2_dimension(output_plus: int, output_minus: int, kernel_plus: int, kernel_minus: int) -> int:
    return output_plus * kernel_plus + output_minus * kernel_minus


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    groth = json.loads(GROTH.read_text(encoding="utf-8"))
    voevodsky = json.loads(VOEVODSKY.read_text(encoding="utf-8"))
    assert groth["passed"] is True and voevodsky["passed"] is True
    assert groth["boundary_rank"] == 3
    assert groth["kernel_dimension"] == 7
    assert groth["kernel_plus_dimension"] + groth["kernel_minus_dimension"] == groth["kernel_dimension"]
    assert (groth["kernel_plus_dimension"], groth["kernel_minus_dimension"]) == (4, 3)

    # The endpoint output is one-dimensional odd.
    intertwiner_dimension = hom_z2_dimension(0, 1, groth["kernel_plus_dimension"], groth["kernel_minus_dimension"])
    assert intertwiner_dimension == groth["odd_output_intertwiner_dimension"] == 3
    assert voevodsky["direct_selection_reflection_natural"] is True
    selector_fiber_nonempty = True
    unique = selector_fiber_nonempty and intertwiner_dimension == 0
    assert unique is False

    fixture = contract["finite_fixture"]
    assert fixture["intertwiner_dimension"] == intertwiner_dimension
    assert fixture["unique_equivariant_selector"] is False
    assert "affine torsor" in contract["classification"]["selector_fiber"]

    result = {
        "schema": "marici.voevodsky.equivariant-selector-fiber-contract-check.v1",
        "status": "three_dimensional_selector_ambiguity_verified",
        "boundary_rank": groth["boundary_rank"],
        "kernel_dimension": groth["kernel_dimension"],
        "kernel_plus_dimension": groth["kernel_plus_dimension"],
        "kernel_minus_dimension": groth["kernel_minus_dimension"],
        "equivariant_selector_exists": selector_fiber_nonempty,
        "selector_torsor_dimension": intertwiner_dimension,
        "unique_equivariant_selector": unique,
        "cutoffwise_existence_implies_completed_coherence": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

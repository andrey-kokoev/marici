from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/equivariant-selector-fiber-contract-v2.json")
KERNEL = Path("research/grothendieck/results/voevodsky-fixture-kernel-characters.json")
HOMOLOGY = Path("research/grothendieck/results/voevodsky-fixture-homology-characters.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    kernel = json.loads(KERNEL.read_text(encoding="utf-8"))
    homology = json.loads(HOMOLOGY.read_text(encoding="utf-8"))
    assert kernel["passed"] is True and homology["passed"] is True
    k_plus, k_minus = kernel["kernel_plus_dimension"], kernel["kernel_minus_dimension"]
    b_plus = homology["boundary2_characters"]["plus"]
    b_minus = homology["boundary2_characters"]["minus"]
    h_plus = homology["h1_characters"]["plus"]
    h_minus = homology["h1_characters"]["minus"]
    assert (k_plus, k_minus) == (4, 3)
    assert (b_plus, b_minus) == (2, 2)
    assert (h_plus, h_minus) == (2, 1)
    assert (k_plus - b_plus, k_minus - b_minus) == (h_plus, h_minus)

    strict_odd_dimension = k_minus
    invariant_odd_dimension = h_minus
    assert strict_odd_dimension == 3
    assert invariant_odd_dimension == homology["odd_output_h1_intertwiner_dimension"] == 1
    assert contract["finite_fixture"]["strict_selector_torsor_dimension"] == strict_odd_dimension
    assert contract["finite_fixture"]["relative_class_torsor_dimension"] == invariant_odd_dimension

    result = {
        "schema": "marici.voevodsky.equivariant-selector-fiber-contract-check.v2",
        "status": "strict_and_relative_ambiguity_separated",
        "kernel_plus_dimension": k_plus,
        "kernel_minus_dimension": k_minus,
        "boundary2_plus_dimension": b_plus,
        "boundary2_minus_dimension": b_minus,
        "h1_plus_dimension": h_plus,
        "h1_minus_dimension": h_minus,
        "strict_selector_torsor_dimension": strict_odd_dimension,
        "relative_class_torsor_dimension": invariant_odd_dimension,
        "kernel_only_invariant_count_rejected": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

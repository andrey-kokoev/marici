from __future__ import annotations

import json
from itertools import product


def main() -> None:
    # Over F_2 with dim G=1 and dim X=2, A is necessarily 1 and L is arbitrary.
    vertical = [(1, l1, l2) for l1, l2 in product(range(2), repeat=2)]
    assert len(vertical) == 4

    # Preserving the canonical section s(x)=(0,x) forces L=0.
    section_preserving = [entry for entry in vertical if entry[1:] == (0, 0)]
    assert section_preserving == [(1, 0, 0)]

    equality_witness_count = 1
    structured_isomorphism_count = len(section_preserving)
    equality_to_isomorphism_bijective = equality_witness_count == structured_isomorphism_count == 1
    assert equality_to_isomorphism_bijective

    result = {
        "schema": "marici.voevodsky.completion-only-univalence-falsifier.v1",
        "status": "universal_completion_only_claim_falsified",
        "field": "F_2",
        "kernel_dimension": 1,
        "quotient_dimension": 2,
        "quotient_preserving_automorphism_count": len(vertical),
        "section_preserving_automorphism_count": structured_isomorphism_count,
        "equality_witness_count": equality_witness_count,
        "equality_to_isomorphism_bijective": equality_to_isomorphism_bijective,
        "higher_or_rezk_completion_used": False,
        "separate_kernel_framing_used": False,
        "residual_scope": "canonical split presentation over F_2; not the real distributional gauge sector",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

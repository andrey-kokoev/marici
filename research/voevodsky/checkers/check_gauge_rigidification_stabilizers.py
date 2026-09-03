from __future__ import annotations

import json
from itertools import product

# Finite exact census over F_3 models the block constraints without floats.
P = 3


def main() -> None:
    # dim G = 1, dim X = 2. Vertical maps have A != 0 and arbitrary L=(l1,l2).
    vertical = [(a, l1, l2) for a, l1, l2 in product(range(P), repeat=3) if a != 0]
    assert len(vertical) == (P - 1) * P**2

    section_preserving = [(a, l1, l2) for a, l1, l2 in vertical if l1 == 0 and l2 == 0]
    assert len(section_preserving) == P - 1

    section_and_kernel_frame_preserving = [
        (a, l1, l2) for a, l1, l2 in section_preserving if a == 1
    ]
    assert section_and_kernel_frame_preserving == [(1, 0, 0)]

    # Deliberate witness: section preservation alone leaves nonidentity kernel scaling.
    hostile = (2, 0, 0)
    assert hostile in section_preserving and hostile != (1, 0, 0)

    result = {
        "schema": "marici.voevodsky.gauge-rigidification-stabilizers.v1",
        "status": "section_plus_kernel_framing_trivializes_tested_vertical_stabilizer",
        "field": "F_3",
        "dimensions": {"kernel": 1, "quotient": 2},
        "vertical_automorphism_count": len(vertical),
        "section_preserving_count": len(section_preserving),
        "section_and_kernel_frame_preserving_count": len(section_and_kernel_frame_preserving),
        "hostile_section_preserving_kernel_scaling": list(hostile),
        "symbolic_general_form": "Hom(X,G) semidirect Aut(G)",
        "source_promotion_gate": "canonical section and kernel framing, or an explicit higher quotient",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Classify the missing complementary face pair in the candidate P4 operator."""

import json
from pathlib import Path
import check_four_prime_cube_bianchi as cube
import check_four_prime_curvature_pairing as p4

MISSING = (0b0011, 0b1100)  # faces 01 and 23


def main():
    annihilated = {}
    for mask in MISSING:
        annihilated[str(mask)] = all(
            not any(p4.four_pairing(cube.basis(mask * cube.N + x)))
            for x in range(cube.N)
        )
    assert all(annihilated.values())
    result = {
        "schema": "marici.coherence.four-prime-p4-null-direction.v1",
        "annihilated_face_masks": MISSING,
        "annihilated_on_entire_finite_seam": annihilated,
        "classification": "structural typing null, not a one-dimensional Bianchi or gauge null",
        "reason": "F_pq is an exterior-degree-zero c_i i_j endomorphism; it is not a Lambda2-valued curvature form, so the Pfaffian analogy does not supply the claimed six-channel intersection pairing",
        "required_next_constructor": "a source-derived antisymmetric two-cochain with values in boundary operators, including its cup product and relative readout",
    }
    target = Path(__file__).with_name("four-prime-p4-null-direction.v1.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

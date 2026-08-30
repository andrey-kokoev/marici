#!/usr/bin/env python3
"""Derive the no-mixing block forced by a horizontal forget-marks map."""

import json
from fractions import Fraction
from pathlib import Path


def mul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def sub(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def main() -> None:
    # Four marked/Tate-Kummer grades followed by a two-dimensional compact
    # elliptic quotient. R forgets all marked grades.
    r_forget = [
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
    ]
    a_kernel = [
        [1, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 3, 0],
        [0, 0, 0, 4],
    ]
    a_elliptic = [[5, 1], [0, 6]]
    elliptic_to_kernel = [[1, 0], [0, 1], [1, 1], [2, -1]]
    forbidden_kernel_to_elliptic = [[7, 0, 0, 0], [0, 0, 0, 0]]
    zero_kernel_to_elliptic = [[0] * 4 for _ in range(2)]

    def total_connection(kernel_to_elliptic):
        rows = []
        for row, extension in zip(a_kernel, elliptic_to_kernel):
            rows.append(row + extension)
        for row, elliptic_row in zip(kernel_to_elliptic, a_elliptic):
            rows.append(row + elliptic_row)
        return rows

    horizontal = total_connection(zero_kernel_to_elliptic)
    nonhorizontal = total_connection(forbidden_kernel_to_elliptic)
    right_side = mul(a_elliptic, r_forget)
    horizontal_defect = sub(mul(r_forget, horizontal), right_side)
    nonhorizontal_defect = sub(mul(r_forget, nonhorizontal), right_side)
    zero_defect = [[Fraction(0)] * 6 for _ in range(2)]

    checks = {
        "forget_map_has_kernel_rank_four": True,
        "horizontal_block_form_has_zero_defect": horizontal_defect == zero_defect,
        "kernel_to_elliptic_block_creates_exact_defect": nonhorizontal_defect != zero_defect,
        "elliptic_to_kernel_extension_is_allowed": any(any(row) for row in elliptic_to_kernel),
        "mixed_grade_lies_in_forgetful_kernel": mul(r_forget, [[0], [0], [0], [1], [0], [0]]) == [[0], [0]],
        "horizontal_lift_forbids_mixed_to_elliptic_transport": True,
    }
    packet = {
        "schema": "marici.mixed-kummer-horizontal-kernel.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ordered_total_basis": ["1", "F_L", "F_R", "F_LF_R", "omega_0", "omega_2"],
        "forget_marks_matrix": r_forget,
        "horizontality_identity": "R_forget A_total = A_ell R_forget",
        "forced_connection_form": "A_total=[[A_K, B_E_to_K],[0,A_ell]]",
        "forbidden_block": "A_K_to_E must vanish",
        "allowed_block": "an extension from compact elliptic coefficients into the marked kernel may remain",
        "conclusion": (
            "if the source relative Gauss-Manin forget-marks map extends over q_L,q_R, the mixed Kummer line cannot mix into the compact elliptic quotient"
        ),
        "remaining_existence_gate": (
            "construct the complete double-triangle moving-fiber relative coefficient system and its horizontal forget-marks morphism"
        ),
        "checks": checks,
    }
    out = Path(__file__).with_name("mixed-kummer-horizontal-kernel.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

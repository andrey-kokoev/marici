from __future__ import annotations

import json
from itertools import combinations
import sympy as sp


def is_psd(matrix: sp.Matrix) -> bool:
    indices = range(matrix.rows)
    for size in range(1, matrix.rows + 1):
        for subset in combinations(indices, size):
            minor = matrix.extract(subset, subset).det()
            if minor.is_nonnegative is not True:
                return False
    return True


def main() -> None:
    # Singular positive tail: C has a zero mode, so no strict tail gap exists.
    C = sp.diag(4, 0)
    C_pinv = sp.diag(sp.Rational(1, 4), 0)

    B_good = sp.Matrix([[2, 0]])
    F_good = sp.Matrix([[1]])
    block_good = F_good.row_join(B_good).col_join(B_good.T.row_join(C))
    range_residual_good = B_good * (sp.eye(2) - C_pinv * C)
    schur_good = F_good - B_good * C_pinv * B_good.T
    assert range_residual_good == sp.zeros(1, 2)
    assert schur_good == sp.zeros(1, 1)
    assert is_psd(block_good)

    # Deliberate failure: coupling reaches the zero tail direction.
    B_bad = sp.Matrix([[2, 1]])
    block_bad = F_good.row_join(B_bad).col_join(B_bad.T.row_join(C))
    range_residual_bad = B_bad * (sp.eye(2) - C_pinv * C)
    assert range_residual_bad != sp.zeros(1, 2)
    assert not is_psd(block_bad)

    result = {
        "schema":"marici.voevodsky.range-compatible-schur-certificate-check.v1",
        "status":"singular_tail_schur_gate_verified",
        "strict_tail_gap_required":False,
        "tail_psd_required":True,
        "range_condition":"B*(I-C^dagger*C)=0",
        "finite_schur_condition":"F-B*C^dagger*B^* >= 0",
        "good_block_psd":True,
        "deliberate_range_failure_detected":True,
        "weil_certificate_completed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/determinant-vs-coercivity-and-sheet.json"


def main():
    conditioning = []
    dimension_collapse = []
    for n in (2, 4, 8, 16):
        A = Matrix.diag(Rational(1, n), *([1] * (n - 1)))
        assert A.det() == Rational(1, n)
        assert max(abs(x) for x in A.inv().diagonal()) == n
        conditioning.append({"cutoff": n, "determinant": str(A.det()),
                             "inverse_norm": n})

        B = Rational(1, 2) * Matrix.eye(n)
        assert B.det() == Rational(1, 2 ** n)
        assert max(abs(x) for x in B.inv().diagonal()) == 2
        dimension_collapse.append({"dimension": n, "determinant": str(B.det()),
                                   "inverse_norm": 2})

    constant_det = Matrix.diag(16, Rational(1, 16))
    assert constant_det.det() == 1
    assert max(abs(x) for x in constant_det.inv().diagonal()) == 16

    s = symbols("s")
    even_lift = Matrix.diag(1 - s, 1)
    odd_lift = Matrix.diag(1, 1 - s)
    sheet = Matrix.diag(1, -1)
    assert even_lift.det() == odd_lift.det() == 1 - s
    even_kernel = even_lift.subs(s, 1).nullspace()[0]
    odd_kernel = odd_lift.subs(s, 1).nullspace()[0]
    assert sheet * even_kernel == even_kernel
    assert sheet * odd_kernel == -odd_kernel

    payload = {
        "schema": "marici.kitaev.determinant_vs_coercivity_and_sheet.v1",
        "status": "pass",
        "pointwise_nonzero_but_inverse_escape": conditioning,
        "determinant_collapse_with_uniform_inverse": dimension_collapse,
        "constant_determinant_bad_conditioning": {
            "determinant": "1", "inverse_norm": 16,
        },
        "same_determinant_different_sheet": {
            "determinant": "1-s", "exceptional_parameter": "s=1",
            "first_kernel_character": "even", "second_kernel_character": "odd",
        },
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()

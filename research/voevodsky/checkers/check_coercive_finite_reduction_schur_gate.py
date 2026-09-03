from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    a, b, c = sp.symbols("a b c", positive=True, real=True)
    W = sp.Matrix([[a, b], [b, c]])
    assert sp.factor(W.det()) == a * c - b**2
    schur = sp.simplify(a - b**2 / c)
    assert sp.simplify(W.det() - c * schur) == 0

    # Deliberate failure: positive diagonal blocks do not imply the full form is positive.
    bad = sp.Matrix([[1, 2], [2, 1]])
    assert bad[0, 0] > 0 and bad[1, 1] > 0
    assert bad.det() == -3
    assert min(bad.eigenvals().keys()) == -1

    # A norm-bound certificate: a>=b^2/c is exactly the scalar Schur condition.
    good = sp.Matrix([[4, 2], [2, 1]])
    assert good.det() == 0
    assert all(ev >= 0 for ev in good.eigenvals())

    result = {
        "schema":"marici.voevodsky.coercive-finite-reduction-schur-gate-check.v1",
        "status":"schur_gate_verified",
        "high_block_coercivity_alone_sufficient":False,
        "finite_low_block_positivity_alone_sufficient":False,
        "cross_block_control_required":True,
        "sufficient_bound":"A_low >= ||B_cross||^2/c_high",
        "deliberate_failure_determinant":-3,
        "passed":True,
        "rh_implication":False
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    y = sp.symbols("y", real=True)
    n, m = sp.symbols("n m", integer=True, positive=True)

    # p_n(y)=y^n in L2([0,1],dy) converges to zero.
    norm_squared = sp.integrate(y ** (2 * n), (y, 0, 1))
    assert norm_squared == 1 / (2 * n + 1)
    assert sp.limit(norm_squared, n, sp.oo) == 0

    # Endpoint evaluation remains one, while differences have zero evaluation form.
    assert (y**n).subs(y, 1) == 1
    assert (y**n - y**m).subs(y, 1) == 0

    # Outside-support evaluation is even more unstable.
    outside_value_squared = sp.Integer(2) ** (2 * n)
    assert sp.limit(outside_value_squared, n, sp.oo) == sp.oo

    result = {
        "schema":"marici.voevodsky.singular-evaluation-closability-obstruction-check.v1",
        "status":"nonclosability_sequence_verified",
        "sequence":"p_n(y)=y^n",
        "reference_norm_squared":"1/(2n+1)->0",
        "endpoint_evaluation_squared":"1",
        "difference_evaluation_squared":"0",
        "outside_support_growth":"z0^(2n) for z0>1",
        "singular_evaluation_closable":False,
        "prime_form_classified_as_measure":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

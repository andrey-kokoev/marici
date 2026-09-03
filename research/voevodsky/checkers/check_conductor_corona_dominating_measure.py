from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Finite disjoint-support fixture for mutually singular measures.
    bulk_weights = sp.diag(2, 3, 0, 0)
    corona_weights = sp.diag(0, 0, 5, 7)
    dominating = bulk_weights + corona_weights

    x = sp.Matrix(sp.symbols("x0:4", real=True))
    bulk_norm = (x.T * bulk_weights * x)[0]
    corona_norm = (x.T * corona_weights * x)[0]
    total_norm = (x.T * dominating * x)[0]
    assert sp.expand(total_norm - bulk_norm - corona_norm) == 0

    bulk_projection = sp.diag(1, 1, 0, 0)
    corona_projection = sp.diag(0, 0, 1, 1)
    assert bulk_projection * corona_projection == sp.zeros(4)
    assert bulk_projection + corona_projection == sp.eye(4)

    # A multiplication form has no cross block on disjoint supports.
    multiplier = sp.diag(*sp.symbols("m0:4", real=True))
    cross = bulk_projection * multiplier * corona_projection
    assert cross == sp.zeros(4)

    result = {
        "schema":"marici.voevodsky.conductor-corona-dominating-measure-check.v1",
        "status":"singular_measure_direct_sum_verified",
        "carrier":"L2(mu_additive+mu_multiplicative)",
        "decomposition":"L2(mu_additive) direct_sum L2(mu_multiplicative)",
        "multiplication_cross_block":0,
        "nonlocal_cross_block_source_derived":False,
        "completed_form_extended":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

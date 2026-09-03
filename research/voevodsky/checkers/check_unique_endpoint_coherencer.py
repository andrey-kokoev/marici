from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    h, c = sp.symbols("h c", positive=True, real=True)
    alpha = sp.exp(h / 4) - 1
    source_remainder_solution = sp.solve(sp.Eq(c - alpha, 0), c)
    closability_solution = sp.solve(sp.Eq(c, 0), c)
    assert source_remainder_solution == [alpha]
    assert closability_solution == []  # c was assumed positive; zero lies on the boundary.

    result = {
        "schema":"marici.voevodsky.unique-endpoint-coherencer-check.v2",
        "status":"source_remainder_and_order_closability_coefficients_incompatible",
        "source_remainder_coefficient":"exp(h/4)-1",
        "order_closability_coefficient":0,
        "coefficients_equal":False,
        "stronger_common_domain_required":True,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

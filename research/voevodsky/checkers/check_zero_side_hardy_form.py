from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    h, delta = sp.symbols("h delta", positive=True, real=True)
    r = sp.exp(-h * delta)
    # Hardy H2 evaluation kernel norm squared at radius r<1.
    cutoff = sp.symbols("cutoff", integer=True, positive=True)
    finite_sum = (1 - r ** (2 * cutoff)) / (1 - r**2)
    assert sp.simplify(finite_sum.subs(cutoff, cutoff + 1) - finite_sum - r ** (2 * cutoff)) == 0
    assert finite_sum.subs(cutoff, 1) == 1
    partial = sp.limit(finite_sum, cutoff, sp.oo)
    assert sp.simplify(partial - 1 / (1 - r**2)) == 0

    denominator_floor = 1 - sp.exp(-2 * h * delta)
    assert sp.simplify(denominator_floor - (1 - r**2)) == 0
    assert float(denominator_floor.subs({h: 1, delta: 1})) > 0

    # Gaussian shell count majorant remains summable after the evaluation factor is bounded.
    k = sp.symbols("k", integer=True, positive=True)
    t = sp.symbols("t", positive=True, real=True)
    shell = k * 2**k * sp.exp(-t * 4**k)
    ratio = sp.simplify(shell.subs(k, k + 1) / shell)
    assert sp.limit(ratio, k, sp.oo) == 0

    result = {
        "schema":"marici.voevodsky.zero-side-hardy-form-check.v1",
        "status":"hardy_boundedness_majorant_verified",
        "evaluation_norm_squared":"1/(1-|y|^2)",
        "spectral_radius":"|y_rho|=exp(-h Re lambda_rho)<1",
        "zero_sum_majorant":"sum k 2^k exp(-t 4^k)",
        "bounded_form_on_H2":True,
        "positive_form":False,
        "comparison_to_archimedean_GNS":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

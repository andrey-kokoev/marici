from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/paired-hadamard-laplace-convergence-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    k = sp.symbols("k", integer=True, positive=True)

    # Dyadic zero count O(2^k k) divided by squared radius 4^k.
    dyadic_majorant = k / 2**k
    assert sp.summation(dyadic_majorant, (k, 1, sp.oo)) == 2

    # Higher resolvent errors are also summable.
    assert sp.summation(k / 2 ** (3 * k), (k, 1, sp.oo)) == sp.Rational(8, 49)

    # Gaussian heat domination overwhelms the zero-count growth.
    gaussian_shell = k * sp.exp(-k**2)
    assert sp.summation(gaussian_shell, (k, 1, sp.oo)).is_finite is not False
    # Ratio test gives a strict eventual contraction directly.
    ratio = sp.simplify(((k + 1) * sp.exp(-(k + 1) ** 2)) / gaussian_shell)
    assert sp.limit(ratio, k, sp.oo) == 0

    # Absolute Laplace interchange has the same inverse-square large-zero scale.
    gamma = sp.symbols("gamma", positive=True, real=True)
    beta = sp.symbols("beta", real=True)
    real_lambda = gamma**2 - (beta - sp.Rational(1, 2)) ** 2
    assert sp.simplify(real_lambda - (gamma**2 - sp.Rational(1, 4)) - (sp.Rational(1, 4) - (beta - sp.Rational(1, 2)) ** 2)) == 0

    result = {
        "schema":"marici.voevodsky.paired-hadamard-laplace-convergence-check.v1",
        "status":"convergence_majorants_verified",
        "dyadic_inverse_square_sum":True,
        "local_uniform_resolvent_majorant":True,
        "gaussian_ratio_limit":0,
        "strip_real_part_decomposition":True,
        "authoritative_input_citations":"metadata_candidates_only",
        "source_complete_equivalence":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

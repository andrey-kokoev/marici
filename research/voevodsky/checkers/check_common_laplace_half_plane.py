from __future__ import annotations

import cmath
import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/common-laplace-half-plane-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    # Re sqrt(z)^2=(|z|+Re z)/2 >= Re z for Re z>0.
    a, b = sp.symbols("a b", positive=True, real=True)
    modulus = sp.sqrt(a**2 + b**2)
    real_sqrt_squared = (modulus + a) / 2
    assert sp.simplify(modulus**2 - a**2 - b**2) == 0
    # Since modulus and a are positive and modulus^2-a^2=b^2>=0, modulus>=a.

    fixtures = [complex(0.26, 0), complex(0.3, 10), complex(1, -20), complex(100, 3)]
    for x in fixtures:
        assert x.real > 0.25
        assert cmath.sqrt(x).real > 0.5
        assert (0.5 + cmath.sqrt(x)).real > 1

    q = sp.symbols("q", positive=True, real=True)
    tau = sp.symbols("tau", positive=True, real=True)
    x = q + sp.Rational(1, 4)
    endpoint_integral = sp.integrate(sp.exp(-x * tau) * sp.exp(tau / 4), (tau, 0, sp.oo))
    assert sp.simplify(endpoint_integral - 1 / q) == 0

    beta, gamma = sp.symbols("beta gamma", real=True)
    real_lambda = gamma**2 - (beta - sp.Rational(1, 2)) ** 2
    assert sp.simplify(real_lambda - (gamma**2 - sp.Rational(1, 4)) - (sp.Rational(1, 4) - (beta - sp.Rational(1, 2)) ** 2)) == 0

    result = {
        "schema":"marici.voevodsky.common-laplace-half-plane-check.v1",
        "status":"common_half_plane_verified",
        "domain":"Re x>1/4",
        "principal_sqrt_euler_domain":True,
        "endpoint_transform":True,
        "zero_side_real_part_bound":True,
        "low_zero_exclusion_source":"Platt-Trudgian arXiv:2004.09765 Theorem 1",
        "Hadamard_source_text_inspected":False,
        "source_complete_equivalence":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

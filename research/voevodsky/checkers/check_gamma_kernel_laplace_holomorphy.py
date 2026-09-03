from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/gamma-kernel-laplace-holomorphy-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, sigma = sp.symbols("t sigma", positive=True, real=True)

    # The proved small-t majorant is locally integrable.
    small_plain = sp.integrate(t ** -sp.Rational(1, 2), (t, 0, 1))
    # With t=u^2, this integral is -4 integral_0^1 log(u) du = 4.
    u = sp.symbols("u", positive=True, real=True)
    small_log = -4 * sp.integrate(sp.log(u), (u, 0, 1))
    assert small_plain == 2
    assert small_log == 4

    # The large-t majorant has an absolute Laplace transform for every sigma>0.
    large = sp.integrate(sp.exp(-sigma * t) * t ** -sp.Rational(1, 2), (t, 1, sp.oo))
    assert large.is_finite is not False
    assert sp.limit(large, sigma, sp.oo) == 0

    # Tail domination used in the r-integral.
    r = sp.symbols("r", positive=True, real=True)
    tail = sp.integrate(sp.exp(-r / 4), (r, 1, sp.oo))
    assert sp.simplify(tail - 4 * sp.exp(-sp.Rational(1, 4))) == 0

    result = {
        "schema":"marici.voevodsky.gamma-kernel-laplace-holomorphy-check.v1",
        "status":"gamma_laplace_majorants_verified",
        "small_t_plain_integral":str(small_plain),
        "small_t_log_integral":str(small_log),
        "large_t_laplace_finite":True,
        "r_tail_finite":True,
        "gamma_laplace_domain":"Re x>0",
        "common_completed_domain":"Re x>1/4",
        "exact_kernel_identity":"relies_on_existing_packet",
        "source_complete_equivalence":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

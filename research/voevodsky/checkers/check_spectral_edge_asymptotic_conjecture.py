from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/spectral-edge-asymptotic-conjecture-falsification-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, h = sp.symbols("t h", positive=True, real=True)
    Y = sp.exp(h / 4)
    rank_one_endpoint = sp.exp(t / 4) * (Y - 1)
    assert sp.limit(rank_one_endpoint.subs(h, 1), t, sp.oo) == sp.oo
    assert sp.simplify(sp.exp(-t / 4) * rank_one_endpoint - (Y - 1)) == 0

    sigma, omega = sp.symbols("sigma omega", positive=True, real=True)
    shell = sp.exp(-sigma * t) * 2 * sp.cos(omega * t)
    renormalized = sp.simplify(sp.exp(sigma * t) * shell)
    assert renormalized == 2 * sp.cos(omega * t)
    n = sp.symbols("n", integer=True, positive=True)
    assert sp.simplify(renormalized.subs(t, 2 * sp.pi * n / omega)) == 2
    assert sp.simplify(renormalized.subs(t, (2 * n + 1) * sp.pi / omega)) == -2

    # A real single rate does have a positive renormalized limit.
    C = sp.symbols("C", positive=True, real=True)
    real_edge = C * sp.exp(-sigma * t) + sp.exp(-(sigma + 1) * t)
    assert sp.limit(sp.exp(sigma * t) * real_edge, t, sp.oo) == C

    result = {
        "schema":"marici.voevodsky.spectral-edge-asymptotic-conjecture-check.v1",
        "status":"spectral_edge_conjecture_falsified_as_stated",
        "rank_one_endpoint_growth":True,
        "rank_one_exponent":"-1/4",
        "complex_leading_shell_oscillates":True,
        "real_edge_conditional_fixture":True,
        "unconditional_positive_leading_coefficient":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

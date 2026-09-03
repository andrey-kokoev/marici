from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/entire-kernel-observer-nerve-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, z, xi, a = sp.symbols("t z xi a", positive=True, real=True)

    # Even two-atom kernel fixture.
    K = sp.exp(-t * a**2) * sp.cos(a * z)
    assert sp.simplify(sp.diff(K, t) - sp.diff(K, z, 2)) == 0
    assert sp.simplify(K.subs(z, -z) - K) == 0

    jets = [
        sp.simplify((-1) ** k * sp.diff(K, t, k).subs(z, 0))
        for k in range(6)
    ]
    assert jets == [sp.exp(-t * a**2) * a ** (2 * k) for k in range(6)]

    taylor_10 = sum(
        (-1) ** k * jets[k] * z ** (2 * k) / sp.factorial(2 * k)
        for k in range(6)
    )
    assert sp.series(K - taylor_10, z, 0, 12).removeO() == 0
    assert sp.simplify(sp.diff(K - taylor_10, z, 12).subs(z, 0)) != 0

    Theta = sp.exp(-t * xi**2) * K.subs(z, -2 * sp.I * t * xi)
    direct_theta = sp.exp(-t * (a - xi) ** 2) / 2 + sp.exp(-t * (-a - xi) ** 2) / 2
    assert sp.simplify(sp.expand_complex(Theta) - direct_theta) == 0

    # Real packet values are evaluations of the same K.
    labels = [sp.Integer(0), sp.Integer(1), sp.Integer(3)]
    gram = sp.Matrix([[K.subs(z, x - y) for y in labels] for x in labels])
    assert gram == gram.T
    assert all(sp.simplify(gram[i, i] - K.subs(z, 0)) == 0 for i in range(3))

    status = contract["status"]
    assert status["global_positivity"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.entire-kernel-observer-nerve-check.v1",
        "status":"three_chart_transition_fixture_verified",
        "heat_equation":True,
        "evenness":True,
        "jet_orders_checked":6,
        "taylor_residual_first_uncontrolled_order":12,
        "shifted_gaussian_pullback":True,
        "gram_packet_restriction":True,
        "global_positivity":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

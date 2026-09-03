from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/generic-mesh-pole-rigidity-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    z = sp.symbols("z")
    h = sp.symbols("h", positive=True, real=True)

    lambdas = [sp.Rational(2), sp.Rational(3) + sp.I, sp.Rational(3) - sp.I]
    weights = [sp.Rational(5), sp.Rational(7), sp.Rational(7)]
    ys = [sp.exp(-h * lam) for lam in lambdas]
    transform = sum(weight / (1 - y * z) for weight, y in zip(weights, ys))

    # At a generic exact mesh, the nonreal conjugate poles remain distinct and exposed.
    h_generic = sp.Rational(1, 3)
    ys_generic = [sp.N(y.subs(h, h_generic), 40) for y in ys]
    assert len({str(value) for value in ys_generic}) == 3
    assert abs(sp.im(ys_generic[1])) > sp.Float("0.1")
    assert sp.simplify(weights[1] * (1 - ys[1])) != 0
    assert sp.simplify(weights[2] * (1 - ys[2])) != 0

    # A single mesh can alias a nonreal phase to a real sampled base.
    b = sp.symbols("b", positive=True, real=True)
    aliased = sp.exp(-sp.I * b * h).subs({b: sp.pi, h: 1})
    assert sp.simplify(aliased + 1) == 0

    # Arbitrarily small meshes remove that alias for fixed nonzero imaginary part.
    for denominator in (10, 100, 1000):
        value = sp.exp(-sp.I * sp.Rational(1, denominator))
        assert sp.simplify(sp.im(value)) != 0

    # The finite generating series equals its pole decomposition exactly.
    moments = [sum(weight * y**n for weight, y in zip(weights, ys)) for n in range(5)]
    series = sp.series(transform, z, 0, 5).removeO()
    assert sp.simplify(series - sum(moments[n] * z**n for n in range(5))) == 0

    result = {
        "schema":"marici.voevodsky.generic-mesh-pole-rigidity-check.v1",
        "status":"finite_generic_mesh_pole_rigidity_verified",
        "distinct_generic_poles":True,
        "nonreal_conjugate_poles_exposed":True,
        "single_mesh_phase_alias_exhibited":True,
        "small_mesh_alias_removed":True,
        "generating_series_orders_checked":5,
        "infinite_source_meromorphic_comparison":False,
        "common_continuation_domain":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

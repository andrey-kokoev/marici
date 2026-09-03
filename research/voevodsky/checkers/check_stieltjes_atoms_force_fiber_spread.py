from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/stieltjes-atoms-force-fiber-spread-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    x, lam, t = sp.symbols("x lam t", positive=True)
    laplace_atom = sp.integrate(lam * t * sp.exp(-(x + lam) * t), (t, 0, sp.oo))
    assert sp.simplify(laplace_atom - lam / (x + lam) ** 2) == 0

    y = sp.symbols("y", real=True)
    beta_density = 6 * y * (1 - y)
    mean = sp.integrate(y * beta_density, (y, 0, 1))
    variance = sp.integrate((y - mean) ** 2 * beta_density, (y, 0, 1))
    assert mean == sp.Rational(1, 2)
    assert variance == sp.Rational(1, 20)

    centered = y - sp.Rational(1, 2)
    moments = [sp.integrate(centered ** (2 * k) * beta_density, (y, 0, 1)) for k in range(10)]
    # Every even monomial in the cosh tilt has nonnegative covariance with centered square.
    covariances = [sp.simplify(moments[k + 1] - moments[1] * moments[k]) for k in range(9)]
    assert all(value >= 0 for value in covariances)
    assert all(value > 0 for value in covariances[1:])

    # Without exchange pairing, the exponential tilt is not midpoint-even.
    delta = sp.symbols("delta", nonzero=True, real=True)
    unpaired = y * (1 - y) * sp.exp(-delta * y)
    assert sp.simplify(unpaired.subs(y, 1 - y) - unpaired) != 0
    paired = y * (1 - y) * sp.cosh(delta * centered)
    assert sp.simplify(paired.subs(y, 1 - y) - paired) == 0

    status = contract["status"]
    assert status["independent_spread_assumption"] == "eliminated"
    assert status["source_derived_stieltjes_measure"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.stieltjes-atoms-force-fiber-spread-check.v1",
        "status":"stieltjes_to_spread_reduction_verified",
        "stieltjes_to_gamma2_atom":True,
        "equal_rate_beta22_mean":str(mean),
        "equal_rate_beta22_variance":str(variance),
        "cosh_tilt_even":True,
        "cosh_tilt_spread_covariances_checked":len(covariances),
        "exchange_pairing_required_for_midpoint_symmetry":True,
        "independent_spread_gate_eliminated":True,
        "source_stieltjes_measure_supplied":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

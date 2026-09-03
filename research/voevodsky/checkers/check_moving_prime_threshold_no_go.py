from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/moving-prime-threshold-no-go-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t, L = sp.symbols("t L", positive=True, real=True)
    atom = t ** sp.Rational(-1, 2) * sp.exp(-L**2 / (4 * t))
    derivative = sp.simplify(sp.diff(atom, t))
    expected = atom * (L**2 - 2 * t) / (4 * t**2)
    assert sp.simplify(derivative - expected) == 0

    first_threshold = sp.log(2) ** 2 / 2
    first_numeric = sp.N(first_threshold, 40)
    assert first_numeric > sp.Float("0.2402", 40)
    assert first_numeric < sp.Float("0.2403", 40)

    # The current sample region lies below every prime-power threshold n>=2.
    tmax = sp.Rational(2, 25)
    for n in range(2, 17):
        threshold = sp.log(n) ** 2 / 2
        assert sp.N(threshold - tmax, 50) > 0

    # Each channel changes sign across its exact threshold.
    for n in (2, 3, 4, 5, 8, 16):
        threshold = sp.log(n) ** 2 / 2
        below = expected.subs({L: sp.log(n), t: threshold / 2})
        above = expected.subs({L: sp.log(n), t: threshold * 2})
        assert sp.N(below, 50) > 0
        assert sp.N(above, 50) < 0

    result = {
        "schema":"marici.voevodsky.moving-prime-threshold-no-go-check.v1",
        "status":"prime_derivative_threshold_no_go_verified",
        "derivative_identity":True,
        "first_threshold":str(first_numeric),
        "small_box_positive_n_range":"2..16",
        "sign_change_fixtures":6,
        "exact_source_normalization_attached":False,
        "global_termwise_prime_factor_falsified":"conditional_on_source_atom",
        "collective_source_factor_falsified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

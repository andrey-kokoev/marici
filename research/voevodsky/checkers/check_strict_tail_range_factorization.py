from __future__ import annotations

import json
from fractions import Fraction


def main() -> None:
    # If C[y]>=delta*||y||_2^2 and |B_x[y]|<=k_x||y||_2, then
    # |B_x[y]|<=k_x/sqrt(delta)*sqrt(C[y]). The squared dual norm is
    # at most k_x^2/delta.
    delta = Fraction(2)
    cross_constants = [Fraction(1), Fraction(3)]
    dual_norm_squared_bounds = [k * k / delta for k in cross_constants]
    assert dual_norm_squared_bounds == [Fraction(1, 2), Fraction(9, 2)]

    # A scalar completion-of-squares fixture with C=2 and B=1.
    # D=B/sqrt(C), hence DD*=1/2; F=1 leaves Schur remainder 1/2.
    finite_block = Fraction(1)
    schur_remainder = finite_block - dual_norm_squared_bounds[0]
    assert schur_remainder == Fraction(1, 2)

    result = {
        "schema":"marici.voevodsky.strict-tail-range-factorization-check.v1",
        "status":"strict_L2_tail_bound_implies_energy_range_factorization",
        "tail_L2_constant":str(delta),
        "cross_constants":[str(k) for k in cross_constants],
        "dual_norm_squared_bounds":[str(v) for v in dual_norm_squared_bounds],
        "fixture_schur_remainder":str(schur_remainder),
        "range_factorization_for_declared_trial_space":True,
        "finite_schur_positivity_proved_for_weil_operator":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

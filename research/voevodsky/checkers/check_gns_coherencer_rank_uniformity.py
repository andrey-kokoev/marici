from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # A finite generalized eigenvalue fixture: relative form bounds are ordinary
    # operator bounds after conjugation by G^{-1/2}.
    G = sp.diag(1, 4)
    P = sp.Matrix([[sp.Rational(1, 2), 1], [1, 2]])
    G_half_inverse = sp.diag(1, sp.Rational(1, 2))
    T = sp.simplify(G_half_inverse * P * G_half_inverse)
    assert T == sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
    assert set(T.eigenvals().keys()) == {0, 1}
    assert sp.simplify(G + P) == sp.simplify(sp.diag(1, 2) * (sp.eye(2) + T) * sp.diag(1, 2))

    # Deliberate failure: every finite truncation may be bounded, without one
    # rank-uniform operator bound.
    N = sp.symbols("N", integer=True, positive=True)
    finite_norm = N
    assert sp.limit(finite_norm, N, sp.oo) == sp.oo

    result = {
        "schema":"marici.voevodsky.gns-coherencer-rank-uniformity-check.v1",
        "status":"relative_operator_reduction_verified",
        "finite_relative_operator_spectrum":["0","1"],
        "bounded_operator_sufficient_condition":"sup_N ||G_N^(-1/2) P_N G_N^(-1/2)|| < infinity",
        "general_condition":"closable symmetric form with uniform lower bound -1",
        "positivity_condition":"inf spectrum(I+T)>=0",
        "finite_bounds_imply_uniform_bound":False,
        "prime_operator_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

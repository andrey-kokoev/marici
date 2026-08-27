import json
import sympy as sp


def cayley(unitary):
    identity = sp.eye(unitary.rows)
    raw = sp.I * (identity + unitary) * (identity - unitary).inv()
    return raw.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))


def main():
    root3 = sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
    root4 = (1 + sp.I) / sp.sqrt(2)
    phases = [root3, root4]
    swap = sp.Matrix([[0, 1], [1, 0]])
    omega = sp.Matrix([1, 1]) / sp.sqrt(2)
    unitaries = [sp.diag(a, sp.conjugate(a)) for a in phases]
    generators = [cayley(u) for u in unitaries]

    checks = {
        "cyclic_state_is_reciprocal_invariant": swap * omega == omega,
        "both_phases_are_unitary": all(sp.simplify(u.conjugate().T * u) == sp.eye(2) for u in unitaries),
        "both_obey_reciprocal_sewing": all(
            sp.simplify(swap * u * swap - u.conjugate().T) == sp.zeros(2) for u in unitaries
        ),
        "both_cayley_generators_are_self_adjoint": all(
            (a - a.conjugate().T).applyfunc(sp.simplify) == sp.zeros(2) for a in generators
        ),
        "sewn_boundary_generators_are_distinct": generators[0] != generators[1],
    }
    result = {
        "schema": "marici.grothendieck.reciprocal-sewing-cayley-phase-family.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "generators": [
            [[str(sp.simplify(x)) for x in matrix.row(i)] for i in range(2)]
            for matrix in generators
        ],
        "interpretation": (
            "Reciprocal covariance, a common maximal abelian algebra, and an invariant cyclic state "
            "leave a continuous conjugate-phase family. Modular sewing alone does not select the Cayley boundary phase."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

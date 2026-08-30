import json
import sympy as sp


def main():
    # A finite spectral chart for a maximal abelian boundary algebra.
    # The cyclic vector has nonzero support on every atom.
    omega = sp.Matrix([1, 1]) / sp.sqrt(2)
    U1 = sp.diag(sp.I, -1)
    U2 = sp.diag(-sp.I, -1)
    probe = sp.diag(2, 3)
    identity = sp.eye(2)

    A1 = sp.simplify(sp.I * (identity + U1) * (identity - U1).inv())
    A2 = sp.simplify(sp.I * (identity + U2) * (identity - U2).inv())

    checks = {
        "same_maximal_abelian_algebra": sp.simplify(U1 * probe - probe * U1) == sp.zeros(2)
        and sp.simplify(U2 * probe - probe * U2) == sp.zeros(2),
        "same_cyclic_vector": all(entry != 0 for entry in omega),
        "both_cayley_generators_self_adjoint": A1 == A1.conjugate().T and A2 == A2.conjugate().T,
        "boundary_generators_are_distinct": A1 != A2,
        "spectral_readouts_are_distinct": A1.charpoly().as_expr() != A2.charpoly().as_expr(),
    }

    result = {
        "schema": "marici.grothendieck.weyl-masa-cayley-phase-no-go.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "A1": [[str(x) for x in A1.row(i)] for i in range(2)],
        "A2": [[str(x) for x in A2.row(i)] for i in range(2)],
        "interpretation": (
            "A maximal commuting boundary algebra and a common cyclic vector do not select a unique "
            "Cayley phase or self-adjoint boundary generator. A further source-derived phase selector is required."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

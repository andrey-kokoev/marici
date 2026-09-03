"""A q-dependent positive transport metric exists for every invertible flow."""
import json
import sympy as sp


def main():
    u11, u12, u21, u22 = sp.symbols("u11 u12 u21 u22", real=True)
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22", real=True)
    U = sp.Matrix([[u11, u12], [u21, u22]])
    A = sp.Matrix([[a11, a12], [a21, a22]])
    H = sp.simplify(U.inv().T * U.inv())
    # If U'=AU, then (U^-1)'=-U^-1 A.
    Hdot = sp.simplify(-A.T * H - H * A)
    conservation = sp.simplify(Hdot + A.T * H + H * A)
    detU = sp.factor(U.det())
    first_minor = sp.factor(H[0, 0])
    determinant = sp.factor(H.det())
    checks = {
        "lyapunov_transport_identity": conservation == sp.zeros(2),
        "first_minor_is_sum_of_squares_over_det_squared": sp.simplify(first_minor - (u21**2 + u22**2) / detU**2) == 0,
        "determinant_is_inverse_square": sp.simplify(determinant - 1 / detU**2) == 0,
    }
    result = {
        "schema": "marici.grothendieck.transport-metric-tautology.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "metric": [[str(sp.factor(x)) for x in H.row(i)] for i in range(2)],
        "first_principal_minor": str(first_minor),
        "determinant": str(determinant),
        "disposition": "Every invertible real two-dimensional flow admits this positive q-dependent conserved metric. Existence alone cannot distinguish theta from hostile sources or exclude off-seam zeros.",
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

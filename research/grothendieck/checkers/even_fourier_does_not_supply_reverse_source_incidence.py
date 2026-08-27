import json
import sympy as sp


def main():
    f = sp.symbols("f", real=True, nonzero=True)
    fourier_even = sp.Matrix(
        [[sp.sqrt(3) / 3, sp.sqrt(6) / 3], [sp.sqrt(6) / 3, -sp.sqrt(3) / 3]]
    )
    forward = sp.Matrix([[0, f], [0, 0]])
    residual = sp.simplify(fourier_even * forward * fourier_even - forward.conjugate().T)
    expected = f * sp.Matrix([[sp.sqrt(2), -1], [-1, -sp.sqrt(2)]]) / 3
    checks = {
        "even_fourier_is_self_adjoint_involution": fourier_even == fourier_even.conjugate().T
        and sp.simplify(fourier_even**2) == sp.eye(2),
        "conjugation_residual_is_exact": sp.simplify(residual - expected) == sp.zeros(2),
        "residual_has_full_rank": residual.rank() == 2,
        "fourier_does_not_produce_adjoint_incidence": residual != sp.zeros(2),
    }
    result = {
        "schema": "marici.grothendieck.even-fourier-reverse-incidence-no-go.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "residual": [[str(x) for x in residual.row(i)] for i in range(2)],
        "interpretation": (
            "The normalized even Fourier involution selects Lagrangian boundary geometry but does not "
            "conjugate the one-way theta forcing into its adjoint. Reverse incidence is an independent constructor."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

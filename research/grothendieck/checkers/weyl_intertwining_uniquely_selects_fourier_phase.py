import json
import sympy as sp


def main():
    root = sp.exp(2 * sp.pi * sp.I / 3)
    clock = sp.diag(1, root, root**2)
    shift = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    fourier = sp.Matrix(3, 3, lambda j, k: root ** (j * k)) / sp.sqrt(3)

    variables = sp.symbols("s0:9")
    selector = sp.Matrix(3, 3, variables)
    residuals = list(selector * shift - clock * selector)
    residuals += list(selector * clock - shift.inv() * selector)
    coefficient_matrix, _ = sp.linear_eq_to_matrix(residuals, variables)
    intertwiner_basis = coefficient_matrix.nullspace()

    position_vacuum = sp.Matrix([1, 0, 0])
    momentum_vacuum = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    checks = {
        "fourier_exchanges_shift_for_clock": sp.simplify(fourier * shift - clock * fourier) == sp.zeros(3),
        "fourier_exchanges_clock_for_inverse_shift": sp.simplify(
            fourier * clock - shift.inv() * fourier
        ) == sp.zeros(3),
        "intertwiner_space_is_one_dimensional": len(intertwiner_basis) == 1,
        "source_vacuum_normalization_is_exact": fourier * position_vacuum == momentum_vacuum,
    }
    result = {
        "schema": "marici.grothendieck.weyl-intertwining-fourier-phase-rigidity.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "intertwiner_dimension": len(intertwiner_basis),
        "interpretation": (
            "The operator exchanging the two irreducible Weyl polarizations is unique up to scalar. "
            "The source vacuum normalization fixes the scalar and selects the Fourier phase."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

import json
import sympy as sp


def clean(matrix):
    return matrix.applyfunc(lambda x: sp.simplify(sp.expand_complex(x)))


def main():
    root = sp.exp(2 * sp.pi * sp.I / 3)
    fourier = sp.Matrix(3, 3, lambda j, k: root ** (j * k)) / sp.sqrt(3)
    reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    even_basis = sp.Matrix.hstack(
        sp.Matrix([1, 0, 0]),
        sp.Matrix([0, 1, 1]) / sp.sqrt(2),
    )
    odd_basis = sp.Matrix([0, 1, -1]) / sp.sqrt(2)
    even_fourier = clean(even_basis.conjugate().T * fourier * even_basis)
    odd_fourier = clean(odd_basis.conjugate().T * fourier * odd_basis)
    full_defect = clean(fourier - fourier.conjugate().T)
    even_defect = clean(even_fourier - even_fourier.conjugate().T)

    checks = {
        "fourier_square_is_reflection": clean(fourier**2 - reflection) == sp.zeros(3),
        "full_fourier_graph_is_not_isotropic": full_defect != sp.zeros(3),
        "even_sector_is_fourier_invariant": clean(fourier * even_basis - even_basis * even_fourier) == sp.zeros(3, 2),
        "even_fourier_is_self_adjoint": even_defect == sp.zeros(2),
        "even_fourier_is_involutive": clean(even_fourier**2) == sp.eye(2),
        "even_graph_is_maximal_isotropic": even_defect == sp.zeros(2) and even_basis.cols == 2,
        "odd_sector_retains_quarter_turn": clean(odd_fourier**2) == -sp.eye(1),
    }
    result = {
        "schema": "marici.grothendieck.even-fourier-graph-lagrangian.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "even_fourier": [[str(x) for x in even_fourier.row(i)] for i in range(2)],
        "odd_fourier": [[str(x) for x in odd_fourier.row(i)] for i in range(1)],
        "interpretation": (
            "The full Fourier graph is not isotropic for the standard Green form. "
            "Reflection-even completion turns Fourier into a self-adjoint involution, making its graph Lagrangian; "
            "the odd sector carries the quarter-turn obstruction."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

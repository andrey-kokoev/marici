import json
from pathlib import Path

import sympy as sp
import itertools


def main():
    nu, x = sp.symbols("nu x")
    r0, r1, r2, l0, l1, l2 = sp.symbols(
        "r0 r1 r2 l0 l1 l2"
    )

    # Finite spectral atoms provide an exact algebraic oracle for the kernel.
    right = [(r0, 5), (r1, 7), (r2, 11)]
    left = [(l0, 5), (l1, 7), (l2, 11)]
    dispersive = nu**2 * sum(
        r / (a**2 * (a - nu)) + l / (a**2 * (a + nu))
        for (r, a), (l, _) in zip(right, left)
    )
    series = sp.series(dispersive, nu, 0, 6).removeO().expand()

    gates = {}
    for degree in range(2, 6):
        expected = sum(
            (r + (-1) ** degree * l) / a ** (degree + 1)
            for (r, a), (l, _) in zip(right, left)
        )
        gates[f"moment_character_degree_{degree}"] = (
            sp.simplify(series.coeff(nu, degree) - expected) == 0
        )

    X = sp.Matrix([[0, 1], [1, 0]])
    a, b = sp.symbols("a b")
    p0 = sp.Matrix([a, a])
    p1 = sp.Matrix([b, -b])
    gates["constant_subtraction_is_crossing_even"] = X * p0 == p0
    gates["linear_subtraction_is_crossing_odd"] = X * p1 == -p1

    # Solve the generic degree-one crossing equation and verify dimension two.
    c0, c1, d0, d1 = sp.symbols("c0 c1 d0 d1")
    vector = sp.Matrix([c0 + c1 * x, d0 + d1 * x])
    crossed = X * vector.subs(x, -x)
    equations = sp.Poly(vector - crossed, x).coeffs()
    solution = sp.linsolve(equations, (c0, c1, d0, d1))
    gates["subtraction_space_has_two_parameters"] = solution == {
        (d0, -d1, d0, d1)
    }

    words = list(itertools.product((-1, 1), repeat=4))
    index = {word: i for i, word in enumerate(words)}
    crossing = sp.zeros(16)
    for word in words:
        crossed_word = (word[2], word[1], word[0], word[3])
        crossing[index[crossed_word], index[word]] = 1
    gates["full_crossing_is_involutive"] = crossing * crossing == sp.eye(16)
    gates["full_crossing_plus_eigenspace_has_rank_twelve"] = (
        16 - (crossing - sp.eye(16)).rank() == 12
    )
    gates["full_crossing_minus_eigenspace_has_rank_four"] = (
        16 - (crossing + sp.eye(16)).rank() == 4
    )
    gates["phi1_crosses_to_declared_partner"] = (
        crossing[index[(1, -1, -1, 1)], index[(-1, -1, 1, 1)]] == 1
    )

    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()), gates

    result = {
        "schema": "marici.qed-vector-dispersion-conventions.v1",
        "gates": gates,
        "crossing_coordinate": "nu=s+T/2",
        "threshold": "nu0=4+T/2",
        "subtraction_basis": ["(1,1)", "nu*(1,-1)"],
        "full_crossing_eigenspace_dimensions": {"even": 12, "odd": 4},
        "conclusion": (
            "The coupled kernel reproduces the certified plus/minus moment "
            "characters, and crossing leaves exactly two subtraction directions."
        ),
    }
    out = Path(__file__).parents[1] / "results" / "qed-vector-dispersion-conventions.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

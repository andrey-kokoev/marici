import json
import sympy as sp


def main():
    omega = sp.exp(2 * sp.pi * sp.I / 3)
    clock = sp.diag(1, omega, omega**2)
    shift = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    symbols = sp.symbols("x0:9")
    x = sp.Matrix(3, 3, symbols)
    equations = list(x * clock - clock * x) + list(x * shift - shift * x)
    solution = sp.linsolve(equations, symbols)
    expected = {(symbols[8], 0, 0, 0, symbols[8], 0, 0, 0, symbols[8])}
    vacuum = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    checks = {
        "clock_shift_obey_weyl_relation": sp.simplify(clock * shift - omega * shift * clock) == sp.zeros(3),
        "joint_commutant_is_scalar": solution == expected,
        "normalized_vacuum_removes_scalar_ambiguity": sp.solve(
            sp.Eq(symbols[8] * vacuum[0], vacuum[0]), symbols[8]
        ) == [1],
    }
    result = {
        "schema": "marici.grothendieck.full-weyl-schur-phase-rigidity.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "joint_commutant": str(solution),
        "interpretation": (
            "Compatibility with both noncommuting Weyl polarizations reduces phase ambiguity to a scalar; "
            "fixing the normalized theta state removes that scalar."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

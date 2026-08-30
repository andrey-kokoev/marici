import json
import sympy as sp


def main():
    u0, u1, u2 = sp.symbols("u0 u1 u2")
    w0, w1, w2 = sp.symbols("w0 w1 w2", nonzero=True)
    unitary = sp.diag(u0, u1, u2)
    omega = sp.Matrix([w0, w1, w2])
    residual = sp.expand(unitary * omega - omega)
    solved = [sp.solve(sp.Eq(entry, 0), variable)[0] for entry, variable in zip(residual, (u0, u1, u2))]

    checks = {
        "cyclic_support_is_full": all(entry.is_nonzero for entry in omega),
        "stabilizer_equations_force_identity_phase": solved == [1, 1, 1],
        "identity_phase_fixes_vacuum": sp.eye(3) * omega == omega,
    }
    result = {
        "schema": "marici.grothendieck.cyclic-vacuum-stabilizer-phase-rigidity.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "solution": [str(x) for x in solved],
        "interpretation": (
            "Inside a maximal abelian spectral algebra, a unitary multiplier that fixes a cyclic "
            "full-support vector is the identity almost everywhere. Stabilization, unlike observation, selects the phase."
        ),
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

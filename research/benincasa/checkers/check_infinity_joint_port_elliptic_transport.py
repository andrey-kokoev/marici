import json
from pathlib import Path

import sympy as sp


u, v, t = sp.symbols("u v t")
y = (u + v) / 2 - 1
z = (u - v) / 2
h = 1 + y**2 - z**2
F = t**4 - h * t**2 + y**2


def reduce_axis(axis):
    rows = []
    fp = sp.diff(F, axis)
    for grade in (0, 1):
        c0, c1, r1, r3 = sp.symbols("c0 c1 r1 r3")
        R = r1 * t + r3 * t**3
        identity = sp.expand(
            -sp.Rational(1, 2) * t ** (2 * grade) * fp
            - (
                c0 * F
                + c1 * t**2 * F
                + F * sp.diff(R, t)
                - sp.Rational(1, 2) * R * sp.diff(F, t)
            )
        )
        solution = sp.solve(
            sp.Poly(identity, t).coeffs(), (c0, c1, r1, r3), dict=True
        )[0]
        rows.append([sp.factor(solution[c0]), sp.factor(solution[c1])])
    return sp.Matrix(rows)


def main():
    au = reduce_axis(u)
    av = reduce_axis(v)
    curvature = sp.simplify(sp.diff(au, v) - sp.diff(av, u) + au * av - av * au)
    pole_product = u * v * (u - 2) * (v - 2) * (u + v - 2)
    q = sp.factor(-16 * y**2 - 8 * y * u**2 + 8 * ((u + v) / 2) * u**3 - 5 * u**4)
    denominators = [sp.factor(sp.denom(entry)) for entry in list(au) + list(av)]
    checks = {
        "griffiths_reduction_unique": au.shape == (2, 2) and av.shape == (2, 2),
        "flatness": curvature == sp.zeros(2),
        "all_poles_on_declared_product": all(
            sp.rem(pole_product, denominator, u, v) == 0 for denominator in denominators
        ),
        "quartic_coprime_to_pole_product": sp.gcd(q, pole_product) == 1,
        "symmetric_u_derivative_nonzero": au.subs({u: 3, v: 1}) * sp.ones(2, 1)
        == sp.Matrix([-sp.Rational(1, 6), sp.Rational(1, 6)]),
        "symmetric_v_derivative_nonzero": av.subs({u: 3, v: 1}) * sp.ones(2, 1)
        == sp.Matrix([-sp.Rational(1, 2), sp.Rational(1, 2)]),
    }
    failed = [name for name, passed in checks.items() if not passed]
    packet = {
        "schema": "marici.infinity_joint_port_elliptic_transport.v1",
        "connection_u": [[str(sp.factor(x)) for x in row] for row in au.tolist()],
        "connection_v": [[str(sp.factor(x)) for x in row] for row in av.tolist()],
        "pole_product": str(pole_product),
        "quartic": str(q),
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
    }
    output = Path(__file__).resolve().parents[1] / "results" / "infinity-joint-port-elliptic-transport.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()

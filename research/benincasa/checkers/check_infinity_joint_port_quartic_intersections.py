import json
from pathlib import Path

import sympy as sp


u, v = sp.symbols("u v")
q = -u**4 + 4*u**3*v - 4*u**3 - 4*u**2*v + 4*u**2 - 8*u*v + 16*u - 4*v**2 + 16*v - 16
au = sp.Matrix([
    [-(u - 1) / (2*u*(u - 2)), 1 / (u*(u - 2)*(u + v - 2))],
    [-(u + v - 2) / (4*u*(u - 2)), (u - 1) / (2*u*(u - 2))],
])
av = sp.Matrix([
    [-(v - 1) / (2*v*(v - 2)), 1 / (v*(v - 2)*(u + v - 2))],
    [-(u + v - 2) / (4*v*(v - 2)), (v - 1) / (2*v*(v - 2))],
])


def matrix_rank_and_square(matrix):
    return matrix.rank(), sp.simplify(matrix * matrix) == sp.zeros(2)


def main():
    restrictions = {
        "u=0": sp.factor(q.subs(u, 0)),
        "u=2": sp.factor(q.subs(u, 2)),
        "v=0": sp.factor(q.subs(v, 0)),
        "v=2": sp.factor(q.subs(v, 2)),
        "u+v-2=0": sp.factor(q.subs(v, 2-u)),
    }
    residue_v0 = (v * av).applyfunc(lambda entry: sp.factor(sp.limit(entry, v, 0)))
    alpha = -1 + sp.sqrt(5)
    residue_v0_alpha = residue_v0.subs(u, alpha)
    residue_signed = sp.zeros(2)
    residue_signed[0, 1] = sp.factor(1 / (u * (u - 2)))
    residue_signed_point = residue_signed.subs(u, sp.Rational(8, 5))
    rank_v0, square_v0 = matrix_rank_and_square(residue_v0_alpha)
    rank_signed, square_signed = matrix_rank_and_square(residue_signed_point)
    checks = {
        "u0_only_deeper_corner": restrictions["u=0"] == -4*(v-2)**2,
        "u2_only_deeper_corner": restrictions["u=2"] == -4*(v-2)**2,
        "v2_only_deeper_corners": restrictions["v=2"] == -u**2*(u-2)**2,
        "v0_two_quadratic_points": restrictions["v=0"] == -(u**2+2*u-4)**2,
        "signed_wall_one_generic_point": restrictions["u+v-2=0"] == -u**3*(5*u-8),
        "v0_generic_residue_rank_one_nilpotent": rank_v0 == 1 and square_v0,
        "signed_generic_residue_rank_one_nilpotent": rank_signed == 1 and square_signed,
    }
    failed = [name for name, passed in checks.items() if not passed]
    packet = {
        "schema": "marici.infinity_joint_port_quartic_intersections.v1",
        "quartic_restrictions": {key: str(value) for key, value in restrictions.items()},
        "generic_quadratic_points_on_v0": "u=-1+-sqrt(5)",
        "generic_rational_point_on_signed_wall": {"u": "8/5", "v": "2/5"},
        "residue_v0": [[str(sp.factor(x)) for x in row] for row in residue_v0.tolist()],
        "residue_signed_at_rational_point": [[str(x) for x in row] for row in residue_signed_point.tolist()],
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
    }
    output = Path(__file__).resolve().parents[1] / "results" / "infinity-joint-port-quartic-intersections.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()

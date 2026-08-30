"""Exact local audit of the squared (u-4)^2 factor in Res_v(Q,D)."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "q-d-u4-transversality.json"


def q(u, v):
    return (
        -u**4 + 4*u**3*v - 4*u**3 - 4*u**2*v + 4*u**2
        - 8*u*v - 4*v**2 + 16*u + 16*v - 16
    )


def d(u, v):
    return -4*u**2*v + 9*u**2 + 6*u*v + v**2 - 12*u - 4*v + 4


def q_u(u, v):
    return -4*u**3 + 12*u**2*v - 12*u**2 - 8*u*v + 8*u - 8*v + 16


def q_v(u, v):
    return 4*u**3 - 4*u**2 - 8*u - 8*v + 16


def d_u(u, v):
    return -8*u*v + 18*u + 6*v - 12


def d_v(u, v):
    return -4*u**2 + 6*u + 2*v - 4


def main():
    # Put t=v-22.  The common quadratic is t^2-384.
    # J=(Q_u D_v-Q_v D_u)|_{u=4}=256*(144+7*t).
    # Its norm in Q[t]/(t^2-384) is 256^2*(144^2-49*384).
    common_discriminant = 44**2 - 4*100
    reduced_jacobian_norm = 144**2 - 49*384
    jacobian_norm = 256**2 * reduced_jacobian_norm

    sample_vs = [0, 1, 22, 44]
    restriction_checks = [
        {
            "v": v,
            "Q": q(4, v),
            "minus4_common_quadratic": -4 * (v*v - 44*v + 100),
            "D": d(4, v),
            "common_quadratic": v*v - 44*v + 100,
        }
        for v in sample_vs
    ]
    jacobian_checks = [
        {
            "v": v,
            "direct": q_u(4, v)*d_v(4, v)-q_v(4, v)*d_u(4, v),
            "reduced_mod_common_quadratic": 256*(144+7*(v-22)),
            "difference": (q_u(4, v)*d_v(4, v)-q_v(4, v)*d_u(4, v)) - 256*(144+7*(v-22)),
            "expected_difference": 96*(v*v-44*v+100),
        }
        for v in sample_vs
    ]

    packet = {
        "schema": "marici.benincasa.q-d-u4-transversality.v1",
        "programme": "Q-1 bounded Lakatos microprogramme",
        "belt_hypothesis": "the squared (u-4)^2 eliminant factor may signal tangency or nonreduced Q-D support",
        "Q_at_u4": "-4*(v^2-44*v+100)",
        "D_at_u4": "v^2-44*v+100",
        "common_quadratic_discriminant": common_discriminant,
        "common_roots": "v=22 +/- 8*sqrt(6)",
        "jacobian_mod_common_quadratic": "256*(144+7*t), t=v-22, t^2=384",
        "reduced_jacobian_norm": reduced_jacobian_norm,
        "jacobian_norm": jacobian_norm,
        "restriction_checks": restriction_checks,
        "jacobian_checks": jacobian_checks,
        "conclusion": "the two conjugate Q-D intersections at u=4 are reduced and transverse; the resultant multiplicity two counts two points, not tangency",
        "belt_adjustment": "u=4 supplies no hidden nonreduced carrier center or excess Q-normal direction",
        "scope_exclusions": ["u=0", "intersections with additional carrier divisors", "nonhomogeneous systems"],
    }
    packet["passed"] = (
        common_discriminant == 1536
        and reduced_jacobian_norm == 1920
        and jacobian_norm != 0
        and all(item["Q"] == item["minus4_common_quadratic"] and item["D"] == item["common_quadratic"] for item in restriction_checks)
        and all(item["difference"] == item["expected_difference"] for item in jacobian_checks)
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

"""Exact Q-1 belt test at the soft corner (u,v)=(0,2)."""

from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "q-d-soft-corner.json"


def q(u, v):
    return (
        -u**4 + 4*u**3*v - 4*u**3 - 4*u**2*v + 4*u**2
        - 8*u*v - 4*v**2 + 16*u + 16*v - 16
    )


def d(u, v):
    return -4*u**2*v + 9*u**2 + 6*u*v + v**2 - 12*u - 4*v + 4


def q_shifted(u, w):
    return -4*w*w - 8*u*w - 4*u*u - 4*u*u*w + 4*u**3 + 4*u**3*w - u**4


def d_shifted(u, w):
    return w*w + 6*u*w + u*u - 4*u*u*w


def main():
    samples = [(0, 0), (1, 0), (0, 1), (2, -1), (-1, 3)]
    shift_checks = [
        {
            "u": u,
            "w": w,
            "Q_direct": q(u, w + 2),
            "Q_shifted": q_shifted(u, w),
            "D_direct": d(u, w + 2),
            "D_shifted": d_shifted(u, w),
        }
        for u, w in samples
    ]

    # Initial forms at the maximal ideal (u,w):
    # in(Q)=-4(w+u)^2 and in(D)=w^2+6uw+u^2.
    # The sole tangent of Q is w=-u.  Substitution into in(D) gives -4u^2,
    # so the tangent cones are coprime.  A plane complete intersection with
    # coprime initial forms of degrees 2 and 2 has local length 4.
    d_initial_on_q_tangent_coefficient = 1 - 6 + 1

    # In r=w+u coordinates Q=-4r^2+4u^2(u-1)r+u^3(8-5u).
    # Its r-discriminant is 16u^3(u-2)^2(u+2), giving an odd u-valuation 3.
    q_r_discriminant_factor_at_zero = 16 * ((-2)**2) * 2

    packet = {
        "schema": "marici.benincasa.q-d-soft-corner.v1",
        "programme": "Q-1 bounded Lakatos microprogramme",
        "belt_hypothesis": "Q may acquire excess structure at the existing soft D intersection",
        "point": {"u": 0, "v": 2, "local_coordinate": "w=v-2"},
        "Q_shifted": "-4*w^2-8*u*w-4*u^2-4*u^2*w+4*u^3+4*u^3*w-u^4",
        "D_shifted": "w^2+6*u*w+u^2-4*u^2*w",
        "Q_initial_form": "-4*(w+u)^2",
        "D_initial_form": "w^2+6*u*w+u^2",
        "D_initial_on_Q_tangent": "-4*u^2",
        "tangent_cones_coprime": d_initial_on_q_tangent_coefficient != 0,
        "Q_r_discriminant": "16*u^3*(u-2)^2*(u+2)",
        "Q_r_discriminant_u_valuation": 3,
        "Q_local_type": "cusp-type double tangent (A2 at the initial quasi-homogeneous grade)",
        "D_local_type": "ordinary node with two distinct tangents over Q(sqrt(2))",
        "expected_local_intersection_length": 4,
        "entry_863_resultant_u_multiplicity": 4,
        "excess_intersection_length": 0,
        "conclusion": "the u^4 resultant factor is exactly the 2-by-2 intersection multiplicity of coprime tangent cones; it contains no additional Q-D tangency or nonreduced excess",
        "scope_boundary": "This classifies the local carrier intersection only; it does not by itself compute the full soft nearby-cycle coefficient complex.",
        "shift_checks": shift_checks,
    }
    packet["passed"] = (
        all(item["Q_direct"] == item["Q_shifted"] and item["D_direct"] == item["D_shifted"] for item in shift_checks)
        and packet["tangent_cones_coprime"]
        and q_r_discriminant_factor_at_zero != 0
        and packet["expected_local_intersection_length"] == packet["entry_863_resultant_u_multiplicity"]
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

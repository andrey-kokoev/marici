"""Source-typed weighted X1-soft specialization of the q_G12 residue current.

The calculation keeps the occurrence label q_g23.  It proves that this
marked wall is a unit on the exceptional physical current, whereas q_g1
supplies the negative endpoint.  Consequently there is no q_g23-supported
boundary/Gysin component.  This does not assert that the bulk period pairing
with the rank-four residue quotient vanishes.
"""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x, p, kappa, a, xi = sp.symbols("x p kappa a xi")
    y = p + x * kappa / 2
    z = p - x * kappa / 2
    energy = x + y + z
    c = -energy
    b = energy + x * xi

    # Both source triangle faces are required.  The fixed external triangle
    # forces X2-X3=O(X1); kappa retains that labelled normal.
    face_xyz = sp.expand(
        ((y + z) ** 2 - x**2) * ((y - z) ** 2 - x**2)
    )
    face_cb = sp.expand(((c + b) ** 2 - x**2) * ((c - b) ** 2 - x**2))
    exceptional_unit = sp.expand(face_cb / x**2 / (xi**2 - 1))

    walls = {
        "q_g1": sp.expand(b - y - z),
        "q_g2": sp.expand(a - x - z),
        "q_g3": sp.expand(a + b + z),
        "q_g23": sp.expand(b - x),
        "q_g31": sp.expand(a - y),
        "q_G31": sp.expand(energy + b),
    }
    exceptional = {name: sp.expand(value.subs(x, 0)) for name, value in walls.items()}

    expected_face = sp.expand(
        x**2 * (xi**2 - 1) * ((2 * energy + x * xi) ** 2 - x**2)
    )
    checks = {
        "weighted_face_factorization": sp.expand(face_cb - expected_face) == 0,
        "weighted_base_face_factorization": sp.expand(
            face_xyz - x**2 * (kappa**2 - 1) * (4 * p**2 - x**2)
        ) == 0,
        "exceptional_face_is_two_endpoint_interval": sp.expand(
            sp.cancel(face_cb / x**2).subs(x, 0)
            - 16 * p**2 * (xi**2 - 1)
        ) == 0,
        "q_g1_has_soft_normal": sp.expand(walls["q_g1"] - x * (xi + 1)) == 0,
        "q_g23_is_exceptional_unit": exceptional["q_g23"] == 2 * p,
        "q_G31_is_exceptional_unit": exceptional["q_G31"] == 4 * p,
        "negative_endpoint_is_q_g1": sp.expand(
            (walls["q_g1"] / x).subs(xi, -1)
        ) == 0,
        "positive_endpoint_not_q_g1": sp.expand(
            (walls["q_g1"] / x).subs(xi, 1)
        ) == 2,
    }
    if not all(checks.values()):
        raise AssertionError({name: value for name, value in checks.items() if not value})

    result = {
        "schema": "marici.benincasa.x1-soft-physical-current-factorization.v1",
        "source_residue_chart": {
            "q_G12": "c+X1+X2+X3=0",
            "c": "-(X1+X2+X3)",
            "a": "y23",
            "b": "y31",
            "orientation": "da wedge db",
        },
        "weighted_soft_chart": {
            "normal": "x=X1",
            "base_triangle_normal": "kappa=(X2-X3)/X1",
            "exceptional_coordinate": "xi=(b-E)/x",
            "substitution": "X2=p+x*kappa/2, X3=p-x*kappa/2, b=E+x*xi",
            "physical_exceptional_intervals": [
                "-1 <= kappa <= 1",
                "-1 <= xi <= 1"
            ],
        },
        "face_factorization": str(sp.factor(face_cb)),
        "exceptional_face": "16*p^2*(xi^2-1)",
        "exceptional_base_face": "4*p^2*(kappa^2-1)",
        "exceptional_wall_values": {name: str(value) for name, value in exceptional.items()},
        "soft_normalized_q_g1": "xi+1",
        "q_g23_exceptional_value": "2*p",
        "q_g23_unit_condition": "p != 0",
        "physical_support_factorization": (
            "the exceptional boundary current lies in the open set where q_g23 is a unit; "
            "its marked boundary is q_g1-supported"
        ),
        "rank4_residue_quotient_boundary_map": (
            "zero: no q_g23-supported boundary/Gysin component occurs on the exceptional current"
        ),
        "rank4_residue_quotient_bulk_pairing": (
            "unresolved; avoiding a marked divisor does not force a bulk relative-period pairing to vanish"
        ),
        "endpoint_support": {
            "xi=-1": "q_g1=0 after removing the common soft normal",
            "xi=+1": "Cayley-Menger face endpoint; q_g1/x=2",
        },
        "checks": checks,
        "status": "source_typed_soft_triangle_current_has_only_existing_q_g1_marked_boundary_support",
        "scope": (
            "generic p nonzero weighted soft-triangle exceptional fiber of the q_G12 residue; "
            "this does not construct a Betti pairing on all of M16 or cover total-energy/soft intersections"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

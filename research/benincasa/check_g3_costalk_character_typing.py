"""Check whether the physical g3 wall preserves the nine-master parity group."""
from __future__ import annotations

import json

import sympy as sp


def scalar_multiple(left: sp.Expr, right: sp.Expr, variables: tuple[sp.Symbol, ...]) -> bool:
    left_poly = sp.Poly(left, *variables)
    right_poly = sp.Poly(right, *variables)
    if left_poly.total_degree() != right_poly.total_degree():
        return False
    quotient = None
    for monomial in set(left_poly.monoms()) | set(right_poly.monoms()):
        lv = left_poly.coeff_monomial(monomial)
        rv = right_poly.coeff_monomial(monomial)
        if rv == 0:
            if lv != 0:
                return False
            continue
        ratio = sp.factor(lv / rv)
        if quotient is None:
            quotient = ratio
        elif sp.factor(ratio - quotient) != 0:
            return False
    return quotient is not None


def main() -> None:
    a, b, z = sp.symbols("a b z")
    wall = a + b + z
    orbit = []
    stabilizer = []
    for sign_a in (-1, 1):
        for sign_b in (-1, 1):
            image = sp.expand(wall.subs({a: sign_a * a, b: sign_b * b}))
            fixed = scalar_multiple(image, wall, (a, b, z))
            orbit.append(
                {
                    "sign_a": sign_a,
                    "sign_b": sign_b,
                    "wall_image": str(image),
                    "preserves_physical_wall": fixed,
                }
            )
            if fixed:
                stabilizer.append([sign_a, sign_b])

    assert stabilizer == [[1, 1]]
    assert len({row["wall_image"] for row in orbit}) == 4

    result = {
        "schema": "marici.g3-costalk-character-typing.v1",
        "physical_wall": str(wall),
        "C2a_times_C2b_orbit": orbit,
        "generic_wall_stabilizer": stabilizer,
        "stabilizer_order": 1,
        "nine_master_character_blocks": {
            "odd_odd": ["e1"],
            "odd_even": ["e2", "e3"],
            "even_odd": ["e4", "e5"],
            "even_even": ["e6", "e7", "e8", "e9"],
        },
        "normalization_involution": "w -> -w",
        "normalization_involution_is_C2a_or_C2b": False,
        "character_match_to_T7_is_typed": False,
        "canonical_target_line_selected": False,
        "new_carrier_datum": False,
        "required_next_map": "nonequivariant local Gysin connecting morphism from the source wall",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

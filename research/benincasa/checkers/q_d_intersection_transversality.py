"""Exact first protective-belt test for the Q microprogramme.

The eliminant of the predeclared divisor D against Q is inherited from Entry
863.  This checker proves that its nontrivial cubic factor is squarefree and
irreducible over Q.  Hence its three geometric conjugates are reduced simple
intersections; they do not define a hidden nonreduced Q-supported center.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "results" / "q-d-intersection-transversality.json"


def trim(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def remainder(left, right):
    left = left[:]
    while len(left) >= len(right) and left:
        scale = left[-1] / right[-1]
        shift = len(left) - len(right)
        for index, coefficient in enumerate(right):
            left[index + shift] -= scale * coefficient
        trim(left)
    return left


def gcd_degree(left, right):
    left = [Fraction(x) for x in left]
    right = [Fraction(x) for x in right]
    while right:
        left, right = right, remainder(left, right)
    return len(left) - 1


def main():
    # C(u)=16u^3-57u^2+56u-16, coefficient order low to high.
    cubic = [-16, 56, -57, 16]
    derivative = [56, -114, 48]
    a, b, c, d = 16, -57, 56, -16
    discriminant = (
        b * b * c * c
        - 4 * a * c**3
        - 4 * b**3 * d
        - 27 * a * a * d * d
        + 18 * a * b * c * d
    )

    possible_roots = {
        Fraction(sign * numerator, denominator)
        for sign in (-1, 1)
        for numerator in (1, 2, 4, 8, 16)
        for denominator in (1, 2, 4, 8, 16)
    }
    rational_roots = sorted(
        root
        for root in possible_roots
        if sum(Fraction(coefficient) * root**power for power, coefficient in enumerate(cubic)) == 0
    )

    packet = {
        "schema": "marici.benincasa.q-d-intersection-transversality.v1",
        "programme": "bounded Q Lakatos microprogramme",
        "belt_hypothesis": "Q may acquire excess structure at an existing divisor intersection",
        "tested_stratum": "generic nontrivial component of Q intersect D",
        "entry_863_eliminant": "-u^4*(u-4)^2*(16*u^3-57*u^2+56*u-16)",
        "nontrivial_factor": "16*u^3-57*u^2+56*u-16",
        "discriminant": discriminant,
        "discriminant_factorization": "2^9*71",
        "gcd_with_derivative_degree": gcd_degree(cubic, derivative),
        "rational_roots": [str(root) for root in rational_roots],
        "irreducible_over_Q": not rational_roots,
        "squarefree": discriminant != 0 and gcd_degree(cubic, derivative) == 0,
        "geometric_conclusion": "one degree-three closed point with three reduced conjugate geometric intersections; generic local intersection multiplicity one",
        "connection_input": "Entry 871 proves the admissible horizontal gauge and generic marked-relative extension are Q-regular",
        "nearby_cycle_conclusion": "at the generic cubic Q-D intersections, Q is a transverse regular parameter and contributes no separate logarithmic residue or excess nearby-cycle direction",
        "scope_exclusions": ["u=0", "u=4", "other carrier intersections", "nonhomogeneous systems"],
    }
    packet["passed"] = (
        packet["discriminant"] == 36352
        and packet["gcd_with_derivative_degree"] == 0
        and packet["irreducible_over_Q"]
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

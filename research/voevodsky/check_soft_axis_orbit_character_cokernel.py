"""Characterwise cokernel census for the deck-orbit-completed exact complex."""

import importlib.util
from pathlib import Path


P = 2305843009213693951
SECTORS = ((1, 1), (1, 0), (0, 1), (0, 0))

dependency = Path(__file__).with_name("check_soft_axis_deck_orbit_completion.py")
spec = importlib.util.spec_from_file_location("deck", dependency)
deck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deck)


def finite(coefficient):
    return coefficient.numerator * pow(coefficient.denominator, P - 2, P) % P


def rank(columns):
    basis = {}
    for column in columns:
        vector = dict(column)
        while vector:
            pivot = min(vector)
            if pivot in basis:
                factor = vector[pivot]
                for row, value in basis[pivot].items():
                    vector[row] = (vector.get(row, 0) - factor * value) % P
                    if not vector[row]:
                        vector.pop(row, None)
            else:
                inverse = pow(vector[pivot], P - 2, P)
                basis[pivot] = {row: value * inverse % P for row, value in vector.items()}
                break
    return len(basis)


def restrict(poly, cutoff, u_degree, character):
    return {
        monomial: finite(coefficient)
        for monomial, coefficient in poly.items()
        if monomial[0] <= u_degree
        and monomial[1] + monomial[2] <= cutoff
        and (-1) ** monomial[1] == character
    }


def census(cutoff, u_degree, character):
    rows = [
        (ud, ad, total - ad)
        for ud in range(u_degree + 1)
        for total in range(cutoff + 1)
        for ad in range(total + 1)
        if (-1) ** ad == character
    ]
    position = {monomial: index for index, monomial in enumerate(rows)}
    columns = []
    for sector in SECTORS:
        for total in range(cutoff + 1):
            for ad in range(total + 1):
                f = deck.mul(deck.power(deck.a, ad), deck.power(deck.b, total - ad))
                for is_q in (False, True):
                    generator = deck.exact(sector, f, is_q)
                    for u_power in range(u_degree + 1):
                        candidate = deck.mul(deck.power(deck.u, u_power), generator)
                        # Use only filtered columns whose complete support lies in the cutoff.
                        if candidate and max(m[1] + m[2] for m in candidate) <= cutoff:
                            projected = restrict(candidate, cutoff, u_degree, character)
                            if projected:
                                columns.append({position[m]: c for m, c in projected.items()})
    return len(rows) - rank(columns)


results = []
for cutoff in (16, 20, 24, 28):
    plus_special = census(cutoff, 0, 1)
    minus_special = census(cutoff, 0, -1)
    plus_dual = census(cutoff, 1, 1)
    minus_dual = census(cutoff, 1, -1)
    results.append((cutoff, plus_special, minus_special, plus_dual, minus_dual))
    print(
        f"cutoff_{cutoff}: special(+,-)=({plus_special},{minus_special}) "
        f"dual(+,-)=({plus_dual},{minus_dual})"
    )

assert all(ps == 2 * cutoff + 1 for cutoff, ps, _, _, _ in results)
assert all(ms == 2 * cutoff - 1 for cutoff, _, ms, _, _ in results)
assert all(pd == 4 * cutoff + 1 for cutoff, _, _, pd, _ in results)
assert all(md == 3 * cutoff for cutoff, _, _, _, md in results)
assert all(2 * ps - pd == 1 for _, ps, _, pd, _ in results)
assert all(2 * ms - md == cutoff - 2 for cutoff, _, ms, _, md in results)
print("plus first-order flatness defect: 1")
print("minus first-order flatness defect: D-2")
print("total orbit-completed defect: D-1")

"""Authoritative finite Q_D census used in the soft-axis comparison.

This materializes the previously inline audit without changing its bases,
deck-orbit completion, projection, or cutoff admission rule.
"""

from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path

P = 2305843009213693951
SECTORS = ((1, 1), (1, 0), (0, 1), (0, 0))
EXPECTED = {
    12: (105, 68, 31),
    16: (155, 106, 57),
    20: (213, 152, 91),
    24: (279, 206, 133),
}

dependency = Path(__file__).parents[1] / "voevodsky" / "check_soft_axis_deck_orbit_completion.py"
spec = importlib.util.spec_from_file_location("deck", dependency)
deck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deck)


def finite(x):
    return x.numerator * pow(x.denominator, P - 2, P) % P


def rank(columns):
    basis = {}
    for source in columns:
        vector = {row: finite(value) for row, value in source.items() if value}
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                inverse = pow(vector[pivot], P - 2, P)
                basis[pivot] = {row: value * inverse % P for row, value in vector.items()}
                break
            factor = vector[pivot]
            for row, value in basis[pivot].items():
                vector[row] = (vector.get(row, 0) - factor * value) % P
                if not vector[row]:
                    vector.pop(row, None)
    return len(basis)


def component_rows(cutoff, u_degree):
    # e_a is odd under rho(a)=-a; e_b and e_u are even.
    rows = []
    for component, frame_character in ((0, -1), (1, 1), (2, 1)):
        for ud in range(u_degree + 1):
            for total in range(cutoff + 1):
                for ad in range(total + 1):
                    if (-1) ** ad * frame_character == 1:
                        rows.append((component, ud, ad, total - ad))
    return rows


def census(cutoff):
    rows = component_rows(cutoff, 1)
    position = {monomial: index for index, monomial in enumerate(rows)}
    columns = []

    def emit(parts):
        support = [monomial for part in parts for monomial in part]
        if not support:
            return
        # Whole-column admission: never truncate individual components.
        if any(ud >= 2 or ad + bd > cutoff for ud, ad, bd in support):
            return
        column = {}
        for component, part in enumerate(parts):
            for (ud, ad, bd), coefficient in part.items():
                key = (component, ud, ad, bd)
                if key in position:  # plus-character projection
                    row = position[key]
                    column[row] = column.get(row, Q(0)) + coefficient
        column = {row: value for row, value in column.items() if value}
        if column:
            columns.append(column)

    euler = (
        deck.scale(deck.a, Q(1, 4)),
        {},
        deck.scale(deck.u, Q(1, 2)),
    )

    for sa, sb in SECTORS:
        ea, eb = 2 - sa, 2 - sb
        for conjugate in (False, True):
            l2 = deck.L2_plus if conjugate else deck.L2_minus
            base = deck.mul(deck.power(deck.L1, ea), deck.power(l2, eb))
            for total in range(cutoff + 1):
                for ad in range(total + 1):
                    f = deck.mul(deck.power(deck.a, ad), deck.power(deck.b, total - ad))
                    m = deck.mul(f, base)

                    c_p = deck.scale(deck.mul(deck.derivative(f, 2), base), -1)
                    if sa:
                        c_p = deck.add(
                            c_p,
                            deck.scale(
                                deck.mul(f, deck.power(deck.L1, ea - 1), deck.power(l2, eb)),
                                sa,
                            ),
                        )
                    h_p = ({}, deck.scale(m, Q(3, 2)), {})
                    emit([deck.add(h_p[i], deck.mul(c_p, euler[i])) for i in range(3)])

                    c_q = deck.mul(deck.derivative(f, 1), base)
                    if sb:
                        c_q = deck.add(
                            c_q,
                            deck.scale(
                                deck.mul(f, deck.power(deck.L1, ea), deck.power(l2, eb - 1)),
                                -sb,
                            ),
                        )
                    h_q = (deck.scale(m, Q(-3, 2)), {}, {})
                    emit([deck.add(h_q[i], deck.mul(c_q, euler[i])) for i in range(3)])

    # Principal Euler columns E(P_D).
    for total in range(cutoff + 1):
        for ad in range(total + 1):
            p = deck.mul(deck.power(deck.a, ad), deck.power(deck.b, total - ad))
            emit([deck.mul(p, component) for component in euler])

    full_dimension = len(rows) - rank(columns)
    rows_zero = [row for row in rows if row[1] == 0]
    zero_position = {row: index for index, row in enumerate(rows_zero)}
    zero_columns = []
    for column in columns:
        restricted = {
            zero_position[rows[row]]: value
            for row, value in column.items()
            if rows[row][1] == 0
        }
        if restricted:
            zero_columns.append(restricted)
    special_dimension = len(rows_zero) - rank(zero_columns)
    torsion_dimension = 2 * special_dimension - full_dimension
    return full_dimension, special_dimension, torsion_dimension


def main():
    results = {cutoff: census(cutoff) for cutoff in EXPECTED}
    assert results == EXPECTED
    for cutoff, triple in results.items():
        print(f"D={cutoff}: dim_Q={triple[0]} dim_Q_mod_u={triple[1]} t={triple[2]}")
    print(json.dumps({
        "schema": "marici.benincasa.q_d_census.v1",
        "results": {str(k): list(v) for k, v in results.items()},
        "closed_form": "t_D=(D/2)^2-D/2+1",
    }, sort_keys=True))


if __name__ == "__main__":
    main()

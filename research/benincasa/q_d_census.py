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
EXPECTED_KOSZUL_AUDIT = {
    12: (16, (15, 22), (5, 20, 6)),
    16: (22, (21, 32), (7, 42, 8)),
    20: (28, (27, 42), (9, 72, 10)),
    24: (34, (33, 52), (11, 110, 12)),
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

    def emit(parts, target=columns):
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
            target.append(column)

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

    # Compute the intrinsic Koszul filtration on H(Q_D,u).  Intersections are
    # taken by ranks; in particular the relation among the three elementary
    # syzygies is retained rather than assigning monomial families by hand.
    u_columns = []
    for row, (component, ud, ad, bd) in enumerate(rows):
        if ud == 0:
            shifted = position.get((component, 1, ad, bd))
            if shifted is not None:
                u_columns.append({shifted: Q(1)})

    def frozen(poly):
        return {monomial: value for monomial, value in poly.items() if monomial[0] == 0}

    ka = frozen(deck.derivative(deck.K, 1))
    kb = frozen(deck.derivative(deck.K, 2))
    ku = frozen(deck.derivative(deck.K, 0))
    s0_columns = []
    sau_columns = []
    for total in range(cutoff + 1):
        for ad in range(total + 1):
            multiplier = deck.mul(deck.power(deck.a, ad), deck.power(deck.b, total - ad))
            emit(
                [deck.scale(deck.mul(multiplier, kb), -1), deck.mul(multiplier, ka), {}],
                s0_columns,
            )
            emit(
                [{}, deck.scale(deck.mul(multiplier, ku), -1), deck.mul(multiplier, kb)],
                s0_columns,
            )
            emit(
                [deck.scale(deck.mul(multiplier, ku), -1), {}, deck.mul(multiplier, ka)],
                sau_columns,
            )

    def multiply_column_by_u(column):
        shifted = {}
        for row, value in column.items():
            component, ud, ad, bd = rows[row]
            if ud == 0:
                target = position[(component, 1, ad, bd)]
                shifted[target] = shifted.get(target, Q(0)) + value
        return {row: value for row, value in shifted.items() if value}

    s1_columns = s0_columns + sau_columns
    rank_i = rank(columns)
    module_defect = (
        rank(columns + [multiply_column_by_u(column) for column in columns]) - rank_i
    )
    cycle_defects = (
        rank(columns + [multiply_column_by_u(column) for column in s0_columns]) - rank_i,
        rank(columns + [multiply_column_by_u(column) for column in s1_columns]) - rank_i,
    )

    b_columns = columns + u_columns
    rank_b = rank(b_columns)
    rank_b_s0 = rank(b_columns + s0_columns)
    rank_b_s1 = rank(b_columns + s1_columns)
    filtration = (
        rank_b_s0 - rank_b,
        rank_b_s1 - rank_b_s0,
        torsion_dimension - (rank_b_s1 - rank_b),
    )
    return (
        full_dimension,
        special_dimension,
        torsion_dimension,
        module_defect,
        cycle_defects,
        filtration,
    )


def main():
    results = {cutoff: census(cutoff) for cutoff in EXPECTED}
    assert {cutoff: result[:3] for cutoff, result in results.items()} == EXPECTED
    assert {cutoff: result[3:] for cutoff, result in results.items()} == EXPECTED_KOSZUL_AUDIT
    for cutoff, result in results.items():
        print(
            f"D={cutoff}: dim_Q={result[0]} dim_Q_mod_u={result[1]} t={result[2]} "
            f"module_defect={result[3]} cycle_defects={result[4]} "
            f"formal_F0={result[5][0]} formal_F1/F0={result[5][1]} formal_H/F1={result[5][2]}"
        )
    print(json.dumps({
        "schema": "marici.benincasa.q_d_census.v1",
        "results": {str(k): [*v[:4], list(v[4]), list(v[5])] for k, v in results.items()},
        "closed_form": "t_D=(D/2)^2-D/2+1",
    }, sort_keys=True))


if __name__ == "__main__":
    main()

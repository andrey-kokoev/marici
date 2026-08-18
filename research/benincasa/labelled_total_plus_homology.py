"""Middle homology census for the genuine R-linear plus total complex."""

from fractions import Fraction as Q
import importlib.util
from pathlib import Path

here = Path(__file__).parent
spec = importlib.util.spec_from_file_location("total", here / "check_soft_axis_labelled_total_truncation.py")
total = importlib.util.module_from_spec(spec)
spec.loader.exec_module(total)

P = 2305843009213693951


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


def target_rows(cutoff):
    rows = []
    for ud in range(2):
        for degree in range(cutoff + 1):
            for ad in range(degree + 1):
                if ad % 2 == 0:
                    rows.append(("B", 0, ud, ad, degree - ad))
    for component, character in ((0, -1), (1, 1), (2, 1)):
        for ud in range(2):
            for degree in range(cutoff - 2):
                for ad in range(degree + 1):
                    if (-1) ** ad * character == 1:
                        rows.append(("G", component, ud, ad, degree - ad))
    return rows


def census(cutoff):
    rows = target_rows(cutoff)
    position = {row: i for i, row in enumerate(rows)}
    columns = []

    def emit(scalar, lift):
        column = {}
        for (ud, ad, bd), value in scalar.items():
            row = position.get(("B", 0, ud, ad, bd))
            if row is not None:
                column[row] = column.get(row, Q(0)) + value
        for component, part in enumerate(lift):
            for (ud, ad, bd), value in part.items():
                row = position.get(("G", component, ud, ad, bd))
                if row is not None:
                    column[row] = column.get(row, Q(0)) + value
        column = {row: value for row, value in column.items() if value}
        if column:
            columns.append(column)

    for sa, sb in total.SECTORS:
        ea, eb = 2 - sa, 2 - sb
        for label in ("p", "q"):
            transport = (-1) ** (eb + (label == "q"))
            for degree in range(cutoff - 3 - ea - eb + 1):
                for ad in range(degree + 1):
                    f = total.monomial(ad, degree - ad)
                    minus = total.labelled_map(f, sa, sb, False, label)
                    plus = total.labelled_map(f, sa, sb, True, label)
                    coefficient = transport * (-1) ** ad
                    scalar = total.deck.add(minus[0], total.deck.scale(plus[0], coefficient))
                    lift = tuple(total.deck.add(minus[1][i], total.deck.scale(plus[1][i], coefficient)) for i in range(3))
                    emit(scalar, lift)
                    emit(total.deck.mul(total.deck.u, scalar), tuple(total.deck.mul(total.deck.u, x) for x in lift))

    principal_rank_r = 0
    for degree in range(cutoff - 4 + 1):
        for ad in range(degree + 1):
            if ad % 2:
                continue
            p = total.monomial(ad, degree - ad)
            scalar = total.deck.mul(total.deck.K, p)
            lift = tuple(total.deck.mul(p, x) for x in total.EULER)
            emit(scalar, lift)
            emit(total.deck.mul(total.deck.u, scalar), tuple(total.deck.mul(total.deck.u, x) for x in lift))
            principal_rank_r += 1

    image_rank = rank(columns)
    b_dimension = sum(1 for row in rows if row[0] == "B")
    r_dimension = b_dimension - 2 * principal_rank_r
    homology_dimension = len(rows) - r_dimension - image_rank

    zero_rows = [i for i, row in enumerate(rows) if row[2] == 0]
    zero_position = {row: i for i, row in enumerate(zero_rows)}
    zero_columns = []
    for column in columns:
        restricted = {zero_position[row]: value for row, value in column.items() if row in zero_position}
        if restricted:
            zero_columns.append(restricted)
    image_rank_zero = rank(zero_columns)
    b_zero = b_dimension // 2
    r_zero = b_zero - principal_rank_r
    homology_zero = len(zero_rows) - r_zero - image_rank_zero
    return len(rows), image_rank, homology_dimension, homology_zero


for cutoff in (12, 16, 20, 24):
    print(cutoff, census(cutoff))

#!/usr/bin/env python3
"""Derive the complete first Koszul syzygies of marked-pole multiplication."""

import contextlib
import importlib
import io
import json
from itertools import combinations, product
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    moving = importlib.import_module("check_rank26_moving_relation_coherence")

words = moving.words
base = moving.base
charts = moving.charts
P = base.PRIME


def add_scaled(target, source, scale):
    for column, coefficient in source.items():
        base.add_value(target, column, scale * coefficient)


def relation_row(pres, qi, k_pole, levels, exponent):
    columns = pres["columns"]
    qpoly = pres["q"][charts.SOURCE_NAMES[qi]]
    raised = list(levels)
    raised[qi] += 1
    row = {columns[(k_pole, *levels, exponent)]: 1}
    for term, coefficient in base.multiply_monomial(qpoly, exponent, -1):
        base.add_value(row, columns[(k_pole, *raised, term)], coefficient)
    return row


def multiply_relation(pres, row, polynomial):
    ordered = pres["ordered_columns"]
    columns = pres["columns"]
    result = {}
    for column, coefficient in row.items():
        k_pole, *rest = ordered[column]
        exponent = rest.pop()
        for term, product_coefficient in base.multiply_monomial(
            polynomial, exponent, coefficient
        ):
            base.add_value(result, columns[(k_pole, *rest, term)], product_coefficient)
    return result


def main():
    point = words.REFERENCE_POINT
    pres = words.presentation(point)
    q = [pres["q"][name] for name in charts.SOURCE_NAMES]
    tested = 0
    failures = 0
    first_failure_support = None
    q_count = len(q)
    for qi, qj in combinations(range(q_count), 2):
        other = [index for index in range(q_count) if index not in (qi, qj)]
        for other_levels in product(range(1, charts.Q_DEPTH + 1), repeat=len(other)):
            levels = [1] * q_count
            for index, level in zip(other, other_levels):
                levels[index] = level
            for k_pole in range(charts.K_DEPTH + 1):
                for exponent in base.monomials_at_most(words.AMBIENT - 2):
                    levels_i = list(levels)
                    levels_i[qi] += 1
                    levels_j = list(levels)
                    levels_j[qj] += 1
                    square = {}
                    add_scaled(square, relation_row(pres, qi, k_pole, levels, exponent), 1)
                    add_scaled(
                        square,
                        multiply_relation(
                            pres,
                            relation_row(pres, qj, k_pole, tuple(levels_i), exponent),
                            q[qi],
                        ),
                        1,
                    )
                    add_scaled(square, relation_row(pres, qj, k_pole, levels, exponent), -1)
                    add_scaled(
                        square,
                        multiply_relation(
                            pres,
                            relation_row(pres, qi, k_pole, tuple(levels_j), exponent),
                            q[qj],
                        ),
                        -1,
                    )
                    square = {c: v % P for c, v in square.items() if v % P}
                    tested += 1
                    if square:
                        failures += 1
                        if first_failure_support is None:
                            first_failure_support = len(square)

    expected = (
        len(list(combinations(range(q_count), 2)))
        * (charts.Q_DEPTH ** (q_count - 2))
        * (charts.K_DEPTH + 1)
        * len(base.monomials_at_most(words.AMBIENT - 2))
    )
    checks = {
        "all_ten_occurrence_pairs_tested": len(list(combinations(range(q_count), 2))) == 10,
        "complete_labelled_square_family_tested": tested == expected,
        "every_koszul_square_vanishes_raw": failures == 0,
    }
    result = {
        "schema": "marici.rank26-marked-pole-first-syzygies.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "point": list(point),
        "syzygy_formula": "R_i + q_i R_j^(i) - R_j - q_j R_i^(j) = 0",
        "labelled_syzygies_tested": tested,
        "expected_labelled_syzygies": expected,
        "failures": failures,
        "first_failure_support": first_failure_support,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-marked-pole-first-syzygies.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

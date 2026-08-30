#!/usr/bin/env python3
"""Test the combined K/q multiplication syzygy complex."""

import contextlib
import importlib
import io
import json
from itertools import combinations, product
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    moving = importlib.import_module("check_rank26_moving_relation_coherence")

words, base, charts = moving.words, moving.base, moving.charts


def labels():
    q_count = len(charts.SOURCE_NAMES)
    for k_pole in range(charts.K_DEPTH):
        for levels in product(range(1, charts.Q_DEPTH + 1), repeat=q_count):
            for exponent in base.monomials_at_most(words.AMBIENT - 4):
                yield ("K", k_pole, tuple(levels), exponent)
    for qi in range(q_count):
        for k_pole in range(charts.K_DEPTH + 1):
            for levels in product(range(1, charts.Q_DEPTH + 1), repeat=q_count):
                if levels[qi] == charts.Q_DEPTH:
                    continue
                for exponent in base.monomials_at_most(words.AMBIENT - 1):
                    yield ("q", qi, k_pole, tuple(levels), exponent)


def q_q_rows(pres, pos):
    q_count = len(charts.SOURCE_NAMES)
    q = [pres["q"][name] for name in charts.SOURCE_NAMES]
    for qi, qj in combinations(range(q_count), 2):
        other = [x for x in range(q_count) if x not in (qi, qj)]
        for other_levels in product(range(1, charts.Q_DEPTH + 1), repeat=len(other)):
            levels = [1] * q_count
            for index, level in zip(other, other_levels): levels[index] = level
            for k_pole in range(charts.K_DEPTH + 1):
                for exponent in base.monomials_at_most(words.AMBIENT - 2):
                    li, lj = list(levels), list(levels)
                    li[qi] += 1; lj[qj] += 1
                    row = {}
                    base.add_value(row, pos[("q", qi, k_pole, tuple(levels), exponent)], 1)
                    for term, c in base.multiply_monomial(q[qi], exponent, 1):
                        base.add_value(row, pos[("q", qj, k_pole, tuple(li), term)], c)
                    base.add_value(row, pos[("q", qj, k_pole, tuple(levels), exponent)], -1)
                    for term, c in base.multiply_monomial(q[qj], exponent, -1):
                        base.add_value(row, pos[("q", qi, k_pole, tuple(lj), term)], c)
                    yield "qq", row


def k_q_rows(pres, pos):
    q_count = len(charts.SOURCE_NAMES)
    kpoly = pres["k"]
    q = [pres["q"][name] for name in charts.SOURCE_NAMES]
    for qi in range(q_count):
        other = [x for x in range(q_count) if x != qi]
        for other_levels in product(range(1, charts.Q_DEPTH + 1), repeat=len(other)):
            levels = [1] * q_count
            for index, level in zip(other, other_levels): levels[index] = level
            for k_pole in range(charts.K_DEPTH):
                for exponent in base.monomials_at_most(words.AMBIENT - 5):
                    lq = list(levels); lq[qi] += 1
                    row = {}
                    base.add_value(row, pos[("K", k_pole, tuple(levels), exponent)], 1)
                    for term, c in base.multiply_monomial(kpoly, exponent, 1):
                        base.add_value(row, pos[("q", qi, k_pole + 1, tuple(levels), term)], c)
                    base.add_value(row, pos[("q", qi, k_pole, tuple(levels), exponent)], -1)
                    for term, c in base.multiply_monomial(q[qi], exponent, -1):
                        base.add_value(row, pos[("K", k_pole, tuple(lq), term)], c)
                    yield "Kq", row


def main():
    point = words.REFERENCE_POINT
    pres = words.presentation(point)
    domain = list(labels())
    pos = {label: index for index, label in enumerate(domain)}
    d_rows = list(moving.iter_derived_k_relations(pres, point, 0))
    d_rows.extend(moving.iter_derived_q_relations(pres, point, 0))
    assert len(d_rows) == len(domain)
    d_pivots = {}
    for row in d_rows:
        if row: base.add_pivot(dict(row), d_pivots)

    s_pivots = {}
    counts = {"qq": 0, "Kq": 0}
    composition_failures = 0
    for family, row in list(q_q_rows(pres, pos)) + list(k_q_rows(pres, pos)):
        counts[family] += 1
        image = {}
        for generator, coefficient in row.items():
            for column, value in d_rows[generator].items():
                base.add_value(image, column, coefficient * value)
        if base.reduce_row(image, pres["pivots"]): composition_failures += 1
        base.add_pivot(dict(row), s_pivots)

    domain_dimension = len(domain)
    d_rank = len(d_pivots)
    kernel_dimension = domain_dimension - d_rank
    s_rank = len(s_pivots)
    homology = kernel_dimension - s_rank
    checks = {
        "combined_domain_dimension_is_29424": domain_dimension == 29424,
        "all_predeclared_syzygies_counted": counts == {"qq": 21840, "Kq": 8800},
        "composition_is_zero": composition_failures == 0,
        "combined_multiplication_complex_is_exact": homology == 0,
    }
    result = {
        "schema": "marici.rank26-kq-syzygy-exactness.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "point": list(point), "derivative_axis": 0,
        "domain_dimension": domain_dimension,
        "derivative_rank": d_rank,
        "derivative_kernel_dimension": kernel_dimension,
        "syzygy_generator_counts": counts,
        "syzygy_rank": s_rank,
        "composition_failures": composition_failures,
        "homology_dimension": homology,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-kq-syzygy-exactness.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__": main()

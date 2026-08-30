#!/usr/bin/env python3
"""Test exactness of the first marked-pole syzygy complex at a generic point."""

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


def domain_labels():
    q_count = len(charts.SOURCE_NAMES)
    for qi in range(q_count):
        for k_pole in range(charts.K_DEPTH + 1):
            for levels in product(range(1, charts.Q_DEPTH + 1), repeat=q_count):
                if levels[qi] == charts.Q_DEPTH:
                    continue
                for exponent in base.monomials_at_most(words.AMBIENT - 1):
                    yield (qi, k_pole, tuple(levels), exponent)


def syzygy_rows(pres, positions):
    q_count = len(charts.SOURCE_NAMES)
    q = [pres["q"][name] for name in charts.SOURCE_NAMES]
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
                    row = {}
                    base.add_value(row, positions[(qi, k_pole, tuple(levels), exponent)], 1)
                    for term, coefficient in base.multiply_monomial(q[qi], exponent, 1):
                        base.add_value(
                            row,
                            positions[(qj, k_pole, tuple(levels_i), term)],
                            coefficient,
                        )
                    base.add_value(row, positions[(qj, k_pole, tuple(levels), exponent)], -1)
                    for term, coefficient in base.multiply_monomial(q[qj], exponent, -1):
                        base.add_value(
                            row,
                            positions[(qi, k_pole, tuple(levels_j), term)],
                            coefficient,
                        )
                    yield row


def main():
    point = words.REFERENCE_POINT
    pres = words.presentation(point)
    labels = list(domain_labels())
    positions = {label: index for index, label in enumerate(labels)}

    derivative_pivots = {}
    derivative_rows = []
    derivative_nonzero = 0
    derivative_count = 0
    for row in moving.iter_derived_q_relations(pres, point, 0):
        derivative_rows.append(row)
        derivative_count += 1
        if row:
            derivative_nonzero += 1
            base.add_pivot(dict(row), derivative_pivots)

    syzygy_pivots = {}
    syzygy_count = 0
    composition_failures = 0
    first_composition_failure_support = None
    for row in syzygy_rows(pres, positions):
        syzygy_count += 1
        image = {}
        for generator, coefficient in row.items():
            for column, value in derivative_rows[generator].items():
                base.add_value(image, column, coefficient * value)
        image = base.reduce_row(image, pres["pivots"])
        if image:
            composition_failures += 1
            if first_composition_failure_support is None:
                first_composition_failure_support = len(image)
        base.add_pivot(dict(row), syzygy_pivots)

    domain_dimension = len(labels)
    derivative_rank = len(derivative_pivots)
    kernel_dimension = domain_dimension - derivative_rank
    syzygy_rank = len(syzygy_pivots)
    checks = {
        "domain_has_complete_25200_labels": domain_dimension == 25200,
        "all_derivative_generators_processed": derivative_count == domain_dimension,
        "all_21840_syzygies_processed": syzygy_count == 21840,
        "differentiated_relation_composed_with_syzygy_is_zero": composition_failures == 0,
        "first_syzygy_rank_equals_derivative_kernel_dimension": syzygy_rank == kernel_dimension,
    }
    result = {
        "schema": "marici.rank26-first-syzygy-exactness.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "point": list(point),
        "derivative_axis": 0,
        "domain_dimension": domain_dimension,
        "derivative_nonzero_rows": derivative_nonzero,
        "derivative_rank": derivative_rank,
        "derivative_kernel_dimension": kernel_dimension,
        "first_syzygy_generator_count": syzygy_count,
        "first_syzygy_rank": syzygy_rank,
        "composition_failures": composition_failures,
        "first_composition_failure_support": first_composition_failure_support,
        "homology_dimension": kernel_dimension - syzygy_rank,
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-first-syzygy-exactness.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

"""Census true covariant source jets in the minimal four-face adapter."""

from __future__ import annotations

import contextlib
import importlib
import io
import json
import os
from pathlib import Path

import check_cutoff_inclusion_gauss_manin_adapter as adapter
import check_true_covariant_source_jet_closure as jets


with contextlib.redirect_stdout(io.StringIO()):
    source = importlib.import_module("check_rank26_total_energy_source_word_rees")

P = source.P
DEPTH = int(os.environ.get("MARICI_JET_DEPTH", "5"))
SOURCE_AMBIENT = int(os.environ.get("MARICI_SOURCE_AMBIENT", "8"))
TARGET_STEP = int(os.environ.get("MARICI_TARGET_STEP", "4"))
TARGET_AMBIENT = SOURCE_AMBIENT + TARGET_STEP
ZERO = (0, 0, 0)


def row_add(target, column, value):
    target[column] = jets.jadd(target.get(column, {}), value)
    if not target[column]:
        target.pop(column)


def raw_connection(row, axis, ordered, columns, k, q, k_depth, q_depths):
    kd = {exponent: jets.jderivative(value, axis) for exponent, value in k.items()}
    qd = {
        name: {exponent: jets.jderivative(value, axis) for exponent, value in poly.items()}
        for name, poly in q.items()
    }
    result = {}
    for column, coefficient in row.items():
        k_pole, *rest = ordered[column]
        exponent = rest.pop()
        levels = rest
        if k_pole < k_depth:
            for term, value in kd.items():
                target = (k_pole + 1, *levels, source.rees.base.shifted(exponent, term))
                if target in columns:
                    row_add(
                        result,
                        columns[target],
                        jets.jscale(jets.jmul(coefficient, value), source.rees.charts.GAMMA - k_pole),
                    )
        for qi, level in enumerate(levels):
            if level >= q_depths[qi]:
                continue
            raised = list(levels)
            raised[qi] += 1
            for term, value in qd[source.rees.NAMES[qi]].items():
                target = (k_pole, *raised, source.rees.base.shifted(exponent, term))
                if target in columns:
                    row_add(result, columns[target], jets.jscale(jets.jmul(coefficient, value), -level))
    return result


def covariant(row, axis, ordered, columns, k, q, k_depth, q_depths):
    result = {
        column: derivative
        for column, value in row.items()
        if (derivative := jets.jderivative(value, axis))
    }
    for column, value in raw_connection(row, axis, ordered, columns, k, q, k_depth, q_depths).items():
        row_add(result, column, value)
    return result


def main():
    point = tuple(int(value) for value in os.environ.get("MARICI_JET_POINT", "2,3,-4").split(","))
    source_k_depth = source.rees.charts.K_DEPTH
    source_q_depth = source.rees.charts.Q_DEPTH
    target_k_depth = source_k_depth + 1
    target_q_depths = [source_q_depth + 1] * 3 + [source_q_depth] * 2

    _, columns = adapter.packet(TARGET_AMBIENT, target_k_depth, target_q_depths)
    ordered = [None] * len(columns)
    for label, column in columns.items():
        ordered[column] = label

    relation_rows = adapter.relations(point, columns, TARGET_AMBIENT, target_k_depth, target_q_depths)
    pivots = {}
    for row in relation_rows:
        source.rees.base.add_pivot(dict(row), pivots)

    k, q = jets.fiber_data(point)
    numeric_k, numeric_q = source.rees.base.fiber_data(*point)
    assert jets.polynomial_center(k) == numeric_k
    assert all(jets.polynomial_center(q[name]) == numeric_q[name] for name in source.rees.NAMES)

    roots = [jets.raw_source(columns, q)]
    span = {}
    ranks = []
    exact_depth_ranks = []
    word_counts = []
    frontier = roots
    for depth in range(DEPTH + 1):
        depth_span = {}
        for row in frontier:
            quotient = source.rees.base.reduce_row(jets.center(row), pivots)
            source.rees.base.add_pivot(dict(quotient), depth_span)
            source.rees.base.add_pivot(dict(quotient), span)
        ranks.append(len(span))
        exact_depth_ranks.append(len(depth_span))
        word_counts.append(len(frontier))
        if depth < DEPTH:
            frontier = [
                covariant(row, axis, ordered, columns, k, q, target_k_depth, target_q_depths)
                for row in frontier
                for axis in range(3)
            ]

    result = {
        "schema": "marici.benincasa.adapted-true-covariant-source-jets.v1",
        "field": P,
        "point": list(point),
        "source_ambient": SOURCE_AMBIENT,
        "target_ambient": TARGET_AMBIENT,
        "target_K_depth": target_k_depth,
        "target_q_depths": dict(zip(source.rees.NAMES, target_q_depths, strict=True)),
        "target_column_count": len(columns),
        "target_relation_count": len(relation_rows),
        "target_relation_rank": len(pivots),
        "maximum_jet_depth": DEPTH,
        "words_per_exact_depth": word_counts,
        "exact_depth_quotient_ranks": exact_depth_ranks,
        "cumulative_covariant_ranks": ranks,
        "convention": "all 3^d true covariant words retained; minimal four-face target; no dependent intermediate word pruned",
    }
    suffix = "-".join(f"m{-value}" if value < 0 else str(value) for value in point)
    output = Path(__file__).with_name(
        f"adapted-true-covariant-source-jets-d{DEPTH}-a{SOURCE_AMBIENT}-to-a{TARGET_AMBIENT}-p{P}-point-{suffix}.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

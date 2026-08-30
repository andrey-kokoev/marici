#!/usr/bin/env python3
"""Test whether differentiated raw relation families absorb the Euler defect."""

import contextlib
import importlib
import inspect
import io
import json
from itertools import product
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank26_differentiated_euler_quotient")

words = audit.words
base = words.base
charts = words.charts
P = base.PRIME


def capture_relations(point):
    captured = {"ibp": [], "K_multiplication": [], "q_multiplication": []}
    original = base.add_pivot
    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF

    def capture(row, _pivots):
        line = inspect.currentframe().f_back.f_lineno
        family = {109: "ibp", 117: "K_multiplication", 130: "q_multiplication"}.get(line)
        if family is not None and row:
            captured[family].append(dict(row))

    base.add_pivot = capture
    charts.AMBIENT, charts.CUTOFF = words.AMBIENT, words.CUTOFF
    try:
        charts.presentation(base.fiber_data, point, charts.SOURCE_NAMES)
    finally:
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff
        base.add_pivot = original
    return captured


def derived_relation(row_samples, central_row, pres, axis, point=None):
    point = words.REFERENCE_POINT if point is None else point
    result = {}
    for sample, weight in zip(row_samples, audit.WEIGHTS):
        for column, coefficient in sample.items():
            base.add_value(result, column, weight * coefficient)
    connection = words.raw_connection(pres, point, central_row, axis)
    for column, coefficient in connection.items():
        base.add_value(result, column, coefficient)
    return base.reduce_row(result, pres["pivots"])


def euler_defect(pres, axis, point=None):
    point = words.REFERENCE_POINT if point is None else point
    roots = dict(words.root_rows(pres, point))
    defect = {}
    for source_axis, coordinate in enumerate(point):
        second = audit.covariant_second_derivative(pres, point, source_axis, axis)
        for column, coefficient in second.items():
            base.add_value(defect, column, coordinate * coefficient)
    for column, coefficient in roots[f"D{axis}"].items():
        base.add_value(defect, column, -27 * coefficient)
    return base.reduce_row(defect, pres["pivots"])


def q_polynomial_derivative(point, qi, axis):
    result = {}
    for offset, weight in zip(audit.NODES, audit.WEIGHTS):
        shifted = list(point)
        shifted[axis] += offset
        _, q = base.fiber_data(*shifted)
        polynomial = q[charts.SOURCE_NAMES[qi]]
        for exponent, coefficient in polynomial.items():
            base.add_value(result, exponent, weight * coefficient)
    return result


def iter_derived_q_relations(pres, point, axis):
    """Yield the complete aligned derivative of the labelled q-relation map."""
    columns = pres["columns"]
    q_polynomials = [pres["q"][name] for name in charts.SOURCE_NAMES]
    q_derivatives = [
        q_polynomial_derivative(point, qi, axis)
        for qi in range(len(charts.SOURCE_NAMES))
    ]
    q_count = len(charts.SOURCE_NAMES)
    for qi, (qpoly, q_derivative) in enumerate(zip(q_polynomials, q_derivatives)):
        for k_pole in range(charts.K_DEPTH + 1):
            for levels in product(range(1, charts.Q_DEPTH + 1), repeat=q_count):
                if levels[qi] == charts.Q_DEPTH:
                    continue
                raised = list(levels)
                raised[qi] += 1
                for exponent in base.monomials_at_most(words.AMBIENT - 1):
                    central = {columns[(k_pole, *levels, exponent)]: 1}
                    for term, coefficient in base.multiply_monomial(qpoly, exponent, -1):
                        base.add_value(
                            central,
                            columns[(k_pole, *raised, term)],
                            coefficient,
                        )
                    result = {}
                    for term, coefficient in base.multiply_monomial(
                        q_derivative, exponent, -1
                    ):
                        base.add_value(
                            result,
                            columns[(k_pole, *raised, term)],
                            coefficient,
                        )
                    connection = words.raw_connection(pres, point, central, axis)
                    for column, coefficient in connection.items():
                        base.add_value(result, column, coefficient)
                    yield base.reduce_row(result, pres["pivots"])


def k_polynomial_derivative(point, axis):
    result = {}
    for offset, weight in zip(audit.NODES, audit.WEIGHTS):
        shifted = list(point)
        shifted[axis] += offset
        polynomial, _ = base.fiber_data(*shifted)
        for exponent, coefficient in polynomial.items():
            base.add_value(result, exponent, weight * coefficient)
    return result


def iter_derived_k_relations(pres, point, axis):
    """Yield the aligned derivative of the Cayley--Menger relation map."""
    columns = pres["columns"]
    kpoly = pres["k"]
    k_derivative = k_polynomial_derivative(point, axis)
    q_count = len(charts.SOURCE_NAMES)
    for k_pole in range(charts.K_DEPTH):
        for levels in product(range(1, charts.Q_DEPTH + 1), repeat=q_count):
            for exponent in base.monomials_at_most(words.AMBIENT - 4):
                central = {columns[(k_pole, *levels, exponent)]: 1}
                for term, coefficient in base.multiply_monomial(kpoly, exponent, -1):
                    base.add_value(
                        central,
                        columns[(k_pole + 1, *levels, term)],
                        coefficient,
                    )
                result = {}
                for term, coefficient in base.multiply_monomial(
                    k_derivative, exponent, -1
                ):
                    base.add_value(
                        result,
                        columns[(k_pole + 1, *levels, term)],
                        coefficient,
                    )
                connection = words.raw_connection(pres, point, central, axis)
                for column, coefficient in connection.items():
                    base.add_value(result, column, coefficient)
                yield base.reduce_row(result, pres["pivots"])


def main():
    pres = words.presentation(words.REFERENCE_POINT)
    samples = []
    for offset in audit.NODES:
        shifted = list(words.REFERENCE_POINT)
        shifted[0] += offset
        samples.append(capture_relations(tuple(shifted)))

    family_counts = {family: len(samples[0][family]) for family in samples[0]}
    assert all(
        len(sample[family]) == count
        for family, count in family_counts.items()
        for sample in samples
    )

    defect = euler_defect(pres, 0)
    family_spans = {family: {} for family in family_counts}
    total_span = {}
    derived_nonzero = {}
    processed_counts = {}
    for family, count in family_counts.items():
        nonzero = 0
        processed = 0
        for index in range(count):
            processed += 1
            rows = [sample[family][index] for sample in samples]
            derived = derived_relation(rows, samples[3][family][index], pres, 0)
            if not derived:
                continue
            nonzero += 1
            base.add_pivot(dict(derived), family_spans[family])
            base.add_pivot(dict(derived), total_span)
            if not base.reduce_row(defect, family_spans[family]):
                break
        derived_nonzero[family] = nonzero
        processed_counts[family] = processed

    by_family = {
        family: len(base.reduce_row(defect, span)) for family, span in family_spans.items()
    }
    total_residual = base.reduce_row(defect, total_span)
    checks = {
        "all_relation_families_captured": all(family_counts.values()),
        "derived_relation_span_is_nonzero": bool(total_span),
        "total_derived_relation_span_contains_euler_defect": not total_residual,
    }
    result = {
        "schema": "marici.rank26-moving-relation-coherence.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "point": list(words.REFERENCE_POINT),
        "derivative_axis": 0,
        "relation_generator_counts": family_counts,
        "nonzero_derived_relation_counts": derived_nonzero,
        "processed_generator_counts": processed_counts,
        "early_stop_rule": "stop a family only after its derived span contains the frozen Euler defect",
        "derived_span_ranks": {family: len(span) for family, span in family_spans.items()},
        "total_derived_span_rank": len(total_span),
        "euler_defect_support": len(defect),
        "residual_support_by_single_family": by_family,
        "total_residual_support": len(total_residual),
        "checks": checks,
    }
    output = Path(__file__).with_name("rank26-moving-relation-coherence.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Verify the differentiated Euler identity in the finite de Rham quotient."""

import contextlib
import importlib
import io
import json
import os
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    words = importlib.import_module("derive_rank26_source_word_basis")

P = words.base.PRIME
NODES = tuple(range(-3, 4))


def derivative_weights():
    weights = []
    for node in NODES:
        polynomial = [1]
        denominator = 1
        for other in NODES:
            if other == node:
                continue
            following = [0] * (len(polynomial) + 1)
            for degree, coefficient in enumerate(polynomial):
                following[degree] = (following[degree] - other * coefficient) % P
                following[degree + 1] = (following[degree + 1] + coefficient) % P
            polynomial = following
            denominator = denominator * (node - other) % P
        weights.append(polynomial[1] * pow(denominator, -1, P) % P)
    return tuple(weights)


WEIGHTS = derivative_weights()


def defect_histogram(row, pres):
    by_k_depth = {}
    by_pole_pattern = {}
    by_numerator_degree = {}
    labels = []
    for column in sorted(row):
        label = pres["ordered_columns"][column]
        k_depth = label[0]
        pole_pattern = tuple(label[1:-1])
        numerator_degree = sum(label[-1])
        by_k_depth[str(k_depth)] = by_k_depth.get(str(k_depth), 0) + 1
        pole_key = ",".join(map(str, pole_pattern))
        by_pole_pattern[pole_key] = by_pole_pattern.get(pole_key, 0) + 1
        by_numerator_degree[str(numerator_degree)] = by_numerator_degree.get(str(numerator_degree), 0) + 1
        labels.append(
            {
                "k_depth": k_depth,
                "pole_levels": list(pole_pattern),
                "numerator_exponent": list(label[-1]),
                "coefficient": row[column],
            }
        )
    return {
        "by_k_depth": by_k_depth,
        "by_pole_pattern": by_pole_pattern,
        "by_numerator_degree": by_numerator_degree,
        "labels": labels,
    }


def coefficient_derivative(pres, point, root_name, axis):
    result = {}
    for offset, weight in zip(NODES, WEIGHTS):
        shifted = list(point)
        shifted[axis] += offset
        root = dict(words.root_rows(pres, tuple(shifted)))[root_name]
        for column, coefficient in root.items():
            words.base.add_value(result, column, weight * coefficient)
    return result


def covariant_second_derivative(pres, point, source_axis, derivative_axis):
    root_name = f"D{source_axis}"
    root = dict(words.root_rows(pres, point))[root_name]
    result = coefficient_derivative(pres, point, root_name, derivative_axis)
    connection = words.raw_connection(pres, point, root, derivative_axis)
    for column, coefficient in connection.items():
        words.base.add_value(result, column, coefficient)
    return result


def run(point):
    pres = words.presentation(point)
    roots = dict(words.root_rows(pres, point))
    directions = []
    for derivative_axis in range(3):
        lhs = {}
        for source_axis, coordinate in enumerate(point):
            second = covariant_second_derivative(pres, point, source_axis, derivative_axis)
            for column, coefficient in second.items():
                words.base.add_value(lhs, column, coordinate * coefficient)
        defect = dict(lhs)
        for column, coefficient in roots[f"D{derivative_axis}"].items():
            words.base.add_value(defect, column, -27 * coefficient)
        lhs_reduced = words.base.reduce_row(lhs, pres["pivots"])
        derivative_reduced = words.base.reduce_row(roots[f"D{derivative_axis}"], pres["pivots"])
        reduced = words.base.reduce_row(defect, pres["pivots"])
        common = sorted(set(lhs_reduced).intersection(derivative_reduced))
        scalar = None
        scalar_residual = None
        if common:
            pivot = common[0]
            scalar = lhs_reduced[pivot] * pow(derivative_reduced[pivot], -1, P) % P
            candidate = dict(lhs_reduced)
            for column, coefficient in derivative_reduced.items():
                words.base.add_value(candidate, column, -scalar * coefficient)
            scalar_residual = len(candidate)
        directions.append(
            {
                "derivative_axis": derivative_axis,
                "raw_defect_support": len(defect),
                "reduced_defect_support": len(reduced),
                "identity_holds": not reduced,
                "lhs_is_scalar_multiple_of_Dj": scalar_residual == 0,
                "lhs_scalar_mod_prime": scalar,
                "scalar_residual_support": scalar_residual,
                "reduced_defect_histogram": defect_histogram(reduced, pres),
            }
        )
    return {"point": list(point), "directions": directions}


def main():
    ambient = int(os.environ.get("MARICI_AMBIENT", words.AMBIENT))
    words.AMBIENT = ambient
    points = (words.REFERENCE_POINT,) + (() if os.environ.get("MARICI_REFERENCE_ONLY") else words.CONTROL_POINTS)
    runs = [run(point) for point in points]
    checks = {
        "seven_node_derivative_is_declared": len(NODES) == 7,
        "all_requested_points_tested": len(runs) == len(points),
        "all_differentiated_identities_hold": all(
            direction["identity_holds"] for run in runs for direction in run["directions"]
        ),
    }
    result = {
        "schema": "marici.rank26-differentiated-euler-quotient.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "field": P,
        "ambient_relation_degree": ambient,
        "derivative_nodes": list(NODES),
        "derivative_weights": list(WEIGHTS),
        "identity": "x nabla_j D0 + y nabla_j D1 + z nabla_j D2 = 27 D_j",
        "runs": runs,
        "checks": checks,
        "typing": (
            "Each second derivative contains both the exact coefficient derivative of the parameter-dependent raw D_i row "
            "and the Gauss-Manin connection image before quotient reduction."
        ),
    }
    suffix = f"ambient-{ambient}" + ("-reference" if len(points) == 1 else "-three-points")
    output = Path(__file__).with_name(f"rank26-differentiated-euler-quotient-{suffix}.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

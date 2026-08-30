#!/usr/bin/env python3
"""Certify the primitive integral source presentation behind the barcode.

This checker deliberately stops before quotient reduction.  It constructs the
labelled depth-three de Rham/product-pole relations over Q.  The legacy mode
clears each specialized row and divides by its numerical content.  The
structural-lattice mode instead clears every de Rham row by the source-fixed
Kummer denominator 2 and retains multiplication-source units, so the resulting
integral presentation commutes with external specialization.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research" / "benincasa" / "results" / "interaction-net-integral-source-presentation.json"
PRIMES = (31991, 32003, 32009)
POINT = (2, 3, 4)
K_DEPTH = 3
Q_DEPTH = 2
AMBIENT = 14
LOW_CUTOFF = 7
GAMMA = Fraction(-1, 2)
NAMES = ("g1", "g2", "g3", "g23", "g31")


def monomials_at_most(degree: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(degree + 1) for j in range(degree + 1 - i)]


def shifted(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def derivative(poly: dict[tuple[int, int], int], axis: int) -> dict[tuple[int, int], int]:
    out: dict[tuple[int, int], int] = {}
    for exponent, coefficient in poly.items():
        power = exponent[axis]
        if power:
            target = list(exponent)
            target[axis] -= 1
            out[tuple(target)] = coefficient * power
    return out


def exact_fiber_data(point: tuple[int, int, int]) -> tuple[dict[tuple[int, int], int], dict[str, dict[tuple[int, int], int]]]:
    # Exact evaluation of the source-derived q_G12 residue formulas.  These
    # are the degree pieces F+G_a a^2+G_b b^2+H from
    # check_marked_relative_q.rs, evaluated without a CAS.
    x, y, z = point
    e = x + y + z
    x2, y2, z2, e2 = x*x, y*y, z*z, e*e
    h = x2 + y2 - z2
    g_a = h * (x2 + e2) - 2 * x2 * (y2 + e2)
    g_b = h * (y2 + e2) - 2 * y2 * (x2 + e2)
    h0 = z2 * ((e2 - y2) * (e2 - x2) + e2 * z2)
    k = {
        (4, 0): x2,
        (2, 2): -h,
        (0, 4): y2,
        (2, 0): g_a,
        (0, 2): g_b,
        (0, 0): h0,
    }
    q = {
        "g1": {(0, 1): 1, (0, 0): -(y + z)},
        "g2": {(1, 0): 1, (0, 0): -(x + z)},
        "g3": {(1, 0): 1, (0, 1): 1, (0, 0): z},
        "g23": {(0, 1): 1, (0, 0): -x},
        "g31": {(1, 0): 1, (0, 0): -y},
    }
    return k, q


def primitive(
    row: dict[tuple, Fraction],
    structural_denominator: int | None = None,
) -> dict[tuple, int]:
    row = {label: value for label, value in row.items() if value}
    denominator = structural_denominator or math.lcm(
        *(value.denominator for value in row.values())
    )
    integer = {label: int(value * denominator) for label, value in row.items()}
    if structural_denominator is None:
        content = math.gcd(*(abs(value) for value in integer.values()))
        integer = {label: value // content for label, value in integer.items()}
    first = min(integer)
    if integer[first] < 0:
        integer = {label: -value for label, value in integer.items()}
    return integer


def add(row: dict[tuple, Fraction], label: tuple, value: Fraction | int) -> None:
    row[label] = row.get(label, Fraction(0)) + value
    if not row[label]:
        del row[label]


def canonical_row(row: dict[tuple, int]) -> str:
    entries = [[list(label[:-1]) + [list(label[-1])], value] for label, value in sorted(row.items())]
    return json.dumps(entries, separators=(",", ":"))


def main() -> None:
    point = next(
        (
            tuple(int(value) for value in argument.split("=", 1)[1].split(","))
            for argument in sys.argv[1:] if argument.startswith("--point=")
        ),
        POINT,
    )
    if len(point) != 3:
        raise ValueError("--point requires x,y,z")
    selected_rank_primes = tuple(
        int(argument.split("=", 1)[1])
        for argument in sys.argv[1:] if argument.startswith("--rank-prime=")
    )
    structural_lattice = "--structural-lattice" in sys.argv[1:]
    residual_export = next(
        (
            Path(argument.split("=", 1)[1])
            for argument in sys.argv[1:] if argument.startswith("--export-residual=")
        ),
        None,
    )
    free_labels_export = next(
        (
            Path(argument.split("=", 1)[1])
            for argument in sys.argv[1:] if argument.startswith("--export-free-labels=")
        ),
        None,
    )
    k, q = exact_fiber_data(point)
    kd = [derivative(k, axis) for axis in range(2)]
    qd = {name: [derivative(poly, axis) for axis in range(2)] for name, poly in q.items()}
    rows: list[tuple[str, tuple[int, tuple[int, ...]], dict[tuple, int]]] = []

    # Exact de Rham rows.  The physical Kummer twist is the only denominator;
    # primitive() clears it without choosing a finite-field normalization.
    for k_pole in range(K_DEPTH):
        for levels in product(range(1, Q_DEPTH + 1), repeat=len(NAMES)):
            if any(level == Q_DEPTH for level in levels):
                continue
            for axis in range(2):
                for exponent in monomials_at_most(AMBIENT):
                    row: dict[tuple, Fraction] = {}
                    if exponent[axis]:
                        target = list(exponent)
                        target[axis] -= 1
                        add(row, (k_pole, *levels, tuple(target)), exponent[axis])
                    for term, coefficient in kd[axis].items():
                        add(row, (k_pole + 1, *levels, shifted(exponent, term)),
                            (GAMMA - k_pole) * coefficient)
                    for qi, name in enumerate(NAMES):
                        raised = list(levels)
                        raised[qi] += 1
                        for term, coefficient in qd[name][axis].items():
                            add(row, (k_pole, *raised, shifted(exponent, term)),
                                -levels[qi] * coefficient)
                    rows.append((
                        "de_rham",
                        (k_pole, tuple(levels)),
                        primitive(row, structural_denominator=2 if structural_lattice else None),
                    ))

    # Multiplication by K.
    for k_pole in range(K_DEPTH):
        for levels in product(range(1, Q_DEPTH + 1), repeat=len(NAMES)):
            for exponent in monomials_at_most(AMBIENT - 4):
                row = {(k_pole, *levels, exponent): Fraction(1)}
                for term, coefficient in k.items():
                    add(row, (k_pole + 1, *levels, shifted(exponent, term)), -coefficient)
                rows.append(("k_multiplication", (k_pole, tuple(levels)), primitive(row)))

    # Multiplication by every labelled denominator.
    for qi, name in enumerate(NAMES):
        for k_pole in range(K_DEPTH + 1):
            for levels in product(range(1, Q_DEPTH + 1), repeat=len(NAMES)):
                if levels[qi] == Q_DEPTH:
                    continue
                raised = list(levels)
                raised[qi] += 1
                for exponent in monomials_at_most(AMBIENT - 1):
                    row = {(k_pole, *levels, exponent): Fraction(1)}
                    for term, coefficient in q[name].items():
                        add(row, (k_pole, *raised, shifted(exponent, term)), -coefficient)
                    rows.append((f"q_multiplication:{name}", (k_pole, tuple(levels)), primitive(row)))

    counts: dict[str, int] = {}
    max_abs = 0
    max_width = 0
    digest = hashlib.sha256()
    parent: dict[tuple, tuple] = {}

    def find(label: tuple) -> tuple:
        parent.setdefault(label, label)
        while parent[label] != label:
            parent[label] = parent[parent[label]]
            label = parent[label]
        return label

    def union(left: tuple, right: tuple) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            if right_root < left_root:
                left_root, right_root = right_root, left_root
            parent[right_root] = left_root

    filtration_edges: set[tuple[tuple[int, tuple[int, ...]], tuple[int, tuple[int, ...]]]] = set()
    filtration_violations = []
    domain_block_counts: dict[str, int] = {}
    coordinate_blocks: set[tuple[int, tuple[int, ...]]] = set()
    associated_grade_widths: list[int] = []
    associated_grade_coefficients: dict[tuple, list[int]] = {}
    unit_rewrite_rows: dict[tuple, tuple[int, dict[tuple, int]]] = {}
    for kind, domain_block, row in rows:
        counts[kind] = counts.get(kind, 0) + 1
        domain_key = json.dumps([domain_block[0], list(domain_block[1])], separators=(",", ":"))
        domain_block_counts[domain_key] = domain_block_counts.get(domain_key, 0) + 1
        max_abs = max(max_abs, *(abs(value) for value in row.values()))
        max_width = max(max_width, len(row))
        digest.update(kind.encode())
        digest.update(b":")
        digest.update(canonical_row(row).encode())
        digest.update(b"\n")
        labels = sorted(row)
        source_k, source_levels = domain_block
        for label in labels:
            target_block = (label[0], tuple(label[1:1 + len(NAMES)]))
            coordinate_blocks.add(target_block)
            filtration_edges.add((domain_block, target_block))
            if target_block[0] < source_k or any(
                target < source for source, target in zip(source_levels, target_block[1])
            ):
                filtration_violations.append({
                    "kind": kind,
                    "domain": [source_k, list(source_levels)],
                    "target": [target_block[0], list(target_block[1])],
                })
        diagonal = {
            label: value for label, value in row.items()
            if (label[0], tuple(label[1:1 + len(NAMES)])) == domain_block
        }
        associated_grade_widths.append(len(diagonal))
        for label, value in diagonal.items():
            associated_grade_coefficients.setdefault(label, []).append(value)
            if abs(value) == 1 and label not in unit_rewrite_rows:
                unit_rewrite_rows[label] = (len(associated_grade_widths) - 1, {
                    target: -value * coefficient
                    for target, coefficient in row.items() if target != label
                })
        for label in labels:
            find(label)
        for label in labels[1:]:
            union(labels[0], label)

    component_sizes: dict[tuple, int] = {}
    for label in parent:
        root = find(label)
        component_sizes[root] = component_sizes.get(root, 0) + 1
    sorted_component_sizes = sorted(component_sizes.values(), reverse=True)
    associated_grade_gcd = {
        label: math.gcd(*(abs(value) for value in values))
        for label, values in associated_grade_coefficients.items()
    }
    torsion_histogram: dict[str, int] = {}
    for value in associated_grade_gcd.values():
        if value > 1:
            torsion_histogram[str(value)] = torsion_histogram.get(str(value), 0) + 1
    associated_unconstrained = len(parent) - len(associated_grade_gcd)

    # Unit associated-grade pivots define an integral triangular rewrite
    # system.  Reduce every label and every unused relation to the free grade
    # coordinates without division.
    def height(label: tuple) -> tuple:
        levels = tuple(label[1:1 + len(NAMES)])
        return (label[0] + sum(level - 1 for level in levels), label[0], levels, label[-1])

    normal_forms: dict[tuple, dict[tuple, int]] = {}
    for label in sorted(parent, key=height, reverse=True):
        if label not in unit_rewrite_rows:
            normal_forms[label] = {label: 1}
            continue
        _, rewrite = unit_rewrite_rows[label]
        normal: dict[tuple, int] = {}
        for target, coefficient in rewrite.items():
            if target not in normal_forms:
                raise AssertionError(("nontriangular rewrite", label, target))
            for free_label, free_coefficient in normal_forms[target].items():
                value = normal.get(free_label, 0) + coefficient * free_coefficient
                if value:
                    normal[free_label] = value
                else:
                    normal.pop(free_label, None)
        normal_forms[label] = normal

    selected_rows = {index for index, _ in unit_rewrite_rows.values()}
    residual_rows: list[dict[tuple, int]] = []
    for index, (_, _, row) in enumerate(rows):
        if index in selected_rows:
            continue
        residual: dict[tuple, int] = {}
        for label, coefficient in row.items():
            for free_label, free_coefficient in normal_forms[label].items():
                value = residual.get(free_label, 0) + coefficient * free_coefficient
                if value:
                    residual[free_label] = value
                else:
                    residual.pop(free_label, None)
        if residual:
            residual_rows.append(residual)
    residual_contents = [
        math.gcd(*(abs(value) for value in row.values())) for row in residual_rows
    ]

    residual_export_sha256 = None
    free_labels = sorted(label for label in parent if label not in unit_rewrite_rows)
    if free_labels_export is not None:
        free_labels_export.parent.mkdir(parents=True, exist_ok=True)
        free_labels_export.write_text(
            json.dumps({
                "schema": "marici.integral-residual-free-labels.v1",
                "labels": [list(label[:-1]) + [list(label[-1])] for label in free_labels],
            }, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
    if residual_export is not None:
        free_index = {label: index for index, label in enumerate(free_labels)}
        export_digest = hashlib.sha256()
        residual_export.parent.mkdir(parents=True, exist_ok=True)
        with residual_export.open("w", encoding="utf-8", newline="\n") as stream:
            header = json.dumps({
                "schema": "marici.sparse-integer-matrix.v1",
                "rows": len(residual_rows),
                "columns": len(free_labels),
                "source_presentation_sha256": digest.hexdigest(),
            }, separators=(",", ":")) + "\n"
            stream.write(header)
            export_digest.update(header.encode())
            for row in residual_rows:
                line = ",".join(
                    f"{free_index[label]}:{value}" for label, value in sorted(row.items())
                ) + "\n"
                stream.write(line)
                export_digest.update(line.encode())
        residual_export_sha256 = export_digest.hexdigest()

    def modular_sparse_rank(matrix: list[dict[tuple, int]], prime: int) -> int:
        pivots: dict[tuple, dict[tuple, int]] = {}
        for source in matrix:
            row = {label: value % prime for label, value in source.items() if value % prime}
            while row:
                pivot = min(row)
                if pivot not in pivots:
                    inverse = pow(row[pivot], -1, prime)
                    pivots[pivot] = {
                        label: value * inverse % prime for label, value in row.items()
                    }
                    break
                factor = row[pivot]
                for label, value in pivots[pivot].items():
                    reduced = (row.get(label, 0) - factor * value) % prime
                    if reduced:
                        row[label] = reduced
                    else:
                        row.pop(label, None)
        return len(pivots)

    residual_prime_ranks = {
        str(prime): modular_sparse_rank(residual_rows, prime) for prime in selected_rank_primes
    }

    prime_checks = {}
    for prime in PRIMES:
        zero_rows = sum(all(value % prime == 0 for value in row.values()) for _, _, row in rows)
        changed_support = sum(
            sum(value % prime != 0 for value in row.values()) != len(row) for _, _, row in rows
        )
        prime_checks[str(prime)] = {
            "zero_rows": zero_rows,
            "rows_with_support_loss": changed_support,
            "support_faithful": zero_rows == 0 and changed_support == 0,
        }

    payload = {
        "schema": "marici.interaction-net-integral-source-presentation.v1",
        "status": "pass" if all(item["support_faithful"] for item in prime_checks.values()) else "fail",
        "conventions": {
            "chart": "G12",
            "external_point": list(point),
            "physical_twist": "-1/2",
            "k_depth": K_DEPTH,
            "q_depth": Q_DEPTH,
            "ambient_degree": AMBIENT,
            "normalization": (
                "fixed denominator 2 on every de Rham row; multiplication rows retain their source unit"
                if structural_lattice else
                "clear each rational row denominator, divide by specialized integer content, orient by first labelled coefficient"
            ),
            "scope": "raw labelled source relations before quotient reduction or pivot selection",
        },
        "relation_counts": counts,
        "total_relation_rows": len(rows),
        "maximum_row_width": max_width,
        "maximum_absolute_coefficient": max_abs,
        "label_count": len(parent),
        "relation_graph_component_count": len(sorted_component_sizes),
        "largest_relation_graph_components": sorted_component_sizes[:20],
        "source_filtration": {
            "poset": "C4_K_depth times B5_labelled_denominator_depth",
            "domain_block_count": len(domain_block_counts),
            "coordinate_block_count": len(coordinate_blocks),
            "block_edge_count": len(filtration_edges),
            "nondecreasing": not filtration_violations,
            "violation_count": len(filtration_violations),
            "largest_domain_row_blocks": sorted(domain_block_counts.values(), reverse=True)[:20],
        },
        "associated_grade": {
            "maximum_row_width": max(associated_grade_widths),
            "coordinatewise": max(associated_grade_widths) <= 1,
            "unit_constrained_coordinate_count": sum(value == 1 for value in associated_grade_gcd.values()),
            "torsion_coordinate_count": sum(value > 1 for value in associated_grade_gcd.values()),
            "unconstrained_coordinate_count": associated_unconstrained,
            "torsion_invariant_histogram": torsion_histogram,
        },
        "integral_extension_reduction": {
            "unit_rewrite_count": len(unit_rewrite_rows),
            "free_coordinate_count": sum(label not in unit_rewrite_rows for label in parent),
            "unused_relation_count": len(rows) - len(selected_rows),
            "nonzero_residual_relation_count": len(residual_rows),
            "maximum_residual_width": max((len(row) for row in residual_rows), default=0),
            "maximum_residual_coefficient": max(
                (abs(value) for row in residual_rows for value in row.values()), default=0
            ),
            "nonprimitive_residual_count": sum(content > 1 for content in residual_contents),
            "all_extensions_absorbed_by_unit_rewrites": not residual_rows,
            "residual_good_prime_ranks": residual_prime_ranks,
            "good_prime_quotient_dimensions": {
                prime: associated_unconstrained - rank
                for prime, rank in residual_prime_ranks.items()
            },
            "rank_workflow": (
                "explicit_prime_slice" if selected_rank_primes
                else "not_run_use_compiled_sparse_engine"
            ),
            "residual_export": (
                {
                    "path": str(residual_export),
                    "sha256": residual_export_sha256,
                }
                if residual_export is not None else None
            ),
        },
        "primitive_integer_presentation_sha256": digest.hexdigest(),
        "prime_reduction_checks": prime_checks,
        "conclusion": (
            "The three barcode fields are reductions of one source-normalized primitive integer relation presentation. "
            "Although its undirected relation graph is connected, the source differential is filtered by the product of "
            "K-pole depth and five labelled denominator-depth bits. Characteristic-zero barcode data must therefore be "
            "derived from saturated filtered subquotients, not by lifting finite-field RREF rows."
        ),
    }
    if filtration_violations:
        payload["status"] = "fail"
    if max(associated_grade_widths) > 1:
        payload["status"] = "fail"
    point_suffix = "" if point == POINT else "-point-" + "-".join(str(value) for value in point)
    output = OUT.with_name(OUT.stem + point_suffix + OUT.suffix)
    if selected_rank_primes:
        suffix = "-ranks-" + "-".join(str(prime) for prime in selected_rank_primes)
        output = OUT.with_name(OUT.stem + point_suffix + suffix + OUT.suffix)
    payload["rank_primes_computed"] = list(selected_rank_primes)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if payload["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

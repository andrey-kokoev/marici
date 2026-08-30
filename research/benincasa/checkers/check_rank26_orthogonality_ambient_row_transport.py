#!/usr/bin/env python3
"""Audit the fixed-G12 involution before quotient pivots are selected."""
from __future__ import annotations

import json
import os
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))

P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
os.environ["MARICI_FIELD_PRIME"] = str(P)

import physical_four_mark_residue_twisted_derham as base
import g12_g31_residue_chart_transition as transition

transition.PRIME = P
transition.AMBIENT = 18
transition.CUTOFF = 7
transition.K_DEPTH = 2
transition.Q_DEPTH = 2
transition.GAMMA = -pow(2, -1, P) % P

NAMES = ("g1", "g2", "g3", "g23", "g31")
SOURCE = (3, 4, 5)
TARGET = (4, 3, 5)


def bidual_scalar_presentation(point):
    """The scalar grade of the exact finite presentation used by the bidual reducer."""
    k, all_q = base.fiber_data(*point)
    qs = [all_q[name] for name in NAMES]
    low = [(0, *levels, monomial) for levels in product(range(1, 2), repeat=5) for monomial in base.monomials_at_most(7)]
    low_set = set(low)
    ordered = list(low)
    for k_pole in range(3):
        for levels in product(range(1, 3), repeat=5):
            ordered.extend(label for monomial in base.monomials_at_most(18) if (label := (k_pole, *levels, monomial)) not in low_set)
    columns = {label: index for index, label in enumerate(ordered)}
    pivots = {}
    gamma = -pow(2, -1, P) % P
    kd = [base.derivative(k, axis) for axis in range(2)]
    qd = [[base.derivative(q, axis) for axis in range(2)] for q in qs]
    for k_pole in range(2):
        for levels in product(range(1, 3), repeat=5):
            if 2 in levels:
                continue
            for axis in range(2):
                for exponent in base.monomials_at_most(14):
                    row = {}
                    if exponent[axis]:
                        derived = list(exponent); derived[axis] -= 1
                        base.add_value(row, columns[(k_pole, *levels, tuple(derived))], exponent[axis])
                    for term, coefficient in kd[axis].items():
                        base.add_value(row, columns[(k_pole + 1, *levels, base.shifted(exponent, term))], (gamma - k_pole) * coefficient)
                    for qi, pole in enumerate(levels):
                        raised = list(levels); raised[qi] += 1
                        for term, coefficient in qd[qi][axis].items():
                            base.add_value(row, columns[(k_pole, *raised, base.shifted(exponent, term))], -pole * coefficient)
                    base.add_pivot(row, pivots)
    for k_pole in range(2):
        for levels in product(range(1, 3), repeat=5):
            for exponent in base.monomials_at_most(10):
                row = {columns[(k_pole, *levels, exponent)]: 1}
                for term, coefficient in base.multiply_monomial(k, exponent, -1):
                    base.add_value(row, columns[(k_pole + 1, *levels, term)], coefficient)
                base.add_pivot(row, pivots)
    for qi, qpoly in enumerate(qs):
        for k_pole in range(3):
            for levels in product(range(1, 3), repeat=5):
                if levels[qi] == 2:
                    continue
                raised = list(levels); raised[qi] += 1
                for exponent in base.monomials_at_most(13):
                    row = {columns[(k_pole, *levels, exponent)]: 1}
                    for term, coefficient in base.multiply_monomial(qpoly, exponent, -1):
                        base.add_value(row, columns[(k_pole, *raised, term)], coefficient)
                    base.add_pivot(row, pivots)
    return {"k": k, "q": all_q, "low_labels": low, "ordered_columns": ordered, "columns": columns, "pivots": pivots, "free_low": [c for c in range(len(low)) if c not in pivots]}


def map_label(label):
    k_pole, l1, l2, l3, l23, l31, exponent = label
    i, j = exponent
    return (k_pole, l2, l1, l3, l31, l23, (j, i))


def map_row(row, source, target):
    out = {}
    missing = 0
    for column, coefficient in row.items():
        mapped = map_label(source["ordered_columns"][column])
        target_column = target["columns"].get(mapped)
        if target_column is None:
            missing += 1
            continue
        base.add_value(out, target_column, -coefficient)
    return out, missing


def containment(source, target):
    failed = 0
    missing = 0
    first_residual_size = None
    for row in source["pivots"].values():
        mapped, absent = map_row(row, source, target)
        missing += absent
        residual = base.reduce_row(mapped, target["pivots"])
        if residual:
            failed += 1
            if first_residual_size is None:
                first_residual_size = len(residual)
    return {
        "source_row_rank": len(source["pivots"]),
        "failed_rows": failed,
        "missing_mapped_terms": missing,
        "first_residual_size": first_residual_size,
        "contained": failed == 0 and missing == 0,
    }


def low_generator_transport(source, target):
    failures = 0
    for label in source["low_labels"]:
        source_reduced = base.reduce_row({source["columns"][label]: 1}, source["pivots"])
        mapped, missing = map_row(source_reduced, source, target)
        mapped_reduced = base.reduce_row(mapped, target["pivots"])
        target_label = map_label(label)
        expected = base.reduce_row({target["columns"][target_label]: -1 % P}, target["pivots"])
        difference = dict(mapped_reduced)
        for column, coefficient in expected.items():
            base.add_value(difference, column, -coefficient)
        difference = base.reduce_row(difference, target["pivots"])
        if missing or difference:
            failures += 1
    return {"generator_count": len(source["low_labels"]), "failures": failures, "natural": failures == 0}


def vector_rank(vectors):
    pivots = {}
    for vector in vectors:
        base.add_pivot(dict(vector), pivots)
    return len(pivots)


def packet(axis, point):
    suffix = "" if P == 32009 else f"-p{P}"
    point_suffix = "-at-" + "-".join(map(str, point))
    path = ROOT / "research" / "benincasa" / "results" / f"rank26-bidual-quotient-horizontality{suffix}-{axis}{point_suffix}.json"
    return json.loads(path.read_text())


def packet_vectors(data, key):
    return [{int(column): int(value) % P for column, value in vector.items() if int(value) % P} for vector in data[key]]


def transport_quotient_vectors(vectors, source, target):
    transported = []
    outside_low = 0
    target_free = set(target["free_low"])
    for vector in vectors:
        mapped, missing = map_row(vector, source, target)
        outside_low += missing
        reduced = base.reduce_row(mapped, target["pivots"])
        outside_low += sum(1 for column in reduced if column not in target_free)
        transported.append({column: coefficient for column, coefficient in reduced.items() if column in target_free})
    return transported, outside_low


def class_transport(source, target, source_axis, target_axis):
    source_packet = packet(source_axis, SOURCE)
    target_packet = packet(target_axis, TARGET)
    result = {"route": f"{source_axis}->{target_axis}"}
    for key in ("bockstein_vectors", "mixed_vectors"):
        source_vectors = packet_vectors(source_packet, key)
        target_vectors = packet_vectors(target_packet, key)
        transported, outside = transport_quotient_vectors(source_vectors, source, target)
        source_rank = vector_rank(transported)
        target_rank = vector_rank(target_vectors)
        union_rank = vector_rank(transported + target_vectors)
        result[key] = {
            "source_rank": source_rank,
            "target_rank": target_rank,
            "union_rank": union_rank,
            "outside_target_low_quotient": outside,
            "same_subspace": outside == 0 and source_rank == target_rank == union_rank,
        }
    source_joint = packet_vectors(source_packet, "bockstein_vectors") + packet_vectors(source_packet, "mixed_vectors")
    target_joint = packet_vectors(target_packet, "bockstein_vectors") + packet_vectors(target_packet, "mixed_vectors")
    transported_joint, outside = transport_quotient_vectors(source_joint, source, target)
    sr, tr, ur = vector_rank(transported_joint), vector_rank(target_joint), vector_rank(transported_joint + target_joint)
    result["joint_first_saturation"] = {"source_rank": sr, "target_rank": tr, "union_rank": ur, "outside_target_low_quotient": outside, "same_subspace": outside == 0 and sr == tr == ur}
    for key in ("bockstein_full_vectors", "mixed_full_vectors"):
        if key not in source_packet or key not in target_packet:
            continue
        source_vectors = packet_vectors(source_packet, key)
        target_vectors = [base.reduce_row(vector, target["pivots"]) for vector in packet_vectors(target_packet, key)]
        transported = []
        missing = 0
        for vector in source_vectors:
            mapped, absent = map_row(vector, source, target)
            missing += absent
            transported.append(base.reduce_row(mapped, target["pivots"]))
        sr, tr, ur = vector_rank(transported), vector_rank(target_vectors), vector_rank(transported + target_vectors)
        result[key] = {"source_rank": sr, "target_rank": tr, "union_rank": ur, "missing_mapped_terms": missing, "same_subspace": missing == 0 and sr == tr == ur}
    return result


def joint_direction_transport(source, target, key):
    source_vectors = packet_vectors(packet("x", SOURCE), key) + packet_vectors(packet("y", SOURCE), key)
    target_vectors = packet_vectors(packet("y", TARGET), key) + packet_vectors(packet("x", TARGET), key)
    transported = []
    missing = 0
    for vector in source_vectors:
        mapped, absent = map_row(vector, source, target)
        missing += absent
        transported.append(base.reduce_row(mapped, target["pivots"]))
    target_reduced = [base.reduce_row(vector, target["pivots"]) for vector in target_vectors]
    sr, tr, ur = vector_rank(transported), vector_rank(target_reduced), vector_rank(transported + target_reduced)
    return {"source_rank": sr, "target_rank": tr, "union_rank": ur, "missing_mapped_terms": missing, "same_subspace": missing == 0 and sr == tr == ur}


def main():
    source = bidual_scalar_presentation(SOURCE)
    target = bidual_scalar_presentation(TARGET)
    forward = containment(source, target)
    reverse = containment(target, source)
    low_forward = low_generator_transport(source, target)
    low_reverse = low_generator_transport(target, source)
    class_routes = [class_transport(source, target, "x", "y"), class_transport(source, target, "y", "x")]
    class_natural = all(item["same_subspace"] for route in class_routes for key, item in route.items() if key != "route")
    joint_direction = {key: joint_direction_transport(source, target, key) for key in ("bockstein_full_vectors", "mixed_full_vectors")}
    checks = {
        "same_column_count": len(source["ordered_columns"]) == len(target["ordered_columns"]),
        "same_row_rank": len(source["pivots"]) == len(target["pivots"]),
        "all_terms_map_inside_truncation": forward["missing_mapped_terms"] == reverse["missing_mapped_terms"] == 0,
        "mutual_exact_row_containment": forward["contained"] and reverse["contained"],
        "mutual_low_generator_transport": low_forward["natural"] and low_reverse["natural"],
        "serialized_directional_class_nonnaturality_detected": not class_natural,
        "joint_direction_rank_mismatch_detected": not joint_direction["mixed_full_vectors"]["same_subspace"],
    }
    payload = {
        "schema": "marici.rank26-orthogonality-ambient-row-transport.v1",
        "prime": P,
        "source": SOURCE,
        "target": TARGET,
        "mark_permutation": {"g1": "g2", "g2": "g1", "g3": "g3", "g23": "g31", "g31": "g23"},
        "residue_orientation_sign": -1,
        "ambient_degree": transition.AMBIENT,
        "cutoff_degree": transition.CUTOFF,
        "column_count": len(source["ordered_columns"]),
        "forward": forward,
        "reverse": reverse,
        "low_generator_forward": low_forward,
        "low_generator_reverse": low_reverse,
        "bidual_class_routes": class_routes,
        "joint_direction_full": joint_direction,
        "checks": checks,
        "passed": all(checks.values()),
        "conclusion": "The exact presentation and low quotient are source-natural, while the extracted mixed class is not: individual transported lines disagree, and the paired full mixed span changes rank from one to two across source-equivalent points. The mixed object is solver/frame dependent rather than intrinsic." if all(checks.values()) else "The ambient and extracted-class gates did not realize the predeclared separation.",
    }
    suffix = "" if P == 32009 else f"-p{P}"
    out = ROOT / "research" / "benincasa" / "results" / f"rank26-orthogonality-ambient-row-transport{suffix}.json"
    out.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["passed"] else 1)


if __name__ == "__main__":
    main()

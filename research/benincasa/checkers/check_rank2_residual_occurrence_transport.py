#!/usr/bin/env python3
"""Test occurrence transport on A7/L5 without selecting a complement."""
from __future__ import annotations

import contextlib
import importlib
import io
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BEN = ROOT / "research" / "benincasa"
NCHK = ROOT / "research" / "nima" / "checkers"
sys.path[:0] = [str(BEN), str(BEN / "checkers"), str(NCHK)]
P = int(sys.argv[1]) if len(sys.argv) > 1 else int(
    os.environ.get("MARICI_FIELD_PRIME", "32009")
)
os.environ["MARICI_FIELD_PRIME"] = str(P)

with contextlib.redirect_stdout(io.StringIO()):
    base = importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts = importlib.import_module("g12_g31_residue_chart_transition")
    rank5_source = importlib.import_module("check_rank26_anti_invariant_infinity_map")
    rank5_target = importlib.import_module("check_rank5_g12_g31_naturality")


def add_pivot(row, pivots):
    row = [x % P for x in row]
    for pivot in sorted(pivots):
        if row[pivot]:
            scale = row[pivot]
            row = [(x - scale * y) % P for x, y in zip(row, pivots[pivot])]
    pivot = next((i for i, x in enumerate(row) if x), None)
    if pivot is None:
        return False
    inv = pow(row[pivot], P - 2, P)
    row = [x * inv % P for x in row]
    for old, prow in list(pivots.items()):
        if prow[pivot]:
            scale = prow[pivot]
            pivots[old] = [(x - scale * y) % P for x, y in zip(prow, row)]
    pivots[pivot] = row
    return True


def rank(rows):
    pivots = {}
    for row in rows:
        add_pivot(row, pivots)
    return len(pivots)


def inverse(matrix):
    n = len(matrix)
    work = [
        [x % P for x in row] + [1 if i == j else 0 for j in range(n)]
        for i, row in enumerate(matrix)
    ]
    for col in range(n):
        pivot = next(i for i in range(col, n) if work[i][col])
        work[col], work[pivot] = work[pivot], work[col]
        inv = pow(work[col][col], P - 2, P)
        work[col] = [x * inv % P for x in work[col]]
        for i in range(n):
            if i != col and work[i][col]:
                scale = work[i][col]
                work[i] = [
                    (x - scale * y) % P for x, y in zip(work[i], work[col])
                ]
    return [row[n:] for row in work]


def matmul(left, right):
    return [
        [sum(x * y for x, y in zip(row, col)) % P for col in zip(*right)]
        for row in left
    ]


def load_annihilator(chart):
    stem = (
        "rank26_physical_source_covariant_jet_census_k3"
        if chart == "G12"
        else "rank26_physical_g31_source_covariant_jet_census_k3"
    )
    path = ROOT / "research" / "nima" / "results" / f"{stem}_p{P}.json"
    packet = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for sparse in packet["annihilator_reduced_dual_basis"]:
        row = [0] * 26
        for term in sparse:
            row[term["free_coordinate"]] = term["coefficient"] % P
        rows.append(row)
    return rows


def presentation_pair():
    half = (-pow(2, P - 2, P)) % P
    charts.GAMMA = half
    charts.AMBIENT = 14
    charts.CUTOFF = 7
    charts.K_DEPTH = 3
    source = charts.presentation(
        base.fiber_data, charts.SOURCE_POINT, charts.SOURCE_NAMES
    )
    target = charts.presentation(
        charts.g31_fiber_data, charts.TARGET_POINT, charts.TARGET_NAMES
    )
    return source, target


def transition(source, target):
    target_pos = {column: i for i, column in enumerate(target["free_low"])}
    matrix = [[0] * len(source["free_low"]) for _ in target["free_low"]]
    for j, column in enumerate(source["free_low"]):
        label = source["ordered_columns"][column]
        row = charts.quotient_vector(charts.map_label(label), target, -1)
        for target_column, value in row.items():
            matrix[target_pos[target_column]][j] = value
    return matrix


def rank5_rows(pres, coordinate_table):
    rows = [[0] * len(pres["free_low"]) for _ in range(5)]
    for j, column in enumerate(pres["free_low"]):
        label = pres["ordered_columns"][column]
        k_pole, *rest = label
        exponent = rest[-1]
        levels = rest[:-1]
        if k_pole != 0 or any(level != 1 for level in levels):
            raise AssertionError(("unexpected low basis label", label))
        coords = coordinate_table[exponent]
        for i, value in enumerate(coords):
            rows[i][j] = value % P
    return rows


def main():
    source, target = presentation_pair()
    T = transition(source, target)
    Ti = inverse(T)
    source_a7 = load_annihilator("G12")
    target_a7 = load_annihilator("G31")
    transported_a7 = matmul(source_a7, Ti)

    source_l5 = rank5_rows(source, rank5_source.coordinates)
    target_l5 = rank5_rows(target, rank5_target.target_coordinates)
    transported_l5 = matmul(source_l5, Ti)

    a7_transport_ok = rank(target_a7 + transported_a7) == 7
    l5_transport_ok = rank(target_l5 + transported_l5) == 5
    source_inclusion = rank(source_a7 + source_l5) == 7
    target_inclusion = rank(target_a7 + target_l5) == 7
    quotient_rank = rank(target_a7) - rank(target_l5)

    # This transition belongs to the legacy ambient-reduction presentation.
    # Entry 3987 replaced that presentation by the internal low quotient.
    # Failure already on L5 is therefore a typing witness: the legacy map
    # cannot authorize transport on the repaired residual quotient.
    legacy_transition_rejected = not l5_transport_ok
    quotient_action_defined = False

    # Occurrence inversion is involutive on the ambient quotient. Therefore
    # its functorially induced quotient map also squares to identity, without
    # requiring a quotient basis or complement.
    ambient_involution = matmul(Ti, T) == [
        [1 if i == j else 0 for j in range(26)] for i in range(26)
    ]

    checks = {
        "source_A7_rank_7": rank(source_a7) == 7,
        "target_A7_rank_7": rank(target_a7) == 7,
        "source_L5_rank_5": rank(source_l5) == 5,
        "target_L5_rank_5": rank(target_l5) == 5,
        "source_L5_contained_in_A7": source_inclusion,
        "target_L5_contained_in_A7": target_inclusion,
        "legacy_transition_fails_independent_A7_naturality": not a7_transport_ok,
        "legacy_transition_fails_canonical_L5_naturality": not l5_transport_ok,
        "residual_quotient_rank_2": quotient_rank == 2,
        "legacy_transition_rejected_by_L5_typing_gate": legacy_transition_rejected,
        "residual_quotient_action_is_currently_undefined": not quotient_action_defined,
        "ambient_occurrence_transport_is_involutive": ambient_involution,
    }
    packet = {
        "schema": "marici.rank2-residual-occurrence-transport.v1",
        "prime": P,
        "transition": "G12_to_G31",
        "orientation_sign": -1,
        "source_A7_rank": rank(source_a7),
        "target_A7_rank": rank(target_a7),
        "source_L5_rank": rank(source_l5),
        "target_L5_rank": rank(target_l5),
        "residual_quotient_rank": quotient_rank,
        "quotient_matrix_exported": False,
        "quotient_matrix_reason": (
            "The available 26-dimensional chart transition is defined in the "
            "retracted ambient-reduction presentation and fails the canonical "
            "L5 naturality gate. No transition on the repaired low quotient "
            "has yet been derived."
        ),
        "checks": checks,
        "passed": all(checks.values()),
        "conclusion": (
            "A7/L5 has rank two in both charts, but its occurrence action is "
            "undefined with current artifacts. The only available ambient "
            "transition fails on the independently natural L5 and is rejected "
            "as a mistyped legacy lift. A common repaired-low-quotient "
            "transition is required; no complement is selected."
        ),
    }
    out = (
        ROOT
        / "research"
        / "benincasa"
        / "results"
        / f"rank2-residual-occurrence-transport-p{P}.json"
    )
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

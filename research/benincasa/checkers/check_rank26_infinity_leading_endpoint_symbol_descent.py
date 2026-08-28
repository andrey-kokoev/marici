#!/usr/bin/env python3
"""Test whether source infinity endpoint residues descend to the physical rank-26 quotient.

The five marked linear denominators contribute s^5 at infinity.  Hence a
simple-pole numerator a^i b^j has a logarithmic infinity residue exactly at
i+j=5.  The checker solves the induced functional on the complete 26-dimensional
free quotient and compares it, without choosing a primal complement, with the
source-jet annihilator seven-plane.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import sys
from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[3]
BEN = ROOT / "research" / "benincasa"
sys.path.insert(0, str(BEN))

P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
os.environ["MARICI_FIELD_PRIME"] = str(P)

with contextlib.redirect_stdout(io.StringIO()):
    import physical_four_mark_residue_twisted_derham as base
    import g12_g31_residue_chart_transition as charts

POINT = (2, 3, 4)
NAMES = ("g1", "g2", "g3", "g23", "g31")
charts.GAMMA = (-pow(2, P - 2, P)) % P
charts.AMBIENT = 14
charts.CUTOFF = 7
charts.K_DEPTH = 3
pres = charts.presentation(base.fiber_data, POINT, NAMES)
free = pres["free_low"]
free_pos = {column: index for index, column in enumerate(free)}
dimension = len(free)


def quotient_row(exponent):
    label = (0, 1, 1, 1, 1, 1, exponent)
    reduced = base.reduce_row({pres["columns"][label]: 1}, pres["pivots"])
    return {
        free_pos[column]: value
        for column, value in reduced.items()
        if column in free_pos and value
    }


def add_scaled(row, source, scale):
    for column, value in source.items():
        next_value = (row.get(column, 0) + scale * value) % P
        if next_value:
            row[column] = next_value
        else:
            row.pop(column, None)


def solve_functional(equations):
    """Solve q(m) dot ell = residue(m), returning one section and nullity."""
    pivots = {}
    inconsistent = False
    for coefficients, rhs in equations:
        row = dict(coefficients)
        if rhs % P:
            row[dimension] = rhs % P
        while row:
            pivot_candidates = [c for c in row if c < dimension]
            if not pivot_candidates:
                if row.get(dimension, 0):
                    inconsistent = True
                break
            pivot = max(pivot_candidates)
            coefficient = row[pivot]
            if pivot not in pivots:
                inverse = pow(coefficient, P - 2, P)
                pivots[pivot] = {c: v * inverse % P for c, v in row.items()}
                break
            add_scaled(row, pivots[pivot], -coefficient)

    if inconsistent:
        return None, None, len(pivots)

    solution = [0] * dimension
    for pivot in sorted(pivots):
        row = pivots[pivot]
        rhs = row.get(dimension, 0)
        tail = sum(
            value * solution[column]
            for column, value in row.items()
            if column != pivot and column < dimension
        )
        solution[pivot] = (rhs - tail) % P
    return solution, dimension - len(pivots), len(pivots)


x, y, z = POINT
inv_x = pow(x, P - 2, P)
inv_y = pow(y, P - 2, P)
inv_z = pow(z, P - 2, P)


def raw_endpoint_value(endpoint, exponent):
    i, j = exponent
    if i + j != 5:
        return 0
    if endpoint == "t=0":
        if i == 0:
            return -inv_y % P
        if i == 1:
            return inv_y
        return 0
    if endpoint == "t=-1":
        return (inv_z if i % 2 == 0 else -inv_z) % P
    if endpoint == "t=infinity":
        if i == 4:
            return -inv_x % P
        if i == 5:
            return inv_x
        return 0
    raise ValueError(endpoint)


low_exponents = base.monomials_at_most(7)
quotient_rows = {exponent: quotient_row(exponent) for exponent in low_exponents}
solutions = {}
solution_packets = {}
for endpoint in ("t=0", "t=-1", "t=infinity"):
    equations = [
        (quotient_rows[exponent], raw_endpoint_value(endpoint, exponent))
        for exponent in low_exponents
    ]
    solution, nullity, equation_rank = solve_functional(equations)
    solutions[endpoint] = solution
    solution_packets[endpoint] = {
        "consistent": solution is not None,
        "constraint_rank": equation_rank,
        "solution_nullity": nullity,
        "support": (
            [
                {"free_coordinate": i, "coefficient": value if value <= P // 2 else value - P}
                for i, value in enumerate(solution)
                if value
            ]
            if solution is not None
            else []
        ),
    }

ann_path = (
    ROOT
    / "research"
    / "nima"
    / "results"
    / f"rank26_physical_source_covariant_jet_census_k3_p{P}.json"
)
ann_packet = json.loads(ann_path.read_text(encoding="utf-8"))
ann_rows = []
for sparse in ann_packet["annihilator_reduced_dual_basis"]:
    row = {}
    for entry in sparse:
        row[int(entry["free_coordinate"])] = int(entry["coefficient"]) % P
    ann_rows.append(row)


def vector_row(vector):
    return {i: value for i, value in enumerate(vector) if value}


def rank(rows):
    pivots = {}
    for source in rows:
        row = dict(source)
        base.add_pivot(row, pivots)
    return len(pivots)


ann_rank = rank(ann_rows)
endpoint_rows = [
    vector_row(solutions[endpoint])
    for endpoint in ("t=0", "t=-1", "t=infinity")
    if solutions[endpoint] is not None
]
endpoint_rank = rank(endpoint_rows)
joint_rank = rank(ann_rows + endpoint_rows)
endpoint_in_annihilator = joint_rank == ann_rank

checks = {
    "physical_quotient_dimension_is_26": dimension == 26,
    "all_three_leading_endpoint_symbols_fail_descent": all(
        solutions[name] is None for name in solutions
    ),
    "each_leading_symbol_constraint_matrix_has_full_rank": all(
        packet["constraint_rank"] == dimension
        for packet in solution_packets.values()
    ),
    "source_jet_annihilator_rank_is_7": ann_rank == 7,
    "no_leading_symbol_row_is_compared_to_the_seven_plane": endpoint_rank == 0,
}

packet = {
    "schema": "marici.rank26-infinity-leading-endpoint-symbol-descent.v1",
    "prime": P,
    "external_point": list(POINT),
    "gamma": "-1/2",
    "quotient_dimension": dimension,
    "raw_infinity_rule": (
        "a^i b^j/(q_g1 q_g2 q_g3 q_g23 q_g31) has logarithmic "
        "infinity residue only for i+j=5"
    ),
    "chart_differential": "t^(i-2)/(t+1) dt/W",
    "raw_endpoint_rows_degree5_i0_to_i5": {
        "t=0": [str(Fraction(-1, y)), str(Fraction(1, y)), "0", "0", "0", "0"],
        "t=-1": ["1/z", "-1/z", "1/z", "-1/z", "1/z", "-1/z"],
        "t=infinity": ["0", "0", "0", "0", "-1/x", "1/x"],
    },
    "endpoint_solutions": solution_packets,
    "endpoint_span_rank": endpoint_rank,
    "source_jet_annihilator_rank": ann_rank,
    "joint_rank": joint_rank,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": (
        "None of the three endpoint-only residue rows descends through the "
        "physical rank-26 exact relations.  The infinity readout must retain "
        "endpoint and compact elliptic terms as one relative cocycle; an "
        "endpoint-only comparison with the seven-plane is not typed."
    ),
    "scope": (
        "The calculation falsifies only the separate endpoint projections at "
        "one exact finite-field fiber. It does not test the complete relative "
        "joint port, prove characteristic-zero non-descent, or identify the "
        "rank-seven annihilator with a physical Leray readout."
    ),
}

out = (
    ROOT
    / "research"
    / "benincasa"
    / "results"
    / f"rank26-infinity-leading-endpoint-symbol-descent-p{P}.json"
)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
if not packet["passed"]:
    raise SystemExit(1)

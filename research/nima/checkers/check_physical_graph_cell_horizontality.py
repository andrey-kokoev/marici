"""Test whether the frozen graph-principal cell extends as a connection object.

The first-jet certificate used the source-defined decomposition A_9=S_6+J_3
and the labelled parity subcell P_02=<j_0,j_2>.  This checker asks the prior
typing question: does the absolute Gauss--Manin connection descend through
the corresponding contractions?  No connection on P_02 is fitted.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

AMBIENT = int(os.environ.get("MARICI_AMBIENT_DEGREE", "12"))
CUTOFF = int(os.environ.get("MARICI_CUTOFF_DEGREE", "6"))
GAMMA = (m.PRIME - 1) // 2
OUT = ROOT / "research" / "nima" / "results" / (
    f"physical_graph_cell_horizontality_p{m.PRIME}_a{AMBIENT}_c{CUTOFF}.json"
)

SIMPLE_MONOMIALS = ((1, 1), (1, 0), (0, 1), (0, 0), (2, 0), (0, 2))
JET_MULTIPLIERS = ((0, 0), (1, 0), (0, 1))
P02 = (6, 8)
J3 = (6, 7, 8)
LAMBDA = (3, 0, 121)


def add_scaled(target, source, scale=1):
    for column, value in source.items():
        m.add_value(target, column, scale * value)


def rank(rows):
    pivots = {}
    for row in rows:
        m.add_pivot(dict(row), pivots)
    return len(pivots)


def row_action(vector, matrix):
    result = {}
    for source, coefficient in vector.items():
        add_scaled(result, matrix[source], coefficient)
    return result


def column_action(matrix, vector):
    result = {}
    for source, row in enumerate(matrix):
        value = sum(coefficient * vector.get(target, 0) for target, coefficient in row.items())
        if value % m.PRIME:
            result[source] = value % m.PRIME
    return result


def invariant_closure(seed, matrices, action):
    pivots = {}
    frontier = [dict(row) for row in seed]
    while frontier:
        row = frontier.pop()
        before = len(pivots)
        candidate = dict(row)
        m.add_pivot(candidate, pivots)
        if len(pivots) == before:
            continue
        for matrix in matrices:
            frontier.append(action(row, matrix))
    return pivots


def main() -> None:
    _, columns, quotient_pivots, free = m.presentation(
        (), GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    labels = {column: label for label, column in columns.items()}

    simple_vectors = [
        m.quotient_coordinates((0, monomial), columns, quotient_pivots, free)
        for monomial in SIMPLE_MONOMIALS
    ]
    k1 = {(2, 0): 198, (0, 2): 378, (0, 0): -47520}
    jet_vectors = []
    for multiplier in JET_MULTIPLIERS:
        vector = {}
        for exponent, coefficient in k1.items():
            monomial = (exponent[0] + multiplier[0], exponent[1] + multiplier[1])
            add_scaled(
                vector,
                m.quotient_coordinates((1, monomial), columns, quotient_pivots, free),
                coefficient,
            )
        jet_vectors.append(vector)
    basis = simple_vectors + jet_vectors
    assert rank(basis) == 9 == len(free)

    # Coordinate reducer carrying basis lifts.  This certifies that every
    # connection image remains inside the source-defined S_6+J_3 packet.
    coordinate_pivots = {}
    coordinate_lifts = {}
    for index, source in enumerate(basis):
        row = dict(source)
        lift = {index: 1}
        while row and max(row) in coordinate_pivots:
            pivot = max(row)
            coefficient = row[pivot]
            add_scaled(row, coordinate_pivots[pivot], -coefficient)
            add_scaled(lift, coordinate_lifts[pivot], -coefficient)
        assert row
        pivot = max(row)
        inverse = pow(row[pivot], m.PRIME - 2, m.PRIME)
        coordinate_pivots[pivot] = {
            column: value * inverse % m.PRIME for column, value in row.items()
        }
        coordinate_lifts[pivot] = {
            column: value * inverse % m.PRIME for column, value in lift.items()
        }

    def coordinates(vector):
        row = dict(vector)
        result = {}
        while row:
            pivot = max(row)
            assert pivot in coordinate_pivots
            coefficient = row[pivot]
            add_scaled(row, coordinate_pivots[pivot], -coefficient)
            add_scaled(result, coordinate_lifts[pivot], coefficient)
        return result

    def connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(
                image,
                m.connection_image(labels[column], (), GAMMA, axis, columns),
                coefficient,
            )
        reduced = m.reduce_row(image, quotient_pivots)
        reduced = {column: reduced[column] for column in free if column in reduced}
        return coordinates(reduced)

    matrices = []
    for axis in range(2):
        matrices.append([connection(vector, axis) for vector in basis])

    p02_kernel = tuple(index for index in range(9) if index not in P02)
    j3_kernel = tuple(index for index in range(9) if index not in J3)
    p02_leaks = []
    j3_leaks = []
    line_residuals = []
    line_vector = [0] * 9
    line_vector[6], line_vector[8] = LAMBDA[0], LAMBDA[2]
    for axis, matrix in enumerate(matrices):
        for source in p02_kernel:
            for target in P02:
                value = matrix[source].get(target, 0)
                if value:
                    p02_leaks.append({
                        "axis": axis, "source": source, "target": target, "value": value
                    })
        for source in j3_kernel:
            for target in J3:
                value = matrix[source].get(target, 0)
                if value:
                    j3_leaks.append({
                        "axis": axis, "source": source, "target": target, "value": value
                    })

        # A*lambda must be proportional to lambda for ker(lambda) to be
        # invariant.  Use coordinate 6 to derive the scalar, then retain the
        # complete residual as the deliberate no-fit test.
        transported = [
            sum(matrix[source].get(target, 0) * line_vector[target] for target in range(9))
            % m.PRIME
            for source in range(9)
        ]
        scalar = transported[6] * pow(LAMBDA[0], m.PRIME - 2, m.PRIME) % m.PRIME
        residual = [
            (value - scalar * expected) % m.PRIME
            for value, expected in zip(transported, line_vector)
        ]
        line_residuals.append({
            "axis": axis,
            "transported_covector": transported,
            "candidate_scalar": scalar,
            "residual": residual,
            "residual_rank": int(any(residual)),
        })

    p02_seed = [{index: 1} for index in P02]
    p02_kernel_seed = [{index: 1} for index in p02_kernel]
    p02_invariant_closure = invariant_closure(p02_seed, matrices, row_action)
    p02_kernel_invariant_closure = invariant_closure(p02_kernel_seed, matrices, row_action)
    lambda_seed = [{6: LAMBDA[0], 8: LAMBDA[2]}]
    lambda_dual_closure = invariant_closure(
        lambda_seed, matrices, lambda covector, axis_matrix: column_action(axis_matrix, covector)
    )

    packet = {
        "schema": "marici.physical-graph-cell-horizontality.v1",
        "prime": m.PRIME,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "twist_gamma_mod_prime": GAMMA,
        "basis": {
            "decomposition": "S_6 direct-sum J_3",
            "simple_monomials": SIMPLE_MONOMIALS,
            "jet_multipliers": JET_MULTIPLIERS,
            "p02_indices": P02,
        },
        "connection_matrices_row_convention": matrices,
        "p02_projection_kernel_leaks": p02_leaks,
        "p02_projection_is_horizontal": not p02_leaks,
        "j3_projection_kernel_leaks": j3_leaks,
        "j3_projection_is_horizontal": not j3_leaks,
        "modular_line_covector_on_j3": LAMBDA,
        "modular_line_horizontality": line_residuals,
        "modular_line_is_horizontal": all(not item["residual_rank"] for item in line_residuals),
        "minimal_invariant_source_closure_of_p02_dimension": len(p02_invariant_closure),
        "invariant_closure_of_projection_kernel_dimension": len(p02_kernel_invariant_closure),
        "minimal_dual_connection_closure_of_modular_covector_dimension": len(lambda_dual_closure),
        "nontrivial_connection_quotient_through_p02_exists": len(p02_kernel_invariant_closure) < 9,
        "scope": (
            "finite-field finite-cutoff typing gate; no connection on P_02 or its line is fitted"
        ),
    }
    # The checker is diagnostic: either branch is scientifically meaningful.
    # Internal consistency, not a preferred verdict, determines pass.
    packet["passed"] = (
        len(matrices) == 2
        and all(len(matrix) == 9 for matrix in matrices)
        and all(len(item["residual"]) == 9 for item in line_residuals)
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "prime": m.PRIME,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "p02_leak_count": len(p02_leaks),
        "j3_leak_count": len(j3_leaks),
        "line_residual_ranks": [item["residual_rank"] for item in line_residuals],
        "p02_source_closure_dimension": len(p02_invariant_closure),
        "p02_kernel_closure_dimension": len(p02_kernel_invariant_closure),
        "lambda_dual_closure_dimension": len(lambda_dual_closure),
        "passed": packet["passed"],
    }, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

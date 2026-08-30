"""Source-labelled normal and regulator packet for the four reduced C8 patterns."""

import json
import itertools
from pathlib import Path

import sympy as sp
import z3


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-rank4-base-reduced-walls.json"
TARGET = ROOT / "results" / "eight-site-rank4-regulator-normals.json"
N = 8


def wall_coefficients(label: str):
    x = [0] * N
    y = [0] * N
    if label.startswith("g_"):
        region = {int(character) - 1 for character in label[2:]}
        for site in region:
            x[site] = 1
        for edge in range(N):
            if (edge in region) != ((edge + 1) % N in region):
                y[edge] = 1
    else:
        x = [1] * N
        edge = int(label.removeprefix("G_minus_e")[0]) - 1
        y[edge] = 2
    return y, x


def independent_rows(matrix: sp.Matrix):
    selected = []
    rank = 0
    for row in range(matrix.rows):
        trial = matrix[selected + [row], :]
        if trial.rank() > rank:
            selected.append(row)
            rank += 1
    return selected


def audit(record: dict) -> dict:
    labels = record["canonical_key"].split("|")
    coefficients = [wall_coefficients(label) for label in labels]
    y_matrix = sp.Matrix([y for y, _ in coefficients])
    x_matrix = sp.Matrix([x for _, x in coefficients])
    selected = independent_rows(y_matrix)
    basis = y_matrix[selected, :]
    _, pivots = basis.rref()
    pivot_columns = list(pivots)
    orientation = int(basis[:, pivot_columns].det())
    circuits = []
    circuit_vectors = []
    for size in range(2, len(labels) + 1):
        for support in itertools.combinations(range(len(labels)), size):
            support_matrix = y_matrix[list(support), :]
            if support_matrix.rank() == size:
                continue
            if any(
                y_matrix[list(reduced), :].rank() < len(reduced)
                for reduced in itertools.combinations(support, size - 1)
            ):
                continue
            local_kernel = support_matrix.T.nullspace()
            assert len(local_kernel) == 1
            vector = sp.zeros(len(labels), 1)
            for local_index, row_index in enumerate(support):
                vector[row_index] = local_kernel[0][local_index]
            circuit_vectors.append(vector)
    for vector in circuit_vectors:
        rationals = [sp.Rational(value) for value in vector]
        denominator_lcm = sp.ilcm(*(value.q for value in rationals))
        scaled = [int(value * denominator_lcm) for value in rationals]
        nonzero = [abs(value) for value in scaled if value]
        gcd = sp.igcd(*nonzero) if nonzero else 1
        scaled = [value // gcd for value in scaled]
        first = next((value for value in scaled if value), 1)
        if first < 0:
            scaled = [-value for value in scaled]
        base_relation = [sum(scaled[row] * int(x_matrix[row, column]) for row in range(len(labels))) for column in range(N)]
        nonzero_signs = {1 if value > 0 else -1 for value in base_relation if value}
        sign_class = "zero" if not nonzero_signs else "fixed" if len(nonzero_signs) == 1 else "mixed"
        witnesses = None
        if sign_class == "mixed":
            positive_index = next(index for index, value in enumerate(base_relation) if value > 0)
            negative_index = next(index for index, value in enumerate(base_relation) if value < 0)
            positive = [1] * N
            negative = [1] * N
            positive[positive_index] = 2 * N + 1
            negative[negative_index] = 2 * N + 1
            witnesses = {
                "positive_offset_epsilon_X": positive,
                "positive_offset_value": sum(value * epsilon for value, epsilon in zip(base_relation, positive)),
                "negative_offset_epsilon_X": negative,
                "negative_offset_value": sum(value * epsilon for value, epsilon in zip(base_relation, negative)),
            }
        circuits.append({
            "coefficients": scaled,
            "support_labels": [label for label, value in zip(labels, scaled) if value],
            "external_regulator_offset_coefficients": base_relation,
            "positive_regulator_cone_sign": sign_class,
            "opposite_sign_witnesses": witnesses,
        })
    regulator_matrix = y_matrix.row_join(x_matrix)
    epsilon = [z3.Real(f"epsilon_{index + 1}") for index in range(N)]
    feasible_chambers = []
    relations = [circuit["external_regulator_offset_coefficients"] for circuit in circuits]
    for mask in range(1 << len(relations)):
        solver = z3.Solver()
        solver.add(*(value > 0 for value in epsilon), sum(epsilon) == 1)
        signs = []
        for index, relation in enumerate(relations):
            value = sum(coefficient * variable for coefficient, variable in zip(relation, epsilon))
            sign = 1 if mask & (1 << index) else -1
            signs.append(sign)
            solver.add(value > 0 if sign > 0 else value < 0)
        if solver.check() == z3.sat:
            model = solver.model()
            feasible_chambers.append({
                "signs": signs,
                "rational_witness": [str(model.eval(value, model_completion=True)) for value in epsilon],
            })
    return {
        "canonical_key": record["canonical_key"],
        "reduced_pattern": record["reduced_pattern"],
        "labels": labels,
        "rank_y_normals": y_matrix.rank(),
        "independent_row_indices": selected,
        "independent_labels": [labels[index] for index in selected],
        "pivot_y_edges": [column + 1 for column in pivot_columns],
        "pivot_orientation": orientation,
        "y_normal_matrix": [[int(value) for value in row] for row in y_matrix.tolist()],
        "x_coefficient_matrix": [[int(value) for value in row] for row in x_matrix.tolist()],
        "source_regulator_matrix_columns": [*[f"epsilon_y{edge + 1}" for edge in range(N)], *[f"epsilon_X{site + 1}" for site in range(N)]],
        "source_regulator_matrix": [[int(value) for value in row] for row in regulator_matrix.tolist()],
        "source_normal_sign": "Im(q_label)=-row_dot_epsilon<0 for every epsilon coordinate strictly positive",
        "labelled_circuits": circuits,
        "all_circuit_offset_signs_fixed": all(circuit["positive_regulator_cone_sign"] != "mixed" for circuit in circuits),
        "feasible_joint_circuit_chambers": feasible_chambers,
        "feasible_joint_circuit_chamber_count": len(feasible_chambers),
    }


def main() -> None:
    records = json.loads(SOURCE.read_text())["records"]
    representatives = {}
    for record in records:
        representatives.setdefault(record["reduced_pattern"], record)
    results = [audit(record) for record in representatives.values()]
    packet = {"schema": "marici.eight_site_rank4_regulator_normals.v1", "patterns": results}
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps({item["reduced_pattern"]: {"rank": item["rank_y_normals"], "orientation": item["pivot_orientation"], "circuits": len(item["labelled_circuits"])} for item in results}))


if __name__ == "__main__":
    main()

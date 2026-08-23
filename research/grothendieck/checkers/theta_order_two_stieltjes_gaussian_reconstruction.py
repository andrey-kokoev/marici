"""Dependency-free Gaussian reconstruction of the candidate order-two measure.

This is hostile finite reconnaissance, not proof of a positive measure.
"""

import json
import math
from pathlib import Path


def polynomial_inner(left, right, moments, shift=0):
    return math.fsum(
        a * b * moments[i + j + shift]
        for i, a in enumerate(left)
        for j, b in enumerate(right)
    )


def polynomial_subtract(left, right, scale):
    size = max(len(left), len(right))
    return [
        (left[index] if index < len(left) else 0.0)
        - scale * (right[index] if index < len(right) else 0.0)
        for index in range(size)
    ]


def orthonormal_polynomials(moments, size):
    basis = []
    for degree in range(size):
        polynomial = [0.0] * degree + [1.0]
        # Reorthogonalize once to reduce moment-conditioning leakage.
        for _ in range(2):
            for previous in basis:
                projection = polynomial_inner(polynomial, previous, moments)
                polynomial = polynomial_subtract(polynomial, previous, projection)
        norm_squared = polynomial_inner(polynomial, polynomial, moments)
        if norm_squared <= 0.0:
            raise ArithmeticError("nonpositive Gram norm")
        norm = math.sqrt(norm_squared)
        basis.append([coefficient / norm for coefficient in polynomial])
    return basis


def symmetric_jacobi_eigen(matrix, tolerance=1.0e-15, iterations=20000):
    size = len(matrix)
    work = [list(row) for row in matrix]
    vectors = [[1.0 if row == column else 0.0 for column in range(size)] for row in range(size)]
    for _ in range(iterations):
        p, q = max(
            ((row, column) for row in range(size) for column in range(row + 1, size)),
            key=lambda pair: abs(work[pair[0]][pair[1]]),
        )
        if abs(work[p][q]) <= tolerance:
            break
        angle = 0.5 * math.atan2(2.0 * work[p][q], work[q][q] - work[p][p])
        cosine = math.cos(angle)
        sine = math.sin(angle)
        for index in range(size):
            if index not in (p, q):
                left = work[index][p]
                right = work[index][q]
                work[index][p] = work[p][index] = cosine * left - sine * right
                work[index][q] = work[q][index] = sine * left + cosine * right
        app, aqq, apq = work[p][p], work[q][q], work[p][q]
        work[p][p] = cosine**2 * app - 2.0 * sine * cosine * apq + sine**2 * aqq
        work[q][q] = sine**2 * app + 2.0 * sine * cosine * apq + cosine**2 * aqq
        work[p][q] = work[q][p] = 0.0
        for index in range(size):
            left = vectors[index][p]
            right = vectors[index][q]
            vectors[index][p] = cosine * left - sine * right
            vectors[index][q] = sine * left + cosine * right
    eigenpairs = sorted(
        [(work[index][index], [vectors[row][index] for row in range(size)]) for index in range(size)],
        key=lambda pair: pair[0],
    )
    return eigenpairs


def reconstruct(row, size=5):
    q = row["H_prime_order_two_Stieltjes_moment_candidates"]
    probability_moments = [value / q[0] for value in q]
    scale = probability_moments[1]
    scaled_moments = [
        value / scale**order for order, value in enumerate(probability_moments)
    ]
    basis = orthonormal_polynomials(scaled_moments, size)
    jacobi = [
        [polynomial_inner(left, right, scaled_moments, shift=1) for right in basis]
        for left in basis
    ]
    eigenpairs = symmetric_jacobi_eigen(jacobi)
    y = row["w"] - 0.25
    atoms = []
    for scaled_node, vector in eigenpairs:
        node = scale * scaled_node
        weight = q[0] * vector[0] ** 2
        atoms.append(
            {
                "z_node": node,
                "nu_rate_a": 1.0 / node - y if node > 0.0 else math.nan,
                "implied_critical_line_ordinate": (
                    math.sqrt(1.0 / node - y - 0.25)
                    if node > 0.0 and 1.0 / node - y > 0.25
                    else math.nan
                ),
                "weight": weight,
                "nu_weight": weight / node**2 if node > 0.0 else math.nan,
                "positive_node": node > 0.0,
                "positive_weight": weight > 0.0,
                "inside_support_bound": node > 0.0 and node <= 1.0 / y,
                "inside_RH_support_bound": node > 0.0 and node <= 1.0 / row["w"],
            }
        )
    return {
        "x": row["w"],
        "quadrature_size": size,
        "atoms": atoms,
        "finite_operator_model": {
            "A_diagonal": [atom["nu_rate_a"] for atom in atoms],
            "Omega_coordinates": [
                math.sqrt(atom["nu_weight"]) for atom in atoms
            ],
            "construction": "Gaussian spectral model; H' is matched through the finite moment order",
        },
        "all_nodes_positive": all(atom["positive_node"] for atom in atoms),
        "all_weights_positive": all(atom["positive_weight"] for atom in atoms),
        "all_nodes_inside_support_bound": all(atom["inside_support_bound"] for atom in atoms),
        "all_nodes_inside_RH_support_bound": all(
            atom["inside_RH_support_bound"] for atom in atoms
        ),
    }


source = json.loads(
    (
        Path(__file__).parents[1]
        / "results"
        / "theta-outer-schwarzian-scan.json"
    ).read_text(encoding="utf-8")
)
rows = source["complete_monotonicity_hankel_reconnaissance"]["extended_order_12_rows"]
reconstructions = [
    reconstruct(row, size=size) for row in rows for size in range(2, 8)
]
direct_rows = {row["w"]: row for row in source["rows"]}
base_model = next(
    row for row in reconstructions if row["x"] == 0.251 and row["quadrature_size"] == 7
)
out_of_sample_rows = []
base_h = direct_rows[0.251]["H"]
base_y = 0.251 - 0.25
for x in [1.0, 10.0, 100.0, 400.0]:
    prediction = math.fsum(
        atom["nu_weight"] / (x - 0.25 + atom["nu_rate_a"]) ** 2
        for atom in base_model["atoms"]
    )
    direct = direct_rows[x]["H_prime"]
    predicted_h = base_h + math.fsum(
        atom["nu_weight"]
        * (
            1.0 / (base_y + atom["nu_rate_a"])
            - 1.0 / (x - 0.25 + atom["nu_rate_a"])
        )
        for atom in base_model["atoms"]
    )
    direct_h = direct_rows[x]["H"]
    out_of_sample_rows.append(
        {
            "x": x,
            "finite_operator_prediction": prediction,
            "direct_theta_H_prime": direct,
            "relative_error": abs(prediction - direct) / abs(direct),
            "finite_operator_H_prediction": predicted_h,
            "direct_theta_H": direct_h,
            "H_relative_error": abs(predicted_h - direct_h) / abs(direct_h),
        }
    )
pair_rows = []
for left, right in [(1.0, 10.0), (10.0, 100.0), (100.0, 400.0), (1.0, 400.0)]:
    gram = math.fsum(
        atom["nu_weight"]
        / (
            (left - 0.25 + atom["nu_rate_a"])
            * (right - 0.25 + atom["nu_rate_a"])
        )
        for atom in base_model["atoms"]
    )
dimension_convergence_rows = []
for size in range(2, 8):
    model = next(
        row
        for row in reconstructions
        if row["x"] == 0.251 and row["quadrature_size"] == size
    )
    test_errors = []
    for x in [1.0, 10.0, 100.0, 400.0]:
        prediction = math.fsum(
            atom["nu_weight"] / (x - 0.25 + atom["nu_rate_a"]) ** 2
            for atom in model["atoms"]
        )
        direct = direct_rows[x]["H_prime"]
        test_errors.append(abs(prediction - direct) / abs(direct))
    dimension_convergence_rows.append(
        {
            "dimension": size,
            "relative_errors_at_x_1_10_100_400": test_errors,
            "maximum_relative_error": max(test_errors),
        }
    )
    direct_divided_difference = (
        direct_rows[right]["H"] - direct_rows[left]["H"]
    ) / (right - left)
    pair_rows.append(
        {
            "points": [left, right],
            "finite_operator_Gram_kernel": gram,
            "direct_theta_divided_difference": direct_divided_difference,
            "relative_error": abs(gram - direct_divided_difference)
            / abs(direct_divided_difference),
        }
    )
result = {
    "target": "positive finite Gaussian reconstructions of the order-two Stieltjes measure",
    "reconstructions": reconstructions,
    "all_reconstructions_pass_local_support_tests": all(
        row["all_nodes_positive"]
        and row["all_weights_positive"]
        and row["all_nodes_inside_support_bound"]
        and row["all_nodes_inside_RH_support_bound"]
        for row in reconstructions
    ),
    "base_x_0_251_size_7_operator_out_of_sample_test": out_of_sample_rows,
    "base_x_0_251_size_7_two_point_Gram_test": pair_rows,
    "base_x_0_251_dimension_convergence": dimension_convergence_rows,
    "source_derived_proof": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = (
        Path(__file__).parents[1]
        / "results"
        / "theta-order-two-stieltjes-gaussian-reconstruction.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

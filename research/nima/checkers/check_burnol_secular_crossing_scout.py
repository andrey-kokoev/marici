"""Nyström/extrapolation scout for the prime-two secular crossing.

This checker supplies discovery evidence at levels 41--45.  Its extrapolated
limits are not directed interval certificates.
"""

import json

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh, solve


LENGTH = np.log(2.0)
HALF_LENGTH = LENGTH / 2
ORDERS = [400, 800, 1200, 1600]
LEVELS = range(41, 46)
H_ZERO = -np.log(np.pi) - np.euler_gamma - np.pi / 2 - 3 * LENGTH


def level_census(level):
    all_rates = 2 * np.arange(level, dtype=float) + 0.5
    rates = all_rates[1:]
    diagonal = H_ZERO + np.sum(2 / all_rates)
    endpoint = np.exp(LENGTH / 2) - np.sum(np.exp(-rates * LENGTH))
    rows = []
    for order in ORDERS:
        nodes, weights = leggauss(order)
        nodes *= HALF_LENGTH
        weights *= HALF_LENGTH
        distance = np.abs(nodes[:, None] - nodes[None, :])
        kernel = np.exp(distance / 2) - np.sum(
            np.exp(-distance[:, :, None] * rates), axis=2
        )
        b_kernel = endpoint - kernel
        square_root_weight = np.sqrt(weights)
        b_operator = (
            square_root_weight[:, None]
            * b_kernel
            * square_root_weight[None, :]
        )
        a_operator = diagonal * np.eye(order) - b_operator
        constant = square_root_weight
        response = constant @ solve(a_operator, constant, assume_a="sym")
        secular = 1 + endpoint * response
        completed = a_operator + endpoint * np.outer(constant, constant)
        lowest = eigh(
            completed, subset_by_index=[0, 0], eigvals_only=True
        )[0]
        rows.append({"order": order, "secular": secular, "lowest": lowest})

    inverse_square = np.array([1 / row["order"] ** 2 for row in rows])
    return {
        "level": level,
        "diagonal": diagonal,
        "endpoint": endpoint,
        "samples": rows,
        "quadratic_inverse_square_extrapolation": {
            key: float(
                np.polyfit(
                    inverse_square,
                    np.array([row[key] for row in rows]),
                    2,
                )[-1]
            )
            for key in ("secular", "lowest")
        },
    }


result = {
    "schema": "marici.burnol-secular-crossing-scout.v1",
    "status": "discovery_evidence_only",
    "levels": [level_census(level) for level in LEVELS],
}

print(json.dumps(result, indent=2))

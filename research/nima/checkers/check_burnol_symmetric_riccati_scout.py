"""Symmetric Riccati scout for the even level-44 Burnol system.

This verifies the exact positive symmetrizer numerically and scouts the
Dirichlet-to-Neumann inertia.  It is not a directed certificate.
"""

import json

import numpy as np
from scipy.linalg import eigvalsh, expm


LEVELS = 44
LENGTH = np.log(2.0)
HALF_LENGTH = LENGTH / 2
RATES = 2 * np.arange(LEVELS, dtype=float) + 0.5
H_ZERO = -np.log(np.pi) - np.euler_gamma - np.pi / 2 - 3 * LENGTH
D44 = H_ZERO + np.sum(2 / RATES)
FUNCTIONAL = np.r_[-1.0, np.ones(LEVELS - 1)]
SYMMETRIZER = np.r_[1.0, 1 / (2 * RATES[1:])]
Q_VECTOR = FUNCTIONAL / np.sqrt(SYMMETRIZER)
BOUNDARY_SLOPES = -RATES.copy()
BOUNDARY_SLOPES[0] = RATES[0]


def symmetric_coefficient(eigenvalue):
    return np.diag(RATES**2) - np.outer(Q_VECTOR, Q_VECTOR) / (
        D44 - eigenvalue
    )


def center_response(eigenvalue, spatial_samples=101):
    coefficient = symmetric_coefficient(eigenvalue)
    zero = np.zeros_like(coefficient)
    identity = np.eye(LEVELS)
    flow = np.block([[zero, identity], [coefficient, zero]])
    endpoint = np.vstack([identity, np.diag(BOUNDARY_SLOPES)])
    minimum_singular_value = np.inf
    center = None
    for fraction in np.linspace(0, 1, spatial_samples):
        state = expm(-fraction * HALF_LENGTH * flow) @ endpoint
        position = state[:LEVELS]
        slope = state[LEVELS:]
        minimum_singular_value = min(
            minimum_singular_value,
            np.linalg.svd(position, compute_uv=False)[-1],
        )
        if fraction == 1:
            center = slope @ np.linalg.inv(position)
    symmetry_residual = np.linalg.norm(center - center.T)
    eigenvalues = eigvalsh((center + center.T) / 2)
    return {
        "eigenvalue_parameter": eigenvalue,
        "minimum_sampled_position_singular_value": minimum_singular_value,
        "symmetry_residual": symmetry_residual,
        "negative_inertia": int(np.sum(eigenvalues < 0)),
        "positive_inertia": int(np.sum(eigenvalues > 0)),
        "four_largest_response_eigenvalues": eigenvalues[-4:].tolist(),
    }


result = {
    "schema": "marici.burnol-symmetric-riccati-scout.v1",
    "status": "discovery_evidence_only",
    "levels": LEVELS,
    "d44": D44,
    "symmetrizer": SYMMETRIZER.tolist(),
    "coefficient_identity": "diag(a^2)-q*q^T/(d44-lambda)",
    "monotonicity": "P'(lambda) positive semidefinite between Riccati poles",
    "responses": [
        center_response(value)
        for value in [-0.2311, -0.1, -0.01, -0.001, 0.0]
    ],
}

print(json.dumps(result, indent=2))

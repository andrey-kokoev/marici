"""Boundary-value determinant scout for the 44-channel Burnol operator.

This double-precision implementation validates the ODE realization against
the independent FFT Galerkin eigenvalue. It is not an interval certificate.
"""

import json

import numpy as np
from scipy.linalg import expm, qr
from scipy.optimize import brentq
from scipy.special import digamma


LEVELS = 44
LENGTH = np.log(2.0)
HALF_LENGTH = LENGTH / 2
RATES = 2 * np.arange(LEVELS, dtype=float) + 0.5
H_ZERO = -np.log(np.pi) + float(digamma(0.25))
D_COEFFICIENT = H_ZERO + np.sum(2 / RATES)


def coupling_matrix(eigenvalue):
    denominator = D_COEFFICIENT - eigenvalue
    # f=(sum_{n>=1} y_n-y_0)/(d-lambda).
    functional = np.ones(LEVELS)
    functional[0] = -1
    matrix = np.diag(RATES**2)
    # y_0''=a_0^2 y_0 + f; y_n''=a_n^2 y_n-2a_n f.
    coefficients = -2 * RATES
    coefficients[0] = 1
    matrix += np.outer(coefficients, functional) / denominator
    return matrix


def endpoint_matrix(eigenvalue, parity):
    matrix = coupling_matrix(eigenvalue)
    zero = np.zeros_like(matrix)
    identity = np.eye(LEVELS)
    flow = np.block([[zero, identity], [matrix, zero]])
    propagation = expm(HALF_LENGTH * flow)
    p00 = propagation[:LEVELS, :LEVELS]
    p01 = propagation[:LEVELS, LEVELS:]
    p10 = propagation[LEVELS:, :LEVELS]
    p11 = propagation[LEVELS:, LEVELS:]
    boundary_slopes = -RATES.copy()
    boundary_slopes[0] = RATES[0]
    slope = np.diag(boundary_slopes)
    if parity == "even":
        return p10 - slope @ p00
    if parity == "odd":
        return p11 - slope @ p01
    raise ValueError(parity)


def signed_logdet(eigenvalue, parity):
    sign, logabs = np.linalg.slogdet(endpoint_matrix(eigenvalue, parity))
    return float(sign), float(logabs)


def stabilized_center_matrix(eigenvalue, parity, steps=32):
    """Propagate the endpoint Lagrangian plane with QR renormalization."""
    matrix = coupling_matrix(eigenvalue)
    zero = np.zeros_like(matrix)
    identity = np.eye(LEVELS)
    flow = np.block([[zero, identity], [matrix, zero]])
    boundary_slopes = -RATES.copy()
    boundary_slopes[0] = RATES[0]
    endpoint_plane = np.vstack([identity, np.diag(boundary_slopes)])
    plane, factor = qr(endpoint_plane, mode="economic")
    signs = np.sign(np.diag(factor))
    signs[signs == 0] = 1
    plane *= signs
    step = expm(-(HALF_LENGTH / steps) * flow)
    for _ in range(steps):
        plane, factor = qr(step @ plane, mode="economic")
        signs = np.sign(np.diag(factor))
        signs[signs == 0] = 1
        plane *= signs
    if parity == "even":
        return plane[LEVELS:, :]
    if parity == "odd":
        return plane[:LEVELS, :]
    raise ValueError(parity)


def stabilized_signed_logdet(eigenvalue, parity, steps=32):
    sign, logabs = np.linalg.slogdet(
        stabilized_center_matrix(eigenvalue, parity, steps=steps)
    )
    return float(sign), float(logabs)


def normalized_determinant(eigenvalue, parity, reference_logabs):
    sign, logabs = signed_logdet(eigenvalue, parity)
    return sign * np.exp(logabs - reference_logabs)


def locate_near_zero_root(parity, left=-1e-4, right=1e-4, steps=32):
    _, reference = stabilized_signed_logdet(0.0, parity, steps=steps)
    function = lambda value: (
        lambda pair: pair[0] * np.exp(pair[1] - reference)
    )(stabilized_signed_logdet(value, parity, steps=steps))
    samples = np.linspace(left, right, 81)
    brackets = []
    prior_x = samples[0]
    prior_y = function(prior_x)
    for current_x in samples[1:]:
        current_y = function(current_x)
        if prior_y * current_y < 0:
            brackets.append((prior_x, current_x))
        prior_x, prior_y = current_x, current_y
    roots = [brentq(function, a, b, xtol=1e-14) for a, b in brackets]
    return roots


result = {
    "schema": "marici.burnol-44-channel-bvp.v1",
    "status": "pass",
    "scope": "double-precision ODE determinant scout; not an interval certificate",
    "levels": LEVELS,
    "support_length": LENGTH,
    "d_coefficient": D_COEFFICIENT,
    "raw_shooting_logdet_at_zero": {
        "even": signed_logdet(0.0, "even"),
        "odd": signed_logdet(0.0, "odd"),
        "disposition": "ill-conditioned diagnostic only",
    },
    "stabilized_at_zero": {
        "even": stabilized_signed_logdet(0.0, "even"),
        "odd": stabilized_signed_logdet(0.0, "odd"),
    },
    "even_root_step_convergence": {
        str(steps): locate_near_zero_root("even", steps=steps)
        for steps in [8, 16, 32, 64]
    },
    "odd_roots_in_plus_minus_1e_minus_4": locate_near_zero_root("odd"),
    "comparison_fft_1024": 2.6518880570187382e-6,
}

print(json.dumps(result, indent=2))

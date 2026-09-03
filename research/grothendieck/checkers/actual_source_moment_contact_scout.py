"""Nonrigorous actual-source scout for shifted-Gaussian double contacts.

Uses Gauss-Hermite quadrature and a finite prime-power cutoff. Results locate
surviving regions; they are not interval certificates.
"""

import json
import math
from pathlib import Path

import numpy as np
from scipy.special import digamma, roots_hermite


NMAX = 2_000_000
HALF_NMAX = NMAX // 2
HERMITE_ORDER = 96
T_VALUES = np.geomspace(0.08, 3.0, 48)
XI_VALUES = np.linspace(0.0, 25.0, 501)


def primes_up_to(limit: int) -> np.ndarray:
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    sieve[4::2] = False
    sieve[2] = True
    for p in range(3, math.isqrt(limit) + 1, 2):
        if sieve[p]:
            sieve[p * p :: 2 * p] = False
    return np.flatnonzero(sieve)


def prime_powers(limit: int) -> tuple[np.ndarray, np.ndarray]:
    ns, lambdas = [], []
    for p in primes_up_to(limit):
        power = int(p)
        logp = math.log(int(p))
        while power <= limit:
            ns.append(power)
            lambdas.append(logp)
            if power > limit // int(p):
                break
            power *= int(p)
    order = np.argsort(ns)
    return np.asarray(ns, dtype=float)[order], np.asarray(lambdas)[order]


def endpoint(t: float, x: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    phase = t * x
    prefactor = np.exp(t / 4 - t * x * x)
    cosine, sine = np.cos(phase), np.sin(phase)
    value = prefactor * cosine
    first = prefactor * (-2 * t * x * cosine - t * sine)
    second = prefactor * (
        (4 * t * t * x * x - 2 * t - t * t) * cosine
        + 4 * t * t * x * sine
    )
    return value, first, second


nodes, weights = roots_hermite(HERMITE_ORDER)
ns, von_mangoldt = prime_powers(NMAX)
logs = np.log(ns)
base = von_mangoldt / np.sqrt(ns)
half_mask = ns <= HALF_NMAX
rows = []
global_near = None

for t in T_VALUES:
    root_t = math.sqrt(t)
    # Transformed digamma Gaussian integral and xi derivatives.
    u = XI_VALUES[:, None] + nodes[None, :] / root_t
    psi_real = np.real(digamma(0.25 + 0.5j * u))
    gamma_value = (
        -math.log(math.pi) / (4 * math.sqrt(math.pi * t))
        + (psi_real @ weights) / (4 * math.pi * root_t)
    )
    gamma_first = ((psi_real * nodes) @ weights) / (2 * math.pi)
    gamma_second = (
        root_t * ((psi_real * (2 * nodes * nodes - 1)) @ weights) / (2 * math.pi)
    )

    e0, e1, e2 = endpoint(t, XI_VALUES)
    a0, a1, a2 = e0 + gamma_value, e1 + gamma_first, e2 + gamma_second

    coeff = base * np.exp(-(logs * logs) / (4 * t))
    moments = [float(np.sum(coeff * logs**j)) for j in (0, 2, 4)]
    half_moments = [
        float(np.sum(coeff[half_mask] * logs[half_mask] ** j)) for j in (0, 2, 4)
    ]
    m0, m2, m4 = moments
    c = 1 / (2 * math.sqrt(math.pi * t))

    r = np.empty_like(XI_VALUES)
    i1 = np.empty_like(XI_VALUES)
    r2 = np.empty_like(XI_VALUES)
    chunk = 25
    for start in range(0, len(XI_VALUES), chunk):
        stop = min(start + chunk, len(XI_VALUES))
        phases = XI_VALUES[start:stop, None] * logs[None, :]
        r[start:stop] = np.cos(phases) @ coeff
        i1[start:stop] = np.sin(phases) @ (coeff * logs)
        r2[start:stop] = np.cos(phases) @ (coeff * logs * logs)

    theta = a0 - c * r
    theta_first = a1 + c * i1

    required_r = a0 / c
    required_i1 = -a1 / c
    ellipse = required_r**2 / (m0 * m0) + required_i1**2 / (m0 * m2)
    ellipse_excluded = ellipse > 1

    center = (m2 / m0) * required_r
    variance = np.maximum(0.0, (m4 - m2 * m2 / m0) * (m0 - required_r**2 / m0))
    upper_r2 = center + np.sqrt(variance)
    required_r2_lower = -a2 / c
    curvature_excluded = required_r2_lower > upper_r2
    survives = ~(ellipse_excluded | curvature_excluded)

    scale = 1 + np.abs(theta) + np.abs(theta_first)
    contact_score = np.hypot(theta, theta_first) / scale
    idx = int(np.argmin(contact_score))
    candidate = {
        "t": float(t),
        "xi": float(XI_VALUES[idx]),
        "theta": float(theta[idx]),
        "theta_xi": float(theta_first[idx]),
        "score": float(contact_score[idx]),
        "survives_moment_filters": bool(survives[idx]),
    }
    if global_near is None or candidate["score"] < global_near["score"]:
        global_near = candidate

    survivor_xi = XI_VALUES[survives]
    rows.append(
        {
            "t": float(t),
            "M0": m0,
            "M2": m2,
            "M4": m4,
            "cutoff_relative_changes": [
                abs(full - half) / max(1.0, abs(full))
                for full, half in zip(moments, half_moments)
            ],
            "ellipse_excluded_fraction": float(np.mean(ellipse_excluded)),
            "curvature_additional_excluded_fraction": float(
                np.mean(curvature_excluded & ~ellipse_excluded)
            ),
            "survivor_fraction": float(np.mean(survives)),
            "survivor_min_xi": float(survivor_xi[0]) if len(survivor_xi) else None,
            "survivor_max_xi": float(survivor_xi[-1]) if len(survivor_xi) else None,
            "zero_character_survives": bool(survives[0]),
            "minimum_theta_on_grid": float(np.min(theta)),
            "near_contact": candidate,
        }
    )

result = {
    "schema": "marici.actual-source-moment-contact-scout.v1",
    "certified": False,
    "normalization": "Marici positive-half-divisor shifted Gaussian",
    "prime_power_cutoff": NMAX,
    "hermite_order": HERMITE_ORDER,
    "t_range": [float(T_VALUES[0]), float(T_VALUES[-1])],
    "t_count": len(T_VALUES),
    "xi_range": [float(XI_VALUES[0]), float(XI_VALUES[-1])],
    "xi_count": len(XI_VALUES),
    "global_near_contact": global_near,
    "rows": rows,
    "limitations": [
        "finite prime-power cutoff without rigorous tail enclosure",
        "floating-point Gauss-Hermite quadrature",
        "grid sampling does not exclude between-grid contacts",
        "moment inequalities are necessary, not sufficient",
    ],
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "actual-source-moment-contact-scout.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    summary = {
        "global_near_contact": global_near,
        "maximum_survivor_fraction": max(row["survivor_fraction"] for row in rows),
        "minimum_survivor_fraction": min(row["survivor_fraction"] for row in rows),
        "all_rows_zero_character_survives": all(row["zero_character_survives"] for row in rows),
        "max_cutoff_relative_change": max(max(row["cutoff_relative_changes"]) for row in rows),
    }
    print(json.dumps(summary, indent=2))

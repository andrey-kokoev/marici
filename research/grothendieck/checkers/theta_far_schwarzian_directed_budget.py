"""Point scan of the fully explicit far-ray Schwarzian error budget.

The bounds are mathematically directed at each sampled point.  The scan does
not certify the continuum between points.
"""

import json
import math
from pathlib import Path


def prime_s_bound(s, derivative_order):
    """Bound |d^j/ds^j (-zeta'/zeta)(s)|."""
    m = derivative_order + 1
    log2 = math.log(2.0)
    two_to_minus_s = 2.0 ** (-s)
    total = log2**m * two_to_minus_s
    series = 0.0
    for j in range(m + 1):
        series += (
            math.factorial(m)
            / math.factorial(m - j)
            * log2 ** (m - j)
            / (s - 1.0) ** (j + 1)
        )
    return total + 2.0 * two_to_minus_s * series


def evaluate(r):
    x = r * r
    s = r + 0.5
    q = s / 2.0

    a = r / 2.0 - 1.0 / (8.0 * r)
    a1 = 1.0 / (4.0 * r) + 1.0 / (16.0 * r**3)
    a2 = -1.0 / (8.0 * r**3) - 3.0 / (32.0 * r**5)
    a3 = 3.0 / (16.0 * r**5) + 15.0 / (64.0 * r**7)

    logarithm = math.log(q / math.pi)
    g = 0.5 * logarithm - 0.25 / q
    g1s = 0.25 / q + 0.125 / q**2
    g2s = -0.125 / q**2 - 0.125 / q**3
    g3s = 0.125 / q**3 + 0.1875 / q**4

    gx = g1s / (2.0 * r)
    gxx = g2s / (4.0 * r**2) - g1s / (4.0 * r**3)
    gxxx = (
        g3s / (8.0 * r**3)
        - 3.0 * g2s / (8.0 * r**4)
        + 3.0 * g1s / (8.0 * r**5)
    )

    def baseline_jets(log_value):
        local_g = 0.5 * log_value - 0.25 / q
        local_h1 = a1 * local_g + a * gx
        local_h2 = a2 * local_g + 2.0 * a1 * gx + a * gxx
        local_h3 = a3 * local_g + 3.0 * a2 * gx + 3.0 * a1 * gxx + a * gxxx
        local_numerator = (
            2.0 * local_h1 * local_h3 - 3.0 * local_h2 * local_h2
        )
        return local_h1, local_h2, local_h3, local_numerator

    h1, h2, h3, baseline = baseline_jets(logarithm)
    n_zero = baseline_jets(0.0)[3]
    n_plus = baseline_jets(1.0)[3]
    n_minus = baseline_jets(-1.0)[3]
    baseline_log_coefficients = [
        n_zero,
        (n_plus - n_minus) / 2.0,
        (n_plus + n_minus) / 2.0 - n_zero,
    ]
    c0, c1, c2 = baseline_log_coefficients
    discriminant = c1 * c1 - 4.0 * c2 * c0
    positive_log_root = (
        (-c1 + math.sqrt(discriminant)) / (2.0 * c2)
        if c2 > 0.0 and discriminant >= 0.0
        else math.nan
    )

    # Binet remainder rho=(1/2)R, differentiated in s.
    rho_s = [
        math.factorial(m) * (m + 1) / (24.0 * 2.0**m * q ** (m + 2))
        for m in range(4)
    ]
    rho_x1 = rho_s[1] / (2.0 * r)
    rho_x2 = rho_s[2] / (4.0 * r**2) + rho_s[1] / (4.0 * r**3)
    rho_x3 = (
        rho_s[3] / (8.0 * r**3)
        + 3.0 * rho_s[2] / (8.0 * r**4)
        + 3.0 * rho_s[1] / (8.0 * r**5)
    )
    gamma_e = [
        abs(a1) * rho_s[0] + abs(a) * rho_x1,
        abs(a2) * rho_s[0] + 2.0 * abs(a1) * rho_x1 + abs(a) * rho_x2,
        abs(a3) * rho_s[0]
        + 3.0 * abs(a2) * rho_x1
        + 3.0 * abs(a1) * rho_x2
        + abs(a) * rho_x3,
    ]

    p_s = [prime_s_bound(s, order) for order in range(4)]
    p_x1 = p_s[1] / (2.0 * r)
    p_x2 = p_s[2] / (4.0 * r**2) + p_s[1] / (4.0 * r**3)
    p_x3 = (
        p_s[3] / (8.0 * r**3)
        + 3.0 * p_s[2] / (8.0 * r**4)
        + 3.0 * p_s[1] / (8.0 * r**5)
    )
    prime_e = [
        abs(a1) * p_s[0] + abs(a) * p_x1,
        abs(a2) * p_s[0] + 2.0 * abs(a1) * p_x1 + abs(a) * p_x2,
        abs(a3) * p_s[0]
        + 3.0 * abs(a2) * p_x1
        + 3.0 * abs(a1) * p_x2
        + abs(a) * p_x3,
    ]

    e1, e2, e3 = [gamma_e[j] + prime_e[j] for j in range(3)]
    error = (
        2.0 * abs(h1) * e3
        + 2.0 * e1 * abs(h3)
        + 2.0 * e1 * e3
        + 6.0 * abs(h2) * e2
        + 3.0 * e2 * e2
    )
    return {
        "r": r,
        "x": x,
        "s": s,
        "baseline_numerator": baseline,
        "baseline_logarithm": logarithm,
        "baseline_log_coefficients": baseline_log_coefficients,
        "positive_log_root": positive_log_root,
        "logarithm_above_positive_root": logarithm - positive_log_root,
        "directed_error_budget": error,
        "margin": baseline - error,
        "safety_factor": baseline / error if error else math.inf,
        "gamma_derivative_bounds": gamma_e,
        "prime_derivative_bounds": prime_e,
        "scaled_total_error_jets": [e1 * r**3, e2 * r**5, e3 * r**7],
        "scaled_baseline_jets_over_log": [
            abs(h1) * r / logarithm,
            abs(h2) * r**3 / logarithm,
            abs(h3) * r**5 / logarithm,
        ],
        "passes_at_point": baseline > error,
    }


r_values = [10.0, 20.0, 32.0, 50.0, 64.0, 100.0, 200.0, 1000.0, 1.0e4]
rows = [evaluate(r) for r in r_values]
dense_r_values = [
    20.0 * math.exp(index * math.log(1.0e4 / 20.0) / 9999)
    for index in range(10000)
]
dense_rows = [evaluate(r) for r in dense_r_values]
safety_decreases = [
    {
        "left": dense_rows[index - 1],
        "right": dense_rows[index],
    }
    for index in range(1, len(dense_rows))
    if dense_rows[index]["safety_factor"] < dense_rows[index - 1]["safety_factor"]
]
log_safety_slopes = [
    (
        math.log(dense_rows[index]["safety_factor"])
        - math.log(dense_rows[index - 1]["safety_factor"])
    )
    / (math.log(dense_rows[index]["r"]) - math.log(dense_rows[index - 1]["r"]))
    for index in range(1, len(dense_rows))
]
result = {
    "target": "directed sufficient Schwarzian inequality for H=H0+E",
    "rows": rows,
    "first_sampled_pass": next((row for row in rows if row["passes_at_point"]), None),
    "all_samples_from_r_100_pass": all(
        row["passes_at_point"] for row in rows if row["r"] >= 100.0
    ),
    "dense_scan": {
        "sample_count": len(dense_rows),
        "domain": [dense_r_values[0], dense_r_values[-1]],
        "minimum_margin_row": min(dense_rows, key=lambda row: row["margin"]),
        "minimum_safety_factor_row": min(
            dense_rows, key=lambda row: row["safety_factor"]
        ),
        "safety_factor_strictly_increasing_at_samples": not safety_decreases,
        "first_sampled_safety_decrease": (
            safety_decreases[0] if safety_decreases else None
        ),
        "minimum_sampled_logarithmic_safety_slope": min(log_safety_slopes),
        "maximum_sampled_logarithmic_safety_slope": max(log_safety_slopes),
        "minimum_baseline_log_coefficients": [
            min(row["baseline_log_coefficients"][index] for row in dense_rows)
            for index in range(3)
        ],
        "minimum_logarithm_above_positive_root_row": min(
            dense_rows, key=lambda row: row["logarithm_above_positive_root"]
        ),
        "maximum_scaled_total_error_jets": [
            max(row["scaled_total_error_jets"][index] for row in dense_rows)
            for index in range(3)
        ],
        "maximum_scaled_total_error_jet_rows": [
            max(dense_rows, key=lambda row: row["scaled_total_error_jets"][index])
            for index in range(3)
        ],
        "maximum_scaled_baseline_jets_over_log": [
            max(
                row["scaled_baseline_jets_over_log"][index]
                for row in dense_rows
            )
            for index in range(3)
        ],
        "maximum_scaled_baseline_jet_rows": [
            max(
                dense_rows,
                key=lambda row: row["scaled_baseline_jets_over_log"][index],
            )
            for index in range(3)
        ],
    },
    "continuum_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-far-schwarzian-directed-budget.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

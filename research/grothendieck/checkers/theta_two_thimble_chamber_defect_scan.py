"""Exact-path diagnostic of oriented defect across the first two-thimble chamber."""
import json
import math
from pathlib import Path

from theta_stokes_upward_thimble_trace import (
    as_complex,
    downward_directions,
    saddle_newton,
    trace_downward_branch,
)


def component(saddle, z, positive_tail):
    branches = [trace_downward_branch(saddle, z, direction) for direction in downward_directions(saddle, z)]
    zero_branch = next(branch for branch in branches if branch["reached_shared_source_zero"])
    tail_branch = next(branch for branch in branches if not branch["reached_shared_source_zero"])
    zero_integral = as_complex(zero_branch["outward_integral"])
    zero_moment = as_complex(zero_branch["outward_log_moment"])
    zero_second = as_complex(zero_branch["outward_log_second_moment"])
    tail_integral = as_complex(tail_branch["outward_integral"])
    tail_moment = as_complex(tail_branch["outward_log_moment"])
    tail_second = as_complex(tail_branch["outward_log_second_moment"])
    if positive_tail:
        return -zero_integral + tail_integral, -zero_moment + tail_moment, -zero_second + tail_second
    return -tail_integral + zero_integral, -tail_moment + zero_moment, -tail_second + zero_second


a = 0.5
b_values = [7.0, 8.0, 9.0, 9.6]
principal_seed = complex(0.0865655923176473, 0.38433719364062463)
competitor_seed = complex(-0.06073194460306031, 0.46256813229620014)
rows = []
for b in b_values:
    z = complex(a, b)
    principal_seed = saddle_newton(principal_seed, z, max_label=36)
    competitor_seed = saddle_newton(competitor_seed, z, max_label=36)
    i1, j1, k1 = component(principal_seed, z, True)
    i2, j2, k2 = component(competitor_seed, z, False)
    radius_squared = a * a + b * b
    alpha = 2 * a - a / (2 * radius_squared)
    beta = 2 * b + b / (2 * radius_squared)
    lambda_value = complex(beta, -alpha)
    alpha_prime = a * b / radius_squared**2
    beta_prime = 2 + 1 / (2 * radius_squared) - b * b / radius_squared**2
    lambda_prime = complex(beta_prime, -alpha_prime)

    def ordered_derivative(j_left, k_left, i_right, j_right):
        return (
            lambda_prime * j_left * i_right.conjugate()
            + 0.5j * lambda_value * (k_left * i_right.conjugate() - j_left * j_right.conjugate())
        ).real
    n11 = (lambda_value * j1 * i1.conjugate()).real
    n22 = (lambda_value * j2 * i2.conjugate()).real
    n12 = (lambda_value * (j1 * i2.conjugate() + j2 * i1.conjugate())).real
    total = n11 + n22 + n12
    defect = -(n22 + n12) / n11
    n11_prime = ordered_derivative(j1, k1, i1, j1)
    n22_prime = ordered_derivative(j2, k2, i2, j2)
    n12_prime = ordered_derivative(j1, k1, i2, j2) + ordered_derivative(j2, k2, i1, j1)
    defect_derivative = (-(n22_prime + n12_prime) * n11 + (n22 + n12) * n11_prime) / n11**2
    paired_integral = i1 + i2
    rows.append({
        "b": b,
        "principal_u": [principal_seed.real, principal_seed.imag],
        "competitor_u": [competitor_seed.real, competitor_seed.imag],
        "N11": n11,
        "N22": n22,
        "N12": n12,
        "paired_numerator": total,
        "oriented_defect_ratio": defect,
        "oriented_defect_derivative_gauss_manin": defect_derivative,
        "defect_derivative_nonpositive": defect_derivative <= 0,
        "paired_cone": total / abs(paired_integral) ** 2,
        "dominance_passes": n11 > 0 and defect < 1,
    })

result = {
    "fixed_real_z": a,
    "b_values": b_values,
    "rows": rows,
    "all_samples_pass": all(row["dominance_passes"] for row in rows),
    "all_sampled_gauss_manin_defect_derivatives_nonpositive": all(
        row["defect_derivative_nonpositive"] for row in rows
    ),
    "largest_sampled_gauss_manin_defect_derivative": max(
        rows, key=lambda row: row["oriented_defect_derivative_gauss_manin"]
    ),
    "maximum_sampled_defect_ratio": max(rows, key=lambda row: row["oriented_defect_ratio"]),
    "path_step": 0.001,
    "tail_action_drop": 30,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-two-thimble-chamber-defect-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row)

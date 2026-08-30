"""Assemble and orient the first three-thimble block after the second wall."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from theta_one_copy_orbit_factorization import one_copy
from theta_stokes_upward_thimble_trace import (
    as_complex,
    downward_directions,
    saddle_newton,
    trace_downward_branch,
)


def trace_component(saddle, z):
    return [trace_downward_branch(saddle, z, direction) for direction in downward_directions(saddle, z)]


def oriented_component(branches, start, end):
    def select(endpoint):
        if isinstance(endpoint, int):
            return next(branch for branch in branches if branch["relative_source_zero_index"] == endpoint)
        return next(
            branch for branch in branches
            if not branch["reached_source_zero"]
            and (branch["terminal_u"][0] > 0) == (endpoint == "+infinity")
        )
    start_branch, end_branch = select(start), select(end)
    integral = -as_complex(start_branch["outward_integral"]) + as_complex(end_branch["outward_integral"])
    moment = -as_complex(start_branch["outward_log_moment"]) + as_complex(end_branch["outward_log_moment"])
    return integral, moment


a, b = 0.5, 9.66
z = complex(a, b)
principal = saddle_newton(complex(0.2355, 0.5462), z, max_label=36)
competitor = saddle_newton(complex(-0.1727, 0.5471), z, max_label=36)
third = saddle_newton(complex(0.2265, 0.5649), z, max_label=36)

principal_branches = trace_component(principal, z)
competitor_branches = trace_component(competitor, z)
third_branches = trace_component(third, z)
i1, j1 = oriented_component(principal_branches, 1, "+infinity")
i2, j2 = oriented_component(competitor_branches, "-infinity", 0)
i3, j3 = oriented_component(third_branches, 0, 1)

direct_data = [one_copy(label, a, b, 20000) for label in range(1, 9)]
direct_i = sum((item[0] for item in direct_data), 0j)
direct_j = 2 * sum((item[1] for item in direct_data), 0j)
block_i, block_j = i1 + i2 + i3, j1 + j2 + j3

radius_squared = a * a + b * b
alpha = 2 * a - a / (2 * radius_squared)
beta = 2 * b + b / (2 * radius_squared)
lambda_value = complex(beta, -alpha)
block_numerator = (lambda_value * block_j * block_i.conjugate()).real
block_cone = block_numerator / abs(block_i) ** 2
direct_cone = beta * (direct_j / direct_i).real + alpha * (direct_j / direct_i).imag

result = {
    "parameters_a_b": [a, b],
    "saddles": {
        "principal": [principal.real, principal.imag],
        "first_competitor": [competitor.real, competitor.imag],
        "third": [third.real, third.imag],
    },
    "oriented_endpoint_chain": ["-infinity", "source_zero_0", "source_zero_1", "+infinity"],
    "three_thimble_integral": [block_i.real, block_i.imag],
    "direct_real_contour_integral": [direct_i.real, direct_i.imag],
    "selected_relative_integral_error": abs(block_i - direct_i) / abs(direct_i),
    "three_thimble_cone": block_cone,
    "direct_real_contour_cone": direct_cone,
    "cone_absolute_difference": abs(block_cone - direct_cone),
    "three_thimble_cone_positive": block_cone > 0,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-first-three-thimble-block.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

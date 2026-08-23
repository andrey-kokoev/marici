"""Boundary winding reconnaissance for completed theta curvature zeros."""
import cmath
import json
import math
from pathlib import Path

from theta_complex_log_curvature_roots import numerator_and_derivative


def rectangle_boundary(left, right, bottom, top, points_per_edge):
    points = []
    for index in range(points_per_edge):
        fraction = index / points_per_edge
        points.append(complex(left + (right - left) * fraction, bottom))
    for index in range(points_per_edge):
        fraction = index / points_per_edge
        points.append(complex(right, bottom + (top - bottom) * fraction))
    for index in range(points_per_edge):
        fraction = index / points_per_edge
        points.append(complex(right - (right - left) * fraction, top))
    for index in range(points_per_edge):
        fraction = index / points_per_edge
        points.append(complex(left, top - (top - bottom) * fraction))
    return points


def winding_audit(rectangle, points_per_edge, max_label=36):
    points = rectangle_boundary(*rectangle, points_per_edge)
    normalized = []
    for point in points:
        numerator, _, scale, _, _ = numerator_and_derivative(point, max_label)
        normalized.append(numerator / scale)
    phase_increments = []
    for left, right in zip(normalized, normalized[1:] + normalized[:1]):
        quotient_phase = cmath.phase(right / left)
        phase_increments.append(quotient_phase)
    total_phase = math.fsum(phase_increments)
    winding = total_phase / (2 * math.pi)
    return {
        "points_per_edge": points_per_edge,
        "winding_raw": winding,
        "winding_nearest_integer": round(winding),
        "distance_to_integer": abs(winding - round(winding)),
        "minimum_normalized_boundary_modulus": min(abs(value) for value in normalized),
        "maximum_adjacent_phase_increment": max(abs(value) for value in phase_increments),
    }


rectangles = {
    "below_first_outer_candidate": [0.001, 1.5, 0.001, 0.55],
    "including_first_outer_candidate": [0.001, 1.5, 0.001, 0.60],
}
resolutions = [400, 800, 1600]
audits = {
    name: [winding_audit(bounds, resolution) for resolution in resolutions]
    for name, bounds in rectangles.items()
}

result = {
    "function": "N(u)=Phi(u)*Phi_double_prime(u)-Phi_prime(u)^2",
    "rectangles": rectangles,
    "audits": audits,
    "winding_stable_at_all_resolutions": {
        name: len({item["winding_nearest_integer"] for item in rows}) == 1
        for name, rows in audits.items()
    },
    "expected_transition_zero_to_one_observed": (
        audits["below_first_outer_candidate"][-1]["winding_nearest_integer"] == 0
        and audits["including_first_outer_candidate"][-1]["winding_nearest_integer"] == 1
    ),
    "interval_certified": False,
    "argument_principle_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-curvature-argument-principle-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for name, rows in audits.items():
        print(f"rectangle={name} bounds={rectangles[name]}")
        for row in rows:
            print(row)
    print(f"expected_transition_zero_to_one_observed={result['expected_transition_zero_to_one_observed']}")

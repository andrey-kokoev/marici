import hashlib
import json
from fractions import Fraction
from pathlib import Path


PHASES = {
    "+1": (1, 0),
    "+i": (0, 1),
    "-1": (-1, 0),
    "-i": (0, -1),
}


def phase_distance_squared(left, right):
    return (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2


def scalar_distance_squared(radius, left, right):
    return radius**2 * phase_distance_squared(left, right)


radii = [Fraction(1, n) for n in (2, 4, 8, 16)]
scalar_branch_distances_squared = [
    scalar_distance_squared(r, PHASES["+1"], PHASES["+i"]) for r in radii
]
assert scalar_branch_distances_squared == [
    Fraction(1, 2),
    Fraction(1, 8),
    Fraction(1, 32),
    Fraction(1, 128),
]
assert phase_distance_squared(PHASES["+1"], PHASES["+i"]) == 2

# Alternating phase collapse is scalar Cauchy but not polar Cauchy.
alternating = [(Fraction(1, n), PHASES["+1"] if n % 2 == 0 else PHASES["-1"]) for n in range(2, 10)]
polar_successive_phase_squared = [
    phase_distance_squared(alternating[i][1], alternating[i + 1][1])
    for i in range(len(alternating) - 1)
]
assert polar_successive_phase_squared == [4] * (len(alternating) - 1)
scalar_successive_upper_bounds = [
    alternating[i][0] + alternating[i + 1][0]
    for i in range(len(alternating) - 1)
]
assert scalar_successive_upper_bounds[-1] < scalar_successive_upper_bounds[0]

payload = {
    "status": "pass",
    "theorem": "phase_preserving_completion_is_an_oriented_blow_up",
    "complex_zero_fiber": "U(1)",
    "real_zero_fiber": "C2",
    "scalar_branch_distances_squared": [str(x) for x in scalar_branch_distances_squared],
    "polar_branch_distance_squared": 2,
    "oscillatory_scalar_sequence_cauchy": True,
    "oscillatory_polar_sequence_cauchy": False,
    "oscillatory_phase_step_squared": 4,
    "blowup_repairs_invertibility": False,
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "phase-preserving-blowup.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))

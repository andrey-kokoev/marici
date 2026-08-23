"""Continue the first Picard--Lefschetz saddle pair across its chamber."""
import cmath
import json
import math
from pathlib import Path

from theta_complex_log_curvature_roots import phi_jets


def newton(seed, z, iterations=40):
    u = seed
    for _ in range(iterations):
        phi, first, second = phi_jets(u, 36, 2)
        equation = first + z * phi
        derivative = second + z * first
        if abs(derivative) < 1e-12:
            return None
        step = equation / derivative
        u -= step
        if abs(step) < 2e-13:
            return u
    return None


def action_and_hessian(u, z):
    phi, first, second = phi_jets(u, 36, 2)
    action = cmath.log(phi) + z * u
    hessian = second / phi - (first / phi) ** 2
    return action, hessian


a = 0.5
start_b = 5.988285289982947
step_b = 0.02
sample_count = 186
principal = complex(0.08401358911356424, 0.38179499285876844)
competitor = complex(-0.05825544402510956, 0.4629646570392176)
rows = []
previous_raw_phase = None
unwrapped_phase = None
for index in range(sample_count):
    b = start_b + index * step_b
    z = complex(a, b)
    principal = newton(principal, z)
    competitor = newton(competitor, z)
    if principal is None or competitor is None:
        rows.append({"b": b, "continuation_failed": True})
        break
    principal_action, principal_hessian = action_and_hessian(principal, z)
    competitor_action, competitor_hessian = action_and_hessian(competitor, z)
    raw_phase = principal_action.imag - competitor_action.imag
    if previous_raw_phase is None:
        unwrapped_phase = raw_phase
    else:
        increment = raw_phase - previous_raw_phase
        increment -= 2 * math.pi * round(increment / (2 * math.pi))
        unwrapped_phase += increment
    previous_raw_phase = raw_phase
    rows.append({
        "b": b,
        "principal_u": [principal.real, principal.imag],
        "competitor_u": [competitor.real, competitor.imag],
        "saddle_separation": abs(principal - competitor),
        "principal_hessian_absolute": abs(principal_hessian),
        "competitor_hessian_absolute": abs(competitor_hessian),
        "unwrapped_action_phase_difference": unwrapped_phase,
        "action_real_difference": principal_action.real - competitor_action.real,
    })

valid_rows = [row for row in rows if not row.get("continuation_failed")]
minimum_separation = min(valid_rows, key=lambda row: row["saddle_separation"])
phase_sign_changes = []
for left, right in zip(valid_rows, valid_rows[1:]):
    if left["unwrapped_action_phase_difference"] * right["unwrapped_action_phase_difference"] < 0:
        phase_sign_changes.append([left["b"], right["b"]])

result = {
    "fixed_real_z": a,
    "start_b": start_b,
    "step_b": step_b,
    "rows": rows,
    "minimum_saddle_separation_row": minimum_separation,
    "unwrapped_phase_sign_change_brackets": phase_sign_changes,
    "continuation_reached_final_sample": len(valid_rows) == sample_count,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-first-two-saddle-chamber-trace.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"valid_rows={len(valid_rows)}")
    print(f"minimum_saddle_separation_row={minimum_separation}")
    print(f"unwrapped_phase_sign_change_brackets={phase_sign_changes}")
    print(f"last_row={rows[-1]}")

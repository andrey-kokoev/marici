"""Trace the near-collision third saddle and its Stokes equality at a=1/2."""
import cmath
import json
import math
from pathlib import Path

from theta_complex_log_curvature_roots import phi_jets


def newton(seed, z, iterations=50):
    u = seed
    for _ in range(iterations):
        phi, first, second = phi_jets(u, 36, 2)
        equation = first + z * phi
        derivative = second + z * first
        if abs(derivative) < 1e-11:
            return None
        step = equation / derivative
        u -= step
        if abs(step) < 2e-13:
            return u
    return None


def action(u, z):
    phi = phi_jets(u, 36, 0)[0]
    return cmath.log(phi) + z * u


def trace_direction(start_b, end_b, step, principal_seed, third_seed):
    rows = []
    count = round((end_b - start_b) / step)
    principal, third = principal_seed, third_seed
    for index in range(count + 1):
        b = start_b + index * step
        z = complex(0.5, b)
        principal = newton(principal, z)
        third = newton(third, z)
        if principal is None or third is None:
            break
        principal_action = action(principal, z)
        third_action = action(third, z)
        delta = principal_action.imag - third_action.imag
        rows.append({
            "b": b,
            "principal_u": [principal.real, principal.imag],
            "third_u": [third.real, third.imag],
            "saddle_separation": abs(principal - third),
            "phase_equality_function_sin_half_delta": math.sin(delta / 2),
            "action_real_difference": principal_action.real - third_action.real,
        })
    return rows


start_b = 8.5
principal_seed = complex(0.19333059517162157, 0.4824525417875359)
third_seed = complex(0.2489351127033218, 0.6058677514517087)
downward = trace_direction(start_b, 8.0, -0.01, principal_seed, third_seed)
upward = trace_direction(start_b, 10.0, 0.01, principal_seed, third_seed)
rows = list(reversed(downward[1:])) + upward

brackets = []
for left, right in zip(rows, rows[1:]):
    if left["phase_equality_function_sin_half_delta"] * right["phase_equality_function_sin_half_delta"] < 0:
        brackets.append([left["b"], right["b"]])

minimum_separation = min(rows, key=lambda row: row["saddle_separation"])


def refine_bracket(bracket):
    left_b, right_b = bracket
    left_row = min(rows, key=lambda row: abs(row["b"] - left_b))
    right_row = min(rows, key=lambda row: abs(row["b"] - right_b))
    left_p, right_p = complex(*left_row["principal_u"]), complex(*right_row["principal_u"])
    left_t, right_t = complex(*left_row["third_u"]), complex(*right_row["third_u"])
    for _ in range(42):
        middle_b = (left_b + right_b) / 2
        z = complex(0.5, middle_b)
        middle_p = newton((left_p + right_p) / 2, z)
        middle_t = newton((left_t + right_t) / 2, z)
        delta = action(middle_p, z).imag - action(middle_t, z).imag
        value = math.sin(delta / 2)
        left_value = left_row["phase_equality_function_sin_half_delta"] if left_b == bracket[0] else None
        if left_value is None:
            left_delta = action(left_p, complex(0.5, left_b)).imag - action(left_t, complex(0.5, left_b)).imag
            left_value = math.sin(left_delta / 2)
        if left_value * value <= 0:
            right_b, right_p, right_t = middle_b, middle_p, middle_t
        else:
            left_b, left_p, left_t = middle_b, middle_p, middle_t
    b = (left_b + right_b) / 2
    z = complex(0.5, b)
    p = newton((left_p + right_p) / 2, z)
    t = newton((left_t + right_t) / 2, z)
    pa, ta = action(p, z), action(t, z)
    return {
        "b": b,
        "principal_u": [p.real, p.imag],
        "third_u": [t.real, t.imag],
        "action_imaginary_difference": pa.imag - ta.imag,
        "action_real_difference": pa.real - ta.real,
        "bracket_width": right_b - left_b,
    }


refined_walls = [refine_bracket(bracket) for bracket in brackets]


def upward_field(u, z):
    phi, first = phi_jets(u, 36, 1)
    gradient = first / phi + z
    return gradient.conjugate() / abs(gradient)


def rk4(u, z, step):
    k1 = upward_field(u, z)
    k2 = upward_field(u + step * k1 / 2, z)
    k3 = upward_field(u + step * k2 / 2, z)
    k4 = upward_field(u + step * k3, z)
    return u + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def upward_directions(saddle, z):
    phi, first, second = phi_jets(saddle, 36, 2)
    hessian = second / phi - (first / phi) ** 2
    direction = cmath.exp(-0.5j * cmath.phase(hessian))
    return direction, -direction


def trace_upward(saddle, z, direction, step=0.001, maximum_steps=3000):
    u = saddle + 1e-4 * direction
    previous = u
    for index in range(maximum_steps):
        following = rk4(u, z, step)
        if previous.imag * following.imag <= 0 and index > 3:
            fraction = abs(previous.imag) / (abs(previous.imag) + abs(following.imag))
            crossing_real = previous.real + fraction * (following.real - previous.real)
            field = upward_field(complex(crossing_real, 0), z)
            return {"real_axis_crossing": crossing_real, "oriented_sign": 1 if field.imag > 0 else -1}
        previous, u = u, following
        if abs(u.real) > 3 or abs(u.imag) > 0.775:
            break
    return {"real_axis_crossing": None, "terminal_u": [u.real, u.imag]}


flow_samples = []
third_seed_for_flow = third_seed
for b in (9.53, 9.60, 9.66):
    z = complex(0.5, b)
    third_seed_for_flow = newton(third_seed_for_flow, z)
    flow_samples.append({
        "b": b,
        "third_u": [third_seed_for_flow.real, third_seed_for_flow.imag],
        "upward_branches": [
            trace_upward(third_seed_for_flow, z, direction)
            for direction in upward_directions(third_seed_for_flow, z)
        ],
    })
result = {
    "fixed_real_z": 0.5,
    "b_range": [rows[0]["b"], rows[-1]["b"]],
    "step_b": 0.01,
    "rows": rows,
    "phase_equality_brackets": brackets,
    "minimum_separation_row": minimum_separation,
    "refined_stokes_walls": refined_walls,
    "third_saddle_upward_flow_samples": flow_samples,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-third-saddle-stokes-trace.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"row_count={len(rows)}")
    print(f"phase_equality_brackets={brackets}")
    print(f"minimum_separation_row={minimum_separation}")
    print(f"refined_stokes_walls={refined_walls}")
    print(f"third_saddle_upward_flow_samples={flow_samples}")

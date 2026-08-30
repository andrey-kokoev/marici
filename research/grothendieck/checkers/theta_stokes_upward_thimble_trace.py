"""Trace upward thimbles near the first principal action-phase equality."""
import cmath
import json
import math
from pathlib import Path

from theta_complex_log_curvature_roots import phi_jets
from theta_completed_saddle_stokes_scan import saddle_newton


def logarithmic_gradient(u, z):
    phi, first = phi_jets(u, 36, 1)
    return first / phi + z


def unit_upward_field(u, z):
    gradient = logarithmic_gradient(u, z)
    magnitude = abs(gradient)
    if magnitude < 1e-14:
        return None
    return gradient.conjugate() / magnitude


def unit_downward_field(u, z):
    field = unit_upward_field(u, z)
    return None if field is None else -field


def rk4_step(u, z, step):
    k1 = unit_upward_field(u, z)
    if k1 is None:
        return None
    k2 = unit_upward_field(u + step * k1 / 2, z)
    k3 = unit_upward_field(u + step * k2 / 2, z) if k2 is not None else None
    k4 = unit_upward_field(u + step * k3, z) if k3 is not None else None
    if None in (k2, k3, k4):
        return None
    return u + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def rk4_downward_step(u, z, step):
    def field(value):
        return unit_downward_field(value, z)
    k1 = field(u)
    if k1 is None:
        return None
    k2 = field(u + step * k1 / 2)
    k3 = field(u + step * k2 / 2) if k2 is not None else None
    k4 = field(u + step * k3) if k3 is not None else None
    if None in (k2, k3, k4):
        return None
    return u + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def upward_directions(saddle, z):
    phi, first, second = phi_jets(saddle, 36, 2)
    hessian = second / phi - (first / phi) ** 2
    direction = cmath.exp(-0.5j * cmath.phase(hessian))
    return direction, -direction


def downward_directions(saddle, z):
    upward = upward_directions(saddle, z)[0]
    direction = 1j * upward
    return direction, -direction


def completed_action(u, z):
    phi = phi_jets(u, 36, 0)[0]
    return cmath.log(phi) + z * u


def completed_integrand(u, z):
    return cmath.exp(z * u) * phi_jets(u, 36, 0)[0]


def trace_downward_branch(saddle, z, direction, step=0.001, maximum_steps=12000):
    u = saddle + 1e-4 * direction
    initial_action = completed_action(u, z)
    integral = 0j
    moment = 0j
    second_moment = 0j
    source_zeros = (
        complex(0, 0.6388300536005935),
        complex(0.2556475134765196, 0.6955398322128286),
    )
    reached_source_zero = False
    source_zero_index = None
    for index in range(maximum_steps):
        following = rk4_downward_step(u, z, step)
        if following is None:
            break
        value_u = completed_integrand(u, z)
        value_following = completed_integrand(following, z)
        increment = following - u
        integral += (value_u + value_following) * increment / 2
        moment += (2 * u * value_u + 2 * following * value_following) * increment / 2
        second_moment += ((2 * u) ** 2 * value_u + (2 * following) ** 2 * value_following) * increment / 2
        u = following
        action = completed_action(u, z)
        nearest_index, source_zero = min(
            enumerate(source_zeros), key=lambda item: abs(u - item[1])
        )
        if abs(u - source_zero) < 5e-3:
            segment_start = u
            segment_steps = 100
            for segment_index in range(segment_steps):
                left = segment_start + (source_zero - segment_start) * segment_index / segment_steps
                right = segment_start + (source_zero - segment_start) * (segment_index + 1) / segment_steps
                value_left = completed_integrand(left, z)
                value_right = completed_integrand(right, z)
                increment = right - left
                integral += (value_left + value_right) * increment / 2
                moment += (2 * left * value_left + 2 * right * value_right) * increment / 2
                second_moment += ((2 * left) ** 2 * value_left + (2 * right) ** 2 * value_right) * increment / 2
            u = source_zero
            reached_source_zero = True
            source_zero_index = nearest_index
            break
        if action.real < initial_action.real - 30:
            break
        if abs(u.real) > 3 or abs(u.imag) > 0.775:
            break
    terminal_action = completed_action(u, z)
    return {
        "terminal_u": [u.real, u.imag],
        "steps_taken": index + 1,
        "real_action_drop": initial_action.real - terminal_action.real,
        "imaginary_action_drift": terminal_action.imag - initial_action.imag,
        "reached_30_action_drop": initial_action.real - terminal_action.real >= 30,
        "reached_source_zero": reached_source_zero,
        "relative_source_zero_index": source_zero_index,
        "reached_shared_source_zero": reached_source_zero and source_zero_index == 0,
        "outward_integral": [integral.real, integral.imag],
        "outward_log_moment": [moment.real, moment.imag],
        "outward_log_second_moment": [second_moment.real, second_moment.imag],
    }


def trace_branch(saddle, z, direction, step=0.001, maximum_steps=12000):
    u = saddle + 1e-4 * direction
    previous = u
    minimum_imaginary_absolute = abs(u.imag)
    intersection = None
    for index in range(maximum_steps):
        following = rk4_step(u, z, step)
        if following is None:
            break
        minimum_imaginary_absolute = min(minimum_imaginary_absolute, abs(following.imag))
        if previous.imag * following.imag <= 0 and index > 3:
            fraction = abs(previous.imag) / (abs(previous.imag) + abs(following.imag))
            crossing_real = previous.real + fraction * (following.real - previous.real)
            crossing_field = unit_upward_field(complex(crossing_real, 0), z)
            intersection = {
                "real_u": crossing_real,
                "step_index": index,
                "upward_flow_real_component": crossing_field.real,
                "upward_flow_imaginary_component": crossing_field.imag,
                "oriented_intersection_sign_against_positive_real_contour": (
                    1 if crossing_field.imag > 0 else -1
                ),
            }
            break
        previous, u = u, following
        if abs(u.real) > 3 or abs(u.imag) > 0.775:
            break
    return {
        "intersection_with_real_axis": intersection,
        "minimum_abs_imag_u": minimum_imaginary_absolute,
        "terminal_u": [u.real, u.imag],
        "steps_taken": index + 1,
    }


principal_seed = complex(0.08401358911356424, 0.38179499285876844)
competitor_seed = complex(-0.05825544402510956, 0.4629646570392176)
b_values = [5.95, 5.988285289982947, 6.03]
rows = []
for b in b_values:
    z = complex(0.5, b)
    principal = saddle_newton(principal_seed, z, max_label=36)
    competitor = saddle_newton(competitor_seed, z, max_label=36)
    row = {"b": b, "saddles": {}}
    for name, saddle in (("principal", principal), ("competitor", competitor)):
        traces = [trace_branch(saddle, z, direction) for direction in upward_directions(saddle, z)]
        row["saddles"][name] = {"u": [saddle.real, saddle.imag], "upward_branches": traces}
    rows.append(row)

resolution_audit = []
for b in (5.95, 6.03):
    z = complex(0.5, b)
    competitor = saddle_newton(competitor_seed, z, max_label=36)
    crossing_direction = upward_directions(competitor, z)[0]
    resolution_audit.append({
        "b": b,
        "traces": [
            {"step": step, **trace_branch(competitor, z, crossing_direction, step=step)}
            for step in (0.002, 0.001, 0.0005)
        ],
    })

downward_audit = []
z_above = complex(0.5, 6.03)
for name, seed in (("principal", principal_seed), ("competitor", competitor_seed)):
    saddle = saddle_newton(seed, z_above, max_label=36)
    downward_audit.append({
        "saddle": name,
        "u": [saddle.real, saddle.imag],
        "branches": [
            trace_downward_branch(saddle, z_above, direction)
            for direction in downward_directions(saddle, z_above)
        ],
    })


def as_complex(pair):
    return complex(*pair)


downward_by_name = {item["saddle"]: item for item in downward_audit}
principal_zero = next(branch for branch in downward_by_name["principal"]["branches"] if branch["reached_shared_source_zero"])
principal_tail = next(branch for branch in downward_by_name["principal"]["branches"] if not branch["reached_shared_source_zero"])
competitor_zero = next(branch for branch in downward_by_name["competitor"]["branches"] if branch["reached_shared_source_zero"])
competitor_tail = next(branch for branch in downward_by_name["competitor"]["branches"] if not branch["reached_shared_source_zero"])
principal_integral = -as_complex(principal_zero["outward_integral"]) + as_complex(principal_tail["outward_integral"])
principal_moment = -as_complex(principal_zero["outward_log_moment"]) + as_complex(principal_tail["outward_log_moment"])
competitor_integral = -as_complex(competitor_tail["outward_integral"]) + as_complex(competitor_zero["outward_integral"])
competitor_moment = -as_complex(competitor_tail["outward_log_moment"]) + as_complex(competitor_zero["outward_log_moment"])
paired_integral = principal_integral + competitor_integral
paired_moment = principal_moment + competitor_moment
paired_barycenter = paired_moment / paired_integral
pair_radius_squared = 0.25 + z_above.imag**2
pair_alpha = 1 - 0.5 / (2 * pair_radius_squared)
pair_beta = 2 * z_above.imag + z_above.imag / (2 * pair_radius_squared)
exact_pair_diagnostic = {
    "principal_integral": [principal_integral.real, principal_integral.imag],
    "competitor_integral": [competitor_integral.real, competitor_integral.imag],
    "paired_integral": [paired_integral.real, paired_integral.imag],
    "paired_log_moment": [paired_moment.real, paired_moment.imag],
    "paired_log_barycenter": [paired_barycenter.real, paired_barycenter.imag],
    "paired_outer_cone": pair_beta * paired_barycenter.real + pair_alpha * paired_barycenter.imag,
    "tail_action_drop_target": 30,
    "interval_certified": False,
}

result = {
    "fixed_real_z": 0.5,
    "stokes_candidate_b": 5.988285289982947,
    "rows": rows,
    "competitor_crossing_resolution_audit": resolution_audit,
    "downward_branch_audit_at_stokes_b": downward_audit,
    "oriented_plus_pair_thimble_quadrature": exact_pair_diagnostic,
    "flow": "du/ds=conjugate(S_prime)/abs(S_prime)",
    "original_contour": "real u axis",
    "intersection_numbers_certified": False,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-stokes-upward-thimble-trace.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(f"b={row['b']}")
        for name, saddle in row["saddles"].items():
            print(f"  {name} u={saddle['u']} branches={saddle['upward_branches']}")
    print(f"competitor_crossing_resolution_audit={resolution_audit}")
    print(f"downward_branch_audit_at_stokes_b={downward_audit}")
    print(f"oriented_plus_pair_thimble_quadrature={exact_pair_diagnostic}")

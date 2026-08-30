"""Reconnaissance of completed theta saddle actions along z=1/2+ib."""
import cmath
import json
import math
from pathlib import Path

from theta_complex_log_curvature_roots import phi_jets


def saddle_newton(seed, z, max_label=28, iterations=50):
    u = seed
    for _ in range(iterations):
        if not (math.isfinite(u.real) and math.isfinite(u.imag)):
            return None
        if abs(u.real) > 2 or abs(u.imag) >= 0.75:
            return None
        try:
            phi, first, second = phi_jets(u, max_label, 2)
        except OverflowError:
            return None
        equation = first + z * phi
        derivative = second + z * first
        if abs(derivative) < 1e-250:
            return None
        step = equation / derivative
        u -= step
        if abs(step) < 2e-12:
            residual = abs(equation) / (abs(first) + abs(z * phi))
            return u if residual < 1e-9 else None
    return None


def saddle_census(z):
    roots = []
    for real_index in range(-10, 11, 2):
        for imag_index in range(-14, 15, 2):
            seed = complex(real_index / 10, imag_index / 20)
            root = saddle_newton(seed, z)
            if root is None or not (-1.5 < root.real < 1.5 and abs(root.imag) < 0.74):
                continue
            if any(abs(root - known) < 1e-7 for known in roots):
                continue
            roots.append(root)
    roots.sort(key=lambda value: (abs(value), value.real, value.imag))
    saddles = []
    for root in roots:
        phi, first, second = phi_jets(root, 36, 2)
        equation = first + z * phi
        action = cmath.log(phi) + z * root
        hessian = second / phi - (first / phi) ** 2
        saddles.append({
            "u": [root.real, root.imag],
            "relative_equation_residual": abs(equation) / (abs(first) + abs(z * phi)),
            "action": [action.real, action.imag],
            "hessian_absolute": abs(hessian),
        })
    closest_pair = None
    for left_index in range(len(saddles)):
        for right_index in range(left_index + 1, len(saddles)):
            delta = saddles[left_index]["action"][1] - saddles[right_index]["action"][1]
            phase_distance = abs(math.sin(delta / 2))
            candidate = {
                "indices": [left_index, right_index],
                "mod_2pi_phase_distance_sine": phase_distance,
                "real_action_difference": saddles[left_index]["action"][0] - saddles[right_index]["action"][0],
            }
            if closest_pair is None or phase_distance < closest_pair["mod_2pi_phase_distance_sine"]:
                closest_pair = candidate
    return saddles, closest_pair


a = 0.5
b_values = [index / 2 for index in range(20)]
rows = []
for b in b_values:
    z = complex(a, b)
    saddles, closest_pair = saddle_census(z)
    rows.append({"b": b, "saddle_count": len(saddles), "saddles": saddles, "closest_action_phase_pair": closest_pair})

# Track the saddle born on the positive real source axis.
previous_u = None
for row in rows:
    saddle_values = [complex(*item["u"]) for item in row["saddles"]]
    if not saddle_values:
        row["principal_saddle_index"] = None
        row["principal_closest_phase_competitor"] = None
        continue
    if previous_u is None:
        eligible = [(index, value) for index, value in enumerate(saddle_values) if value.real > 0]
        principal_index, principal_u = min(eligible, key=lambda pair: abs(pair[1].imag))
    else:
        principal_index, principal_u = min(enumerate(saddle_values), key=lambda pair: abs(pair[1] - previous_u))
    previous_u = principal_u
    principal_action = row["saddles"][principal_index]["action"]
    competitors = []
    for index, saddle in enumerate(row["saddles"]):
        if index == principal_index:
            continue
        delta = principal_action[1] - saddle["action"][1]
        competitors.append({
            "index": index,
            "mod_2pi_phase_distance_sine": abs(math.sin(delta / 2)),
            "real_action_difference": principal_action[0] - saddle["action"][0],
        })
    row["principal_saddle_index"] = principal_index
    row["principal_saddle_u"] = [principal_u.real, principal_u.imag]
    row["principal_closest_phase_competitor"] = min(
        competitors, key=lambda item: item["mod_2pi_phase_distance_sine"]
    ) if competitors else None

nontrivial_pairs = [row for row in rows if row["closest_action_phase_pair"] is not None]
closest_row = min(
    nontrivial_pairs,
    key=lambda row: row["closest_action_phase_pair"]["mod_2pi_phase_distance_sine"],
) if nontrivial_pairs else None


def action_at_saddle(u, z):
    phi = phi_jets(u, 36, 0)[0]
    return cmath.log(phi) + z * u


# Refine the phase equality between the physical branch and its persistent
# nearby competitor, bracketed by b=5.5 and b=6.0.
left_b, right_b = 5.5, 6.0
left_row = next(row for row in rows if row["b"] == left_b)
right_row = next(row for row in rows if row["b"] == right_b)
left_principal = complex(*left_row["principal_saddle_u"])
right_principal = complex(*right_row["principal_saddle_u"])
left_competitor = complex(*left_row["saddles"][left_row["principal_closest_phase_competitor"]["index"]]["u"])
right_competitor = complex(*right_row["saddles"][right_row["principal_closest_phase_competitor"]["index"]]["u"])

for _ in range(45):
    middle_b = (left_b + right_b) / 2
    z = complex(a, middle_b)
    principal_seed = (left_principal + right_principal) / 2
    competitor_seed = (left_competitor + right_competitor) / 2
    middle_principal = saddle_newton(principal_seed, z, max_label=36)
    middle_competitor = saddle_newton(competitor_seed, z, max_label=36)
    principal_action = action_at_saddle(middle_principal, z)
    competitor_action = action_at_saddle(middle_competitor, z)
    phase_difference = principal_action.imag - competitor_action.imag
    if phase_difference > 0:
        right_b = middle_b
        right_principal = middle_principal
        right_competitor = middle_competitor
    else:
        left_b = middle_b
        left_principal = middle_principal
        left_competitor = middle_competitor

stokes_b = (left_b + right_b) / 2
stokes_z = complex(a, stokes_b)
stokes_principal = saddle_newton((left_principal + right_principal) / 2, stokes_z, max_label=36)
stokes_competitor = saddle_newton((left_competitor + right_competitor) / 2, stokes_z, max_label=36)
stokes_principal_action = action_at_saddle(stokes_principal, stokes_z)
stokes_competitor_action = action_at_saddle(stokes_competitor, stokes_z)
refined_stokes_candidate = {
    "z": [a, stokes_b],
    "principal_u": [stokes_principal.real, stokes_principal.imag],
    "competitor_u": [stokes_competitor.real, stokes_competitor.imag],
    "action_imaginary_difference": stokes_principal_action.imag - stokes_competitor_action.imag,
    "action_real_difference": stokes_principal_action.real - stokes_competitor_action.real,
    "b_bracket_width": right_b - left_b,
    "intersection_number_change_established": False,
}
stokes_radius_squared = a * a + stokes_b * stokes_b
stokes_alpha = 2 * a - a / (2 * stokes_radius_squared)
stokes_beta = 2 * stokes_b + stokes_b / (2 * stokes_radius_squared)


def saddle_log_barycenter_cone(u):
    # Since log(x)=2u, this is the leading saddle proxy for M(z).
    return stokes_beta * (2 * u.real) + stokes_alpha * (2 * u.imag)


principal_cone = saddle_log_barycenter_cone(stokes_principal)
competitor_cone = saddle_log_barycenter_cone(stokes_competitor)
principal_weight = math.exp(stokes_principal_action.real)
competitor_weight = math.exp(stokes_competitor_action.real)
plus_pair_cone = (
    principal_weight * principal_cone + competitor_weight * competitor_cone
) / (principal_weight + competitor_weight)
refined_stokes_candidate["saddle_log_barycenter_cone_proxy"] = {
    "principal": principal_cone,
    "competitor": competitor_cone,
    "competitor_to_principal_weight_ratio": competitor_weight / principal_weight,
    "canonical_plus_pair": plus_pair_cone,
    "picard_lefschetz_orientation_sign_determined": False,
}

result = {
    "fixed_real_z": a,
    "b_values": b_values,
    "rows": rows,
    "closest_sampled_action_phase_approach": closest_row,
    "refined_principal_stokes_candidate": refined_stokes_candidate,
    "intersection_numbers_computed": False,
    "stokes_transition_certified": False,
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-completed-saddle-stokes-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(
            f"b={row['b']:.1f} saddles={row['saddle_count']} "
            f"principal_u={row.get('principal_saddle_u')} "
            f"principal_closest={row.get('principal_closest_phase_competitor')}"
        )
    print(f"refined_principal_stokes_candidate={refined_stokes_candidate}")

"""WP287: exact interval-robust gate for a calibrated domain selector."""

import json
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def energy(configuration, edges, edge_values, biases):
    return -sum(edge_values[k] * configuration[i] * configuration[j] for k, (i, j) in enumerate(edges)) - sum(
        biases[i] * configuration[i] for i in range(len(configuration))
    )


def flip(configuration, index):
    changed = list(configuration)
    changed[index] *= -1
    return tuple(changed)


def incident_upper_sums(vertex_count, edges, edge_intervals):
    totals = [sp.S.Zero] * vertex_count
    for (i, j), (_, upper) in zip(edges, edge_intervals):
        totals[i] += upper
        totals[j] += upper
    return totals


def corner_audit(vertex_count, edges, edge_intervals, bias_intervals):
    configurations = list(product((-1, 1), repeat=vertex_count))
    all_minus = (-1,) * vertex_count
    all_plus = (1,) * vertex_count
    corners = []
    all_monotone = True
    hostile_corner = None
    for edge_choice in product((0, 1), repeat=len(edges)):
        edge_values = [edge_intervals[k][choice] for k, choice in enumerate(edge_choice)]
        for bias_choice in product((0, 1), repeat=vertex_count):
            biases = [bias_intervals[k][choice] for k, choice in enumerate(bias_choice)]
            corner_monotone = True
            for configuration in configurations:
                base = energy(configuration, edges, edge_values, biases)
                for index, spin in enumerate(configuration):
                    cost = energy(flip(configuration, index), edges, edge_values, biases) - base
                    corner_monotone = corner_monotone and (cost < 0 if spin == -1 else cost > 0)
            if not corner_monotone and hostile_corner is None:
                base = energy(all_minus, edges, edge_values, biases)
                costs = [energy(flip(all_minus, i), edges, edge_values, biases) - base for i in range(vertex_count)]
                hostile_corner = {
                    "edge_values": [str(value) for value in edge_values],
                    "biases": [str(value) for value in biases],
                    "all_minus_flip_costs": [str(value) for value in costs],
                    "all_minus_is_local_minimum": all(cost >= 0 for cost in costs),
                }
            all_monotone = all_monotone and corner_monotone
            corners.append(corner_monotone)
    worst_edges = [upper for _, upper in edge_intervals]
    worst_biases = [lower for lower, _ in bias_intervals]
    worst_base = energy(all_minus, edges, worst_edges, worst_biases)
    worst_costs = [energy(flip(all_minus, i), edges, worst_edges, worst_biases) - worst_base for i in range(vertex_count)]
    return {
        "corner_count": len(corners),
        "all_corners_strictly_monotone": bool(all_monotone),
        "first_nonmonotone_corner": hostile_corner,
        "low_bias_high_wall_completion": {
            "edge_values": [str(value) for value in worst_edges],
            "biases": [str(value) for value in worst_biases],
            "all_minus_flip_costs": [str(value) for value in worst_costs],
            "all_minus_is_local_minimum": all(cost >= 0 for cost in worst_costs),
        },
        "favored_state": list(all_plus),
    }


def main():
    edges = [(0, 1), (1, 2), (0, 2)]
    edge_intervals = [
        (sp.Rational(9, 10), sp.Rational(11, 10)),
        (sp.Rational(9, 5), sp.Rational(11, 5)),
        (sp.Rational(27, 10), sp.Rational(33, 10)),
    ]
    upper_wall_budgets = incident_upper_sums(3, edges, edge_intervals)
    robust_bias_intervals = [
        (sp.Rational(23, 5), sp.Rational(5)),
        (sp.Rational(7, 2), sp.Rational(39, 10)),
        (sp.Rational(57, 10), sp.Rational(61, 10)),
    ]
    nominal_only_bias_intervals = [
        (sp.Rational(39, 10), sp.Rational(9, 2)),
        (sp.Rational(29, 10), sp.Rational(7, 2)),
        (sp.Rational(49, 10), sp.Rational(11, 2)),
    ]
    central_edges = [sum(interval) / 2 for interval in edge_intervals]
    central_biases = [sum(interval) / 2 for interval in nominal_only_bias_intervals]
    central_incident = incident_upper_sums(3, edges, [(value, value) for value in central_edges])

    robust = corner_audit(3, edges, edge_intervals, robust_bias_intervals)
    nominal_only = corner_audit(3, edges, edge_intervals, nominal_only_bias_intervals)
    robust_margins = [lower - wall for (lower, _), wall in zip(robust_bias_intervals, upper_wall_budgets)]

    checks = {
        "nominal_centers_pass_local_selector": all(bias > wall for bias, wall in zip(central_biases, central_incident)),
        "robust_lower_biases_exceed_upper_wall_budgets": all(margin > 0 for margin in robust_margins),
        "all_robust_interval_corners_are_strictly_monotone": robust["all_corners_strictly_monotone"],
        "nominally_passing_packet_fails_under_uncertainty": not nominal_only["all_corners_strictly_monotone"],
        "hostile_completion_traps_wrong_uniform_state": nominal_only["low_bias_high_wall_completion"]["all_minus_is_local_minimum"],
        "all_interval_corners_were_enumerated": robust["corner_count"] == 64 and nominal_only["corner_count"] == 64,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP287",
        "theorem_domain": "independent closed calibration intervals for positive heterogeneous edge tensions and local biases on a finite graph",
        "robust_selector_condition": "for every vertex i, lower(h_i) > sum_j upper(J_ij)",
        "upper_incident_wall_budgets": [str(value) for value in upper_wall_budgets],
        "robust_bias_intervals": [[str(value) for value in interval] for interval in robust_bias_intervals],
        "robust_margins": [str(value) for value in robust_margins],
        "robust_corner_audit": robust,
        "nominal_only_bias_intervals": [[str(value) for value in interval] for interval in nominal_only_bias_intervals],
        "nominal_centers": {
            "edge_values": [str(value) for value in central_edges],
            "incident_wall_budgets": [str(value) for value in central_incident],
            "biases": [str(value) for value in central_biases],
        },
        "nominal_only_corner_audit": nominal_only,
        "classification": "robust conditional selector certificate only when worst-case calibrated local margins are positive; nominal rank or central values do not suffice",
        "smallest_exact_falsifier": "the nominal central weighted triangle passes every local inequality, but its low-bias/high-wall admitted corner traps all-minus",
        "remaining_physical_instrument_gate": "obtain joint source-calibrated uncertainty sets, including correlations and support, and propagate them through actual dynamics and the branch-to-physical16 map",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp287_robust_calibrated_domain_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

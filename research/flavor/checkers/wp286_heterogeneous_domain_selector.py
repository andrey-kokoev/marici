"""WP286: exact local criterion for heterogeneous biased domain selection."""

import json
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def energy(configuration, weighted_edges, biases):
    wall = -sum(weight * configuration[i] * configuration[j] for i, j, weight in weighted_edges)
    source = -sum(biases[i] * configuration[i] for i in range(len(configuration)))
    return wall + source


def flip(configuration, index):
    changed = list(configuration)
    changed[index] *= -1
    return tuple(changed)


def incident_weights(vertex_count, weighted_edges):
    totals = [sp.S.Zero] * vertex_count
    for i, j, weight in weighted_edges:
        totals[i] += weight
        totals[j] += weight
    return totals


def exhaustive_audit(vertex_count, weighted_edges, biases):
    all_plus = (1,) * vertex_count
    configurations = list(product((-1, 1), repeat=vertex_count))
    minus_costs = []
    plus_costs = []
    local_minima = []
    strict_paths = True
    for configuration in configurations:
        base = energy(configuration, weighted_edges, biases)
        costs = [energy(flip(configuration, i), weighted_edges, biases) - base for i in range(vertex_count)]
        if all(cost >= 0 for cost in costs):
            local_minima.append(configuration)
        for spin, cost in zip(configuration, costs):
            (minus_costs if spin == -1 else plus_costs).append(cost)

        current = configuration
        prior = base
        while -1 in current:
            current = flip(current, current.index(-1))
            following = energy(current, weighted_edges, biases)
            strict_paths = strict_paths and following < prior
            prior = following
        strict_paths = strict_paths and current == all_plus
    return {
        "minimum_minus_flip_margin": str(-max(minus_costs)),
        "minimum_plus_flip_margin": str(min(plus_costs)),
        "local_minima": [list(cfg) for cfg in local_minima],
        "unique_favored_local_minimum": local_minima == [all_plus],
        "all_canonical_paths_strict": bool(strict_paths),
    }


def main():
    local_bias, incident_sum = sp.symbols("local_bias incident_sum", positive=True)
    worst_minus_cost = 2 * (incident_sum - local_bias)
    worst_plus_cost = 2 * (local_bias - incident_sum)

    edges = [(0, 1, sp.Rational(1)), (1, 2, sp.Rational(2)), (0, 2, sp.Rational(3))]
    incident = incident_weights(3, edges)
    admitted_biases = [weight + 1 for weight in incident]
    hostile_biases = [sp.Rational(3), sp.Rational(5, 2), sp.Rational(4)]
    admitted = exhaustive_audit(3, edges, admitted_biases)
    hostile = exhaustive_audit(3, edges, hostile_biases)
    all_minus = [-1, -1, -1]

    checks = {
        "symbolic_minus_cost_negative_exactly_above_local_threshold": sp.simplify(worst_minus_cost.subs(local_bias, incident_sum + 1)) == -2,
        "symbolic_plus_cost_positive_exactly_above_local_threshold": sp.simplify(worst_plus_cost.subs(local_bias, incident_sum + 1)) == 2,
        "admitted_packet_satisfies_every_local_inequality": all(bias > weight for bias, weight in zip(admitted_biases, incident)),
        "admitted_packet_has_unique_favored_local_minimum": admitted["unique_favored_local_minimum"],
        "admitted_packet_paths_are_strict": admitted["all_canonical_paths_strict"],
        "hostile_packet_has_positive_total_bias": sum(hostile_biases) > 0,
        "hostile_packet_violates_every_local_inequality": all(bias < weight for bias, weight in zip(hostile_biases, incident)),
        "hostile_packet_traps_wrong_uniform_vacuum": all_minus in hostile["local_minima"],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP286",
        "theorem_domain": "finite undirected graph with positive heterogeneous edge tensions J_ij, positive vertex biases h_i, and zero-temperature single-spin descent",
        "necessary_and_sufficient_uniform_monotonicity_condition": "for every vertex i, h_i > sum_j J_ij",
        "exact_worst_case_costs_at_vertex_i": {
            "minus_to_plus": str(worst_minus_cost),
            "plus_to_minus": str(worst_plus_cost),
        },
        "weighted_triangle": {
            "edges": [[i, j, str(weight)] for i, j, weight in edges],
            "incident_weight_sums": [str(value) for value in incident],
            "admitted_biases": [str(value) for value in admitted_biases],
            "admitted_audit": admitted,
            "hostile_biases": [str(value) for value in hostile_biases],
            "hostile_audit": hostile,
        },
        "classification": "local conditional branch selector only when every source bias dominates its incident wall budget; a global or averaged bias certificate is nonfaithful",
        "smallest_exact_falsifier": "weighted triangle J_01=1, J_12=2, J_02=3 with biases (3,5/2,4): total bias is positive, but all-minus is a strict local minimum because every h_i is below its incident wall budget",
        "remaining_physical_instrument_gate": "derive spatially resolved h_i and J_ij in one calibrated source frame, the physical update law and uncertainty bounds, then provide the branch-to-physical16 map",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp286_heterogeneous_domain_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

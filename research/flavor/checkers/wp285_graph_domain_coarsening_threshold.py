"""WP285: exact graph-topology threshold for biased domain coarsening."""

import json
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def energy(configuration, edges, wall_tension, bias):
    return -wall_tension * sum(configuration[i] * configuration[j] for i, j in edges) - bias * sum(configuration)


def flip(configuration, index):
    changed = list(configuration)
    changed[index] *= -1
    return tuple(changed)


def degrees(vertex_count, edges):
    result = [0] * vertex_count
    for i, j in edges:
        result[i] += 1
        result[j] += 1
    return result


def local_minima(vertex_count, edges, wall_tension, bias):
    configurations = product((-1, 1), repeat=vertex_count)
    return [
        cfg
        for cfg in configurations
        if all(energy(flip(cfg, i), edges, wall_tension, bias) >= energy(cfg, edges, wall_tension, bias) for i in range(vertex_count))
    ]


def monotone_minus_path(configuration, edges, wall_tension, bias):
    current = configuration
    record = [energy(current, edges, wall_tension, bias)]
    while -1 in current:
        current = flip(current, current.index(-1))
        record.append(energy(current, edges, wall_tension, bias))
    return current, record


def audit_graph(name, vertex_count, edges):
    graph_degrees = degrees(vertex_count, edges)
    maximum_degree = max(graph_degrees)
    weak_bias = maximum_degree - 1
    strong_bias = maximum_degree + 1
    all_minus = (-1,) * vertex_count
    all_plus = (1,) * vertex_count
    weak_minima = local_minima(vertex_count, edges, 1, weak_bias)
    strong_minima = local_minima(vertex_count, edges, 1, strong_bias)
    paths = [monotone_minus_path(cfg, edges, 1, strong_bias) for cfg in product((-1, 1), repeat=vertex_count)]
    paths_strict = all(
        final == all_plus
        and len(record) - 1 == cfg.count(-1)
        and all(after < before for before, after in zip(record, record[1:]))
        for cfg, (final, record) in zip(product((-1, 1), repeat=vertex_count), paths)
    )
    return {
        "name": name,
        "vertex_count": vertex_count,
        "degrees": graph_degrees,
        "maximum_degree": maximum_degree,
        "weak_bias": weak_bias,
        "strong_bias": strong_bias,
        "wrong_uniform_vacuum_is_weak_local_minimum": all_minus in weak_minima,
        "strong_local_minima": [list(cfg) for cfg in strong_minima],
        "strong_unique_minimum_is_all_plus": strong_minima == [all_plus],
        "all_enumerated_strong_paths_strict": paths_strict,
    }


def main():
    wall_tension, bias, degree = sp.symbols("wall_tension bias degree", positive=True)
    worst_minus_flip_cost = 2 * (wall_tension * degree - bias)
    worst_plus_flip_cost = 2 * (bias - wall_tension * degree)

    triangle = [(0, 1), (1, 2), (0, 2)]
    cycle5 = [(i, (i + 1) % 5) for i in range(5)]
    complete4 = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    audits = [
        audit_graph("triangle", 3, triangle),
        audit_graph("cycle_5", 5, cycle5),
        audit_graph("complete_4", 4, complete4),
    ]
    checks = {
        "worst_minus_cost_is_negative_above_threshold": sp.simplify(worst_minus_flip_cost.subs(bias, wall_tension * degree + 1)) < 0,
        "worst_plus_cost_is_positive_above_threshold": sp.simplify(worst_plus_flip_cost.subs(bias, wall_tension * degree + 1)) > 0,
        "regular_graphs_trap_wrong_vacuum_below_threshold": all(audit["wrong_uniform_vacuum_is_weak_local_minimum"] for audit in audits),
        "above_threshold_unique_local_minimum_is_favored_vacuum": all(audit["strong_unique_minimum_is_all_plus"] for audit in audits),
        "above_threshold_every_enumerated_configuration_has_strict_path": all(audit["all_enumerated_strong_paths_strict"] for audit in audits),
        "triangle_exactly_realizes_smallest_stated_falsifier": audits[0]["wrong_uniform_vacuum_is_weak_local_minimum"] and audits[0]["weak_bias"] == 1,
        "topology_changes_numeric_threshold": audits[1]["maximum_degree"] != audits[2]["maximum_degree"],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP285",
        "theorem_domain": "finite undirected graph Ising domains with uniform J>0, uniform h>0, and zero-temperature single-spin energy descent",
        "exact_worst_case_flip_costs": {
            "minus_to_plus": str(worst_minus_flip_cost),
            "plus_to_minus": str(worst_plus_flip_cost),
        },
        "topology_uniform_monotone_threshold": "h>J*Delta, where Delta is maximum graph degree",
        "audited_graphs": audits,
        "classification": "conditional graph-domain branch selector above a topology-dependent threshold; neither a physical16 selector nor an instrument until J, h, graph geometry, and dynamics are source-derived",
        "smallest_exact_falsifier": "on the triangle, J=1 and h=1 favor plus globally but all-minus is a strict local minimum because each first flip costs 2",
        "remaining_physical_instrument_gate": "derive the domain adjacency or continuum geometry, J and h normalization, allowed update law, temperature, tunneling, expansion, defects, runtime, and mapping from the selected branch to physical16",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp285_graph_domain_coarsening_threshold.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

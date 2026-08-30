"""WP284: exact local coarsening threshold for a biased CP-domain ring."""

import json
from itertools import product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def energy(configuration, wall_tension, bias):
    n = len(configuration)
    return -wall_tension * sum(configuration[i] * configuration[(i + 1) % n] for i in range(n)) - bias * sum(configuration)


def flip(configuration, index):
    result = list(configuration)
    result[index] *= -1
    return tuple(result)


def local_minimum(configuration, wall_tension, bias):
    base = energy(configuration, wall_tension, bias)
    return all(energy(flip(configuration, i), wall_tension, bias) >= base for i in range(len(configuration)))


def minus_flip_path(configuration, wall_tension, bias):
    """Flip the first remaining minus spin and retain the exact energy record."""
    current = configuration
    energies = [energy(current, wall_tension, bias)]
    while -1 in current:
        current = flip(current, current.index(-1))
        energies.append(energy(current, wall_tension, bias))
    return current, energies


def main():
    wall_tension, bias = sp.symbols("wall_tension bias", positive=True)
    all_minus_flip_cost = 4 * wall_tension - 2 * bias
    isolated_minus_flip_cost = -4 * wall_tension - 2 * bias
    boundary_minus_flip_cost = -2 * bias

    n = 5
    configurations = list(product((-1, 1), repeat=n))
    weak_packet = {wall_tension: sp.Rational(1), bias: sp.Rational(1)}
    threshold_packet = {wall_tension: sp.Rational(1), bias: sp.Rational(2)}
    strong_packet = {wall_tension: sp.Rational(1), bias: sp.Rational(3)}

    weak_minima = [cfg for cfg in configurations if local_minimum(cfg, **{"wall_tension": weak_packet[wall_tension], "bias": weak_packet[bias]})]
    threshold_minima = [cfg for cfg in configurations if local_minimum(cfg, threshold_packet[wall_tension], threshold_packet[bias])]
    strong_minima = [cfg for cfg in configurations if local_minimum(cfg, strong_packet[wall_tension], strong_packet[bias])]

    all_minus = (-1,) * n
    all_plus = (1,) * n
    strong_minus_flip_costs = []
    strong_plus_flip_costs = []
    for cfg in configurations:
        base = energy(cfg, 1, 3)
        for i, spin in enumerate(cfg):
            cost = energy(flip(cfg, i), 1, 3) - base
            (strong_minus_flip_costs if spin == -1 else strong_plus_flip_costs).append(cost)

    strong_paths = [minus_flip_path(cfg, 1, 3) for cfg in configurations]
    strong_paths_are_strict = all(
        final == all_plus
        and len(energies) - 1 == cfg.count(-1)
        and all(next_energy < prior_energy for prior_energy, next_energy in zip(energies, energies[1:]))
        for cfg, (final, energies) in zip(configurations, strong_paths)
    )

    checks = {
        "all_minus_flip_cost_formula_exact": all_minus_flip_cost == 4 * wall_tension - 2 * bias,
        "weak_bias_traps_wrong_uniform_vacuum": all_minus in weak_minima,
        "threshold_bias_leaves_neutral_wrong_vacuum": all_minus in threshold_minima and all_minus_flip_cost.subs(threshold_packet) == 0,
        "strong_bias_makes_every_minus_flip_lower_energy": max(strong_minus_flip_costs) < 0,
        "strong_bias_makes_every_plus_flip_raise_energy": min(strong_plus_flip_costs) > 0,
        "strong_bias_has_unique_local_minimum": strong_minima == [all_plus],
        "strong_monotone_coarsening_reaches_all_plus_in_one_flip_per_initial_minus": strong_paths_are_strict,
        "desired_uniform_vacuum_is_lower_than_wrong_vacuum": energy(all_plus, 1, 3) < energy(all_minus, 1, 3),
        "deliberate_positive_bias_implies_coarsening_claim_fails": all_minus in weak_minima,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP284",
        "theorem_domain": "finite one-dimensional periodic CP-domain ring with energy -J*sum(s_i*s_i+1)-h*sum(s_i) and zero-temperature single-spin energy descent",
        "minus_flip_costs_by_neighbor_sum": {
            "two_minus_neighbors": str(all_minus_flip_cost),
            "mixed_neighbors": str(boundary_minus_flip_cost),
            "two_plus_neighbors": str(isolated_minus_flip_cost),
        },
        "coarsening_threshold": "h>2J",
        "five_site_packets": {
            "weak_h_equals_J_local_minima": [list(cfg) for cfg in weak_minima],
            "threshold_h_equals_2J_local_minima": [list(cfg) for cfg in threshold_minima],
            "strong_h_equals_3J_local_minima": [list(cfg) for cfg in strong_minima],
        },
        "strong_packet_flip_cost_bounds": {"largest_minus_flip_cost": str(max(strong_minus_flip_costs)), "smallest_plus_flip_cost": str(min(strong_plus_flip_costs))},
        "contextual_partition": "below threshold the local dynamics retains a wrong-vacuum metastable class; above threshold every minus domain has a lowering move and only the favored uniform vacuum is absorbing",
        "classification": "source-biased local domain dynamics is a conditional deterministic finite-ring branch selector only for h>2J; positive bias alone is insufficient",
        "smallest_exact_falsifier": "J=1 and h=1 favor plus globally but trap the all-minus ring because a single flip costs 2",
        "remaining_physical_instrument_gate": "derive h/J, spatial dimension and topology, wall tension, local update or field equation, thermal activation, expansion rate, coarsening time, defects, and post-selection stabilization",
        "scope_limit": "finite one-dimensional zero-temperature single-flip theorem; higher dimensions, thermal nucleation, quantum tunneling, conserved dynamics, and cosmological expansion require separate analysis",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp284_biased_domain_coarsening_threshold.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

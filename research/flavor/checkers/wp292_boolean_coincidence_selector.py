"""WP292: exact Boolean coincidence hierarchy for selector failures."""

import json
from itertools import combinations
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def moment(atoms, subset):
    return sp.Rational(sum(all(atom[index] == 1 for index in subset) for atom in atoms), len(atoms))


def tower(atoms, vertex_count):
    return {
        tuple(subset): moment(atoms, subset)
        for order in range(1, vertex_count + 1)
        for subset in combinations(range(vertex_count), order)
    }


def union_probability(atoms):
    return sp.Rational(sum(any(atom) for atom in atoms), len(atoms))


def inclusion_exclusion(moment_tower, vertex_count):
    return sp.simplify(
        sum(
            (-1) ** (len(subset) + 1) * moment_tower[subset]
            for order in range(1, vertex_count + 1)
            for subset in combinations(range(vertex_count), order)
        )
    )


def main():
    even_parity = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
    odd_parity = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)]
    even_tower = tower(even_parity, 3)
    odd_tower = tower(odd_parity, 3)
    singles_and_pairs = [subset for subset in even_tower if len(subset) <= 2]
    even_union = union_probability(even_parity)
    odd_union = union_probability(odd_parity)
    even_reconstructed = inclusion_exclusion(even_tower, 3)
    odd_reconstructed = inclusion_exclusion(odd_tower, 3)

    checks = {
        "packets_have_equal_cardinality": len(even_parity) == len(odd_parity) == 4,
        "all_single_failure_probabilities_match": all(even_tower[key] == odd_tower[key] == sp.Rational(1, 2) for key in even_tower if len(key) == 1),
        "all_pair_failure_probabilities_match": all(even_tower[key] == odd_tower[key] == sp.Rational(1, 4) for key in even_tower if len(key) == 2),
        "third_order_coincidence_separates_packets": even_tower[(0, 1, 2)] == 0 and odd_tower[(0, 1, 2)] == sp.Rational(1, 4),
        "global_failure_probabilities_differ": even_union == sp.Rational(3, 4) and odd_union == 1,
        "lower_towers_are_contextually_equivalent": all(even_tower[key] == odd_tower[key] for key in singles_and_pairs),
        "complete_even_tower_reconstructs_union": even_reconstructed == even_union,
        "complete_odd_tower_reconstructs_union": odd_reconstructed == odd_union,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    def serialize(moment_tower):
        return {"".join(str(index) for index in key): str(value) for key, value in moment_tower.items()}

    result = {
        "work_package": "WP292",
        "theorem_domain": "three labelled Boolean local-failure events with exact uniform finite laws",
        "even_parity_packet": {
            "atoms": [list(atom) for atom in even_parity],
            "coincidence_tower": serialize(even_tower),
            "global_failure_probability": str(even_union),
        },
        "odd_parity_packet": {
            "atoms": [list(atom) for atom in odd_parity],
            "coincidence_tower": serialize(odd_tower),
            "global_failure_probability": str(odd_union),
        },
        "contextual_partition": "all probes through pair order place the packets in one class; the triple-coincidence probe and complete Boolean tower separate them",
        "reconstruction_rule": "P(union_i F_i)=sum_nonempty_T (-1)^(|T|+1) P(intersection_{i in T} F_i)",
        "classification": "pairwise coincidence is not faithful for global selector risk; the complete finite coincidence tower is faithful for the labelled Boolean failure packet",
        "smallest_exact_falsifier": "even- and odd-parity three-bit laws have identical singles and pairs, but global failure is 3/4 versus 1",
        "remaining_physical_instrument_gate": "derive executable higher-order coincidence measurements with common clocks, labels, detector resolution, and accidental-coincidence subtraction from the flavor source",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp292_boolean_coincidence_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

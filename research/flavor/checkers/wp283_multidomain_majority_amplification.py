"""WP283: exact majority amplification and domain-geometry obstruction."""

import json
from math import comb
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def majority_error(n, p):
    threshold = (n + 1) // 2
    return sp.factor(sum(sp.binomial(n, k) * p**k * (1 - p) ** (n - k) for k in range(threshold)))


def cyclic_walls(configuration):
    return sum(configuration[i] != configuration[(i + 1) % len(configuration)] for i in range(len(configuration)))


def main():
    p = sp.Rational(3, 4)
    errors = {n: majority_error(n, p) for n in range(1, 20, 2)}
    target = sp.Rational(1, 100)
    first_passing = min(n for n, error in errors.items() if error <= target)

    contiguous = (1, 1, 1, -1, -1)
    alternating = (1, -1, 1, -1, 1)
    contiguous_mean = sp.Rational(sum(contiguous), len(contiguous))
    alternating_mean = sp.Rational(sum(alternating), len(alternating))
    contiguous_walls = cyclic_walls(contiguous)
    alternating_walls = cyclic_walls(alternating)

    checks = {
        "single_cell_error_is_one_quarter": errors[1] == sp.Rational(1, 4),
        "majority_error_decreases_on_tested_odd_counts": all(errors[n2] < errors[n1] for n1, n2 in zip(range(1, 18, 2), range(3, 20, 2))),
        "seventeen_cells_still_fail_one_percent": errors[17] == sp.Rational(106384445, 8589934592) and errors[17] > target,
        "nineteen_cells_first_pass_one_percent": first_passing == 19 and errors[19] == sp.Rational(611828695, 68719476736),
        "hostile_configurations_have_same_majority": sum(contiguous) == sum(alternating) == 1,
        "hostile_configurations_have_same_mean": contiguous_mean == alternating_mean == sp.Rational(1, 5),
        "hostile_configurations_have_different_wall_counts": contiguous_walls == 2 and alternating_walls == 4,
        "majority_statistic_does_not_determine_wall_energy": contiguous_walls != alternating_walls,
        "deliberate_majority_probability_implies_physical_coarsening_claim_fails": contiguous_walls != alternating_walls,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP283",
        "theorem_domain": "odd independent CP domains with favored-branch probability p=3/4 and a formal majority aggregator",
        "majority_errors_exact": {str(n): str(error) for n, error in errors.items()},
        "one_percent_target": str(target),
        "first_passing_domain_count": first_passing,
        "first_passing_error": str(errors[first_passing]),
        "hostile_spatial_pair": {
            "contiguous": {"configuration": list(contiguous), "mean": str(contiguous_mean), "cyclic_walls": contiguous_walls},
            "alternating": {"configuration": list(alternating), "mean": str(alternating_mean), "cyclic_walls": alternating_walls},
        },
        "contextual_partition": "formal majority readout separates vote counts but identifies spatial configurations with different domain-wall content and evolution",
        "classification": "independent-domain majority can amplify a probabilistic branch readout, but it is not a physical global flavor selector without a source-derived coarsening or aggregation operation",
        "first_nonfaithful_arrow": "local branch ensemble -> globally homogenized flavor vacuum",
        "smallest_exact_falsifier": "the five-domain strings +++-- and +-+-+ have the same majority and mean but two versus four cyclic walls",
        "remaining_physical_instrument_gate": "derive spatial coupling, wall tension and mobility, expansion/quench history, coarsening time, boundary conditions, global readout support, and stabilization",
        "scope_limit": "the binomial theorem assumes independent identical domains and an external majority aggregator; correlated nucleation and physical wall dynamics define different experiments",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp283_multidomain_majority_amplification.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

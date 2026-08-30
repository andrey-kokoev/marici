"""WP291: exact dependence obstruction for global selector failure."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def marginal_law(atoms, index):
    counts = {}
    for atom in atoms:
        counts[atom[index]] = counts.get(atom[index], 0) + 1
    total = len(atoms)
    return sorted((value, sp.Rational(count, total)) for value, count in counts.items())


def global_failure(atoms):
    return sp.Rational(sum(any(value <= 0 for value in atom) for atom in atoms), len(atoms))


def moments(law):
    mean = sum(value * probability for value, probability in law)
    variance = sum((value - mean) ** 2 * probability for value, probability in law)
    return sp.simplify(mean), sp.simplify(variance)


def main():
    correlated_atoms = [(-1, -1, -1)] + [(2, 2, 2)] * 8 + [(3, 3, 3)] * 3
    disjoint_atoms = [(-1, 3, 3), (3, -1, 3), (3, 3, -1), (3, 3, 3)] + [(2, 2, 2)] * 8
    correlated_marginals = [marginal_law(correlated_atoms, i) for i in range(3)]
    disjoint_marginals = [marginal_law(disjoint_atoms, i) for i in range(3)]
    correlated_failure = global_failure(correlated_atoms)
    disjoint_failure = global_failure(disjoint_atoms)
    marginal_failure = sum(probability for value, probability in correlated_marginals[0] if value <= 0)
    mean, variance = moments(correlated_marginals[0])

    vertex_count = 3
    global_target = sp.Rational(1, 100)
    required_local_target = global_target / vertex_count
    required_squared_ratio = sp.simplify(1 / required_local_target - 1)
    ratio = sp.symbols("ratio", nonnegative=True)
    solved_ratio = sp.solve_univariate_inequality(1 / (1 + ratio**2) <= required_local_target, ratio)

    checks = {
        "both_joint_packets_have_twelve_equal_atoms": len(correlated_atoms) == len(disjoint_atoms) == 12,
        "all_three_marginal_laws_match_exactly": correlated_marginals == disjoint_marginals,
        "every_marginal_has_mean_two_variance_one": all(moments(law) == (2, 1) for law in correlated_marginals + disjoint_marginals),
        "every_marginal_failure_is_one_twelfth": marginal_failure == sp.Rational(1, 12),
        "correlated_global_failure_is_one_twelfth": correlated_failure == sp.Rational(1, 12),
        "disjoint_global_failure_is_one_quarter": disjoint_failure == sp.Rational(1, 4),
        "disjoint_packet_saturates_union_bound": disjoint_failure == vertex_count * marginal_failure,
        "one_percent_three_vertex_union_gate_requires_squared_ratio_299": required_squared_ratio == 299,
        "solver_returns_sqrt_299_threshold": solved_ratio.equals(ratio >= sp.sqrt(299)),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP291",
        "theorem_domain": "three local selector margins with identical calibrated marginal laws and unrestricted dependence",
        "shared_marginal": {
            "law": [[str(value), str(probability)] for value, probability in correlated_marginals[0]],
            "mean": str(mean),
            "variance": str(variance),
            "failure_probability": str(marginal_failure),
        },
        "joint_packets": {
            "perfectly_aligned_failures": {"global_failure_probability": str(correlated_failure)},
            "disjoint_failures": {"global_failure_probability": str(disjoint_failure)},
        },
        "global_union_certificate": "P(any m_i<=0) <= sum_i P(m_i<=0)",
        "one_percent_three_vertex_gate": {
            "required_local_failure_bound": str(required_local_target),
            "required_local_signal_to_uncertainty_ratio": "mu_i/sigma_i >= sqrt(299)",
        },
        "contextual_partition": "all marginal moment and tail probes place the two joint packets in one class; a coincidence-sensitive joint probe separates them",
        "classification": "marginal calibration supplies only a worst-case union certificate for global selection; dependence-sensitive source probes are required for a sharper result",
        "smallest_exact_falsifier": "two three-margin packets have identical marginals, but aligned failures give global risk 1/12 while disjoint failures give 1/4",
        "remaining_physical_instrument_gate": "measure or source-derive cross-domain dependence in a common frame, including coincidence timing and detector resolution, or accept the predeclared union-bound budget",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp291_joint_tail_selector_bound.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

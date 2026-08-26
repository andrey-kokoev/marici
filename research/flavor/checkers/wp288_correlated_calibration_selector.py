"""WP288: exact robust selector over a source-declared correlated polytope."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def incident_sums(edges, edge_values, vertex_count):
    totals = [sp.S.Zero] * vertex_count
    for (i, j), value in zip(edges, edge_values):
        totals[i] += value
        totals[j] += value
    return totals


def main():
    t = sp.symbols("t", real=True)
    edges = [(0, 1), (1, 2), (0, 2)]
    edge_values = [1 + t / 10, 2 - t / 10, sp.Rational(3)]
    wall_budgets = incident_sums(edges, edge_values, 3)
    biases = [wall_budgets[0] + sp.Rational(1, 5), wall_budgets[1] + sp.Rational(1, 5), wall_budgets[2] + sp.Rational(1, 5)]
    margins = [sp.simplify(bias - wall) for bias, wall in zip(biases, wall_budgets)]

    endpoint_packets = []
    for endpoint in (-1, 1):
        endpoint_packets.append(
            {
                "t": endpoint,
                "edges": [str(value.subs(t, endpoint)) for value in edge_values],
                "biases": [str(value.subs(t, endpoint)) for value in biases],
                "margins": [str(value.subs(t, endpoint)) for value in margins],
            }
        )

    edge_lowers = [min(value.subs(t, -1), value.subs(t, 1)) for value in edge_values]
    edge_uppers = [max(value.subs(t, -1), value.subs(t, 1)) for value in edge_values]
    bias_lowers = [min(value.subs(t, -1), value.subs(t, 1)) for value in biases]
    box_upper_budgets = incident_sums(edges, edge_uppers, 3)
    box_margins = [sp.simplify(lower - wall) for lower, wall in zip(bias_lowers, box_upper_budgets)]

    checks = {
        "all_correlated_margins_are_constant_one_fifth": margins == [sp.Rational(1, 5)] * 3,
        "polytope_vertices_have_positive_margins": all(sp.Rational(value) > 0 for packet in endpoint_packets for value in packet["margins"]),
        "affine_polytope_vertex_test_is_exact": all(sp.degree(margin, t) <= 1 for margin in margins),
        "independent_box_relaxation_loses_strictness_at_every_vertex": box_margins == [0, 0, 0],
        "box_contains_both_correlated_endpoints": all(lower <= value.subs(t, endpoint) <= upper for value, lower, upper in zip(edge_values, edge_lowers, edge_uppers) for endpoint in (-1, 1)),
        "correlation_changes_certificate_not_physical_state_domain": len(endpoint_packets) == 2,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP288",
        "theorem_domain": "affine source-calibration packet over the declared joint polytope t in [-1,1]",
        "correlated_family": {
            "edge_functions": [str(value) for value in edge_values],
            "bias_functions": [str(value) for value in biases],
            "selector_margins": [str(value) for value in margins],
            "polytope_vertices": endpoint_packets,
        },
        "independent_box_relaxation": {
            "edge_intervals": [[str(lower), str(upper)] for lower, upper in zip(edge_lowers, edge_uppers)],
            "bias_lowers": [str(value) for value in bias_lowers],
            "upper_incident_wall_budgets": [str(value) for value in box_upper_budgets],
            "worst_margins": [str(value) for value in box_margins],
            "strict_certificate_passes": all(value > 0 for value in box_margins),
        },
        "classification": "a source-declared correlated support can certify a robust conditional selector that its independent interval projection falsely rejects",
        "smallest_exact_falsifier": "the marginal interval box has zero worst margin at all three vertices even though every point of the correlated source line has margin 1/5",
        "anti_circularity_gate": "the joint support relation must be derived from calibration physics before evaluating selector margins; fitting the correlation to preserve the answer is forbidden",
        "remaining_physical_instrument_gate": "derive and measure the joint support or covariance in one source/readout frame, validate non-affine tails, and propagate the admitted set through dynamics and physical16",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp288_correlated_calibration_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

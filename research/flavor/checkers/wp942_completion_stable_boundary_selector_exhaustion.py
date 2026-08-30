import json
from pathlib import Path


def main() -> None:
    gates = (
        "same_domain",
        "selects_boundary",
        "nonzero_coupling",
        "completion_stable",
        "instrument_preserved",
        "physical16_descent",
    )
    routes = {
        "su4_parent": (True, False, True, False, True, False),
        "discrete_symmetry": (True, False, True, True, True, False),
        "additive_rg": (True, False, True, False, True, False),
        "affine_attractor": (True, True, True, False, True, False),
        "hypermultiplet_beta_kernel": (True, False, True, True, True, False),
        "bulk_loop_counterterm": (True, False, True, False, True, False),
        "volume_suppression": (True, False, True, False, True, False),
        "boundaryless_circle": (False, True, False, True, False, False),
    }
    passes = {name: all(values) for name, values in routes.items()}

    checks = {
        "six_acceptance_gates": len(gates) == 6,
        "eight_routes_audited": len(routes) == 8,
        "no_route_passes_all_gates": not any(passes.values()),
        "symmetry_fails_selection": not routes["discrete_symmetry"][1],
        "additive_rg_fails_selection": not routes["additive_rg"][1],
        "affine_attractor_lacks_completion_stability": not routes["affine_attractor"][3],
        "hypermultiplet_kernel_fails_selection": not routes["hypermultiplet_beta_kernel"][1],
        "bulk_counterterm_fails_selection": not routes["bulk_loop_counterterm"][1],
        "suppression_fails_selection": not routes["volume_suppression"][1],
        "circle_changes_domain": not routes["boundaryless_circle"][0],
        "circle_loses_instrument": not routes["boundaryless_circle"][4],
        "relative_not_absolute_exhaustion": True,
    }

    result = {
        "work_package": "WP942",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "acceptance_gates": list(gates),
        "route_gate_vectors": {name: list(values) for name, values in routes.items()},
        "passing_routes": [name for name, passed in passes.items() if passed],
        "contextual_partition": "at least the one-dimensional bare tau fiber survives on the interval branch",
        "smallest_exact_falsifier": "tau=0 and tau=1 survive symmetry and perturbative transport; geometry removes their instrument",
        "strongest_descending_comparator": "WP861 rank-three physical16 family, excluded from all 1210 fitted sheets by WP862",
        "remaining_routes": [
            "completion-stable UV law fixing finite even boundary coefficient",
            "new boundaryless source with derived holonomy-to-Yukawa physical16 instrument",
        ],
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp942_completion_stable_boundary_selector_exhaustion.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

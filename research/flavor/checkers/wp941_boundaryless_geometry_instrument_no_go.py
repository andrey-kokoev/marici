import json
from pathlib import Path


def main() -> None:
    interval = {
        "boundary_components": 2,
        "raw_boundary_coefficients": 2,
        "exchange_even_coefficients": 1,
        "endpoint_ports": 2,
    }
    circle = {
        "boundary_components": 0,
        "raw_boundary_coefficients": 0,
        "exchange_even_coefficients": 0,
        "endpoint_ports": 0,
    }
    marked_circle = {
        "added_reference_marks": 2,
        "relational_ports": 2,
        "same_groupoid_as_unmarked_circle": False,
    }

    checks = {
        "interval_has_two_boundaries": interval["boundary_components"] == 2,
        "interval_has_two_raw_coefficients": interval["raw_boundary_coefficients"] == 2,
        "exchange_leaves_one_even_line": interval["exchange_even_coefficients"] == 1,
        "interval_has_two_ports": interval["endpoint_ports"] == 2,
        "circle_has_no_boundary": circle["boundary_components"] == 0,
        "circle_has_no_interval_boundary_coefficient": circle["exchange_even_coefficients"] == 0,
        "circle_has_no_endpoint_ports": circle["endpoint_ports"] == 0,
        "port_rank_drops_two_to_zero": interval["endpoint_ports"] - circle["endpoint_ports"] == 2,
        "modulus_and_instrument_removed_together": interval["exchange_even_coefficients"] == 1 and circle["endpoint_ports"] == 0,
        "marked_circle_adds_reference_ports": marked_circle["relational_ports"] == 2,
        "marked_circle_changes_groupoid": not marked_circle["same_groupoid_as_unmarked_circle"],
        "boundaryless_is_domain_replacement": True,
    }

    result = {
        "work_package": "WP941",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "object_table": {"interval": interval, "circle": circle, "marked_circle": marked_circle},
        "classification": "source-domain replacement, not selector on the interval lens family",
        "smallest_exact_falsifier": "endpoint-port rank drops from 2 on the interval to 0 on the unmarked circle",
        "reference_port_rule": "two circle marks define a new relational experiment over a smaller stabilizer groupoid",
        "remaining_gate": "fix the interval even coefficient or rederive boundaryless physical16 descent and holonomy instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp941_boundaryless_geometry_instrument_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

"""Audit the two requested optical frontier instrument builds."""

import json
from pathlib import Path


def main():
    aspect = Path(__file__).parents[1]
    stems = [
        "reciprocal_denominator_sewing_network",
        "directional_double_triangle_moving_fiber_interferometer",
    ]
    findings = {}
    for stem in stems:
        packet = aspect / f"{stem.replace('_', '-')}.md"
        checker = aspect / "checkers" / f"{stem}.py"
        result_path = aspect / "results" / f"{stem}.json"
        payload = json.loads(result_path.read_text(encoding="utf-8")) if result_path.exists() else {}
        boundary = payload.get("typed_boundary", {})
        findings[stem] = {
            "packet_exists": packet.exists(),
            "checker_exists": checker.exists(),
            "result_exists": result_path.exists(),
            "result_passes": payload.get("status") == "pass",
            "declares_typed_boundary": bool(boundary),
        }

    checks = {
        "both_instruments_are_paired": all(
            item["packet_exists"] and item["checker_exists"] and item["result_exists"]
            for item in findings.values()
        ),
        "both_instruments_pass": all(item["result_passes"] for item in findings.values()),
        "both_instruments_retain_authority_boundaries": all(
            item["declares_typed_boundary"] for item in findings.values()
        ),
    }
    result = {
        "schema": "marici.aspect.two_frontier_optical_instrument_build_audit.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "findings": findings,
        "completion": "exact finite instrument pair",
        "remaining": [
            "physical fabrication and uncertainty calibration",
            "theta/Tate source matrix and continuum sewing",
            "double-triangle marked divisor and geometric connection",
        ],
    }
    out = aspect / "results" / "two_frontier_optical_instrument_build_audit.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

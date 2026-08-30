#!/usr/bin/env python3
"""Show that coarse endpoint aggregation cancels a nonzero route packet."""

import json
from pathlib import Path


def main():
    endpoints = (-1, 1)
    boundary = {-1: -1, 1: 1}
    factors = {
        "negative_occurrence": {"equation": "xi+1", "zero": -1},
        "positive_occurrence": {"equation": "xi-1", "zero": 1},
    }
    route_packet = tuple(boundary[data["zero"]] for data in factors.values())
    coarse_sum = sum(route_packet)
    checks = {
        "coarse_face_meets_both_endpoints": all(data["zero"] in endpoints for data in factors.values()),
        "both_resolved_routes_are_nonzero": all(value != 0 for value in route_packet),
        "resolved_route_packet_has_opposite_orientations": route_packet == (-1, 1),
        "coarse_unweighted_aggregation_cancels": coarse_sum == 0,
        "cancellation_is_not_route_loss": route_packet != (0, 0),
    }
    result = {
        "schema": "marici.occurrence-resolved-endpoint-cancellation.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "physical_chain": "Gamma_xi=[-1,1] with boundary [1]-[-1]",
        "coarse_face": "xi^2-1=(xi+1)(xi-1)",
        "occurrences": factors,
        "resolved_boundary_route_packet": list(route_packet),
        "coarse_aggregation_map": "sigma(r_minus,r_plus)=r_minus+r_plus",
        "coarse_readout": coarse_sum,
        "mechanism": "nonzero occurrence routes cancel only after the coarse sum; this is interference/forgetful aggregation, not absence of support",
        "checks": checks,
    }
    output = Path(__file__).with_name("occurrence-resolved-endpoint-cancellation.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

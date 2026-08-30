#!/usr/bin/env python3
"""Typing inventory for existing maps near the kinematic coordinate origins."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def main():
    routes = [
        {
            "route": "fiber coordinate-boundary Gysin",
            "source_locus": "a=0 or b=0",
            "target": "finite-sextic boundary vanishing cycles",
            "gate": "wrong_locus",
            "entries": [812, 813, 826, 841],
        },
        {
            "route": "site-soft Cut-nearby Rees map",
            "source_locus": "X1=0 or X2=0 in the homogeneous residue system",
            "target": "rank-three conductor occurrence lattice",
            "gate": "wrong_target",
            "entries": [351, 352, 353, 355],
        },
        {
            "route": "generic five-pole localization/base change",
            "source_locus": "homogeneous conormal I=(nu1,nu2,nu3)",
            "target": "label-preserving N2",
            "gate": "no_scalar_source_map",
            "entries": [699, 700, 701],
        },
        {
            "route": "contact-product mixed variation",
            "source_locus": "nu_i=nu_j=0",
            "target": "rank-one invariant mixed line",
            "gate": "monodromy_character_mismatch",
            "source_character": [1, 1],
            "required_character": [-1, -1],
            "entries": [2143, 2144, 2145, 2146, 2147],
        },
        {
            "route": "Jacobian rank drop",
            "source_locus": "V(P1,P2,P3) union_i V(Xi,Pi)",
            "target": "none",
            "gate": "rank_census_is_not_a_morphism",
            "entries": [2578, 2583],
        },
    ]
    checks = {
        "all_routes_have_declared_source_locus": all(r["source_locus"] for r in routes),
        "all_routes_have_declared_target": all(r["target"] for r in routes),
        "no_existing_route_passes_all_typing_gates": all(r["gate"] != "pass" for r in routes),
        "contact_character_obstruction_retained": routes[3]["source_character"] != routes[3]["required_character"],
    }
    packet = {
        "schema": "marici.coordinate_origin_map_inventory.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "routes": routes,
        "checks": checks,
        "conclusion": (
            "No already-constructed route types a scalar total-energy/conormal "
            "map into the cyclic quadratic line at a kinematic coordinate origin."
        ),
        "scope_warning": (
            "This closes the existing-map inventory only. It does not exclude a "
            "new source-derived coefficient Hessian or physical-cycle morphism."
        ),
    }
    output = ROOT / "results" / "coordinate-origin-map-inventory.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": packet["status"], "checks": checks}, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()

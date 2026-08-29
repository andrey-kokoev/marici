#!/usr/bin/env python3
"""Exact constructor-completion ladder with a fixed Bell obstruction witness."""
import itertools, json, math
from pathlib import Path

ASPECT = Path(__file__).resolve().parent.parent
CONTRACT = ASPECT / "contracts" / "local-completion-global-obstruction-ladder.v1.json"
RESULT = ASPECT / "results" / "local_completion_global_obstruction_ladder.json"

def correlation(a, b):
    return -math.cos(2 * math.radians(a - b))

def chsh(e):
    return abs(e[0][0] + e[0][1] + e[1][0] - e[1][1])

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    a = contract["settings_degrees"]["A"]
    b = contract["settings_degrees"]["B"]
    e = [[correlation(x, y) for y in b] for x in a]
    observed = chsh(e)
    tau = contract["correlation_tolerance"]
    lower = observed - 4 * tau
    local_vertex_max = max(abs(a0*b0 + a0*b1 + a1*b0 - a1*b1)
                           for a0, a1, b0, b1 in itertools.product((-1, 1), repeat=4))
    cumulative = []
    rung_results = []
    for expected_id, rung in enumerate(contract["rungs"]):
        cumulative.extend(rung["adds"])
        rung_results.append({
            "id": rung["id"], "name": rung["name"],
            "cumulative_fields": list(cumulative),
            "inclusive_chsh": observed,
            "conservative_lower": lower,
            "obstruction_survives": lower > contract["chsh_local_ceiling"]
        })
    required_final = {"wing", "setting", "setting_source_health", "scattered_photon_energy",
                      "scattered_photon_direction", "electron_recoil", "target_excitation",
                      "outcome", "no_click", "analyzer_frame", "coincidence_class", "reset_id"}
    checks = {
        "rung_ids_contiguous": all(r["id"] == i for i, r in enumerate(contract["rungs"])),
        "completion_is_monotone": all(set(rung_results[i-1]["cumulative_fields"]) < set(rung_results[i]["cumulative_fields"])
                                      for i in range(1, len(rung_results))),
        "final_constructor_complete": set(cumulative) == required_final,
        "local_polytope_ceiling_exact": local_vertex_max == 2,
        "quantum_fixture_exact": abs(observed - 2 * math.sqrt(2)) < 1e-12,
        "obstruction_survives_every_rung": all(r["obstruction_survives"] for r in rung_results),
        "no_click_is_inclusive": 0 in contract["outcomes"],
        "falsifier_is_rung_localized": "inclusive_chsh_lower_at_or_below_2_after_rung" in contract["falsifiers"],
        "claim_boundary_preserved": not any(contract["claim_boundary"].values())
    }
    result = {
        "schema": "marici.aspect.local-completion-global-obstruction-ladder-result.v1",
        "passed": all(checks.values()), "checks": checks,
        "correlations": e, "chsh": observed, "conservative_chsh_lower": lower,
        "witness_distance_lower_bound": (observed - 2) / 4,
        "local_vertex_max": local_vertex_max, "rungs": rung_results,
        "verdict": "local_completion_preserves_global_obstruction_mathematical_fixture",
        "physical_status": "not_run"
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["passed"] else 1)

if __name__ == "__main__":
    main()

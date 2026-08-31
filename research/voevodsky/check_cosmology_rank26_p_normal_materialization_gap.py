"""Audit whether the rank-26 p-normal protocol is already materialized.

This is repeat iteration 1 after the protocol gate.  It independently re-reads
mutable state and checks that existing Benincasa rank-26 artifacts do not already
supply the p-normal test matrix at (3,6,-3).  In particular, the total-energy
Rees code/artifacts use sum-zero slices and total-energy tangents, so they cannot
be relabelled as the p-normal derivative computation.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOE = ROOT / "research" / "voevodsky"
VOE_RESULTS = VOE / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
BEN = ROOT / "research" / "benincasa"
OUT = VOE_RESULTS / "cosmology_rank26_p_normal_materialization_gap.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_load_json(path: Path) -> dict | None:
    if path.stat().st_size > 8_000_000:
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def dot(a: list[int] | tuple[int, ...], b: list[int] | tuple[int, ...]) -> int:
    return sum(x * y for x, y in zip(a, b))


def main() -> None:
    protocol = load(VOE_RESULTS / "cosmology_rank26_p_normal_protocol_gate.json")
    prior = load(NIMA_RESULTS / "cosmology_p_normal_rank26_relation_bockstein_prior_art.json")
    frontier = load(NIMA_RESULTS / "cosmology_current_activation_frontier_exhaustion.json")
    total_energy_rees = load(BEN / "rank26-total-energy-rees-source-comparison-a12-p32009-point-3-5-m8.json")
    total_energy_closure = load(BEN / "rank26-total-energy-source-word-closure-a12-p32009-point-3-5-m8.json")

    assert protocol["passed"] is True
    assert prior["passed"] is True
    assert frontier["passed"] is True
    assert total_energy_rees["schema"].endswith("rank26-total-energy-rees-source-comparison.v1")
    assert total_energy_closure["schema"].endswith("rank26-total-energy-source-word-closure.v1")

    p_covector = protocol["p_normal_covector"]
    p_point = protocol["test_point_xyz"]
    assert p_covector == [1, 1, 3]
    assert p_point == [3, 6, -3]
    assert dot(p_covector, p_point) == 0
    assert sum(p_point) == 6

    # The strongest nearby available rank-26 Rees artifacts are total-energy
    # artifacts at a different point and normal geometry.
    te_point = total_energy_rees["point"]
    assert te_point == total_energy_closure["point"] == [3, 5, -8]
    assert sum(te_point) == 0
    assert dot(p_covector, te_point) != 0

    total_energy_tangents = total_energy_rees["tangent_source_closure"]["source_record"]["tangents"]
    total_energy_tangent_p_values = [dot(p_covector, tangent) for tangent in total_energy_tangents]
    assert total_energy_tangent_p_values == [-2, -2]

    p_tangent = protocol["integral_unit_normals"]["p_tangent_difference"]
    assert dot(p_covector, p_tangent) == 0
    assert sum(p_tangent) == 0  # shared tangent, but not the span used by the stored total-energy packet

    json_files = sorted(list(BEN.glob("rank26*.json")) + list((BEN / "results").glob("rank26*.json")))
    loaded = []
    materialized_p_point = []
    p_normal_named = []
    for path in json_files:
        obj = safe_load_json(path)
        if obj is None:
            continue
        loaded.append(str(path.relative_to(ROOT)).replace("\\", "/"))
        if obj.get("point") == p_point or obj.get("generic_p_normal_test_point", {}).get("xyz") == p_point:
            materialized_p_point.append(str(path.relative_to(ROOT)).replace("\\", "/"))
        text_markers = " ".join(
            str(obj.get(key, "")) for key in ("schema", "status", "scope", "normal_connection")
        ).lower()
        if "p-normal" in text_markers or "p_normal" in text_markers:
            p_normal_named.append(str(path.relative_to(ROOT)).replace("\\", "/"))

    # No Benincasa rank-26 JSON in the scanned corpus materializes the p-normal
    # point/matrix.  Nima's prior-art JSON names the p-normal protocol, but it is
    # intentionally an algorithmic opening, not a computed class.
    assert materialized_p_point == []

    result = {
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-materialization-gap.v1",
        "status": "p_normal_rank26_protocol_not_materialized_in_existing_rank26_artifacts",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_rank26_p_normal_protocol_gate.json",
            "research/nima/results/cosmology_p_normal_rank26_relation_bockstein_prior_art.json",
            "research/nima/results/cosmology_current_activation_frontier_exhaustion.json",
            "research/benincasa/rank26-total-energy-rees-source-comparison-a12-p32009-point-3-5-m8.json",
            "research/benincasa/rank26-total-energy-source-word-closure-a12-p32009-point-3-5-m8.json",
        ],
        "p_normal_target": {
            "covector": p_covector,
            "test_point": p_point,
            "p_at_test_point": dot(p_covector, p_point),
            "total_energy_at_test_point": sum(p_point),
        },
        "nearest_stored_rank26_rees_packet": {
            "point": te_point,
            "p_value_at_point": dot(p_covector, te_point),
            "total_energy": sum(te_point),
            "normal_connection": total_energy_closure["normal_connection"],
            "tangents": total_energy_tangents,
            "p_values_on_total_energy_tangents": total_energy_tangent_p_values,
            "raw_relation_count": total_energy_rees["raw_relation_count"],
            "column_count": total_energy_rees["column_count"],
        },
        "scan": {
            "rank26_json_files_loaded": len(loaded),
            "materialized_benincasa_files_at_p_normal_test_point": materialized_p_point,
            "benincasa_rank26_files_with_p_normal_marker_in_summary_fields": p_normal_named,
        },
        "decision": "existing total-energy/gamma rank-26 packets cannot be relabelled as the p-normal computation; only the algorithm may be reused",
        "missing_materialization": [
            "rank-26 labelled relation rows evaluated at (3,6,-3) on p=0",
            "first derivatives along nx=(1,0,0) and ny=(0,1,0)",
            "reduction modulo the special exact image and the p-tangent derived span generated from nx-ny=(1,-1,0)",
            "map from any surviving quotient line to the ordered wall/exceptional-face horn column",
        ],
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

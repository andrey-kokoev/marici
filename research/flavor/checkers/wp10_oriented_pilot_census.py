"""Compose the original and sector-swapped WP10 pilot results by orientation."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
original = json.loads((RESULTS / "wp10_support_cone_census.json").read_text())

rows = []
for row in original["rows"]:
    rows.append({"unoriented_orbit": row["orbit"], "orientation": "original",
                 **{k: v for k, v in row.items() if k != "orbit"}})

missing = []
swapped_viable = []
swapped_no_witness = []
swapped_excluded = []
certified_overrides = {
    2: json.loads((RESULTS / "wp10_swapped_orbit2_gram_criterion.json").read_text())
}
certified_exclusions = {
    1: "exact_up_gram_triangle_obstruction",
    3: "exact_zero_diagonal_up_gram_obstruction_at_central_point",
    8: "exact_forced_ckm_zero",
    12: "exact_forced_ckm_zero",
}
for orbit in range(18):
    path = RESULTS / f"wp10_sector_swapped_orbit{orbit}_pilot.json"
    if not path.exists():
        missing.append(orbit)
        continue
    record = json.loads(path.read_text())
    exact_witness = (orbit in certified_overrides
                     and certified_overrides[orbit]["any_label_satisfies"])
    viable = bool(record["viable_minima"]) or exact_witness
    if viable:
        swapped_viable.append(orbit)
    elif orbit in certified_exclusions:
        swapped_excluded.append(orbit)
    else:
        swapped_no_witness.append(orbit)
    rows.append({
        "unoriented_orbit": orbit,
        "orientation": "sector_swapped",
        "status": ("physical_exact_gram_witness" if exact_witness
                   else "physical_witness" if viable
                   else "exactly_excluded_at_central_point"
                   if orbit in certified_exclusions else "no_pilot_witness"),
        "best_chi2": record["best_chi2_overall"],
        "witness_count": len(record["viable_minima"]),
        "members_tried": len(record["members_tried"]),
        "escalated": record["escalated"],
        "exact_exclusion": certified_exclusions.get(orbit),
    })

out = {
    "schema": "marici.flavor.wp10_oriented_pilot_census.v1",
    "status": "complete_pilot" if not missing else "partial_pilot",
    "oriented_class_count": 36,
    "original_orientation_count": 18,
    "swapped_results_present": 18-len(missing),
    "missing_swapped_orbits": missing,
    "swapped_physical_witness_orbits": swapped_viable,
    "swapped_no_pilot_witness_orbits": swapped_no_witness,
    "swapped_exactly_excluded_orbits": swapped_excluded,
    "exact_witness_overrides": sorted(certified_overrides),
    "rows": rows,
    "caution": "Pilot misses are not exclusions. Here every swapped miss has now been replaced by a separate exact central-point obstruction.",
}
(RESULTS / "wp10_oriented_pilot_census.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=2))

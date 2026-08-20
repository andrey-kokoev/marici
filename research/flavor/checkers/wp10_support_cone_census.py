"""Finite support-cone viability census for all 18 nine-link orbits.

This is an evidence compositor, not a new fit: it joins WP7's explicit
physical witnesses for 14 orbits with WP10's structural exclusion
certificates for the remaining four.
"""
import json
from pathlib import Path

ensemble = json.loads(Path("research/flavor/results/wp7_ensemble.json").read_text())
three = json.loads(Path("research/flavor/results/wp10_orbit1_exact_obstruction.json").read_text())
orbit3 = json.loads(Path("research/flavor/results/wp10_orbit3_gram_criterion.json").read_text())
robust3 = json.loads(Path("research/flavor/results/wp10_orbit3_gram_3sigma_box.json").read_text())
typing = json.loads(Path("research/flavor/results/wp10_sector_exchange_typing_audit.json").read_text())

rows = []
for rec in ensemble["orbits"]:
    idx = rec["orbit_index"]
    viable = bool(rec["viable_minima"])
    if viable:
        rows.append({"orbit": idx, "status": "physical_witness",
                     "best_chi2": rec["best_chi2_overall"],
                     "witness_count": len(rec["viable_minima"])})
    elif idx == 1:
        rows.append({"orbit": idx, "status": "excluded",
                     "mechanism": "forbidden down-Gram off-diagonal zero"})
    elif idx in (8, 12):
        rows.append({"orbit": idx, "status": "excluded",
                     "mechanism": "orthogonal isolated sector eigenvectors force CKM zero"})
    elif idx == 3:
        rows.append({"orbit": idx, "status": "excluded",
                     "mechanism": "positive zero-diagonal Gram-cone inequality",
                     "robust_3sigma_compatible_corners": robust3["all_excluded"]})
    else:
        raise AssertionError(f"unclassified failed orbit {idx}")

inside = [r["orbit"] for r in rows if r["status"] == "physical_witness"]
outside = [r["orbit"] for r in rows if r["status"] == "excluded"]
assert len(rows) == 18
assert inside == [0,2,4,5,6,7,9,10,11,13,14,15,16,17]
assert outside == [1,3,8,12]
assert three["all_three_pairs_excluded"]
assert not orbit3["any_label_satisfies"]

out = {
    "schema": "marici.flavor.support_cone_census.v1",
    "status": "complete_for_18_chosen_orientations_incomplete_for_physical_oriented_census",
    "orbit_count": 18,
    "physical_oriented_orbit_count": typing["oriented_s3_orbit_count"],
    "physical_witness_orbits": inside,
    "structurally_excluded_orbits": outside,
    "rows": rows,
    "typing": {
        "positive_side": "explicit fitted texture maps to the physical point",
        "negative_side": "source-support invariant excludes the physical point",
        "caution": "positive witnesses are numerical; negative certificates are symbolic plus high-precision/interval-style source-data audits; the original orbit quotient also identifies Yu with Yd, but physical feasibility is sector-labelled, so the exchanged 18 orientations remain unclassified",
    },
    "conclusion": "Among the 18 chosen orientations, 14 have witnesses and four are excluded. This is not a complete physical support census: the 18 sector-exchanged orientations must be tested separately.",
}
target = Path("research/flavor/results/wp10_support_cone_census.json")
target.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k != "rows"}, indent=2))

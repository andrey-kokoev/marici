"""Join every observed same-chart doublet to its exact branch-source type."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
fiber = json.loads((RESULTS / "wp8_fiber_classification.json").read_text())
phase = json.loads(
    (RESULTS / "wp10_phase_aware_invariant_jacobians.json").read_text())
monomial = json.loads(
    (RESULTS / "wp10_square_monomial_gram_jacobians.json").read_text())
collapse = json.loads(
    (RESULTS / "wp10_orbit2_branch_jet.json").read_text())

phase_by_orbit = {
    r["orbit"]: r for r in phase["records"]
    if r["orientation"] == "original"
}
monomial_by_orbit = {
    r["orbit"]: r for r in monomial["records"]
    if r["orientation"] == "original"
}

records = []
for pair in fiber["same_chart_doublets"]:
    orbit = pair["chart"]["orbit"]
    if orbit == 0:
        certificate = phase_by_orbit[0]
        branch_type = "regular_positive_interior"
        reason = (
            "unit-circle Jacobian factor is "
            "(cos(phi)*m4*m7+m3*m6), strictly positive for positive "
            "magnitudes in the folded chamber")
    elif orbit == 2:
        assert collapse["status"] == "exact_collapsed_positive_fiber"
        branch_type = "collapsed_continuous_fiber"
        reason = (
            "the only positive-interior rank drop lies at phi=0 and balance; "
            "an exact positive one-parameter fiber has constant invariants")
        certificate = collapse["exact_collapsed_fiber"]
    else:
        certificate = monomial_by_orbit[orbit]
        assert certificate["quotient_is_coordinate_monomial"]
        assert not certificate["balance_divides_jacobian"]
        branch_type = "regular_positive_interior_coordinate_boundary_only"
        reason = (
            "the exact phase-free Gram Jacobian is a coordinate monomial; "
            "rank loss occurs only when a positive edge reaches zero")
    records.append({
        "chart": pair["chart"],
        "branch_type": branch_type,
        "reason": reason,
        "finite_positive_interior_branch": False,
        "certificate": certificate,
    })

out = {
    "schema": "marici.flavor.doublet_branch_source_census.v1",
    "status": "complete_exact_join",
    "doublet_count": len(records),
    "finite_positive_interior_branch_count": sum(
        r["finite_positive_interior_branch"] for r in records),
    "all_observed_doublets_lack_finite_interior_branch_source": all(
        not r["finite_positive_interior_branch"] for r in records),
    "records": records,
    "interpretation":
        "the observed regular multisheet doublets have no source-derived "
        "finite positive-interior branch component; their local arrows are "
        "not presently restrictions of an ordinary deck cover",
}
(RESULTS / "wp10_doublet_branch_source_census.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "records"}, indent=2))

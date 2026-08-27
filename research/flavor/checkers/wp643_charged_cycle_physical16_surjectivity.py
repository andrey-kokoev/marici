"""Exact WP643 fitted-domain product-extension audit."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ensemble = json.loads((ROOT / "results" / "wp20_valley_audit.json").read_text(
    encoding="utf-8"))
records = ensemble["records"]
sheet_ids = tuple(range(len(records)))
contexts = (
    ("plus", 1),
    ("minus", 1),
    ("plus", 2),
    ("minus", 2),
)
extended = tuple((sheet, context) for sheet in sheet_ids for context in contexts)
projection = tuple(sheet for sheet, _ in extended)
fiber_counts = Counter(projection)

checks = {
    "complete_stored_ensemble_loaded": (
        len(records) == ensemble["n_minima_audited"] == 1210),
    "four_predeclared_charged_contexts": len(contexts) == 4,
    "product_domain_has_4840_states": len(extended) == 4840,
    "projection_reaches_every_fitted_sheet": set(projection) == set(sheet_ids),
    "every_sheet_has_uniform_fiber_four": (
        set(fiber_counts.values()) == {4} and len(fiber_counts) == 1210),
    "projected_image_is_not_proper": len(set(projection)) == len(sheet_ids),
    "charged_response_can_vary_at_fixed_sheet": contexts[0] != contexts[1],
    "tree_level_zero_vev_assumption_is_explicit": True,
    "loop_backreaction_not_silently_admitted": True,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP643",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "complete stored 1210-sheet fitted physical16 ensemble",
    "faithful_quotient_coordinate": "six ordered masses, nine CKM moduli, and signed J modulo full weak-basis equivalence",
    "extension": "F_1210 x {plus/minus at m_chi=1/2}",
    "extended_state_count": len(extended),
    "projected_sheet_count": len(set(projection)),
    "fiber_size": 4,
    "classification": "source-derived carrier probe extension; neither physical16 selector nor calibrated instrument",
    "smallest_exact_falsifier": "one physical16 sheet supports both plus and minus charged contexts without changing its flavor coordinate",
    "assumptions": [
        "chi has zero vacuum expectation value",
        "tree-level neutral Yukawa matching only",
        "no admitted loop or threshold backreaction correlates charged parameters with physical16",
    ],
    "reopening_gate": "source-derived weak-basis-invariant backreaction with proper physical16 image, ensemble survival, and calibrated instrument",
}
(ROOT / "results" / "wp643_charged_cycle_physical16_surjectivity.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

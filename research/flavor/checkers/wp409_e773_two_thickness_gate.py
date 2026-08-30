"""Exact authority audit of the completed E773 two-regenerator experiment."""

import json
from pathlib import Path

import sympy as sp


L1, L2 = sp.Integer(40), sp.Integer(61)
design = sp.Matrix([[1, L1, L1**2], [1, L2, L2**2]])
kernel = design.nullspace()[0]

# A source-off setting would add the missing third row and identify a quadratic
# thickness law.  It was not a simultaneously observed E773 vacuum beam.
completed_design = sp.Matrix([[1, 0, 0], *design.tolist()])

# Each regenerator spectrum has an independent incident-flux normalization when
# no vacuum beam calibrates the input spectrum.  A relative response cannot be
# predicted from the first beam without fitting the second normalization.
F1, F2, response1, response2 = sp.symbols("F1 F2 R1 R2", nonzero=True, real=True)
records = sp.Matrix([F1 * response1, F2 * response2])
flux_jacobian = records.jacobian([F1, F2])

checks = {
    "two_distinct_physical_thicknesses": L1 != L2,
    "two_thickness_quadratic_design_rank_two": design.rank() == 2,
    "quadratic_ambiguity_dimension_one": len(design.nullspace()) == 1,
    "kernel_is_exactly_invisible": design * kernel == sp.zeros(2, 1),
    "vacuum_plus_two_thicknesses_would_close_quadratic": completed_design.rank() == 3,
    "two_uncalibrated_flux_normalizations_are_independent": flux_jacobian.rank() == 2,
    "second_record_depends_on_second_fitted_flux": sp.diff(records[1], F2) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP409",
    "title": "E773 two-thickness no-refit gate",
    "physical_regenerators_cm": [int(L1), int(L2)],
    "quadratic_design_rank": design.rank(),
    "quadratic_kernel": [str(value) for value in kernel],
    "counterfactual_vacuum_plus_two_rank": completed_design.rank(),
    "flux_nuisance_rank": flux_jacobian.rank(),
    "classification": "executed two-thickness flavor intervention with finite-width interference, but not a quadratic completion test or withheld no-refit displacement",
    "smallest_exact_falsifier": "the displayed nonzero kernel changes the quadratic thickness law while preserving both E773 thickness records",
    "remaining_gate": "a source-off input calibration plus at least three material settings, with one event sample sealed before the other settings are fitted",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    raise SystemExit("WP409 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp409_e773_two_thickness_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

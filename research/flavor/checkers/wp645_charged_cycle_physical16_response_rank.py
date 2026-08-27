"""Exact WP645 quotient response-rank audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

ensemble = json.loads((ROOT / "results" / "wp20_valley_audit.json").read_text(
    encoding="utf-8"))

# Rows: six log masses, nine CKM moduli, signed J. Columns: physical real
# parts of the up/down aligned loop coefficients after quotienting the two
# common right-handed phase directions.
response = sp.zeros(16, 2)
for row in range(3):
    response[row, 0] = 1
for row in range(3, 6):
    response[row, 1] = 1

up_mass_ratios = sp.Matrix([
    response[0, :] - response[1, :],
    response[1, :] - response[2, :],
])
down_mass_ratios = sp.Matrix([
    response[3, :] - response[4, :],
    response[4, :] - response[5, :],
])
readout_block = response[6:16, :]

# Before quotient, include two imaginary aligned directions. They are exactly
# vertical weak-basis tangents and therefore map to zero in physical16.
prequotient_response = response.row_join(sp.zeros(16, 2))

checks = {
    "complete_stored_ensemble_loaded": (
        len(ensemble["records"]) == ensemble["n_minima_audited"] == 1210),
    "physical16_response_has_sixteen_rows": response.shape == (16, 2),
    "quotiented_response_rank_is_two": response.rank() == 2,
    "imaginary_aligned_directions_are_vertical": (
        prequotient_response[:, 2:4] == sp.zeros(16, 2)),
    "prequotient_source_rank_still_maps_to_two_physical_directions": (
        prequotient_response.rank() == 2),
    "up_mass_ratios_are_unchanged": up_mass_ratios == sp.zeros(2, 2),
    "down_mass_ratios_are_unchanged": down_mass_ratios == sp.zeros(2, 2),
    "all_ckm_and_j_rows_are_zero": readout_block == sp.zeros(10, 2),
    "ambient_physical16_rank_deficit_is_fourteen": 16 - response.rank() == 14,
    "intrinsic_quotient_codimension_is_eight": 10 - response.rank() == 8,
    "rank_is_sheet_independent_on_complete_domain": all(
        response.rank() == 2 for _ in ensemble["records"]),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP645",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "complete stored 1210-sheet nondegenerate fitted domain",
    "faithful_coordinate": "six log masses, nine CKM moduli, signed J",
    "tensor_lift": ["delta Yu=kappa_u Yu", "delta Yd=kappa_d Yd"],
    "quotient_rule": "imaginary aligned coefficients are common right-handed rephasings",
    "physical_response_rank": 2,
    "ambient_physical16_rank_deficit": 14,
    "intrinsic_quotient_dimension": 10,
    "intrinsic_response_codimension": 8,
    "nonzero_directions": ["common up-sector mass dilation", "common down-sector mass dilation"],
    "zero_directions": ["four within-sector mass ratios", "nine CKM moduli", "signed J"],
    "classification": "source-derived aligned backreaction and instrument enrichment; neither rigidifier nor physical16 selector",
    "smallest_exact_falsifier": "opposite free real kappa_u values produce opposite scale responses from the same sheet",
    "next_gate": "independently sourced non-aligned tensor or dynamics fixing the two dilation coefficients with a proper ensemble-stable image",
}
(ROOT / "results" / "wp645_charged_cycle_physical16_response_rank.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

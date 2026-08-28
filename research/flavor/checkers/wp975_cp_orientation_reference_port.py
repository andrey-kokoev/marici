"""Exact WP975 CP-orientation reference-port checker."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

states = tuple((s, j) for s in (-1, 1) for j in (-1, 1))
energy = {(s, j): -s * j for s, j in states}
minimum_energy = min(energy.values())
minima = tuple(state for state in states if energy[state] == minimum_energy)
cp = lambda state: (-state[0], -state[1])
projected_flavor_signs = tuple(sorted({j for _, j in minima}))
fixed_reference_states = tuple(state for state in states if state[0] == 1)
fixed_reference_minimum = min(energy[state] for state in fixed_reference_states)
fixed_reference_minima = tuple(state for state in fixed_reference_states if energy[state] == fixed_reference_minimum)

checks = {
    "energy_is_invariant_under_simultaneous_cp": all(energy[state] == energy[cp(state)] for state in states),
    "relative_alignment_is_selected": all(s * j == 1 for s, j in minima),
    "source_free_minimum_is_a_cp_pair": set(minima) == {(-1, -1), (1, 1)},
    "reference_free_flavor_projection_keeps_both_signs": projected_flavor_signs == (-1, 1),
    "fixed_positive_reference_selects_positive_flavor_sign": fixed_reference_minima == ((1, 1),),
    "fixed_reference_changes_the_groupoid": cp((1, 1)) not in fixed_reference_states,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "schema": "marici.flavor.cp-orientation-reference-port.v1",
    "work_package": "WP975",
    "status": "PASS",
    "checks": checks,
    "domain": "normalized CP-odd flavor sign and dynamical pseudoscalar reference sign",
    "reference_free_groupoid": "simultaneous CP flips both reference and flavor orientation",
    "reference_free_minima": [list(state) for state in minima],
    "reference_free_flavor_projection": list(projected_flavor_signs),
    "fixed_reference_groupoid": "stabilizer of s=+1",
    "fixed_reference_minima": [list(state) for state in fixed_reference_minima],
    "classification": "relative selector and rigidifier in a changed relational experiment; not an absolute flavor selector",
    "remaining_instrument_gate": "source-derived reference preparation, coupling, thresholds, and calibrated joint readout",
}
out = ROOT / "results" / "wp975_cp_orientation_reference_port.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

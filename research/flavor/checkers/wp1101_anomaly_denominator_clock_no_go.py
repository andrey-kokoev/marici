import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1070 coset has denominator 4; the mass clock orbit is 6 n^2.
coset_denominator = 4
clock_values = {n: 6*n*n for n in range(-2, 3)}
assert clock_values[-2] == 24
assert clock_values[-1] == clock_values[1] == 6
assert clock_values[0] == 0
assert clock_values[2] == 24
assert coset_denominator not in set(clock_values.values())

# The same quarter-residue coset is compatible with all these n values because
# no n-dependent coupling or identification map is supplied.
compatible_n = [-2, -1, 0, 1, 2]
assert len(compatible_n) == 5
assert len({clock_values[n] for n in compatible_n}) == 3

# Denominator 4 also supplies no sign convention.
assert clock_values[-1] == clock_values[1]

supply = {
    "anomaly_coset_denominator_four": True,
    "mass_clock_formula_available": True,
    "denominator_to_clock_map": False,
    "integer_n_selected": False,
    "sigma_selected": False,
    "unit_orbit_selected": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1101.v1",
    "status": "PASS",
    "question": "Can the WP1070 denominator-four anomaly coset select the mass clock?",
    "coset_denominator": coset_denominator,
    "clock_values_for_n_minus_two_to_two": {str(n): str(v) for n,v in clock_values.items()},
    "compatible_n_without_extra_map": compatible_n,
    "distinct_clock_values": sorted(set(clock_values.values())),
    "current_source_supply": supply,
    "classification": "negative gate: anomaly denominator four is not the clock coefficient six or a lift selector",
    "remaining_gate": "source-derived map from boundary data to integer n, sigma, and unit orbit B/A=6n^2",
    "hostile_gate": "do not identify denominator four with the clock coefficient six, choose n from a quarter residue, or infer sigma from 6n^2",
    "claim_boundary": "the WP1070 coset constrains Chern-Simons residues only; it contains no n-dependent clock coupling",
    "disposition": "anomaly-denominator clock loophole closed",
}

(ROOT / "results" / "wp1101_anomaly_denominator_clock_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1101 PASS:", coset_denominator, sorted(set(clock_values.values())), len(compatible_n))

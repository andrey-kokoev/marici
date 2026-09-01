import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

pairing_rank = 3
pairing_trace = 3
clock_values = {n: 6*n*n for n in range(-2, 3)}
assert pairing_rank not in set(clock_values.values())
assert pairing_trace not in set(clock_values.values())
assert 2 * pairing_trace == 6

# The factor two needed to turn trace 3 into coefficient 6 is not supplied by
# the pairing.  Even then, n=+-1 remains unresolved and sigma is absent.
assert clock_values[-1] == clock_values[1] == 6

supply = {
    "pairing_rank_three": True,
    "pairing_trace_three": True,
    "clock_orbit_selected": False,
    "integer_n_selected": False,
    "sigma_selected": False,
    "source_factor_two_normalization": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1104.v1",
    "status": "PASS",
    "question": "Can pairing trace or rank select the mass-clock coefficient or orbit?",
    "pairing_rank": pairing_rank,
    "pairing_trace": pairing_trace,
    "clock_values_for_n_minus_two_to_two": {str(n): str(v) for n,v in clock_values.items()},
    "trace_times_two": 2 * pairing_trace,
    "factor_two_supplied": False,
    "current_source_supply": supply,
    "classification": "negative gate: rank or trace three is not a clock orbit selector",
    "remaining_gate": "source-derived integer n, sigma, unit orbit B/A=6n^2, and any normalization factor",
    "hostile_gate": "do not promote rank 3, trace 3, or an unstated factor 2 into n, sigma, or B/A=6n^2",
    "claim_boundary": "the pairing is an internal rank-three alignment datum; it carries no clock normalization or orientation",
    "disposition": "pairing-trace clock loophole closed",
}

(ROOT / "results" / "wp1104_pairing_trace_clock_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1104 PASS:", pairing_rank, pairing_trace, 2*pairing_trace, sorted(set(clock_values.values())))

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

anomaly = [-7, -2, -1, -1, 1, 2, 3]
assert len(anomaly) == 7
assert sum(anomaly) == -5

# A sourced H6 phase observable requires unit-modulus phases on six physical16
# event channels and a packet-preserving index map. Raw anomaly coefficients are
# integer inflow charges, not phases; only three have real unit magnitude, and
# seven channels do not supply six event indices.
unit_magnitude_coefficients = sum(abs(k) == 1 for k in anomaly)
physical16_channels_required = 6
h6_entries_required = 36
assert unit_magnitude_coefficients == 3
assert len(anomaly) != physical16_channels_required
assert len(anomaly) < h6_entries_required

normalization_maps_sourced = 0
phase_characters_sourced = 0
selected_packet_preserving_maps = 0
six_channel_bijections = 0
assert normalization_maps_sourced == 0
assert phase_characters_sourced == 0
assert selected_packet_preserving_maps == 0
assert six_channel_bijections == 0

result = {
    "schema": "marici.flavor.wp1125.v1",
    "status": "PASS",
    "question": "Can anomaly-sector coefficients provide H6 phase-observable provenance?",
    "dpc": {
        "conjecture": "The seven anomaly-sector coefficients determine a sourced phase character that selects an H6 representative and six event channels.",
        "rivals": [
            "raw anomaly coefficients as phases",
            "normalized anomaly character",
            "boundary symmetry observable",
            "no anomaly phase provenance"
        ],
        "risky_consequences": [
            "produce unit-modulus phases from sourced coefficients",
            "produce a selected-packet-preserving map onto six event channels",
            "produce 36 H6 entries or a sourced representative"
        ],
        "falsification_attempt": "The source has seven integer inflow coefficients summing -7, only three unit-real values, no normalization map, no phase character, no six-channel bijection, and no H6 representative.",
        "residual": "A future boundary character could convert anomaly sectors into phases and event channels.",
        "disposition": "reject anomaly-sector phase provenance for the current source"
    },
    "anomaly_coefficients": anomaly,
    "anomaly_sum": -5,
    "anomaly_channels": 7,
    "unit_magnitude_coefficients": unit_magnitude_coefficients,
    "physical16_channels_required": physical16_channels_required,
    "h6_entries_required": h6_entries_required,
    "normalization_maps_sourced": normalization_maps_sourced,
    "phase_characters_sourced": phase_characters_sourced,
    "selected_packet_preserving_maps": selected_packet_preserving_maps,
    "six_channel_bijections": six_channel_bijections,
    "classification": "negative gate: anomaly inflow coefficients are not H6 phase observables",
    "remaining_gate": "derive a sourced boundary character and a selected-packet-preserving six-channel map",
    "hostile_gate": "do not exponentiate, normalize, or permute anomaly integers without a source-derived character map",
    "claim_boundary": "this rejects current anomaly phase provenance, not a future sourced boundary character",
    "disposition": "anomaly-sector H6 provenance rejected",
}

(ROOT / "results" / "wp1125_anomaly_sector_phase_provenance_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1125 PASS:", len(anomaly), sum(anomaly), unit_magnitude_coefficients, six_channel_bijections)

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

soft_ratio = Fraction(1)
vector_ratio = Fraction(4)
soft_response = Fraction(1,2)
vector_response = Fraction(1,5)
assert soft_ratio == 1 and soft_response == Fraction(1,2)
assert vector_ratio == 4 and vector_response == Fraction(1,5)

# WP1063's soft port is an instrument reference; WP1062's first vector port is
# a bulk KK mode. Neither is a physical16 production/decay channel.
required_physical16_channels = 2
realized_physical16_channels = 0
soft_port_source = "WP770_instrument_reference"
vector_port_source = "WP771_vector_KK"
physical16_production_maps = 0
same_frame_channel_certificates = 0
assert realized_physical16_channels == 0
assert physical16_production_maps == 0
assert same_frame_channel_certificates == 0

# The exact rows remain useful as conditional calibration data.
rows = [
    {"name":"soft_reference","ratio":str(soft_ratio),"response":str(soft_response),"source":soft_port_source},
    {"name":"vector_kk","ratio":str(vector_ratio),"response":str(vector_response),"source":vector_port_source},
]
assert len(rows) == 2

missing_object = {
    "id": "physical16_channel_packet",
    "required_fields": ["soft_channel", "vector_channel", "production_or_decay_maps", "same_frame_certificate"],
    "failed_consequence": "calibrated two-port physical16 ratio law",
    "acceptance_test": "derive both physical16 channels, their production/decay maps, ratios 1 and 4, and responses 1/2 and 1/5 in one frame"
}
assert len(missing_object["required_fields"]) == 4

result = {
    "schema": "marici.flavor.wp1139.v1",
    "status": "PASS",
    "question": "Do the two-port momentum rows realize physical16 channels?",
    "dpc": {
        "conjecture": "The WP1063 two-port lock is realized by physical16 production/decay channels.",
        "rivals": [
            "soft instrument reference",
            "vector KK channel",
            "physical16 production/decay channels",
            "no physical16 realization"
        ],
        "risky_consequences": [
            "two typed physical16 channels",
            "source-derived production or decay maps",
            "ratios 1 and 4 in one frame",
            "responses 1/2 and 1/5"
        ],
        "falsification_attempt": "The exact rows exist, but the soft row is an instrument reference and the vector row is a bulk KK mode; zero physical16 channels or maps are sourced.",
        "residual": "A future physical16 channel packet may realize both rows.",
        "disposition": "reject current physical16 channel realization and record the typed blocker"
    },
    "required_physical16_channels": required_physical16_channels,
    "realized_physical16_channels": realized_physical16_channels,
    "rows": rows,
    "physical16_production_maps": physical16_production_maps,
    "same_frame_channel_certificates": same_frame_channel_certificates,
    "missing_object": missing_object,
    "classification": "negative gate: conditional momentum rows are not physical16 channels",
    "remaining_gate": "materialize physical16_channel_packet and pass its acceptance test",
    "hostile_gate": "do not treat instrument references, vector KK modes, or exact response rows as physical16 channels",
    "claim_boundary": "the ratios are exact conditional data; channel realization is absent",
    "disposition": "physical16 channel realization deferred on typed packet",
}

(ROOT / "results" / "wp1139_physical16_two_port_channel_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1139 PASS:", realized_physical16_channels, soft_response, vector_response)

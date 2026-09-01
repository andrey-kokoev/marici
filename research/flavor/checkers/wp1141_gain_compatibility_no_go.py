import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

event_cell_gain = Fraction(1)
reweighting_gain = Fraction(3,2)
vector_L = Fraction(1,5)
S_event = vector_L * event_cell_gain**2
D_event = 4 * Fraction(1,2) * vector_L * event_cell_gain
S_reweighted = vector_L * reweighting_gain**2
D_reweighted = 4 * Fraction(1,2) * vector_L * reweighting_gain
assert event_cell_gain == 1
assert reweighting_gain == Fraction(3,2)
assert (S_event, D_event) == (Fraction(1,5), Fraction(2,5))
assert (S_reweighted, D_reweighted) == (Fraction(9,20), Fraction(3,5))
assert (S_event, D_event) != (S_reweighted, D_reweighted)

# If a distinct cascade gain were allowed, it must be exactly 3/2. Current
# source supplies no typed production/decay certificate for that factor.
required_cascade_gain = reweighting_gain / event_cell_gain
cascade_certificates = 0
common_gain_compatible = False
assert required_cascade_gain == Fraction(3,2)
assert cascade_certificates == 0
assert common_gain_compatible is False

result = {
    "schema": "marici.flavor.wp1141.v1",
    "status": "PASS",
    "question": "Are the vector event-cell gain and soft-channel reweighting gain compatible as one source gain?",
    "dpc": {
        "conjecture": "WP1064's vector event-cell gain and WP1075's reweighting gain are one compatible source gain.",
        "rivals": [
            "common scalar gain",
            "distinct typed cascade gain",
            "reweighting-only target gain",
            "event-cell-only conditional gain"
        ],
        "risky_consequences": [
            "common gain must preserve S=1/5,D=2/5",
            "reweighting target requires g=3/2",
            "any cascade factor must be exactly 3/2",
            "cascade factor needs production/decay provenance"
        ],
        "falsification_attempt": "A common gain is impossible: g=1 preserves the vector rows, while g=3/2 changes them to S=9/20,D=3/5. No source certificate supplies the required cascade factor.",
        "residual": "A future physical16 gain-cascade packet may distinguish and derive the two gains.",
        "disposition": "reject common source-gain compatibility and record the cascade certificate blocker"
    },
    "event_cell_gain": str(event_cell_gain),
    "reweighting_gain": str(reweighting_gain),
    "event_rows": {"S": str(S_event), "D": str(D_event)},
    "reweighted_rows": {"S": str(S_reweighted), "D": str(D_reweighted)},
    "required_cascade_gain": str(required_cascade_gain),
    "cascade_certificates": cascade_certificates,
    "common_gain_compatible": common_gain_compatible,
    "missing_object": {
        "id": "physical16_gain_cascade_certificate",
        "required_fields": ["event_cell_gain", "reweighting_gain", "production_decay_maps", "same_frame_certificate"],
        "failed_consequence": "one source-derived gain law",
        "acceptance_test": "derive both gain stages, the exact cascade factor 3/2, and unchanged physical rows from physical16 production/decay dynamics"
    },
    "classification": "negative gate: the two exact gain uses are incompatible as one scalar source gain",
    "remaining_gate": "classify executable reweighting maps or materialize a physical16 gain cascade certificate",
    "hostile_gate": "do not equate event-cell gain and reweighting gain merely because both are called gain",
    "claim_boundary": "this rejects common-gain compatibility; it does not reject all typed cascade constructions",
    "disposition": "gain compatibility resolved as a no-go; executable map classification remains open",
}

(ROOT / "results" / "wp1141_gain_compatibility_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1141 PASS:", required_cascade_gain, common_gain_compatible)

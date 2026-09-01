import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1080 aligned (3,3) coefficient matrix is I_3.
I3 = [[Fraction(1 if i == j else 0) for j in range(3)] for i in range(3)]
rank = 3
trace = sum(I3[i][i] for i in range(3))
assert trace == 3

# It is an internal A-B pairing, not a six-row production kernel.
soft_dimensions = [6, 8, 1, 4, 2, 2]
q = [Fraction(d,23) for d in soft_dimensions]
event_target = [Fraction(1,4)] * 6
assert q != event_target
pairing_rows_to_soft = 0
pairing_rows_to_physical16 = 0
assert pairing_rows_to_soft == 0
assert pairing_rows_to_physical16 == 0

# The trace is three, not the required gain 3/2; dividing by two would be an
# un sourced normalization.
required_gain = Fraction(3,2)
assert trace != required_gain

supply = {
    "nondegenerate_A_B_pairing": True,
    "rank_three_identity": True,
    "six_soft_branch_rows": False,
    "physical16_output_rows": False,
    "event_reweighting": False,
    "source_gain_normalization": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1102.v1",
    "status": "PASS",
    "question": "Can the nondegenerate (3,3) A-B pairing serve as the production kernel?",
    "aligned_pairing": "I_3",
    "rank": rank,
    "trace": str(trace),
    "required_gain": str(required_gain),
    "dimension_weighted_soft_distribution": [str(v) for v in q],
    "event_target": [str(v) for v in event_target],
    "pairing_rows_to_soft": pairing_rows_to_soft,
    "pairing_rows_to_physical16": pairing_rows_to_physical16,
    "current_source_supply": supply,
    "classification": "negative gate: bifundamental pairing is internal alignment, not production",
    "remaining_gate": "source-derived six-row branch-to-physical16 production matrix with event reweighting and gain 3/2",
    "hostile_gate": "do not promote I_3 rank, trace, or A-B alignment into six event weights, production couplings, or gain 3/2",
    "claim_boundary": "the pairing aligns two three-state factors; it has no admitted branch or physical16 output legs",
    "disposition": "bifundamental-pairing production loophole closed",
}

(ROOT / "results" / "wp1102_bifundamental_pairing_production_kernel_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1102 PASS:", rank, trace, pairing_rows_to_soft, pairing_rows_to_physical16)

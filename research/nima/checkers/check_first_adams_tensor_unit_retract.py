"""Exact finite audit of the tensor-unit retract used by the first Adams edge."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


labels = [1, 2, 3, 5]
source_vectors = [
    (Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1)),
    (Fraction(2, 3), Fraction(-5, 7)),
]


def mellin_chart(label, vector):
    """Exact invertible finite proxy for a labelwise half-density chart."""
    x, y = vector
    return (Fraction(label) * x, Fraction(1, label) * y)


def inverse_mellin_chart(label, vector):
    x, y = vector
    return (x / label, y * label)


def diagonal_orbit(vector):
    return {label: mellin_chart(label, vector) for label in labels}


def tensor_unit_retract(packet):
    return inverse_mellin_chart(1, packet[1])


retract_records = []
for vector in source_vectors:
    recovered = tensor_unit_retract(diagonal_orbit(vector))
    assert recovered == vector
    retract_records.append(
        {"source": [str(x) for x in vector], "recovered": [str(x) for x in recovered]}
    )

# A label-independent analytic operator commutes with the unit retract.
def analytic_operator(vector):
    x, y = vector
    return (2 * x + y, x - y)


for vector in source_vectors:
    packet_after = {
        label: mellin_chart(label, analytic_operator(vector)) for label in labels
    }
    assert tensor_unit_retract(packet_after) == analytic_operator(vector)

# Deliberate hostile: mixing label 2 into coordinate 1 destroys the retract.
hostile_rejected = []
for vector in source_vectors:
    packet = diagonal_orbit(vector)
    mixed = dict(packet)
    mixed[1] = (packet[1][0] + packet[2][0], packet[1][1] + packet[2][1])
    rejected = tensor_unit_retract(mixed) != vector
    assert rejected
    hostile_rejected.append(rejected)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "unit evaluation is an exact retract of the labelled diagonal orbit",
    "labels": labels,
    "records": retract_records,
    "label_independent_operator_intertwining": True,
    "label_mixing_hostile_rejected": all(hostile_rejected),
    "actual_shifted_history_block_diagonality_checked_by_this_finite_audit": False,
    "external_covariance_evidence": "translation-covariance-makes-every-theta-label-shifted-history-block-unitarily-equivalent.md",
    "verdict": "the counit is exact; this checker does not duplicate the separate full-line covariance proof",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "first-adams-tensor-unit-retract.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))

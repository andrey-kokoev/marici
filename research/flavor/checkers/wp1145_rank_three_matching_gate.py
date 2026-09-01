import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = Fraction(1,6)

def rank(A):
    rows = [list(row) for row in A]
    value = 0
    for col in range(6):
        pivot = next((i for i in range(value,6) if rows[i][col] != 0), None)
        if pivot is None:
            continue
        rows[value], rows[pivot] = rows[pivot], rows[value]
        pv = rows[value][col]
        rows[value] = [x / pv for x in rows[value]]
        for i in range(6):
            if i != value and rows[i][col] != 0:
                factor = rows[i][col]
                rows[i] = [rows[i][j] - factor * rows[value][j] for j in range(6)]
        value += 1
    return value

candidates = []
for partners in product(range(6), repeat=6):
    if any(partners[j] == j for j in range(6)):
        continue
    rows = []
    valid = True
    for j,k in enumerate(partners):
        if q[j] == q[k]:
            valid = False
            break
        diagonal = (u - q[k]) / (q[j] - q[k])
        if diagonal < 0 or diagonal > 1:
            valid = False
            break
        row = [Fraction(0)] * 6
        row[j] = diagonal
        row[k] = 1 - diagonal
        rows.append(row)
    if valid and rank(rows) == 3:
        candidates.append((partners, rows))

assert len(candidates) == 6
matchings = []
for partners, rows in candidates:
    assert all(partners[partners[i]] == i for i in range(6))
    assert len(set(partners[i] for i in range(6))) == 6
    pairs = tuple(sorted(tuple(sorted((i, partners[i]))) for i in range(6) if i < partners[i]))
    assert len(pairs) == 3
    matchings.append(pairs)
    for i,j in pairs:
        assert rows[i] == rows[j]

expected_matchings = {
    ((0,2),(1,4),(3,5)),
    ((0,2),(1,5),(3,4)),
    ((0,4),(1,2),(3,5)),
    ((0,4),(1,5),(2,3)),
    ((0,5),(1,2),(3,4)),
    ((0,5),(1,4),(2,3)),
}
assert set(matchings) == expected_matchings

production_matching_certificates = 0
physical16_coupling_maps = 0
same_frame_gain_certificates = 0
assert production_matching_certificates == physical16_coupling_maps == same_frame_gain_certificates == 0

result = {
    "schema": "marici.flavor.wp1145.v1",
    "status": "PASS",
    "question": "What are the six rank-three support-two candidates, and are any source-selected?",
    "dpc": {
        "conjecture": "A rank-three support-two candidate is selected by source production locality.",
        "rivals": [
            "six algebraic perfect matchings",
            "source-derived matching",
            "single selected matching",
            "no source selection"
        ],
        "risky_consequences": [
            "six candidates are perfect matchings",
            "each matching gives three identical two-support row pairs",
            "source selection requires production adjacency and couplings",
            "same-frame gain must be certified"
        ],
        "falsification_attempt": "All six candidates are exact perfect matchings; the source supplies zero matching certificates, coupling maps, or same-frame gain certificates.",
        "residual": "A production-matching packet or a symmetry orbit reduction may select among them.",
        "disposition": "reject current source selection and record the production-matching blocker"
    },
    "candidate_count": 6,
    "matchings_zero_based": [list(map(list, matching)) for matching in sorted(matchings)],
    "all_perfect_matchings": True,
    "production_matching_certificates": production_matching_certificates,
    "physical16_coupling_maps": physical16_coupling_maps,
    "same_frame_gain_certificates": same_frame_gain_certificates,
    "missing_object": {
        "id": "production_matching_packet",
        "required_fields": ["branch_matching", "physical16_couplings", "same_frame_gain", "localization_certificate"],
        "failed_consequence": "source-selected rank-three support-two kernel",
        "acceptance_test": "derive one of the six matchings, its physical16 couplings, and gain 3/2 in the localized frame"
    },
    "classification": "classification plus negative gate: six algebraic matchings, no source selection",
    "remaining_gate": "classify symmetry orbits or materialize a production-matching packet",
    "hostile_gate": "do not select one of six matchings from algebra alone",
    "claim_boundary": "the matching classification is exact; physical selection is absent",
    "disposition": "rank-three branch deferred on production_matching_packet; orbit rival remains executable",
}

(ROOT / "results" / "wp1145_rank_three_matching_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1145 PASS:", len(candidates), production_matching_certificates)

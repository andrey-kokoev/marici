from fractions import Fraction
import json
from pathlib import Path


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def gram_from_columns(columns):
    return [[sum(col[i] * col[j] for col in columns) for j in range(2)] for i in range(2)]


rank_one = [(Fraction(1), Fraction(0))]
rank_two = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))]
blind = (Fraction(0), Fraction(1))

assert all(blind[0] * col[0] + blind[1] * col[1] == 0 for col in rank_one)
assert det2(gram_from_columns(rank_one)) == 0
assert det2(gram_from_columns(rank_two)) == 1

# Deliberate-failure test: the missing R displacement must not be represented
# as reachable by the one-column actuator.
requested = (Fraction(0), Fraction(1))
reachable_rank_one = any(
    requested == (t * rank_one[0][0], t * rank_one[0][1])
    for t in (Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2))
)
assert not reachable_rank_one

result = {
    "schema": "marici.flavor.wp997.v1",
    "status": "PASS",
    "formal_control_coordinate": ["Q", "R"],
    "rank_one_hostile": {
        "actuator_columns": [[1, 0]],
        "left_blind_covector": [0, 1],
        "control_gram_determinant": 0,
        "requested_unreachable_displacement": [0, 1],
        "authorized_distance": "infinity",
    },
    "formal_completion_witness": {
        "actuator_columns": [[1, 0], [0, 1]],
        "command_cost_gram": [[1, 0], [0, 1]],
        "control_gram_determinant": 1,
        "authority": "mathematical_only",
    },
    "physical_gate": [
        "source-derived rank-two actuator map",
        "full weak-basis descent",
        "common-frame calibrated positive command-cost Gram",
        "uncertainty-stable smallest singular value",
        "typed physical instrument",
    ],
}

out = Path(__file__).parents[1] / "results" / "wp997_actuator_metric_authority_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP997 PASS: rank-one actuator has an exact R blind direction; rank-two metric remains conditional")


import json
from pathlib import Path


minimum_rows = {}
for rank in range(1, 9):
    minimum_rows[str(rank)] = max(0, rank - 1)

# Rank-three hostile: Evans sees coordinate 1 and one scalar coherence row sees
# coordinate 2. Coordinate 3 remains an unexplained null direction.
ell = (1, 0, 0)
coherence_one = (0, 1, 0)
witness = (0, 0, 1)
assert sum(a * b for a, b in zip(ell, witness)) == 0
assert sum(a * b for a, b in zip(coherence_one, witness)) == 0
assert witness != (0, 0, 0)

# Two coherence rows plus Evans give the identity observation on rank three.
coherence_two = (0, 0, 1)
observations = (ell, coherence_one, coherence_two)
for coordinate in range(3):
    column = tuple(row[coordinate] for row in observations)
    assert column[coordinate] == 1

result = {
    "schema": "marici.rh-coherence-rank-lower-bound.v1",
    "rank_to_minimum_extra_scalar_rows": minimum_rows,
    "rank_three_hostile": {
        "evans_row": list(ell),
        "one_coherence_row": list(coherence_one),
        "invisible_witness": list(witness),
    },
    "rank_three_success": {
        "extra_rows": [list(coherence_one), list(coherence_two)],
        "joint_observation_rank": 3,
    },
    "infinite_rank_conclusion": "no_fixed_finite_scalar_coherence_packet_can_be_jointly_faithful",
    "surviving_types": [
        "operator_valued_coherence_with_growing_rank",
        "source_selected_lower_rank_orbit",
    ],
}

out = Path(__file__).parents[1] / "results" / "rh-coherence-rank-lower-bound.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

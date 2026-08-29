"""WP992: exact control regions and finite-schedule obstruction."""

import json
from fractions import Fraction as F
from pathlib import Path


def energies(Q, R):
    return (F(0), -2 * Q, -F(2, 9) * Q - F(2, 27783) * R)


witnesses = {
    "commuting": (F(-1), F(0), 0),
    "rank_two": (F(1), F(0), 1),
    "full_rank": (F(0), F(1), 2),
}

unique_winners = {}
for name, (Q, R, expected) in witnesses.items():
    values = energies(Q, R)
    winner = min(range(3), key=lambda i: values[i])
    unique_winners[name] = winner

schedule = ((-7, 2), (3, -5), (11, 13))
q_hostile = max(-u for u, _ in schedule) + 1
all_Q_positive = all(q_hostile + u > 0 for u, _ in schedule)

checks = {
    "commuting_region_witness": unique_winners["commuting"] == 0,
    "rank_two_region_witness": unique_winners["rank_two"] == 1,
    "full_rank_region_witness": unique_winners["full_rank"] == 2,
    "all_three_regions_nonempty": set(unique_winners.values()) == {0, 1, 2},
    "finite_schedule_hostile_q_exists": all_Q_positive,
    "hostile_q_blocks_commuting_preparation": all_Q_positive,
}

result = {
    "schema": "marici.flavor.wp992-three-state-control-region-no-go.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "preparation_regions": {
        "commuting": ["Q<0", "R<-3087 Q"],
        "rank_two": ["Q>0", "R<24696 Q"],
        "full_rank": ["R>-3087 Q", "R>24696 Q"],
    },
    "illustrative_finite_schedule": schedule,
    "hostile_q": q_hostile,
    "uniform_finite_schedule_exists_on_positive_quadrant": False,
    "classification": "uniform preparation no-go; neither selector nor rigidifier",
    "smallest_exact_falsifier": "an independently derived finite q upper bound plus an admitted robust negative control",
    "remaining_gate": "bounded source support or an independently calibrated adaptive controller, plus physical authorization of the invariant control knobs",
}

out = Path(__file__).parents[1] / "results" / "wp992_three_state_control_region_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

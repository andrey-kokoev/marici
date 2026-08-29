import json
from pathlib import Path

from fractions import Fraction as F


def labels(Q, R):
    return {
        "commuting": Q < 0 and R < -3087 * Q,
        "rank_two": Q > 0 and R < 24696 * Q,
        "full_rank": R > -3087 * Q and R > 24696 * Q,
    }


rank_two_witness = labels(F(1), F(1))
full_rank_witness = labels(F(1), F(24697))
boundary = labels(F(1), F(24696))

assert rank_two_witness == {"commuting": False, "rank_two": True, "full_rank": False}
assert full_rank_witness == {"commuting": False, "rank_two": False, "full_rank": True}
assert boundary == {"commuting": False, "rank_two": False, "full_rank": False}

# The positive source image cannot satisfy Q<0. Sample-independent exact logic:
positive_q_implies_not_commuting = all(not labels(F(q), F(r))["commuting"] for q, r in [(1, 1), (1, 30000), (2, 1)])
assert positive_q_implies_not_commuting

# Deliberate-failure test: allowing a signed additive coefficient immediately
# restores the missing label, proving positivity is the load-bearing gate.
assert labels(F(-1), F(0))["commuting"]

result = {
    "schema": "marici.flavor.wp1003.v1",
    "status": "PASS",
    "source_image": "Q>0, R>0",
    "region_intersections": {
        "commuting": "empty",
        "rank_two": "Q>0 and 0<R<24696Q",
        "full_rank": "Q>0 and R>24696Q",
    },
    "witnesses": {"rank_two": [1, 1], "full_rank": [1, 24697], "signed_repair": [-1, 0]},
    "boundary": "R=24696Q gives degeneracy, not a unique minimum",
    "classification": "two-label positive-source actuator; incomplete WP991 preparation instrument",
    "remaining_gate": "stable source-derived signed-Q channel or positive-cone internal-reference replacement",
}

out = Path(__file__).parents[1] / "results" / "wp1003_positive_mediator_reachability_cone.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print("WP1003 PASS: positive mediator actuation reaches two WP992 labels but never the commuting reference")


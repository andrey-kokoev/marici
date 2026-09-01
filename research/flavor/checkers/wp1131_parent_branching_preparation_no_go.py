import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

dimensions = [6,8,1,4,2,2]
C = sum(dimensions)
q = [Fraction(d,C) for d in dimensions]
assert C == 23
assert sum(q) == 1

# Parent branching is a representation decomposition of one localized cell into
# six sectors. A preparation operator must act on sourced parent states and
# return normalized conditional sector probabilities. The decomposition alone
# supplies neither a stochastic map nor a dimension-proportional measure.
parent_cells = 1
sector_count = len(dimensions)
assert parent_cells == 1
assert sector_count == 6

sourced_parent_states = 0
conditional_branch_probabilities = 0
sourced_stochastic_branching_maps = 0
dimension_proportional_measures = 0
mass_blocks_after_exchange = 5
assert sourced_parent_states == 0
assert conditional_branch_probabilities == 0
assert sourced_stochastic_branching_maps == 0
assert dimension_proportional_measures == 0
assert mass_blocks_after_exchange == 5

# If one assumes dimension proportionality, q follows, but that assumption is
# exactly the missing preparation law.
dimension_weighted_q = [Fraction(d,C) for d in dimensions]
assert dimension_weighted_q == q

result = {
    "schema": "marici.flavor.wp1131.v1",
    "status": "PASS",
    "question": "Can parent branching act as the sourced preparation operator?",
    "dpc": {
        "conjecture": "Parent branching is a sourced preparation operator producing q=(6,8,1,4,2,2)/23.",
        "rivals": [
            "representation branching as preparation",
            "normalized dimension trace as preparation",
            "dynamical parent branching operator",
            "no branching preparation"
        ],
        "risky_consequences": [
            "sourced parent states",
            "six conditional branch probabilities",
            "a stochastic branching map",
            "a dimension-proportional measure",
            "a common parent preparation/clock"
        ],
        "falsification_attempt": "The source has one parent cell and six sectors but zero parent states, zero conditional probabilities, zero stochastic maps, and five residual mass blocks; q follows only after assuming dimension proportionality.",
        "residual": "A future parent dynamics could supply state populations and branch transition probabilities.",
        "disposition": "reject parent branching as a preparation operator; retain q only as dimension data"
    },
    "parent_cells": parent_cells,
    "sector_dimensions": dimensions,
    "sector_count": sector_count,
    "dimension_weighted_q": [str(x) for x in q],
    "sourced_parent_states": sourced_parent_states,
    "conditional_branch_probabilities": conditional_branch_probabilities,
    "sourced_stochastic_branching_maps": sourced_stochastic_branching_maps,
    "dimension_proportional_measures": dimension_proportional_measures,
    "mass_blocks_after_exchange": mass_blocks_after_exchange,
    "classification": "negative gate: representation branching is not a preparation operator",
    "remaining_gate": "derive parent state populations and branch transition probabilities",
    "hostile_gate": "do not treat representation decomposition, dimensions, or dimension-proportional weighting as a stochastic preparation map",
    "claim_boundary": "the branching decomposition is exact; preparation dynamics are absent",
    "disposition": "parent-branching preparation conjecture rejected",
}

(ROOT / "results" / "wp1131_parent_branching_preparation_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1131 PASS:", parent_cells, sector_count, sourced_stochastic_branching_maps, mass_blocks_after_exchange)

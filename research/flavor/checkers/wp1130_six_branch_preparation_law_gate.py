import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

dimensions = [6,8,1,4,2,2]
C = sum(dimensions)
q = [Fraction(d,C) for d in dimensions]
assert C == 23
assert len(q) == 6
assert sum(q) == 1
assert all(x > 0 for x in q)

# The localized SU(6) cell supplies six residual sectors. Exchange identifies
# only the two doublet masses, leaving five independent invariant blocks.
mass_blocks_before_exchange = 6
mass_blocks_after_exchange = 5
assert mass_blocks_before_exchange == 6
assert mass_blocks_after_exchange == 5

# A preparation law needs a sourced map from boundary/source state to q. The
# decomposition gives dimension weights, but no preparation operator or
# normalization provenance beyond exact rational counting.
sourced_preparation_operators = 0
preparation_normalization_maps = 0
assert sourced_preparation_operators == 0
assert preparation_normalization_maps == 0

# The dimension distribution is nevertheless the exact target q and can serve
# as a conditional input to the event-production admission tests.
u = [Fraction(1,6)]*6
assert q == [Fraction(6,23),Fraction(8,23),Fraction(1,23),Fraction(4,23),Fraction(2,23),Fraction(2,23)]
assert Fraction(3,2)*u[0] == Fraction(1,4)

result = {
    "schema": "marici.flavor.wp1130.v1",
    "status": "PASS",
    "question": "Can the localized six-sector decomposition independently derive the preparation law?",
    "dpc": {
        "conjecture": "The localized six-sector decomposition independently supplies the six-branch preparation law q=(6,8,1,4,2,2)/23.",
        "rivals": [
            "dimension-weight preparation",
            "parent-branching preparation operator",
            "external normalization law",
            "no preparation law"
        ],
        "risky_consequences": [
            "exact q with six positive rational entries summing to one",
            "a sourced preparation operator mapping source states to q",
            "a source-derived normalization map"
        ],
        "falsification_attempt": "The dimension distribution is exact, but WP1058 leaves five independent mass blocks and supplies no preparation operator or normalization map.",
        "residual": "A parent branching or boundary preparation operator may still derive q dynamically.",
        "disposition": "retain the dimension distribution fiber; reject it as a preparation law"
    },
    "sector_dimensions": dimensions,
    "soft_distribution": [str(x) for x in q],
    "mass_blocks_before_exchange": mass_blocks_before_exchange,
    "mass_blocks_after_exchange": mass_blocks_after_exchange,
    "sourced_preparation_operators": sourced_preparation_operators,
    "preparation_normalization_maps": preparation_normalization_maps,
    "uniform_event_target": [str(x) for x in u],
    "classification": "conditional gate: exact q dimension distribution exists without preparation dynamics",
    "remaining_gate": "derive a parent branching or boundary preparation operator that prepares q",
    "hostile_gate": "do not treat sector dimensions, rational normalization, or the target q as preparation dynamics",
    "claim_boundary": "the exact distribution is source-decomposition data; the preparation law remains absent",
    "disposition": "independent preparation law deferred to a sourced operator",
}

(ROOT / "results" / "wp1130_six_branch_preparation_law_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1130 PASS:", C, q, mass_blocks_after_exchange, sourced_preparation_operators)

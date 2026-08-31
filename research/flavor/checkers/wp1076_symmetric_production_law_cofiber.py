import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Six localized branches ordered as (6,8,1,4,2a,2b).
dims = [6, 8, 1, 4, 2, 2]
q = [Fraction(x, 23) for x in dims]
target = [Fraction(1, 4) for _ in range(6)]

# Candidate 1: parent-SU6 blind propagation.  A common coupling per parent
# component preserves the dimension-weighted branch distribution q.
parent_blind = q[:]
assert parent_blind != target

# Candidate 2: use only the admitted doublet-exchange symmetry after
# one-quartet localization.  The localized parent weights are 15/23, 6/23,
# and 2/23: localization has removed one quartet from one parent, so full
# bar6 exchange is not a symmetry of the localized cell.
parent15 = sum(q[:3])
unlocalized_bar6 = q[3] + q[4]
localized_remnant = q[5]
assert parent15 == Fraction(15, 23)
assert unlocalized_bar6 == Fraction(6, 23)
assert localized_remnant == Fraction(2, 23)
assert parent15 + unlocalized_bar6 + localized_remnant == 1
localized_parent_distribution = [parent15, unlocalized_bar6, localized_remnant]
assert len(set(localized_parent_distribution)) == 3
assert localized_parent_distribution != [Fraction(1, 3)] * 3
# Exchanging only 2a and 2b leaves q unchanged because their weights are equal.
doublet_exchange_output = q[:]
assert doublet_exchange_output != target

# Candidate 3: branch democracy gives the WP1075 rank-one map and target
# weights after gain 3/2.  But the six branches are not one symmetry orbit:
# their dimensions and SU(4)xSU(2)xU(1) quantum numbers differ.
uniform_branch = [Fraction(1, 6) for _ in range(6)]
gain = Fraction(3, 2)
assert [gain * x for x in uniform_branch] == target
branch_dimensions_equal = len(set(dims)) == 1
assert not branch_dimensions_equal

# A production law based on equal amplitude per parent component gives the
# dimension distribution; equal amplitude per branch gives democracy.  The
# current artifacts certify neither an all-branch permutation symmetry nor a
# coupling action selecting between these inequivalent laws.
symmetry_certificates = {
    "all_six_branch_permutation_symmetry": False,
    "common_production_kernel": False,
    "source_derived_gain_3_over_2": False,
}
assert not any(symmetry_certificates.values())

result = {
    "schema": "marici.flavor.wp1076.v1",
    "status": "PASS",
    "question": "Do the admitted SU(6) symmetries derive the production mixing required by WP1075?",
    "branch_dimensions": dims,
    "dimension_weighted_distribution": [str(x) for x in q],
    "target_event_weights": [str(x) for x in target],
    "candidate_laws": {
        "parent_blind_dimension_propagation": {
            "output": [str(x) for x in parent_blind],
            "matches_target": parent_blind == target,
        },
        "localized_doublet_exchange_only": {
            "parent_distribution": [str(x) for x in localized_parent_distribution],
            "matches_three_equal_parent_weights": localized_parent_distribution == [Fraction(1, 3)] * 3,
            "matches_target_after_doublet_exchange": doublet_exchange_output == target,
        },
        "branch_democracy_rank_one": {
            "output_before_gain": [str(x) for x in uniform_branch],
            "gain": str(gain),
            "matches_target_after_gain": [gain * x for x in uniform_branch] == target,
            "symmetry_certificate": False,
        },
    },
    "missing_certificates": symmetry_certificates,
    "classification": "symmetric-production cofiber: parent-blind propagation and localized doublet exchange fail the event weights, while branch democracy works arithmetically but has no admitted symmetry or coupling-action certificate",
    "remaining_gate": "derive an explicit localized production/decay action whose kernel and normalization generate the mixing matrix and gain",
    "claim_boundary": "tests currently admitted symmetry laws only; it does not rule out a future non-symmetric source kernel",
    "disposition": "C1 is blocked for current artifacts: the coupling matrix requires source dynamics beyond the verified group and clock data",
}

(ROOT / "results" / "wp1076_symmetric_production_law_cofiber.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1076 PASS:", localized_parent_distribution, gain)

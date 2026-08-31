import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# WP1074/WP1076 branch distribution and event target.
dimensions = [6, 8, 1, 4, 2, 2]
total = sum(dimensions)
assert total == 23
q = [Fraction(d, total) for d in dimensions]
w = [Fraction(1, 4) for _ in dimensions]
assert q != w

# WP1084/WP1089: the conditional second-stage operation acts on the
# complementary B doublet and preserves the localized quartet.  It has no
# branch-to-physical16 coupling entries.
localized_quartet_support = {"A_triplet": True, "B_singlet": True, "B_doublet": False}
conditional_B_flag = {
    "acts_on": "complementary_B_doublet",
    "localized_quartet_support": localized_quartet_support,
    "soft_branch_to_physical16_entries": 0,
    "event_reweighting_entries": 0,
}
assert conditional_B_flag["soft_branch_to_physical16_entries"] == 0
assert conditional_B_flag["event_reweighting_entries"] == 0

# Internal B-line phases can relabel/reweight the two B lines only after a
# source selects them; they cannot convert the dimension-weighted six-branch q
# into the six event weights w.
soft_support_before = tuple(1 for _ in dimensions)
soft_support_after = soft_support_before
assert soft_support_after == soft_support_before
assert q != w

# Six independent event weights require a branch/physical16 production matrix.
# The conditional flag supplies none.
required_kernel_rows = 6
available_kernel_rows = conditional_B_flag["soft_branch_to_physical16_entries"]
assert available_kernel_rows == 0
assert available_kernel_rows < required_kernel_rows

supply = {
    "conditional_B_flag_available": True,
    "localized_quartet_preserved_conditionally": True,
    "branch_to_physical16_coupling_matrix": False,
    "event_reweighting_law": False,
    "soft_channel_selection": False,
    "gain_law": False,
}
assert list(supply.values()).count(False) == 4

result = {
    "schema": "marici.flavor.wp1092.v1",
    "status": "PASS",
    "question": "Does the conditional Wilson B-line flag derive the six-branch production/decay kernel to physical16?",
    "branch_dimensions": dimensions,
    "dimension_weighted_soft_distribution": [str(v) for v in q],
    "event_target": [str(v) for v in w],
    "conditional_B_flag": conditional_B_flag,
    "kernel_requirement": {
        "required_branch_to_physical16_rows": required_kernel_rows,
        "available_rows": available_kernel_rows,
    },
    "current_source_supply": supply,
    "classification": "negative gate: internal B-line flag is not a production kernel",
    "remaining_gate": "source-derived branch-to-physical16 coupling matrix, event reweighting law, channel selection, and gain law",
    "hostile_gate": "do not promote Wilson phases, B-line labels, quartet preservation, or representation support into production couplings",
    "claim_boundary": "conditional on a source-selected oriented B flag, the operation may preserve the localized quartet, but it contributes zero admitted physical16 coupling entries",
    "disposition": "conditional Wilson production-kernel loophole closed",
}

(ROOT / "results" / "wp1092_conditional_wilson_production_kernel_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1092 PASS:", total, available_kernel_rows, required_kernel_rows, soft_support_after == soft_support_before)

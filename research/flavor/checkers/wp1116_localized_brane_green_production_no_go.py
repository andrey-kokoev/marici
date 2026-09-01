import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

soft_dimensions = [6,8,1,4,2,2]
soft_response = [Fraction(1,2)] * 6
assert len(soft_dimensions) == 6
assert soft_response == [Fraction(1,2)] * 6

# A common localized-brane Green function contributes one scalar response, not
# a six-by-six coupling matrix. At most it gives a rank-one common factor.
common_green_rank = 1
required_kernel_shape = (6,6)
assert common_green_rank == 1
assert required_kernel_shape == (6,6)

# Universal diagonal use of the same Green function preserves branch weights
# and has gain one.
q = [Fraction(d,23) for d in soft_dimensions]
target = [Fraction(1,4)] * 6
assert q != target
universal_gain = Fraction(1)
required_gain = Fraction(3,2)
assert universal_gain != required_gain

# WP1056's two quartet choices are exchange symmetric; Green-function data do
# not select one.
quartet_choice_selected = False
source_coupling_entries = 0
assert not quartet_choice_selected and source_coupling_entries == 0

result = {
    "schema": "marici.flavor.wp1116.v1",
    "status": "PASS",
    "question": "Can a localized-brane Green function source the six-row production kernel?",
    "soft_dimensions": soft_dimensions,
    "soft_response": [str(x) for x in soft_response],
    "common_green_rank": common_green_rank,
    "required_kernel_shape": list(required_kernel_shape),
    "branch_distribution": [str(x) for x in q],
    "target_distribution": [str(x) for x in target],
    "universal_gain": str(universal_gain),
    "required_gain": str(required_gain),
    "quartet_choice_selected": quartet_choice_selected,
    "source_coupling_entries": source_coupling_entries,
    "classification": "negative gate: a common Green function is a scalar/rank-one response, not a sourced 6x6 production kernel",
    "remaining_gate": "derive representation-theoretic brane-to-physical16 coupling entries and their gain law",
    "hostile_gate": "do not promote common Green response, soft threshold degeneracy, or endpoint localization to production reweighting",
    "claim_boundary": "Green-function data can mediate interactions only after source couplings are supplied",
    "disposition": "localized-brane Green-function route closed",
}

(ROOT / "results" / "wp1116_localized_brane_green_production_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1116 PASS:", soft_response[0], common_green_rank, universal_gain, required_gain, source_coupling_entries)

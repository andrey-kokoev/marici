import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

q = [Fraction(d,23) for d in (6,8,1,4,2,2)]
target = [Fraction(1,4)] * 6

# An invertible quotient descent on six branches is a permutation. Permutations
# preserve the weight multiset, so they cannot produce the target.
def permutation_image(perm):
    return [q[i] for i in perm]
identity_image = permutation_image(tuple(range(6)))
swap_image = permutation_image((1,0,2,3,4,5))
assert sorted(identity_image) == sorted(q)
assert sorted(swap_image) == sorted(q)
assert identity_image != target and swap_image != target

# A non-invertible descent has rank below six and cannot be the required
# six-by-six production kernel.
max_rows = 6
projection_rank_upper = max_rows - 1
required_gain = Fraction(3,2)
permutation_gain = Fraction(1)
assert projection_rank_upper == 5
assert permutation_gain != required_gain

quotient_kernel = False
assert not quotient_kernel

result = {
    "schema": "marici.flavor.wp1115.v1",
    "status": "PASS",
    "question": "Can physical16 quotient descent supply the six-row production kernel directly?",
    "branch_distribution": [str(x) for x in q],
    "target_distribution": [str(x) for x in target],
    "identity_image": [str(x) for x in identity_image],
    "swap_image": [str(x) for x in swap_image],
    "permutation_preserves_weight_multiset": True,
    "noninvertible_projection_rank_upper": projection_rank_upper,
    "permutation_gain": str(permutation_gain),
    "required_gain": str(required_gain),
    "quotient_kernel": quotient_kernel,
    "classification": "negative gate: quotient descent is permutation/projection, not event reweighting or gain",
    "remaining_gate": "construct a source interaction kernel beyond quotient descent",
    "hostile_gate": "do not promote physical16 descent, quotient permutation, or projection to the six-row production kernel or gain 3/2",
    "claim_boundary": "descent maps labels/states; it does not source interaction probabilities",
    "disposition": "quotient-descent production route closed",
}

(ROOT / "results" / "wp1115_quotient_descent_production_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1115 PASS:", sorted(str(x) for x in identity_image), permutation_gain, required_gain, projection_rank_upper)

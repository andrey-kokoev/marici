from fractions import Fraction


controls = []
for degree in (2, 3, 4):
    norm_scale = Fraction(1, degree)
    selector_scale = Fraction(1, 1)
    assert norm_scale != selector_scale
    controls.append({
        "degree": degree,
        "scale_for_norm_identity": str(norm_scale),
        "scale_for_selector_identity": str(selector_scale),
        "simultaneous_scale_exists": False,
    })

# C4 -> C2, q(g)=g mod 2.
delta_G = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
push_delta = [delta_G[0] + delta_G[2], delta_G[1] + delta_G[3]]
normalized_pull_push_delta = [push_delta[g % 2] / 2 for g in range(4)]

assert push_delta == [Fraction(1), Fraction(0)]
assert normalized_pull_push_delta == [Fraction(1, 2), Fraction(0), Fraction(1, 2), Fraction(0)]
assert normalized_pull_push_delta != delta_G

# The averaging operator is nevertheless idempotent.
second = []
for g in range(4):
    fiber_sum = sum(normalized_pull_push_delta[h] for h in range(4) if h % 2 == g % 2)
    second.append(fiber_sum / 2)
assert second == normalized_pull_push_delta

print({
    "scalar_controls": controls,
    "C4_to_C2_normalized_selector": [str(x) for x in normalized_pull_push_delta],
    "averaging_projector_idempotent": True,
    "checks": "pass",
})

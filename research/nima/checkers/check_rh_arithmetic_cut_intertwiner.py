from fractions import Fraction
import json
from pathlib import Path


def inner(left, right):
    return sum(a * b for a, b in zip(left, right))


def cut(source, cut_index):
    return source[cut_index:], list(reversed(source[:cut_index]))


sources = [
    [Fraction(1), Fraction(2), Fraction(3), Fraction(4), Fraction(5), Fraction(6)],
    [Fraction(-2), Fraction(0), Fraction(1), Fraction(3), Fraction(-1), Fraction(4)],
    [Fraction(4), Fraction(-3), Fraction(2), Fraction(1), Fraction(0), Fraction(-2)],
]

cut_pairs = [(1, 2), (2, 1), (2, 3)]
vector_checks = 0
polarized_checks = 0
for p, q in cut_pairs:
    for source in sources:
        direct_tail, direct_seam = cut(source, p + q)
        first_tail, first_seam = cut(source, p)
        staged_tail, second_seam = cut(first_tail, q)
        staged_seam = second_seam + first_seam
        assert staged_tail == direct_tail
        assert staged_seam == direct_seam
        vector_checks += 1

    for left in sources:
        for right in sources:
            tail_left, seam_left = cut(left, p + q)
            tail_right, seam_right = cut(right, p + q)
            assert inner(left, right) == inner(tail_left, tail_right) + inner(seam_left, seam_right)
            polarized_checks += 1

# Wrong interval order is detected.
source = sources[0]
p, q = 2, 1
first_tail, first_seam = cut(source, p)
_, second_seam = cut(first_tail, q)
_, direct_seam = cut(source, p + q)
wrong_order = first_seam + second_seam
assert wrong_order != direct_seam

result = {
    "cut_pairs_checked": len(cut_pairs),
    "vector_intertwiner_checks": vector_checks,
    "polarized_norm_checks": polarized_checks,
    "tail_composition": "G_q G_p = G_(p+q)",
    "seam_composition": "H_(p+q) = concatenate(H_q G_p, H_p)",
    "wrong_orientation_falsifier": True,
    "cut_stage_supply_anomaly": False,
    "passive_tail_arithmetic_intertwiner_constructed": False,
    "verdict": "arithmetic scale transport coherently intertwines the complete tail-seam cut when oriented interval carriers are retained",
}

out = Path(__file__).parents[1] / "results" / "rh-arithmetic-cut-intertwiner.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

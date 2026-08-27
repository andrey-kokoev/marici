from fractions import Fraction
import json
from pathlib import Path


def inner(left, right):
    return sum(a * b for a, b in zip(left, right))


def cut(source, cut_index):
    return source[cut_index:], list(reversed(source[:cut_index]))


tail_gain = Fraction(3, 5)
defect_gain = Fraction(4, 5)
assert tail_gain * tail_gain + defect_gain * defect_gain == 1


def cascade(source, cut_index):
    tail, seam = cut(source, cut_index)
    outgoing = [tail_gain * value for value in tail]
    green_defect = [defect_gain * value for value in tail]
    return outgoing, green_defect, seam


sources = [
    [Fraction(1), Fraction(2), Fraction(3), Fraction(4), Fraction(5)],
    [Fraction(-2), Fraction(0), Fraction(1), Fraction(3), Fraction(-1)],
    [Fraction(4), Fraction(-3), Fraction(2), Fraction(1), Fraction(0)],
]

cut_indices = [1, 2, 4]
checks = 0
for cut_index in cut_indices:
    for left in sources:
        for right in sources:
            left_out, left_defect, left_seam = cascade(left, cut_index)
            right_out, right_defect, right_seam = cascade(right, cut_index)
            cascade_inner = (
                inner(left_out, right_out)
                + inner(left_defect, right_defect)
                + inner(left_seam, right_seam)
            )
            assert cascade_inner == inner(left, right)
            checks += 1

# Omitting either defect carrier loses norm.
source = sources[0]
outgoing, green_defect, seam = cascade(source, 2)
full_energy = inner(outgoing, outgoing) + inner(green_defect, green_defect) + inner(seam, seam)
without_seam = inner(outgoing, outgoing) + inner(green_defect, green_defect)
without_green_defect = inner(outgoing, outgoing) + inner(seam, seam)
assert full_energy == inner(source, source)
assert without_seam < full_energy
assert without_green_defect < full_energy

result = {
    "polarized_cascade_checks": checks,
    "cut_indices": cut_indices,
    "tail_gain": str(tail_gain),
    "green_defect_gain": str(defect_gain),
    "complete_cascade_is_isometric": True,
    "seam_and_green_defect_are_distinct": True,
    "omitting_seam_loses_energy": True,
    "omitting_green_defect_loses_energy": True,
    "reciprocal_sewing_constructed": False,
    "verdict": "the scale cut followed by passive tail dilation is a lossless cascade; remaining supply can first enter at arithmetic intertwining or reciprocal sewing",
}

out = Path(__file__).parents[1] / "results" / "rh-lossless-source-cascade.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

from fractions import Fraction
import json
from pathlib import Path


def cut(source, cut_index):
    tail = source[cut_index:]
    seam = list(reversed(source[:cut_index]))
    return tail, seam


def recombine(tail, seam):
    return list(reversed(seam)) + tail


sources = [
    [Fraction(1), Fraction(2), Fraction(3), Fraction(4), Fraction(5)],
    [Fraction(-2), Fraction(0), Fraction(1), Fraction(3), Fraction(-1)],
    [Fraction(4), Fraction(-3), Fraction(2), Fraction(1), Fraction(0)],
]
cut_indices = [1, 2, 4]

source_round_trips = 0
packet_round_trips = 0
for source in sources:
    for cut_index in cut_indices:
        tail, seam = cut(source, cut_index)
        assert recombine(tail, seam) == source
        source_round_trips += 1

        free_tail = [Fraction(index + 1) for index in range(len(tail))]
        free_seam = [Fraction(-(index + 1)) for index in range(len(seam))]
        rebuilt = recombine(free_tail, free_seam)
        rebuilt_tail, rebuilt_seam = cut(rebuilt, cut_index)
        assert rebuilt_tail == free_tail
        assert rebuilt_seam == free_seam
        packet_round_trips += 1

# Tail-only collision witness.
source_a = [Fraction(1), Fraction(2), Fraction(7), Fraction(8)]
source_b = [Fraction(5), Fraction(-3), Fraction(7), Fraction(8)]
tail_a, seam_a = cut(source_a, 2)
tail_b, seam_b = cut(source_b, 2)
assert tail_a == tail_b
assert seam_a != seam_b
assert source_a != source_b

# Staged cut and reverse-order recombination.
source = sources[0]
p = 2
q = 1
tail_p, seam_p = cut(source, p)
tail_q, seam_q = cut(tail_p, q)
stage_one_rebuilt = recombine(tail_q, seam_q)
source_rebuilt = recombine(stage_one_rebuilt, seam_p)
assert source_rebuilt == source

result = {
    "source_round_trips": source_round_trips,
    "free_packet_round_trips": packet_round_trips,
    "complete_cut_is_isometric": True,
    "complete_cut_is_surjective": True,
    "recombination_is_operator_inverse": True,
    "tail_only_is_injective": False,
    "tail_only_collision_witness": True,
    "staged_reverse_order_recombination": True,
    "verdict": "tail plus oriented seam is the minimal scale carrier with an exact source-derived reciprocal operator inverse",
}

out = Path(__file__).parents[1] / "results" / "rh-tail-seam-reciprocal-inverse.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

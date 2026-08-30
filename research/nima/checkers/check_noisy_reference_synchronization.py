from fractions import Fraction
import json
from pathlib import Path


# Z4 character exponents. Gauge action cancels in the signal-reference sum.
signal = 1
reference = 2
relative = (signal + reference) % 4
for gauge in range(4):
    transformed = ((signal + gauge) + (reference - gauge)) % 4
    assert transformed == relative
target_reversed = ((signal + 2) + reference) % 4
assert target_reversed == (relative + 2) % 4

# Formal orbit sum of the four roots of unity has zero coefficient in real and
# imaginary basis without using floating-point complex arithmetic.
root_vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))
orbit_sum = tuple(sum(vector[index] for vector in root_vectors) for index in range(2))
assert orbit_sum == (0, 0)


def attenuation(error_probability):
    return 1 - 2 * error_probability


assert attenuation(Fraction(0)) == 1
assert attenuation(Fraction(1, 4)) == Fraction(1, 2)
assert attenuation(Fraction(1, 2)) == 0

# Binary reference graph.
frames = (1, -1, 1)
edges = (
    frames[0] * frames[1],
    frames[1] * frames[2],
    frames[2] * frames[0],
)
cycle_product = edges[0] * edges[1] * edges[2]
assert cycle_product == 1

global_flipped_frames = tuple(-frame for frame in frames)
global_flipped_edges = (
    global_flipped_frames[0] * global_flipped_frames[1],
    global_flipped_frames[1] * global_flipped_frames[2],
    global_flipped_frames[2] * global_flipped_frames[0],
)
assert global_flipped_edges == edges
assert global_flipped_frames != frames

# An anchor at vertex zero selects one of the two global-sign representatives.
anchored_candidates = [candidate for candidate in (frames, global_flipped_frames) if candidate[0] == 1]
assert anchored_candidates == [frames]

corrupted_edges = (-edges[0], edges[1], edges[2])
assert corrupted_edges[0] * corrupted_edges[1] * corrupted_edges[2] == -1

# Any one of the three edge flips repairs the syndrome; the cycle check detects
# one fault but does not locate it.
repairs = []
for index in range(3):
    candidate = list(corrupted_edges)
    candidate[index] *= -1
    if candidate[0] * candidate[1] * candidate[2] == 1:
        repairs.append(index)
assert repairs == [0, 1, 2]

# Naturality under a two-coordinate presentation swap.
swap = lambda vector: (vector[1], vector[0])
assert swap((1, 1)) == (1, 1)
assert swap((1, 0)) == (0, 1)

result = {
    "schema": "marici.noisy-reference-synchronization.v1",
    "z4_relative_character_invariant": True,
    "target_reversal_detected": True,
    "unpaired_z4_orbit_sum": list(orbit_sum),
    "random_binary_tag_attenuation": "0",
    "triangle_cycle_product": cycle_product,
    "global_sign_ambiguity_count": 2,
    "anchored_frame_count": len(anchored_candidates),
    "single_edge_fault_detected": True,
    "single_edge_fault_uniquely_located": False,
    "natural_selector_fixture": [1, 1],
    "nonnatural_selector_fixture": [1, 0],
    "claim_boundary": "relative reference networks require noise, naturality, cycle, and lineage gates",
    "status": "pass",
}

output = Path(__file__).resolve().parents[1] / "results" / "noisy-reference-synchronization.json"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

from fractions import Fraction
import json
from pathlib import Path


# Exact finite phase-space fixture. Fourier is represented by a cyclic
# permutation. The derivative weight is the pullback of position weight
# through that permutation, the finite analogue of D = F^{-1} Q F.
positions = (-3, -2, -1, 1, 2, 3)
dimension = len(positions)
radius = 2

output_of_input = tuple((j - 2) % dimension for j in range(dimension))
fourier = [[int(i == output_of_input[j]) for j in range(dimension)] for i in range(dimension)]
q_weights = [abs(x) for x in positions]
d_weights = [q_weights[output_of_input[j]] for j in range(dimension)]
visible = [int(abs(x) < radius) for x in positions]


def apply(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(dimension)) for i in range(dimension)]


def norm2(vector):
    return sum(Fraction(x * x) for x in vector)


def weighted_norm2(vector, weights):
    return sum(Fraction((weights[i] * vector[i]) ** 2) for i in range(dimension))


vectors = []
for mask in range(1, 1 << dimension):
    vectors.append([1 if mask & (1 << i) else 0 for i in range(dimension)])

incoming_checked = 0
outgoing_checked = 0
for vector in vectors:
    outside = [vector[i] if not visible[i] else 0 for i in range(dimension)]
    if any(outside):
        transformed = apply(fourier, outside)
        observed = [transformed[i] if visible[i] else 0 for i in range(dimension)]
        assert norm2(observed) <= Fraction(1, radius * radius) * weighted_norm2(outside, q_weights)
        incoming_checked += 1

    inside = [vector[i] if visible[i] else 0 for i in range(dimension)]
    if any(inside):
        transformed = apply(fourier, inside)
        omitted = [transformed[i] if not visible[i] else 0 for i in range(dimension)]
        assert norm2(omitted) <= Fraction(1, radius * radius) * weighted_norm2(inside, d_weights)
        outgoing_checked += 1

# Bare norm cannot supply the R^{-2} bound for a unit vector at weight R.
hostile = [0, 0, 0, 0, 1, 0]
assert norm2(hostile) > Fraction(1, radius * radius) * norm2(hostile)

result = {
    "schema": "marici.nima.mellin-derham-leakage-domination.v1",
    "radius": radius,
    "incoming_vectors_checked": incoming_checked,
    "outgoing_vectors_checked": outgoing_checked,
    "incoming_control": "Mellin position Q",
    "outgoing_control": "de Rham derivative D",
    "decay_rate": "1/R",
    "bare_norm_hostile": True,
    "verdict": "source phase-space graph control repairs both directed leakage blocks",
}

out = Path(__file__).parents[1] / "results" / "mellin-derham-leakage-domination.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

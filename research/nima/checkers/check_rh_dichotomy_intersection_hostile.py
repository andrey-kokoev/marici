import json
from fractions import Fraction
from pathlib import Path


a = Fraction(1, 4)


def p(z):
    return (z - a) * (z - (1 - a))


def conjugated_generator(z):
    return ((-1, 0), (-2 * p(z), 1))


def stable_vector(z):
    return (1, p(z))


def matvec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


samples = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1), Fraction(2)]
rows = []
for z in samples:
    matrix = conjugated_generator(z)
    vector = stable_vector(z)
    assert matvec(matrix, vector) == tuple(-entry for entry in vector)
    assert p(1 - z) == p(z)
    evans = p(z)
    rows.append({
        "z": str(z),
        "stable_vector": [str(entry) for entry in vector],
        "stable_eigenvalue": -1,
        "unstable_eigenvalue": 1,
        "evans_determinant": str(evans),
    })

assert p(a) == 0
assert p(1 - a) == 0

result = {
    "off_seam_parameter": str(a),
    "reciprocal_parameter": str(1 - a),
    "conjugating_frame_determinant": 1,
    "stable_eigenvalue_all_parameters": -1,
    "unstable_eigenvalue_all_parameters": 1,
    "reciprocal_symmetric_evans_divisor": True,
    "samples": rows,
    "verdict": "perfect sector dichotomies permit reciprocal-symmetric stable-bundle intersections",
}

output = Path(__file__).parents[1] / "results" / "rh-dichotomy-intersection-hostile.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))


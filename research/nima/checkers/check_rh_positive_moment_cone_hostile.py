from fractions import Fraction as F
import json
from pathlib import Path


atoms = (F(0), F(1))
weights = (F(1), F(2))


def moment(k):
    return sum(weight * atom**k for atom, weight in zip(atoms, weights))


moments = [moment(k) for k in range(7)]
assert moments == [F(3), F(2), F(2), F(2), F(2), F(2), F(2)]

# Exact Hankel positivity follows from the atomic Gram representation.
test_polynomials = [
    (F(1),),
    (F(0), F(1)),
    (F(1), F(-1)),
    (F(1), F(2), F(-1)),
]
energies = []
for coeffs in test_polynomials:
    energy = sum(
        weight * sum(coeffs[k] * atom**k for k in range(len(coeffs))) ** 2
        for atom, weight in zip(atoms, weights)
    )
    assert energy >= 0
    energies.append(str(energy))

# Let w=exp(z). The endpoint transform is 1+2w.
w = -F(1, 2)
endpoint = F(1) + F(2) * w
assert endpoint == 0

result = {
    "schema": "marici.rh-positive-moment-cone-hostile.v1",
    "positive_measure": "delta_0+2 delta_1",
    "moments_0_through_6": [str(x) for x in moments],
    "sample_hankel_energies": energies,
    "translation_preserves_positive_measure_cone": True,
    "endpoint_transform": "1+2 exp(z)",
    "zero_condition": "exp(z)=-1/2",
    "off_seam_zero": "z=-log(2)+(2k+1)pi i",
    "cone_zero_reflection_for_complex_endpoint": False,
    "conclusion": "positive_moment_cone_is_not_complex_orientation",
}

out = Path(__file__).parents[1] / "results" / "rh-positive-moment-cone-hostile.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

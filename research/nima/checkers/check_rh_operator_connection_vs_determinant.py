from fractions import Fraction
import json
from pathlib import Path


cutoffs = list(range(1, 13))
determinants = []
smallest_gramian = []
identity_smallest_gramian = []
traceless_generators = []

for n in cutoffs:
    diagonal = [Fraction(n), Fraction(1, n), Fraction(1)]
    determinant = diagonal[0] * diagonal[1] * diagonal[2]
    gramian_diagonal = [x * x for x in diagonal]
    determinants.append(determinant)
    smallest_gramian.append(min(gramian_diagonal))
    identity_smallest_gramian.append(Fraction(1))
    # Logarithmic derivative of diag(exp(r), exp(-r), 1).
    traceless_generators.append([1, -1, 0])

assert all(value == 1 for value in determinants)
assert all(sum(generator) == 0 for generator in traceless_generators)
assert smallest_gramian == [Fraction(1, n * n) for n in cutoffs]
assert all(value == 1 for value in identity_smallest_gramian)
assert smallest_gramian[-1] < smallest_gramian[0]

result = {
    "cutoffs": cutoffs,
    "squeeze_determinants": [str(x) for x in determinants],
    "determinant_log_connection": "0",
    "operator_log_connection_diagonal": [1, -1, 0],
    "squeeze_smallest_gramian_values": [str(x) for x in smallest_gramian],
    "identity_smallest_gramian_values": [str(x) for x in identity_smallest_gramian],
    "same_scalar_transport_record": True,
    "same_observability_geometry": False,
    "verdict": "the Tate scalar can be the determinant shadow of transport but cannot replace the operator-valued relative connection",
}

out = Path(__file__).parents[1] / "results" / "rh-operator-connection-vs-determinant.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

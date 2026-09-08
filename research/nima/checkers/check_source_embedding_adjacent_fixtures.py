#!/usr/bin/env python3
"""Exact adjacent-size normalization check for declared four- and five-point fixtures."""
import json
from fractions import Fraction
from pathlib import Path

four_path = Path("research/nima/results/source_embedding_four_point_fixture.json")
five_path = Path("research/nima/results/source_embedding_reference_fixture.json")
four = json.loads(four_path.read_text(encoding="utf-8"))
five = json.loads(five_path.read_text(encoding="utf-8"))
assert (four["n"], five["n"]) == (4, 5)
assert four["dimension"] == 1 and five["dimension"] == 2

# On a0=x, a1=1-x, dlog(a0/a1)=(1/a0+1/a1)dx with unit coefficients.
g0 = Fraction(four["facets"][0]["gradient"][0])
g1 = Fraction(four["facets"][1]["gradient"][0])
assert (g0, g1) == (1, -1)
four_coefficients = [g0, -g1]
assert four_coefficients == [1, 1]

# Five-point unit coefficients are the five cyclic gradient determinants.
gradients = [tuple(Fraction(x) for x in facet["gradient"]) for facet in five["facets"]]
def det(u, v):
    return u[0]*v[1] - u[1]*v[0]
five_coefficients = [det(gradients[i], gradients[(i+1) % 5]) for i in range(5)]
assert five_coefficients == [1] * 5

# If these were source-authorized comparisons, c4=s^2=1 and c5=s^3=1 imply s=1.
# Their declared-example provenance prevents that promotion.
source_authorized = all(candidate["provenance"]["status"] == "source_derived" and candidate["provenance"]["source_locator"] for candidate in (four, five))
assert not source_authorized

result = {
    "schema": "marici.source-embedding-adjacent-fixtures.v1",
    "status": "passed",
    "strength": "exact four- and five-point presentation comparison; not a source normalization",
    "four_point_unit_coefficients": list(map(str, four_coefficients)),
    "five_point_unit_coefficients": list(map(str, five_coefficients)),
    "conditional_descent": "if both comparisons are source-authorized, s^2=s^3=1 forces s=1",
    "source_authorized": source_authorized,
    "promotion_ready": False,
    "residuals": ["four_point_source_locator", "five_point_source_locator", "zero_dimensional_orientation"],
    "boundary": "agreement of declared coordinate presentations at adjacent sizes does not create source provenance or orientation authority",
}
out = Path("research/nima/results/source_embedding_adjacent_fixtures.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

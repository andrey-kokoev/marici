import json
from fractions import Fraction
from pathlib import Path


a = Fraction(1, 4)
reciprocal = 1 - a
seam = Fraction(1, 2)


def bulk_polynomial(z):
    return (z - a) * (z - reciprocal)


def seam_polynomial(z):
    return z - seam


assert bulk_polynomial(a) == 0
assert bulk_polynomial(reciprocal) == 0
assert bulk_polynomial(seam) != 0
assert seam_polynomial(seam) == 0
assert seam_polynomial(a) != 0
assert seam_polynomial(reciprocal) != 0

# Integrated dimensions can coincide even when supported loci differ.
bulk_cohomology_dimension = 2
two_seam_states_dimension = 2
assert bulk_cohomology_dimension == two_seam_states_dimension

result = {
    "scalar_koszul_bulk_differential": "(z-1/4)(z-3/4)",
    "bulk_cohomology_support": [str(a), str(reciprocal)],
    "seam_differential": "z-1/2",
    "seam_cohomology_support": [str(seam)],
    "integrated_bulk_dimension": bulk_cohomology_dimension,
    "comparison_two_seam_states_dimension": two_seam_states_dimension,
    "global_dimension_distinguishes_support": False,
    "supported_cohomology_distinguishes_support": True,
    "scalar_koszul_explanatory": False,
    "required_repair": "source-derived family differential, determinant bridge, and off-seam contraction",
    "verdict": "support must emerge as cohomology of a source family, not be assigned from the scalar divisor",
}

output = Path(__file__).parents[1] / "results" / "rh-supported-koszul-model.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))


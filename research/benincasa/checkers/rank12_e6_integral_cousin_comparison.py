"""Integral versus quarter-enlarged six-occurrence Cousin lattices."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-e6-integral-cousin-comparison.json"

# A one-column integer matrix has sole nonzero Smith invariant equal to the
# gcd of its entries.  Its cokernel has free rank n-1 and torsion Z/gcd.
betti_boundary = [1] * 6
quarter_enlarged_boundary = [4] * 6
forgotten_boundary = [2] * 3

g_betti = math.gcd(*betti_boundary)
g_quarter = math.gcd(*quarter_enlarged_boundary)
g_forgotten = math.gcd(*forgotten_boundary)
assert (g_betti, g_quarter, g_forgotten) == (1, 4, 2)

packet = {
    "schema": "marici.benincasa.rank12_e6_integral_cousin_comparison.v1",
    "occurrence_resolved_betti_boundary": betti_boundary,
    "occurrence_resolved_betti_smith": [g_betti],
    "occurrence_resolved_betti_cokernel": "Z^5",
    "quarter_enlarged_e6_boundary": quarter_enlarged_boundary,
    "quarter_enlarged_e6_smith": [g_quarter],
    "quarter_enlarged_e6_cokernel": "Z^5 plus Z/4",
    "rational_quarter_vector_order": 4,
    "occurrence_forgotten_boundary": forgotten_boundary,
    "occurrence_forgotten_smith": [g_forgotten],
    "occurrence_forgotten_cokernel": "Z^2 plus Z/2",
    "physical_integral_hypercohomology_has_z4": False,
    "interpretation": "The Z/4 class lives in the quarter-enlarged source-normalized de Rham lattice. The occurrence-resolved integral Betti Cousin cokernel is torsion-free.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

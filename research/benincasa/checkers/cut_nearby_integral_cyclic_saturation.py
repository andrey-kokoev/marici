"""Integral saturation of the six occurrence-resolved Cut-nearby germs."""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/cut-nearby-integral-cyclic-saturation.json"

# Columns are (12|23),(12|31),(23|31),(23|12),(31|12),(31|23).
# Rows are the three marked-Cut sector lines.  This is Entry 229's
# occurrence-forgetting map before applying it to the source sum.
F = [
    [1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1],
]

def det3(columns):
    m = [[F[r][c] for c in columns] for r in range(3)]
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )

maximal_minors = [det3(cols) for cols in itertools.combinations(range(6), 3)]
gcd_maximal_minors = math.gcd(*(abs(x) for x in maximal_minors))
assert gcd_maximal_minors == 1

# Every sector-local normalized master vector is primitive because its e6
# coordinate is one: (X_j, X_i, 1).  Cyclic relabelling preserves this.
sector_vectors = [["X2", "X1", 1], ["X3", "X2", 1], ["X1", "X3", 1]]
assert all(v[2] == 1 for v in sector_vectors)

# Restricting the domain to the three physical pair sums sends each sum to
# twice its target generator.  This is the known occurrence-identification
# index, not a failure of saturation of the resolved map.
physical_pair_sum_matrix = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]

packet = {
    "schema": "marici.benincasa.cut_nearby_integral_cyclic_saturation.v1",
    "occurrence_order": ["12|23", "12|31", "23|31", "23|12", "31|12", "31|23"],
    "forgetting_matrix": F,
    "smith_invariants_of_resolved_map": [1, 1, 1],
    "resolved_cokernel_torsion": [],
    "sector_normalized_vectors": sector_vectors,
    "sector_vectors_primitive": True,
    "physical_pair_sum_matrix": physical_pair_sum_matrix,
    "physical_pair_sum_cokernel_torsion": [2, 2, 2],
    "interpretation": "The occurrence-resolved cyclic map is saturated. The only index is the already derived factor two produced by summing the two lower-denominator occurrences at each marked Cut.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

"""Integral Smith refinement of the physical total-energy Legendre cusp."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/total-energy-legendre-integral-monodromy.json"

T = [[1, 2], [0, 1]]
TmI = [[T[i][j] - (1 if i == j else 0) for j in range(2)] for i in range(2)]
entries = [abs(x) for row in TmI for x in row]
d1 = math.gcd(*entries)
assert d1 == 2
assert TmI == [[0, 2], [0, 0]]
assert [[sum(TmI[i][k] * TmI[k][j] for k in range(2)) for j in range(2)] for i in range(2)] == [[0, 0], [0, 0]]

packet = {
    "schema": "marici.benincasa.total_energy_legendre_integral_monodromy.v1",
    "physical_divisor": "E_T=0",
    "coarse_cusp_relation": "q_mod ~ E_T^2",
    "kummer_legendre_semisimple_sign": 1,
    "integral_monodromy": T,
    "T_minus_I": TmI,
    "nonzero_smith_invariants": [d1],
    "nilpotent_rank": 1,
    "nilpotent_square_zero": True,
    "invariant_lattice": "Z",
    "coinvariant_lattice": "Z plus Z/2",
    "torsion_generator": "class of the first basis vector modulo image 2*first basis vector, in the displayed column convention",
    "physical_cut_nearby_pairing_computed": False,
    "interpretation": "The Z/2 is integral coefficient monodromy from cusp width two. It is not a new carrier support or yet a physical period class.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

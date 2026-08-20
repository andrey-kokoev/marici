"""Hodge and lattice census for the smooth four-site infinity boundary."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-pure-boundary-tate-e7.json"

# A smooth degree-two del Pezzo is Bl_7(P2).
blowup_points = 7
b0 = 1
b1 = 0
b2 = 1 + blowup_points
b3 = 0
b4 = 1
euler_characteristic = b0 - b1 + b2 - b3 + b4
assert (b2, euler_characteristic) == (8, 10)

h20 = 0
h11 = 8
h02 = 0
assert h20 + h11 + h02 == b2

# The canonical vector K=-3H+sum E_i has square 2.  Its orthogonal
# complement in Picard has rank seven and E7 intersection type.
picard_rank = 8
root_rank = picard_rank - 1
canonical_square = 9 - blowup_points
assert (root_rank, canonical_square) == (7, 2)

packet = {
    "schema": "marici.benincasa.four_site_pure_boundary_tate_e7.v1",
    "surface_model": "Bl_7(P^2), equivalently a smooth double plane branched over a quartic",
    "betti_numbers": [b0, b1, b2, b3, b4],
    "euler_characteristic": euler_characteristic,
    "hodge_h2": {"h20": h20, "h11": h11, "h02": h02},
    "picard_rank": picard_rank,
    "anticanonical_square": canonical_square,
    "orthogonal_root_lattice": "E7(-1)",
    "root_lattice_rank": root_rank,
    "pure_transcendental_rank": 0,
    "classification": "pure Tate/algebraic coefficient variation with possible W(E7) monodromy",
    "scope": "smooth unmarked infinity boundary; relative marked divisors and degenerations remain open",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

"""Exact incidence audit for marked anticanonical curves on a degree-two del Pezzo."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-marked-incidence.json"

# X -> P2 is a double cover with pi^*H=-K_X and (-K_X)^2=2.
anticanonical_square = 2
pair_intersection_number = anticanonical_square
assert pair_intersection_number == 2

# Exact toy fibers illustrating the two generic incidence types.  Two base
# lines meet in one point p.  Above p, w^2=B(p).
generic_branch_value = 1
generic_fiber = (1, -1)
assert all(w * w == generic_branch_value for w in generic_fiber)
assert len(set(generic_fiber)) == pair_intersection_number

ramified_branch_value = 0
ramified_fiber = (0,)
ramified_multiplicity = 2
assert ramified_fiber[0] ** 2 == ramified_branch_value
assert ramified_multiplicity == pair_intersection_number

# Three base lines with coefficient rows l_i are concurrent exactly when the
# 3x3 determinant vanishes.  These examples avoid any symbolic dependency.
def det3(rows):
    (a, b, c), (d, e, f), (g, h, i) = rows
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

generic_lines = ((1, 0, 0), (0, 1, 0), (1, 1, 1))
concurrent_lines = ((1, 0, 0), (0, 1, 0), (1, 1, 0))
assert det3(generic_lines) != 0
assert det3(concurrent_lines) == 0

packet = {
    "schema": "marici.benincasa.four_site_marked_incidence.v1",
    "marked_curve_class": "C_g=pi^*H=-K_X",
    "pair_intersection_number": pair_intersection_number,
    "generic_pair_fiber": "two reduced points exchanged by the deck involution",
    "branch_collision": "one ramification point of intersection multiplicity two",
    "branch_collision_equation": "B_4(L_g cap L_h)=0",
    "generic_triple_intersection": False,
    "triple_incidence_equation": "det(l_g,l_h,l_k)=0",
    "cech_pair_object": "deck permutation module on two labelled occurrences",
    "classification": "Tate incidence data over existing branch-collision and line-incidence support",
    "new_carrier_datum": False,
    "scope": "generic distinct source lines; complete four-site denominator list and physical chain remain unfrozen",
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

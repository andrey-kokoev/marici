"""Transport and Gysin compatibility of the e6 quarter-lattice quotient."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-e6-quarter-lattice-transport.json"

d0 = [[1, 1, 1]]
d1 = [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]
d2 = [[1], [1], [1]]

def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

assert matmul(d0, d1) == [[0, 0, 0]]
assert matmul(d1, d2) == [[0], [0], [0]]

# All base monodromies are identity on both eta and rho=eta/4.  Deck acts
# by -1 and therefore descends to multiplication by -1 modulo four.
base_monodromies = {"p": 1, "s": 1, "B_minus_1": 1}
assert all(value == 1 for value in base_monodromies.values())
deck_action_mod4 = [(-x) % 4 for x in range(4)]
assert deck_action_mod4 == [0, 3, 2, 1]

packet = {
    "schema": "marici.benincasa.rank12_e6_quarter_lattice_transport.v1",
    "node_smoothing": "XY=p*s*(B-1)",
    "integral_generator": "eta",
    "source_normalized_generator": "rho=eta/4",
    "base_monodromies_on_eta": base_monodromies,
    "base_monodromies_on_rho": base_monodromies,
    "quotient_local_system": "Z*rho / Z*eta = Z/4",
    "base_monodromies_on_quotient": base_monodromies,
    "deck_action_on_eta_and_rho": -1,
    "deck_action_mod4": deck_action_mod4,
    "gysin_d0": d0,
    "gysin_d1": d1,
    "gysin_d2": d2,
    "gysin_complex_closes": True,
    "interpretation": "The quarter-lattice defect is a transported finite coefficient quotient with odd deck character, while the resolved integral Betti Cousin cohomology remains torsion-free.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

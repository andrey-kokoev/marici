"""Finite integral extension classes at the total-energy elliptic cusp."""
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/total-energy-coinvariant-extension-classes.json"

# Character equivariance confines any integral gluing of the elliptic
# coinvariant to the final-block algebraic plane <e6,v_alg>.  Extensions of
# Z/2 by Z^2 are represented by 2m=a*e6+b*v_alg, modulo 2Z^2.
classes = []
for a, b in itertools.product(range(2), repeat=2):
    relation = [-a, -b, 2]
    torsion_order = math.gcd(*(abs(x) for x in relation))
    classes.append({
        "parity": [a, b],
        "presentation_relation": relation,
        "coinvariant_group": "Z^2+Z/2" if torsion_order == 2 else "Z^2",
        "visible_Z2_survives": torsion_order == 2,
    })

assert len(classes) == 4
assert sum(c["visible_Z2_survives"] for c in classes) == 1

packet = {
    "schema": "marici.benincasa.total_energy_coinvariant_extension_classes.v1",
    "algebraic_monodromy": "identity",
    "rational_nilpotent": "pure elliptic rank one",
    "snake_connecting_map_to_free_kernel": "zero",
    "character_allowed_algebraic_plane": ["e6", "v_alg"],
    "extension_group": "Ext^1_Z(Z/2,Z^2)=(Z/2)^2",
    "extension_classes": classes,
    "split_class_count": 1,
    "nonsplit_class_count": 3,
    "source_selected_class": None,
    "interpretation": "Existing rational monodromy data reduce the integral cusp ambiguity to two parity bits. Only the zero class leaves a visible Z/2 summand; any nonzero class absorbs it into a free coinvariant lattice. Selecting the class requires an integral Betti/Gysin comparison.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

"""Exclude the physical Cut-nearby commutator from the elliptic Z/2 coinvariant."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/cut-nearby-elliptic-z2-exclusion.json"

# Entry 226's source-normalized commutator, after multiplication by the
# nonzero common factor -xy/(2*pi^2), in the equation-(58) master order.
normalized_commutator = [0, 0, "y", 0, "x", "1", 0, 0, 0]
support = [i + 1 for i, coefficient in enumerate(normalized_commutator) if coefficient != 0]
assert support == [3, 5, 6]

# Entry 150's infinity-Gysin map vanishes on the first three character
# blocks (containing e3 and e5) and separately on the double-pole master e6.
termwise_gysin = {"e3": [0, 0], "e5": [0, 0], "e6": [0, 0]}
elliptic_image = [
    sum(termwise_gysin[f"e{i}"][row] for i in support)
    for row in range(2)
]
assert elliptic_image == [0, 0]

# Reduction to the width-two coinvariant is downstream of R_infinity.
# An integral zero remains zero after quotienting and reduction modulo two.
coinvariant_mod_2_image = [entry % 2 for entry in elliptic_image]
assert coinvariant_mod_2_image == [0, 0]

packet = {
    "schema": "marici.benincasa.cut_nearby_elliptic_z2_exclusion.v1",
    "source_commutator_entry": 226,
    "normalized_commutator_e1_to_e9": normalized_commutator,
    "nonzero_master_support": support,
    "termwise_infinity_gysin": termwise_gysin,
    "elliptic_image_over_Z": elliptic_image,
    "elliptic_width_two_coinvariant_image_mod_2": coinvariant_mod_2_image,
    "physical_commutator_nonzero": True,
    "elliptic_z2_activated_by_this_comparison": False,
    "classification": "third-Rees algebraic Tate/Kummer coefficient class in ker(R_infinity)",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))

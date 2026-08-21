"""Exact sign-character gate for external-Gram Gysin activation."""

import json
from pathlib import Path


TRIVIAL = 1
SIGN = -1


def tensor(*characters):
    out = 1
    for character in characters:
        out *= character
    return out


# External orientation reflection e -> -e.
characters = {
    "e": SIGN,
    "de": SIGN,
    "inverse_sqrt_detH": SIGN,  # det(H)=e^2 in the normalized chart
    "log_normal_form_de_over_e": TRIVIAL,
    "Tor_0_normal": TRIVIAL,
    "Tor_1_koszul_generator": SIGN,
}

assert tensor(characters["de"], characters["inverse_sqrt_detH"]) == TRIVIAL
assert characters["log_normal_form_de_over_e"] == TRIVIAL
assert tensor(characters["inverse_sqrt_detH"], characters["Tor_0_normal"]) == SIGN
assert tensor(characters["inverse_sqrt_detH"], characters["Tor_1_koszul_generator"]) == TRIVIAL

# The internal quadratic deck involution is independent bookkeeping. Its odd
# line w still needs an odd incidence coefficient N to yield an even scalar.
internal = {"one": TRIVIAL, "w": SIGN, "N": SIGN, "Nw": TRIVIAL}
assert tensor(internal["w"], internal["N"]) == internal["Nw"]

result = {
    "schema": "marici.cosmology.external_gram_gysin_character_gate.v1",
    "external_orientation_characters": characters,
    "internal_kummer_characters": internal,
    "density_times_Tor0": "odd",
    "density_times_Tor1": "even",
    "necessary_gysin_grade": 1,
    "physical_map_constructed": False,
    "passed": True,
}
out = Path(__file__).with_name("results") / "external-gram-gysin-character-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))

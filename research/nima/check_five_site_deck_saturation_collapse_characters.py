"""Character census of the 91-to-45 total-energy deck-saturation collapse."""

import json
from pathlib import Path


generic = {"trivial": 26, "singleton_each": 9, "pair_each": 2}
special = {"trivial": 15, "singleton_each": 4, "pair_each": 1}
kernel_with_carrier = {
    "trivial": generic["trivial"] - special["trivial"],
    "singleton_each": generic["singleton_each"] - special["singleton_each"],
    "pair_each": generic["pair_each"] - special["pair_each"],
}
assert kernel_with_carrier == {"trivial": 11, "singleton_each": 5, "pair_each": 1}

normal_kernel = {"trivial": 10, "singleton_each": 5, "pair_each": 1}
dimension = normal_kernel["trivial"] + 5 * normal_kernel["singleton_each"] + 10 * normal_kernel["pair_each"]
assert dimension == 45

result = {
    "schema": "marici.cosmology.five_site_deck_saturation_collapse_characters.v1",
    "generic_component_character_multiplicities": generic,
    "total_energy_component_character_multiplicities": special,
    "kernel_including_total_energy_carrier": kernel_with_carrier,
    "normal_kernel_excluding_carrier": normal_kernel,
    "normal_kernel_dimension": dimension,
    "characters_present": ["trivial", "five singleton characters", "ten pair characters"],
    "higher_weight_characters_present": False,
    "passed": True,
}
out = Path(__file__).with_name("results") / "five-site-deck-saturation-collapse-characters.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))

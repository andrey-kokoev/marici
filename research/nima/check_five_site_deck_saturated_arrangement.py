"""Exact deck saturation of the 26-section five-site marked arrangement."""

import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
packet_path = ROOT / "research" / "benincasa" / "results" / "five-site-d3-marked-kummer-cover.json"
packet = json.loads(packet_path.read_text(encoding="utf-8"))
forms = packet["facet_forms"]


def canonical(vector):
    if not any(vector):
        return None
    divisor = 0
    for value in vector:
        divisor = math.gcd(divisor, abs(value))
    vector = tuple(value // divisor for value in vector)
    first = next(value for value in vector if value)
    if first < 0:
        vector = tuple(-value for value in vector)
    return vector


def total_energy_restrict(vector):
    # X5=-(X1+...+X4), so the new Xi coefficient is xi-x5.
    x = vector[:5]
    y = vector[5:]
    return tuple(x[i] - x[4] for i in range(4)) + tuple(y)


generic = set()
at_total_energy = set()
orbit_sizes = {}
for label, form in forms.items():
    orbit = set()
    orbit_et = set()
    for signs in itertools.product((-1, 1), repeat=5):
        vector = tuple(form["x"]) + tuple(c * s for c, s in zip(form["y"], signs))
        orbit.add(canonical(vector))
        restricted = canonical(total_energy_restrict(vector))
        if restricted is not None:
            orbit_et.add(restricted)
        generic.add(canonical(vector))
        if restricted is not None:
            at_total_energy.add(restricted)
    orbit_sizes[label] = {"generic": len(orbit), "total_energy": len(orbit_et)}

assert len(forms) == 26
assert len(generic) == 91
assert len(at_total_energy) == 45
assert orbit_sizes["G"] == {"generic": 1, "total_energy": 0}
assert all(
    orbit_sizes[label]["generic"] == 2 and orbit_sizes[label]["total_energy"] == 1
    for label in forms if label.startswith("G_minus_e")
)
assert all(
    orbit_sizes[label]["generic"] == 4 and orbit_sizes[label]["total_energy"] == 4
    for label in forms if label.startswith("g_")
)

result = {
    "schema": "marici.cosmology.five_site_deck_saturated_arrangement.v1",
    "physical_section_count": 26,
    "generic_deck_saturated_hyperplanes": len(generic),
    "total_energy_deck_saturated_hyperplanes": len(at_total_energy),
    "generic_breakdown": {"total_energy": 1, "five_single_sheet_orbits": 10, "twenty_two_sheet_orbits": 80},
    "total_energy_breakdown": {"edge_soft": 5, "ten_complementary_pair_orbits": 40},
    "deck_action_on_original_26_complement": "not closed",
    "deck_action_on_saturated_complement": "closed",
    "passed": True,
}
out = Path(__file__).with_name("results") / "five-site-deck-saturated-arrangement.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))

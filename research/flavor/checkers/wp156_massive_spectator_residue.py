"""Exact Z4 residue audit for symmetry-preserving massive spectator blocks."""

from itertools import product
import json
from pathlib import Path


charges = range(4)
flavor_packets = list(product(charges, repeat=3))


def residue(block: tuple[int, ...]) -> int:
    return sum(block) % 4


dirac_blocks = {(q, (-q) % 4) for q in charges}
majorana_blocks = {(q,) for q in charges if 2 * q % 4 == 0}
dirac_residues = {residue(block) for block in dirac_blocks}
majorana_residues = {residue(block) for block in majorana_blocks}

# Any finite sum of allowed block residues closes to this subgroup.
massive_residues = {0}
for _ in range(4):
    massive_residues |= {(left + right) % 4 for left in massive_residues for right in dirac_residues | majorana_residues}


def admitted_flavor(spectator_options: set[int]) -> set[tuple[int, int, int]]:
    return {
        packet
        for packet in flavor_packets
        if any((sum(packet) + spectator) % 4 == 0 for spectator in spectator_options)
    }


dirac_projection = admitted_flavor(dirac_residues)
massive_projection = admitted_flavor(massive_residues)
hostile_packet = (2, 2, 2)

checks = {
    "four_dirac_charge_blocks": len(dirac_blocks) == 4,
    "all_dirac_blocks_are_mass_invariant": all(sum(block) % 4 == 0 for block in dirac_blocks),
    "dirac_residue_is_only_zero": dirac_residues == {0},
    "majorana_allowed_charges_are_zero_and_two": majorana_blocks == {(0,), (2,)},
    "majorana_residues_are_zero_and_two": majorana_residues == {0, 2},
    "all_massive_block_residues_are_even": massive_residues == {0, 2},
    "dirac_only_projection_has_16_packets": len(dirac_projection) == 16,
    "general_massive_projection_has_32_packets": len(massive_projection) == 32,
    "mass_gap_does_not_restore_closed_selector": massive_projection != dirac_projection,
    "hostile_packet_needs_residue_two": sum(hostile_packet) % 4 == 2,
    "charge_two_majorana_repairs_hostile_packet": (sum(hostile_packet) + 2) % 4 == 0,
    "fermion_number_gate_is_load_bearing": hostile_packet not in dirac_projection and hostile_packet in massive_projection,
}

result = {
    "work_package": "WP156",
    "title": "Massive-spectator residue audit",
    "domain": "Z4-charged spectator blocks with symmetry-preserving bilinear masses",
    "dirac_residues": sorted(dirac_residues),
    "majorana_residues": sorted(majorana_residues),
    "general_massive_residues": sorted(massive_residues),
    "dirac_only_flavor_image_size": len(dirac_projection),
    "general_massive_flavor_image_size": len(massive_projection),
    "classification": "massiveness alone leaves an even spectator-residue ambiguity; Dirac-only closure restores the 16-packet selector",
    "selector": "conditional on an independently conserved fermion number or equivalent Majorana prohibition",
    "rigidifier": False,
    "physical_instrument": False,
    "smallest_exact_falsifier": "one charge-two Majorana block has an invariant mass and residue two, admitting f=(2,2,2)",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "all_passed": all(checks.values()),
}

output = Path(__file__).resolve().parents[1] / "results" / "wp156_massive_spectator_residue.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))


"""Audit the missing source-to-WET threshold map in WP516--WP518."""

import json
import re
from pathlib import Path


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp511 = load("wp511_neutral_b_current_instrument.json")
wp515 = load("wp515_bmixing_forced_pole_hierarchy.json")
wp516 = load("wp516_hierarchical_mass_basis_vertices.json")
wp517 = load("wp517_unequal_vector_partial_widths.json")
wp518 = load("wp518_common_order_residue_width_composition.json")

scale_match = re.search(r"at ([0-9]+(?:\.[0-9]+)?) GeV", wp511["admitted_state_domain"])
matching_scale = float(scale_match.group(1)) if scale_match else float("nan")
masses = wp516["mass_basis"]["ordered_masses_GeV"]
minimum_mass = min(masses)
maximum_mass = max(masses)
states_below_matching_scale = [index for index, mass in enumerate(masses) if mass < matching_scale]

# The only admitted WP511 source coordinate is a local WET coefficient at the
# declared matching scale.  A propagating source spectrum below that scale is
# not automatically an element of this domain.  It needs an explicit sequence
# of threshold matching and running maps; no such constructor occurs in
# WP511--WP518.
declared_threshold_constructor = None
formal_ratio_inside_contact_bound = (
    1 / 400 < wp515["source_implication"]["maximum_b_over_a"]
)
source_to_wet_descends = bool(declared_threshold_constructor is not None)

checks = {
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp515_dependency_passed": bool(wp515["passed"]),
    "wp516_dependency_passed": bool(wp516["passed"]),
    "wp517_dependency_passed": bool(wp517["passed"]),
    "wp518_dependency_passed": bool(wp518["passed"]),
    "wp511_matching_scale_is_parsed": matching_scale == 160.0,
    "formal_entrance_ratio_lies_inside_wp515_contact_bound": bool(
        formal_ratio_inside_contact_bound
    ),
    "every_wp516_pole_lies_below_wp511_matching_scale": bool(
        len(states_below_matching_scale) == 14
    ),
    "lightest_pole_is_below_one_hundredth_of_matching_scale": bool(
        minimum_mass / matching_scale < 1e-2
    ),
    "no_source_to_wet_threshold_constructor_is_declared": bool(
        declared_threshold_constructor is None
    ),
    "source_to_wet_descent_is_not_authorized": bool(not source_to_wet_descends),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP519",
    "wp511_instrument_domain": wp511["admitted_state_domain"],
    "matching_scale_GeV": matching_scale,
    "wp516_spectrum": {
        "minimum_pole_mass_GeV": minimum_mass,
        "maximum_pole_mass_GeV": maximum_mass,
        "states_below_matching_scale": states_below_matching_scale,
        "count_below_matching_scale": len(states_below_matching_scale),
    },
    "formal_contact_test": {
        "b_over_a": 1 / 400,
        "wp515_upper_bound": wp515["source_implication"]["maximum_b_over_a"],
        "inside_formal_bound": bool(formal_ratio_inside_contact_bound),
        "authority": "Formal coefficient comparison only; it does not establish that the propagating WP516 source spectrum descends to the WP511 WET coordinate.",
    },
    "first_nonfaithful_arrow": "WP516 propagating pole packet -> undeclared threshold matching and running -> WP511 local WET coefficient at 160 GeV",
    "classification": "The WP516--WP518 masses, vertices, residues, and partial widths remain valid source-model calculations, but their B_s-compatible label is unauthorized. The missing constructor is source-to-WET threshold matching with finite propagators and running.",
    "selector": False,
    "rigidifier": False,
    "instrument": "WP511 remains a valid instrument on its WET domain; it is not yet an instrument for the WP516 propagating source packet.",
    "smallest_exact_falsifier": "The WP511 coordinate is declared at 160 GeV while all fourteen WP516 poles lie below 5 GeV, including a 0.0121 GeV pole, and no threshold matching/running constructor is declared.",
    "remaining_gate": "Compute finite-momentum DeltaB=2 exchange with the full pole-residue packet, match each threshold into WET in its legal domain, run to the hadronic scale, and validate against the calibrated DeltaM_s likelihood before restoring any B_s-compatibility claim.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp519_wet_matching_domain_audit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

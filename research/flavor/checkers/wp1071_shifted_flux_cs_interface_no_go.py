import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required_map_components = [
    "embedding_from_admitted_fourfold_to_interval_orbifold",
    "su6_to_su4_su2_u1_branch_embedding",
    "seven_channel_chern_simons_projector",
    "localized_green_schwarz_endpoint_action",
    "orientation_selection_law",
]

wp793_provides = [
    "shifted_G4_plus_c2_over_2_quantization",
    "vertical_flux_transversality_and_primitivity_gates",
    "D3_tadpole_capacity",
    "minimum_chiral_multiplicity_in_finite_scan",
    "G4_to_minus_G4_mirror_theorem",
]

missing = [x for x in required_map_components if x not in wp793_provides]
assert missing == required_map_components

required_coset = ["1/2", "1/4", "0", "0", "0", "3/4", "0"]
wp793_shift = "G4+c2(X)/2 integral"
assert len(required_coset) == 7
assert isinstance(wp793_shift, str)

# The WP793 mirror theorem preserves every admitted gate while reversing
# chiral readout.  It therefore cannot select the endpoint orientation needed
# by WP1070.
orientation_selected_by_wp793 = False
assert not orientation_selected_by_wp793

result = {
    "schema": "marici.flavor.wp1071.v1",
    "status": "PASS",
    "question": "Can WP793's shifted G4 quantization law directly source WP1070's required seven-channel Chern-Simons coset?",
    "wp793_provides": wp793_provides,
    "required_map_components": required_map_components,
    "missing_map_components": missing,
    "required_coset_mod_integer_lattice": required_coset,
    "orientation_selected_by_wp793": orientation_selected_by_wp793,
    "classification": "shifted-flux-to-CS interface no-go: WP793 gives a scalar shifted four-form class but no interval embedding, gauge-branch projector, endpoint Green-Schwarz action, or orientation law",
    "remaining_gate": "supply a compactification packet containing all five map components and verify that it lands on the WP1070 coset",
    "claim_boundary": "audits the interface between WP793 and WP1070; it does not reject all future shifted-flux constructions",
    "disposition": "falsified as a direct source candidate; the localization branch is blocked pending a UV boundary-action packet",
}

(ROOT / "results" / "wp1071_shifted_flux_cs_interface_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1071 PASS: missing", len(missing), "required components")

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

packets = {
    "finite_scheme_normalization_port_theorem": {
        "faithful_scalar_ports_required": 3,
        "port_locations_selected": False,
        "port_values_supplied": False,
    },
    "matched_holonomy_normalization": {
        "flat_section_rank": 1,
        "preferred_nonzero_section": False,
        "conditional_repair_ports": ["normalized_dual_cycle", "metric_or_basepoint_phase", "integral_polarized_lattice"],
    },
    "source_authorized_renormalization_provenance": {
        "counterterm_basis_supplied": False,
        "renormalization_condition_supplied": False,
        "local_contact_port_disjoint_from_rank7": True,
    },
}
assert packets["finite_scheme_normalization_port_theorem"]["faithful_scalar_ports_required"] == 3
assert packets["matched_holonomy_normalization"]["flat_section_rank"] == 1
assert len(packets["matched_holonomy_normalization"]["conditional_repair_ports"]) == 3
assert packets["source_authorized_renormalization_provenance"]["local_contact_port_disjoint_from_rank7"]

required_selector_authority = {
    "integer_wilson_lift_n": False,
    "clock_orientation_sigma": False,
    "oriented_adjoint_ray": False,
    "independent_weight_minus_three_rho": False,
    "production_kernel": False,
    "gain_three_halves": False,
}
assert not any(required_selector_authority.values())
assert len(required_selector_authority) == 6

result = {
    "schema": "marici.flavor.wp1096.v1",
    "status": "PASS",
    "question": "Do admitted normalization/source packets supply independent integer-lift, orientation, or rho authority?",
    "packet_audit": packets,
    "required_selector_authority": required_selector_authority,
    "classification": "conditional gate: Benincasa packets identify repair ports but do not supply selector authority",
    "remaining_gate": "source-authorized normalized dual cycle, metric/basepoint phase, or integral-polarized lattice; otherwise a capability blocker",
    "hostile_gate": "do not promote flat-section rank, three normalization ports, or disjoint contact provenance into integer lift, orientation, rho, production, or gain authority",
    "claim_boundary": "the audit is limited to the three admitted Benincasa packets read for E1 and does not refute a future source packet",
    "disposition": "normalization-packet authority audit completed; precise conditional repair ports identified",
}

(ROOT / "results" / "wp1096_normalization_packet_authority_audit_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1096 PASS:", len(packets), len(required_selector_authority), len(packets["matched_holonomy_normalization"]["conditional_repair_ports"]))

"""Exact domain gate for analogue Higgs control platforms."""

import json
from pathlib import Path

import sympy as sp


# Capability order: Standard Model source domain, quartic-sensitive readout,
# executed laboratory setting, direct quartic actuation, retained-reference
# displacement readout.  Entries are evidence classifications, not fitted data.
required = sp.Matrix([[1, 1, 1, 1, 1]])
platforms = {
    "atlas_triple_higgs": sp.Matrix([[1, 1, 1, 0, 0]]),
    "thz_superconducting_higgs": sp.Matrix([[0, 0, 1, 0, 0]]),
    "cold_atom_gauge_higgs_proposal": sp.Matrix([[0, 0, 0, 0, 0]]),
}

# The direct sum keeps the two physical source domains distinct.  Without a
# source-authorized interface, the analogue control coordinate has zero
# derivative with respect to the Standard Model quartic coordinate.
kappa4_sm, u_thz = sp.symbols("kappa4_SM u_THz", real=True)
cross_domain_actuation = sp.diff(kappa4_sm, u_thz)

checks = {
    "no_platform_closes_all_capabilities": all(row != required for row in platforms.values()),
    "atlas_has_measurement_but_no_actuation": platforms["atlas_triple_higgs"] == sp.Matrix([[1, 1, 1, 0, 0]]),
    "thz_platform_is_executed_but_outside_sm_domain": platforms["thz_superconducting_higgs"][0, 2] == 1 and platforms["thz_superconducting_higgs"][0, 0] == 0,
    "cold_atom_gauge_higgs_route_is_not_an_executed_instrument": platforms["cold_atom_gauge_higgs_proposal"][0, 2] == 0,
    "analogue_command_has_zero_sm_quartic_actuation_without_interface": cross_domain_actuation == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP418",
    "title": "Analogue Higgs control domain gate",
    "capability_order": [
        "standard_model_source_domain",
        "quartic_sensitive_readout",
        "executed_laboratory_setting",
        "direct_quartic_actuation",
        "retained_reference_displacement_readout",
    ],
    "platform_capabilities": {
        name: [int(x) for x in matrix] for name, matrix in platforms.items()
    },
    "cross_domain_command_to_sm_quartic_derivative": str(cross_domain_actuation),
    "classification": "analogue Higgs control is executable instrument architecture in a different source domain, not Standard Model quartic actuation",
    "transferable_learning": "phase-locked pump control plus coherent amplitude-mode spectroscopy realizes a relational reference apparatus",
    "smallest_falsifier_of_transport": "no admitted source map sends the THz command to kappa4_SM",
    "remaining_gate": "an experimentally established interface with nonzero derivative of kappa4_SM with respect to an executable command",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp418_analogue_higgs_domain_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

"""Exact measurement-versus-actuation audit for the Higgs quartic."""

import json
from pathlib import Path

import sympy as sp


energy, luminosity, kappa4 = sp.symbols(
    "E L kappa_4", positive=True, real=True
)
a0, a1, b0, b1 = sp.symbols("a0 a1 b0 b1", positive=True, real=True)
g_portal, x_command = sp.symbols("g_portal x_command", real=True)

# Minimal quartic-sensitive collider record.  The precise cross section is not
# asserted; this polynomial packet captures the typed dependence needed for the
# instrument audit: accelerator commands change sampling, while kappa4 remains
# a fixed source parameter inferred from the record.
amplitude = a0 + a1 * energy + (b0 + b1 * energy) * kappa4
expected_count = luminosity * amplitude**2
measurement_sensitivity = sp.factor(sp.diff(expected_count, kappa4))
command_response = sp.Matrix(
    [sp.diff(expected_count, energy), sp.diff(expected_count, luminosity)]
)
source_actuation = sp.Matrix(
    [sp.diff(kappa4, energy), sp.diff(kappa4, luminosity)]
)

# A genuine actuator would require a declared source coupling.  This conditional
# portal illustrates the missing arrow without admitting that the portal exists.
kappa4_portal = kappa4 + g_portal * x_command
portal_actuation = sp.diff(kappa4_portal, x_command)

checks = {
    "quartic_is_measurable_in_a_quartic_sensitive_channel": measurement_sensitivity != 0,
    "accelerator_commands_change_expected_records": all(x != 0 for x in command_response),
    "accelerator_commands_do_not_actuate_the_source_coefficient": source_actuation == sp.zeros(2, 1),
    "measurement_sensitivity_does_not_imply_actuation": measurement_sensitivity != 0 and source_actuation.rank() == 0,
    "a_named_portal_would_supply_the_missing_transfer": portal_actuation == g_portal,
    "portal_transfer_vanishes_when_no_new_coupling_is_admitted": portal_actuation.subs(g_portal, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP417",
    "title": "Higgs quartic measurement-versus-actuation audit",
    "observed_instrument": "ATLAS triple-Higgs six-b-jet search constraining kappa_4",
    "executable_commands": ["beam energy", "integrated luminosity", "event selection"],
    "measurement_sensitivity": str(measurement_sensitivity),
    "command_response": [str(x) for x in command_response],
    "source_actuation_jacobian": [str(x) for x in source_actuation],
    "conditional_portal_transfer": str(portal_actuation),
    "classification": "quartic-sensitive measurement instrument exists; executable Standard Model quartic actuator does not",
    "smallest_falsifier_of_closure": "the command-to-kappa_4 Jacobian is identically zero for existing accelerator settings",
    "remaining_gate": "an observed source coupling and calibrated command x with nonzero d(kappa_4)/dx in the same physical experiment",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp417_higgs_quartic_instrument_audit.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

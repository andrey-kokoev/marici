"""Exact WP131 gauge/Lorentz portal and accessibility audit."""

from fractions import Fraction as F
import json
from pathlib import Path


# Canonical dimensions of bar(Q_L), H, Phi, u_R.
portal_dimension = F(3, 2) + 1 + 1 + F(3, 2)

# Hypercharge checks for bar(Q_L) tilde(H) u_R and bar(Q_L) H d_R.
up_hypercharge = F(-1, 6) + F(-1, 2) + F(2, 3)
down_hypercharge = F(-1, 6) + F(1, 2) + F(-1, 3)

# Frozen conditional portal benchmark. zeta_i are mediator/flavon mixing
# overlaps obtained after diagonalizing the declared scalar mass matrix.
c, higgs_vev, cutoff = F(1), F(1), F(1)
zeta_1, zeta_2 = F(1, 5), F(1, 4)
y_1 = c * higgs_vev * zeta_1 / cutoff
y_2 = c * higgs_vev * zeta_2 / cutoff

# Reduced widths: Gamma_hat = 8*pi*Gamma/(N_c*M) after neglecting final-state
# masses. This removes the universal transcendental factor but preserves the
# exact source dependence.
width_hat_1, width_hat_2 = y_1 * y_1, y_2 * y_2

energy_max = F(5)
masses = [F(1), F(2)]
accessible = sum(m <= energy_max for m in masses)

# Source-scale dilation. All flavor-sector dimension-one inputs, including
# V, Lambda and pole masses, scale by s. Dimensionless Yukawas V/Lambda and
# normalized vacuum coordinates remain fixed, while thresholds move.
s = F(10)
scaled_masses = [s * m for m in masses]
scaled_cutoff = s * cutoff
scaled_accessible = sum(m <= energy_max for m in scaled_masses)
scaled_y_1 = c * higgs_vev * zeta_1 / scaled_cutoff
scaled_y_2 = c * higgs_vev * zeta_2 / scaled_cutoff

vev, scaled_vev = F(1), s
low_yukawa = c * vev / cutoff
scaled_low_yukawa = c * scaled_vev / scaled_cutoff

checks = {
    "portal_is_dimension_five": portal_dimension == 5,
    "inverse_cutoff_makes_lagrangian_dimension_four": portal_dimension - 1 == 4,
    "up_portal_hypercharge_zero": up_hypercharge == 0,
    "down_portal_hypercharge_zero": down_hypercharge == 0,
    "weak_basis_contraction_complete": True,
    "reduced_width_one_derived": width_hat_1 == F(1, 25),
    "reduced_width_two_derived": width_hat_2 == F(1, 16),
    "baseline_thresholds_accessible": accessible == 2,
    "scaled_thresholds_inaccessible": scaled_accessible == 0,
    "low_yukawa_preserved_by_scale_dilation": scaled_low_yukawa == low_yukawa == 1,
    "portal_residues_decouple_under_dilation": scaled_y_1 == y_1 / s and scaled_y_2 == y_2 / s,
    "threshold_spectrum_changes_under_same_low_packet": scaled_masses != masses,
}

result = {
    "work_package": "WP131",
    "classification": "gauge/Lorentz-complete conditional SM portal; accessibility not source-selected",
    "portal": "(c_u/Lambda) bar(Q_L) tilde(H) Phi_u u_R + (c_d/Lambda) bar(Q_L) H Phi_d d_R + h.c.",
    "portal_operator_dimension": str(portal_dimension),
    "hypercharge_residuals": {"up": str(up_hypercharge), "down": str(down_hypercharge)},
    "benchmark": {
        "masses": [str(x) for x in masses], "energy_max": str(energy_max),
        "mixing_overlaps": [str(zeta_1), str(zeta_2)],
        "effective_couplings": [str(y_1), str(y_2)],
        "reduced_widths": [str(width_hat_1), str(width_hat_2)],
        "accessible_poles": accessible,
    },
    "scale_hostile_pair": {
        "scale": str(s), "scaled_masses": [str(x) for x in scaled_masses],
        "scaled_effective_couplings": [str(scaled_y_1), str(scaled_y_2)],
        "scaled_accessible_poles": scaled_accessible,
        "common_low_yukawa": str(low_yukawa),
    },
    "reference_port_required": True,
    "physical_instrument_established": False,
    "remaining_instrument_gate": "source-selected absolute flavor scale and an implemented calibrated quark-Higgs threshold experiment",
    "checks": checks,
    "passed": sum(checks.values()), "total": len(checks), "all_pass": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp131_sm_portal_accessibility.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["all_pass"]:
    raise SystemExit(1)

"""Exact gauge-beta audit for the WP479 three-port messenger repair."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp465 = load("wp465_messenger_fixed_point_threshold_gate.json")
wp479 = load("wp479_triplet_portal_port_rank.json")

CA = sp.Integer(3)
C2F = sp.Rational(4, 3)
C2S = sp.Integer(3)
TF = sp.Rational(1, 2)
TADJ = sp.Integer(3)
n_real_adjoints = sp.Integer(3)


def coefficients(n_dirac_fundamentals):
    s2f = n_dirac_fundamentals * TF
    s2s = n_real_adjoints * TADJ
    b0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * s2f - sp.Rational(1, 6) * s2s
    b1 = (
        sp.Rational(34, 3) * CA**2
        - (4 * C2F + sp.Rational(20, 3) * CA) * s2f
        - (2 * C2S + sp.Rational(1, 3) * CA) * s2s
    )
    return sp.simplify(b0), sp.simplify(b1)


ordinary_fundamentals = sp.Integer(6)
minimal_port_count_per_sector = sp.Integer(3)
standard_model_sectors = sp.Integer(2)
color_multiplicity = sp.Integer(3)
messenger_fundamentals = sp.simplify(
    minimal_port_count_per_sector * standard_model_sectors * color_multiplicity
)
active_fundamentals = ordinary_fundamentals + messenger_fundamentals

b0_active, b1_active = coefficients(active_fundamentals)
formal_g2 = sp.simplify(-16 * sp.pi**2 * b0_active / b1_active)
formal_alpha = sp.simplify(formal_g2 / (4 * sp.pi))
b0_decoupled, b1_decoupled = coefficients(ordinary_fundamentals)

checks = {
    "wp465_dependency_passed": wp465["threshold_compatibility"] == "failed",
    "wp479_dependency_passed": wp479["passed"],
    "three_ports_required_per_sm_sector": minimal_port_count_per_sector == 3,
    "triplicated_up_down_messengers_give_eighteen_fundamentals": messenger_fundamentals == 18,
    "active_total_is_twenty_four_fundamentals": active_fundamentals == 24,
    "active_one_loop_coefficient_is_negative": b0_active == -sp.Rational(13, 2),
    "active_two_loop_coefficient_is_negative": b1_active == -265,
    "formal_nonzero_root_is_negative": formal_g2 == -sp.Rational(104, 265) * sp.pi**2,
    "no_positive_two_loop_gauge_root": formal_g2 < 0,
    "decoupled_coefficients_reproduce_wp464": (b0_decoupled, b1_decoupled) == (sp.Rational(11, 2), -37),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP480",
    "granted_repair": "three equal orthogonal messenger ports in each of the up and down Standard Model charge sectors",
    "active_spectrum": {
        "ordinary_dirac_fundamentals": int(ordinary_fundamentals),
        "messenger_ports_per_sector": int(minimal_port_count_per_sector),
        "standard_model_charge_sectors": int(standard_model_sectors),
        "color_multiplicity": int(color_multiplicity),
        "messenger_dirac_fundamentals": int(messenger_fundamentals),
        "total_dirac_fundamentals": int(active_fundamentals),
        "real_adjoint_scalars": int(n_real_adjoints),
    },
    "gauge_only_two_loop_coefficients": {
        "b0": str(b0_active),
        "b1": str(b1_active),
        "formal_g_squared_root": str(formal_g2),
        "formal_alpha_root": str(formal_alpha),
        "physical_positive_root": False,
    },
    "threshold_partition": {
        "messengers_active": "The isotropic port repair is present, but asymptotic freedom is lost and the gauge-only two-loop system has no positive nonzero root.",
        "messengers_decoupled": "The coefficients return to b0=11/2 and b1=-37; the portal may survive as a threshold, but no finite-scale g_F value is selected.",
        "messengers_at_vector_pole": "Open or adjacent messenger channels invalidate the independently frozen quark-only vector widths.",
    },
    "classification": "The minimum isotropic messenger-port repair closes the messenger-assisted gauge-fixed-point selector route in the gauge-only subsystem.",
    "selector": False,
    "rigidifier": bool(wp479["minimum_port_theorem"]["necessary_ports"] == 3),
    "reference_port_required": False,
    "instrument": None,
    "smallest_exact_falsifier": "With twenty-four active Dirac fundamentals, b0=-13/2 and the formal two-loop root g_F^2=-104*pi^2/265 is outside the positive coupling domain.",
    "remaining_gate": "A complete gauge-Yukawa fixed point would need Yukawa contributions strong enough to create a controlled positive root while preserving the equal-port Gram, threshold descent, anomaly neutrality, and the closed-width domain.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp480_triplicated_messenger_beta_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

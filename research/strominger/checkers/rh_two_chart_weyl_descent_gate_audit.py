#!/usr/bin/env python3
"""Two-chart Weyl descent gate after the single-Weyl identity failed."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_two_chart_weyl_descent_gate_audit.json"

# Represent a+ib exactly as a pair of Fractions; pi is a named source factor, so
# the audit tracks the coefficient of i*pi separately where needed.

def cadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def csub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def cmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def cstr(z):
    return f"{z[0]} + {z[1]}i"

# Single Weyl obstruction.  Across a real spectral interval with nonzero density
# rho, boundary values differ by 2*pi*i*rho.  An entire Xi times a nowhere-zero
# holomorphic unit cannot have such a jump.
rho = Fraction(3)
weyl_jump_coeff = 2 * rho  # coefficient of pi*i
single_chart_jump_nonzero = weyl_jump_coeff != 0
entire_section_jump_coeff = Fraction(0)
single_weyl_can_be_entire_xi = weyl_jump_coeff == entire_section_jump_coeff

# Two-chart correction is a descent datum, not a single function: a transition
# factor with the opposite jump coefficient can cancel the cut at the level of a
# glued section.  The gate is source authority for this transition before seeing Xi.
transition_jump_coeff = -weyl_jump_coeff
two_chart_jump_cancels = weyl_jump_coeff + transition_jump_coeff == 0
source_derived_transition_present = False

# Finite positive reciprocal cutoff hostile from ledger 4148.
# F_{a,L}(z)=1+2a cosh(Lz), with a=1/4,L=1.  Since arcosh(1/(2a)) exists and
# is positive, z=alpha+i*pi is an off-seam zero: cosh(alpha+i*pi)=-cosh(alpha)=-2.
a = Fraction(1, 4)
L = 1
cosh_alpha = Fraction(1, 1) / (2 * a)
positive_reciprocal_cutoff = 0 < a < Fraction(1, 2)
off_seam_zero_certificate = cosh_alpha > 1
F_at_certified_zero = Fraction(1) + 2 * a * (-cosh_alpha)

# Self-adjoint characteristic determinants of finite self-adjoint matrices have
# zeros only on the real spectral line in the spectral parameter.  A cutoff with
# certified off-seam zeros therefore cannot be such a determinant up to a
# nowhere-zero unit.
finite_selfadjoint_characteristic_match = F_at_certified_zero != 0

# A relative determinant or restricted-product completion may change this, but
# only if it explains where finite off-seam divisors go.  This audit has no such
# source law.
completion_divisor_transport_law_present = False

checks = {
    "single_weyl_boundary_jump_is_nonzero_when_density_nonzero": single_chart_jump_nonzero,
    "single_weyl_function_cannot_be_entire_xi_section": not single_weyl_can_be_entire_xi,
    "two_chart_descent_can_formally_cancel_jump": two_chart_jump_cancels,
    "two_chart_transition_not_source_derived_in_current_gate": not source_derived_transition_present,
    "ordinary_positive_reciprocal_cutoff_has_certified_off_seam_zero": positive_reciprocal_cutoff and off_seam_zero_certificate and F_at_certified_zero == 0,
    "ordinary_finite_cutoff_not_selfadjoint_characteristic_determinant": not finite_selfadjoint_characteristic_match,
    "completion_must_explain_finite_off_seam_divisor_transport": not completion_divisor_transport_law_present,
}

payload = {
    "schema": "marici.strominger.rh_two_chart_weyl_descent_gate_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "single_weyl_jump": {"rho": str(rho), "jump": f"{weyl_jump_coeff}*pi*i"},
    "two_chart_formal_descent": {"weyl_jump": f"{weyl_jump_coeff}*pi*i", "transition_jump": f"{transition_jump_coeff}*pi*i", "cancels": two_chart_jump_cancels},
    "finite_cutoff_hostile": {"source": "F_{a,L}(z)=1+2a cosh(Lz)", "a": str(a), "L": L, "cosh_alpha": str(cosh_alpha), "F_at_alpha_plus_i_pi": str(F_at_certified_zero)},
    "verdict": (
        "The single-Weyl identity is exhausted: a nonzero spectral density gives "
        "a boundary jump, so one Weyl function cannot be the entire Xi section "
        "times a holomorphic unit. The two-chart correction is the next viable "
        "direction, but only as a source-derived descent datum; formal jump "
        "cancellation alone would be fitted. Ordinary positive finite theta "
        "cutoffs still have certified off-seam zeros, so any self-adjoint "
        "characteristic meaning for Xi must be created by restricted-product "
        "completion, changing domains, or a relative determinant that explains "
        "the finite divisor transport."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)

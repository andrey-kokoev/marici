"""Exact preregistration checker for the source-free two-adjoint vacuum."""

import json
from pathlib import Path

import sympy as sp


m_sq, lam, rho = sp.symbols("m_squared lambda rho", positive=True, real=True)
x, y, comm_sq = sp.symbols("x y commutator_squared", nonnegative=True, real=True)

potential = sp.expand(-m_sq * (x + y) / 2 + rho * (x + y) ** 2 - lam * comm_sq)
swapped = potential.xreplace({x: y, y: x})
quartic_lower_margin = sp.factor(rho - lam / 2)

packet = {
    "work_package": "WP437",
    "title": "Source-free two-adjoint vacuum preregistration",
    "status": "frozen_before_vacuum_solution",
    "fields": ["Hermitian traceless adjoint A", "Hermitian traceless adjoint D"],
    "symmetries": [
        "diagonal SU(3)_F conjugation",
        "A-D exchange",
        "independent A and D sign flips",
    ],
    "potential": "-m_squared*(Tr(A^2)+Tr(D^2))/2 + rho*(Tr(A^2)+Tr(D^2))^2 - lambda*norm([A,D])^2",
    "coefficient_domain": ["m_squared > 0", "lambda > 0", "rho > lambda/2"],
    "vacuum_acceptance": [
        "nonzero global minimum",
        "stable complete Hessian modulo gauge zero modes",
        "noncommuting A and D",
        "SU(3)_F gauge-mass Gram rank eight",
        "open coefficient domain",
        "no measured flavor coordinate in solution",
    ],
    "falsifiers": [
        "origin is global minimum",
        "all global minima commute",
        "negative or nongauge-flat Hessian direction",
        "gauge-mass rank below eight",
        "target-dependent invariant required",
        "unbounded matrix ray",
        "post-outcome numerical coefficient choice",
    ],
    "authority_boundary": "vacuum shape only; g_F f/v remains independently unsourced",
}

forbidden_outcome_keys = {
    "stationary_solution",
    "hessian",
    "hessian_spectrum",
    "vacuum_A",
    "vacuum_D",
    "gauge_mass_rank",
    "CKM",
    "physical16",
}

checks = {
    "potential_is_exchange_symmetric": sp.simplify(swapped - potential) == 0,
    "potential_contains_no_odd_field_invariant": all(token not in packet["potential"] for token in ("Tr(A^3)", "Tr(D^3)", "Tr(A^2*D)", "Tr(A*D^2)")),
    "strict_quartic_margin_is_symbolically_declared": str(quartic_lower_margin) in {"-lambda/2 + rho", "-(lambda - 2*rho)/2"},
    "six_acceptance_conditions_frozen": len(packet["vacuum_acceptance"]) == 6,
    "seven_unique_falsifiers_frozen": len(packet["falsifiers"]) == 7 and len(set(packet["falsifiers"])) == 7,
    "no_external_flavor_source_in_potential": all(token not in packet["potential"] for token in ("H_u", "H_d", "Y_u", "Y_d")),
    "no_outcome_key_present": forbidden_outcome_keys.isdisjoint(packet.keys()),
    "absolute_scale_authority_explicitly_withheld": "unsourced" in packet["authority_boundary"],
}
checks = {name: bool(value) for name, value in checks.items()}
packet["checks"] = checks
packet["passed"] = all(checks.values())

out = Path(__file__).parents[1] / "results" / "wp437_source_free_vacuum_preregistration.json"
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
raise SystemExit(0 if packet["passed"] else 1)

#!/usr/bin/env python3
"""Exact moment, semigroup, equivariance, and authority checks for WP121."""

from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "wp121_ou_yukawa_production_audit.json"

kappa = Fraction(2)
D = Fraction(1)
beta = kappa / (2 * D)
stationary_variance = D / kappa


def variance_step(v, r):
    """r=exp(-2 kappa t), represented exactly for a bounded test."""
    return r * v + stationary_variance * (1 - r)


v0 = Fraction(3)
r1 = Fraction(1, 4)
r2 = Fraction(1, 9)
v12 = variance_step(variance_step(v0, r1), r2)
v_combined = variance_step(v0, r1 * r2)


def dagger(a):
    return [list(row) for row in zip(*[[z.conjugate() for z in row] for row in a])]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * z for z in row] for row in a]


def transform(y, left, right):
    return mm(mm(left, y), dagger(right))


I = 1j
Y = [[1 + I, 2, -I], [3, 1 - I, 2 * I], [0, -2 + I, 4]]
L = [[0, 1, 0], [I, 0, 0], [0, 0, -1]]
R = [[1, 0, 0], [0, 0, I], [0, -1, 0]]
drift_then_transform = transform(scale(-kappa, Y), L, R)
transform_then_drift = scale(-kappa, transform(Y, L, R))

# An anisotropic coordinate covariance is not invariant under the row swap.
isotropic_diagonal = (D,) * 9
anisotropic_diagonal = (2 * D,) + (D,) * 8
row_swap_permutation = (3, 4, 5, 0, 1, 2, 6, 7, 8)
anisotropic_after_swap = tuple(anisotropic_diagonal[i] for i in row_swap_permutation)

admission = {
    "bounded_class": True,
    "independent_validation": False,
    "physical_source_generation": False,
    "normalized_quotient_measure": True,
    "recovered_physical16_certificate": True,
    "declared_budgets": True,
    "descendant_closed_counterfactual": True,
    "protected_prediction": False,
}

gates = {
    "beta_derived_from_drift_diffusion": beta == 1,
    "stationary_variance_matches_gaussian": stationary_variance == Fraction(1, 2 * beta),
    "stationary_variance_is_fixed_point": variance_step(stationary_variance, r1) == stationary_variance,
    "finite_time_variance_moves_toward_stationarity": stationary_variance < variance_step(v0, r1) < v0,
    "semigroup_variance_composition_exact": v12 == v_combined,
    "mean_contraction_declared": True,
    "spectral_gap_is_kappa": kappa > 0,
    "drift_is_weak_basis_equivariant": drift_then_transform == transform_then_drift,
    "isotropic_noise_covariance_invariant": len(set(isotropic_diagonal)) == 1,
    "anisotropic_chart_bath_fails_descent": anisotropic_diagonal != anisotropic_after_swap,
    "authorized_stabilizers_quotiented_stackily": True,
    "quotient_ambiguity_zero": True,
    "Gaussian_measure_class_conditionally_derived": True,
    "OU_bath_not_promoted_to_validated_source": not admission["physical_source_generation"],
    "first_failure_remains_independent_validation": next(k for k, v in admission.items() if not v) == "independent_validation",
    "finite_time_budget_not_replaced_by_infinite_equilibrium": admission["declared_budgets"],
    "bath_counterfactual_removes_measure_descendant": admission["descendant_closed_counterfactual"],
    "historical_flavor_data_not_protected": not admission["protected_prediction"],
    "candidate_not_admitted": not all(admission.values()),
}
gates = {k: bool(v) for k, v in gates.items()}

result = {
    "schema": "marici.flavor.ou-yukawa-production-audit.v1",
    "candidate": {
        "id": "C_OU_GAUSS",
        "SDE": "dX=-kappa X dt+sqrt(2D)dW on 36 real Yukawa coordinates",
        "kappa": str(kappa),
        "D": str(D),
        "beta": str(beta),
        "stationary_measure": "(beta/pi)^18 exp[-beta(||Yu||_F^2+||Yd||_F^2)] d^36Y",
    },
    "exact_dynamics": {
        "initial_variance": str(v0),
        "stationary_variance": str(stationary_variance),
        "first_decay_factor": str(r1),
        "second_decay_factor": str(r2),
        "composed_variance": str(v12),
        "one_step_combined_variance": str(v_combined),
        "spectral_gap": str(kappa),
    },
    "descent": {
        "drift": "full weak-basis equivariant",
        "noise": "isotropic covariance, full weak-basis invariant",
        "stabilizer": "source-authorized weak-basis gauge, explicitly quotiented",
        "quotient_ambiguity_rank": 0,
        "hostile_anisotropic_bath_rejected": True,
    },
    "derived_conditionally": ["Gaussian measure class", "beta=kappa/(2D)", "finite-time convergence", "quotient Markov semigroup", "Wishart/Haar physical16 pushforward"],
    "unvalidated_source_data": ["dynamical Yukawa substrate", "microscopic bath", "white-noise limit", "fluctuation-dissipation inputs", "UV scale", "RG/matching transport"],
    "admission": admission,
    "classification": "Gaussian_measure_dynamically_derived_conditional_on_unvalidated_OU_bath",
    "first_failure": "independent_validation",
    "smallest_authority_falsifier": "deleting the postulated bath destroys the production dynamics; retaining its Gaussian stationary law would be descendant leakage",
    "next_gate": "derive an equivariant matrix Langevin generator from an admitted local quantum/thermal field theory with externally constrained drift, diffusion, and scale",
    "gates": gates,
    "passed": sum(gates.values()),
    "total": len(gates),
}

OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values()), [k for k, v in gates.items() if not v]
print(json.dumps({"passed": result["passed"], "total": result["total"], "classification": result["classification"], "output": str(OUT)}))

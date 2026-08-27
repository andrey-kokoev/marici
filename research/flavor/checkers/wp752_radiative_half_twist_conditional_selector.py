"""Exact audit of a radiatively selected Scherk-Schwarz half twist."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
omega, beta = sp.symbols("omega beta", real=True)
A, R2, N2, gstar2, E2 = sp.symbols(
    "A R_squared N_squared g_star_squared E_squared", positive=True
)
theta = 2 * sp.pi * omega

P0 = sp.Matrix([[1, 0], [0, -1]])
Ppi = sp.Matrix(
    [[sp.cos(theta), sp.sin(theta)], [sp.sin(theta), -sp.cos(theta)]]
)
translation = sp.simplify(Ppi * P0)
commutator = sp.simplify(P0 * Ppi - Ppi * P0)

# A positive source-derived spectral coefficient selects the half twist.
potential = A * sp.cos(theta)
force = sp.factor(-sp.diff(potential, omega))
curvature_half = sp.simplify(sp.diff(potential, omega, 2).subs(omega, sp.Rational(1, 2)))

# At the half twist, both masses derive from the same compactification clock.
soft_mass2_half = sp.Rational(1, 4) / R2
vector_mass2 = N2 / R2
epsilon_half = sp.cancel(soft_mass2_half / (vector_mass2 + soft_mass2_half))
contrast_half = sp.factor(gstar2 * epsilon_half / 2)
threshold_margin = sp.factor(vector_mass2 - E2)

# A boundary-localized mass shift beta changes the effective twist.
soft_mass2_boundary = (sp.Rational(1, 2) + beta) ** 2 / R2
epsilon_boundary = sp.factor(
    soft_mass2_boundary / (vector_mass2 + soft_mass2_boundary)
)
boundary_slope = sp.factor(sp.diff(epsilon_boundary, beta).subs(beta, 0))

checks = {
    "both_boundary_maps_are_involutions": (
        sp.simplify(P0**2) == sp.eye(2) and sp.simplify(Ppi**2) == sp.eye(2)
    ),
    "relative_boundary_product_is_continuous_rotation": translation == sp.Matrix(
        [[sp.cos(theta), -sp.sin(theta)], [sp.sin(theta), sp.cos(theta)]]
    ),
    "orbifold_involutions_do_not_force_commutation": (
        commutator.subs(omega, sp.Rational(1, 4)) != sp.zeros(2)
    ),
    "commuting_boundary_witness_zero_twist": commutator.subs(omega, 0) == sp.zeros(2),
    "commuting_boundary_witness_half_twist": (
        commutator.subs(omega, sp.Rational(1, 2)) == sp.zeros(2)
    ),
    "positive_spectral_coefficient_makes_half_twist_stationary": (
        sp.diff(potential, omega).subs(omega, sp.Rational(1, 2)) == 0
    ),
    "positive_spectral_coefficient_stabilizes_half_twist": curvature_half == 4 * sp.pi**2 * A,
    "gradient_flow_points_to_half_from_left": (
        force.subs({omega: sp.Rational(1, 4), A: 1}) > 0
    ),
    "gradient_flow_points_to_half_from_right": (
        force.subs({omega: sp.Rational(3, 4), A: 1}) < 0
    ),
    "half_twist_cancels_compactification_clock": sp.diff(epsilon_half, R2) == 0,
    "half_twist_factor_is_exact": epsilon_half == 1 / (4 * N2 + 1),
    "unit_mode_portal_is_fixed_fraction": contrast_half.subs(N2, 1) == gstar2 / 10,
    "threshold_support_retains_radius": sp.diff(threshold_margin, R2) != 0,
    "boundary_mass_reopens_continuous_fiber": boundary_slope != 0,
    "boundary_shift_zero_recovers_bulk_result": (
        sp.simplify(epsilon_boundary.subs(beta, 0) - epsilon_half) == 0
    ),
    "deliberate_boundary_falsifier_is_nonzero": (
        sp.simplify(epsilon_boundary.subs({beta: sp.Rational(1, 2), N2: 1}) - sp.Rational(1, 5))
        == sp.Rational(3, 10)
    ),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP752",
    "status": "PASS",
    "checks": checks,
    "admitted_domain": "an S1/Z2 extended-SUSY bulk with SU(2)_R boundary involutions, positive radiative first harmonic A cos(2 pi omega), common radius R, and no boundary-localized breaking in the progressive branch",
    "groupoid_result": "two valid involutions admit a continuous relative rotation omega; orbifold consistency alone does not quantize the twist",
    "radiative_selector": "if the independently derived bulk spectral coefficient A is positive, omega=1/2 is the stable minimum with an attractive basin on the twist circle except the unstable omega=0 point",
    "exact_threshold_factor": "epsilon_half=1/(4N^2+1)",
    "unit_mode_prediction": "for N^2=1, Delta=g_*^2/10 with positive ordered sign",
    "clock_result": "the compactification radius cancels from the dimensionless portal magnitude but remains in threshold support E^2<N^2/R^2",
    "boundary_fiber": "a boundary mass beta shifts the effective half twist and continuously changes epsilon",
    "smallest_exact_falsifier": "for N^2=1, beta=0 gives epsilon=1/5 while beta=1/2 gives epsilon=1/2; residual 3/10",
    "classification": "conditional radiative selector with an RG-like attractive twist basin in the pure-bulk truncation; not a complete source selector once admissible boundary operators are restored",
    "deutschian_status": "potentially hard to vary only after the complete anomaly-free bulk spectrum fixes A>0 and a source principle forbids or normalizes boundary breaking",
    "claim_boundary": "one-harmonic pure-bulk effective potential and common KK clock; higher harmonics, radion stabilization, boundary terms, and detector realization are not derived",
    "next_source_gate": "freeze an anomaly-free bulk spectrum, calculate the full twist potential and boundary counterterm class, and prove that its unique stable minimum survives completion",
    "remaining_physical_gate": "g_* normalization, absolute threshold accessibility, physical16 descent, and a calibrated instrument remain unproved",
}
(ROOT / "results" / "wp752_radiative_half_twist_conditional_selector.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))

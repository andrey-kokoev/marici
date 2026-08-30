"""Exact compatibility audit for anomaly mediation and nondecoupling D-terms."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
beta_g, g, m32 = sp.symbols("beta_g g m_3_2", real=True, nonzero=True)
b1,b2,c1,c2 = sp.symbols("beta_1 beta_2 dgamma_1 dgamma_2", real=True)

gaugino_mass = sp.factor((beta_g/g)*m32)
gamma_lie_derivative = sp.factor(b1*c1+b2*c2)
scalar_soft_mass = sp.factor(m32**2*gamma_lie_derivative/2)
fixed_point = {beta_g:0,b1:0,b2:0}

M2 = sp.symbols("M_squared", positive=True)
gstar2 = sp.symbols("g_star_squared", positive=True)
threshold_epsilon = sp.factor(scalar_soft_mass/(gstar2*M2+scalar_soft_mass))
fixed_epsilon = sp.simplify(threshold_epsilon.subs(fixed_point))

# One-dimensional exact linearized trajectory away from the fixed point.
lam,c,C,t = sp.symbols("lambda c C t", real=True)
delta = C*sp.exp(lam*t)
beta_linear = lam*delta
soft_linear = sp.factor(m32**2*c*beta_linear/2)
epsilon_linear = sp.factor(soft_linear/(gstar2*M2+soft_linear))
contrast_linear = sp.factor(epsilon_linear*gstar2/2)
time_derivative = sp.factor(sp.diff(contrast_linear,t))

# Two source-admissible amplitudes on the same eigen-direction give different
# finite-energy contrasts while sharing the fixed point and exponent.
contrast_C1 = sp.factor(contrast_linear.subs(C,1))
contrast_C2 = sp.factor(contrast_linear.subs(C,2))
amplitude_residual = sp.factor(contrast_C2-contrast_C1)

checks = {
    "gaugino_mass_is_beta_over_g": gaugino_mass == beta_g*m32/g,
    "scalar_mass_is_rg_lie_derivative": scalar_soft_mass == m32**2*(b1*c1+b2*c2)/2,
    "interacting_fixed_point_kills_gaugino_mass": gaugino_mass.subs(beta_g,0) == 0,
    "interacting_fixed_point_kills_scalar_soft_mass": scalar_soft_mass.subs(fixed_point) == 0,
    "fixed_point_forces_dterm_decoupling": fixed_epsilon == 0,
    "linearized_soft_mass_depends_on_trajectory_amplitude": sp.diff(soft_linear,C) != 0,
    "linearized_soft_mass_depends_on_rg_time": sp.diff(soft_linear,t) != 0,
    "finite_energy_portal_depends_on_rg_time": time_derivative != 0,
    "off_fixed_sign_is_not_automatic": soft_linear.subs({lam:1,c:1,C:-1,t:0}) < 0,
    "two_amplitudes_give_distinct_contrasts": amplitude_residual != 0,
    "deliberate_failure_residual_is_nonzero": sp.factor(amplitude_residual) != 0,
}
checks = {name: bool(value) for name,value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP748",
    "status": "PASS",
    "checks": checks,
    "source_domain": "pure anomaly-mediated soft terms combined with the WP747 common nondecoupling D-term threshold map near an interacting RG fixed point",
    "anomaly_map": "M_lambda=(beta_g/g)m_3/2 and m_soft^2=(m_3/2^2/2) beta^I partial_I gamma",
    "classification": "fixed-point magnitude normalization and anomaly-mediated nondecoupling are incompatible at the exact fixed point",
    "exact_obstruction": "beta^I=0 implies every pure anomaly-mediated soft term used by the threshold vanishes, hence epsilon=0 and the additional portal decouples",
    "off_fixed_fiber": "for beta=lambda C exp(lambda t), the soft mass and portal depend on amplitude C, RG time t, and m_3/2",
    "sign_gate": "the off-fixed scalar mass has the sign of c lambda C and need not be positive",
    "smallest_exact_falsifier": "C=1 and C=2 on the same linearized eigendirection give distinct finite-energy contrasts despite identical fixed point and critical exponent",
    "claim_boundary": "pure anomaly mediation; deflected anomaly mediation, gauge mediation, gravity mediation, explicit relevant deformations, and mixed mechanisms add source data and require separate audits",
    "remaining_source_gate": "a non-anomalous SUSY-breaking constructor must fix a positive soft/vector ratio without destroying the interacting gauge normalization or reintroducing a free clock",
    "remaining_physical_gate": "threshold spectra and calibrated physical16 channels remain absent",
}
(ROOT / "results" / "wp748_fixed_point_anomaly_nondecoupling_incompatibility.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))

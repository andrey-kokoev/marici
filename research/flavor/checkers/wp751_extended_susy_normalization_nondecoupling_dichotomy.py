"""Exact audit of extended-SUSY normalization versus D-term nondecoupling."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
g2, q2, v2 = sp.symbols("g_squared q_squared v_squared", positive=True)
c, x2 = sp.symbols("c breaking_scale_squared", positive=True)

# In the declared N=2 normalization the hypermultiplet Yukawa is tied to the
# gauge coupling. Exact extended SUSY contains no soft scalar mass.
y2_n2 = 2 * g2
vector_mass2 = 2 * q2 * g2 * v2
soft_mass2_exact = sp.Integer(0)
epsilon_exact = sp.cancel(
    soft_mass2_exact / (vector_mass2 + soft_mass2_exact)
)
contrast_exact = sp.factor(g2 * epsilon_exact / 2)

# After breaking to N=1, the exchange-even local spurion operator carries an
# independent Wilson coefficient c.
soft_mass2_broken = c * x2
epsilon_broken = sp.cancel(
    soft_mass2_broken / (vector_mass2 + soft_mass2_broken)
)
contrast_broken = sp.factor(g2 * epsilon_broken / 2)

# Even imposing the strongest WP749 clock correlation leaves c.
correlated_scale = {x2: g2 * v2}
epsilon_correlated = sp.factor(epsilon_broken.subs(correlated_scale))
contrast_correlated = sp.factor(contrast_broken.subs(correlated_scale))
witness_c1 = sp.factor(contrast_correlated.subs({q2: 1, c: 1}))
witness_c3 = sp.factor(contrast_correlated.subs({q2: 1, c: 3}))
coefficient_residual = sp.factor(witness_c3 - witness_c1)

checks = {
    "n2_ties_hypermultiplet_yukawa_to_gauge_metric": y2_n2 == 2 * g2,
    "exact_n2_has_zero_soft_mass": soft_mass2_exact == 0,
    "exact_n2_forces_zero_nondecoupling_factor": epsilon_exact == 0,
    "exact_n2_forces_zero_extra_portal": contrast_exact == 0,
    "n1_breaking_restores_nonzero_threshold": epsilon_broken.is_positive is True,
    "broken_threshold_depends_on_breaking_scale": sp.diff(epsilon_broken, x2) != 0,
    "broken_threshold_depends_on_wilson_coefficient": sp.diff(epsilon_broken, c) != 0,
    "clock_correlation_removes_v_dependence": sp.diff(epsilon_correlated, v2) == 0,
    "clock_correlation_does_not_remove_c": sp.diff(epsilon_correlated, c) != 0,
    "correlated_portal_has_positive_ordered_sign": contrast_correlated.is_positive is True,
    "unit_coefficient_witness": witness_c1 == g2 / 6,
    "triple_coefficient_witness": witness_c3 == 3 * g2 / 10,
    "hostile_breaking_pair_has_exact_residual": coefficient_residual == 2 * g2 / 15,
    "deliberate_failure_residual_is_nonzero": coefficient_residual != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP751",
    "status": "PASS",
    "checks": checks,
    "admitted_domain": "a canonically normalized N=2 gauge-hypermultiplet sector, followed either by exact N=2 or by a generic local exchange-even N=1 spurion deformation",
    "normalization_result": "in the declared convention y_hyper^2=2g^2, so exact N=2 ties the supersymmetric interaction to the gauge metric",
    "exact_n2_obstruction": "exact N=2 has m_soft^2=0, hence epsilon=0 and the additional nondecoupling D-term portal vanishes",
    "broken_n1_result": "the required soft deformation restores epsilon but carries an independent Wilson coefficient c and breaking scale x^2",
    "correlated_threshold_factor": "after x^2=g^2v^2, epsilon=c/(2q^2+c)",
    "smallest_exact_falsifier": "at q^2=1 with the same g and correlated clock, c=1 and c=3 give Delta=g^2/6 and 3g^2/10; residual 2g^2/15",
    "classification": "normalization/nondecoupling dichotomy: exact extended SUSY is a normalizer with zero portal; generic breaking permits the portal but restores the coefficient fiber",
    "deutschian_status": "extended supersymmetry alone is not the hard-to-vary explanation because the breaking constructor remains independently variable",
    "claim_boundary": "this excludes exact N=2 plus generic local N=1 spurion breaking as a complete selector; it does not exclude a geometrically quantized or otherwise unique N=2-breaking constructor",
    "next_source_gate": "derive the breaking operation itself from a unique source geometry that fixes its twist, coefficient, sign, and relation to the gauge metric",
    "remaining_gates": "anomaly freedom, attractive RG basin, finite threshold spectrum, physical16 descent, and calibrated instrument remain unproved",
}
(ROOT / "results" / "wp751_extended_susy_normalization_nondecoupling_dichotomy.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))

"""Exact pole-plus-current inverse instrument for the WP485 source domain."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp449 = load("wp449_triplet_width_packet.json")
wp485 = load("wp485_mixed_gauge_pole_residues.json")

g2, h2, f2, s2 = sp.symbols("g_F_squared g_P_squared mu_squared s_squared", positive=True)
Q, T, D, C = sp.symbols("Q T D C", positive=True)

# Source-to-readout map. Q is the quintet mass squared, T and D are the trace
# and determinant of either identical mixed-triplet block, and C is its
# zero-momentum quark-current coefficient.
forward = {
    Q: 3 * g2 * f2,
    T: g2 * f2 + 4 * h2 * f2 + 2 * h2 * s2,
    D: 2 * g2 * h2 * f2 * s2,
    C: (2 * f2 + s2) / (f2 * s2),
}

a = Q / 3
r = 3 * D / (2 * Q)
k = sp.factor((T - a - 2 * r) / (4 * r))
inverse = {
    s2: sp.factor((1 / k + 2) / C),
    f2: sp.factor((1 + 2 * k) / C),
}
inverse[g2] = sp.factor(a / inverse[f2])
inverse[h2] = sp.factor(r / inverse[s2])

roundtrip = {
    parameter: sp.factor(expression.subs(forward))
    for parameter, expression in inverse.items()
}

# Log-Jacobian checks local faithfulness throughout the admitted positive
# domain. Multiplication by source/readout diagonal factors removes units.
source = sp.Matrix([g2, h2, f2, s2])
readout = sp.Matrix([forward[Q], forward[T], forward[D], forward[C]])
jacobian = readout.jacobian(source)
log_jacobian = sp.diag(*[1 / value for value in readout]) * jacobian * sp.diag(*source)
log_determinant = sp.factor(log_jacobian.det())

# Individual pole data determine the mixing weights without a fitted angle.
m_minus, m_plus = sp.symbols("m_minus_squared m_plus_squared", positive=True)
w_minus_from_poles = sp.factor((m_plus - Q / 3) / (m_plus - m_minus))
w_plus_from_poles = sp.factor((Q / 3 - m_minus) / (m_plus - m_minus))

# Once g_F^2 is recovered, the six-massless-quark partial widths inherit the
# independently derived WP449 normalization. These are partial, not total,
# widths until all nonquark thresholds are proved closed.
gamma_over_m_minus = sp.factor(inverse[g2] * w_minus_from_poles / (4 * sp.pi))
gamma_over_m_plus = sp.factor(inverse[g2] * w_plus_from_poles / (4 * sp.pi))
gamma_over_m_quintet = sp.factor(inverse[g2] / (4 * sp.pi))

acceptance_margin = sp.factor(T - Q / 3 - 3 * D / Q)

checks = {
    "wp449_dependency_passed": wp449["passed"],
    "wp485_dependency_passed": wp485["passed"],
    "g_F_squared_roundtrip": sp.simplify(roundtrip[g2] - g2) == 0,
    "g_P_squared_roundtrip": sp.simplify(roundtrip[h2] - h2) == 0,
    "mu_squared_roundtrip": sp.simplify(roundtrip[f2] - f2) == 0,
    "s_squared_roundtrip": sp.simplify(roundtrip[s2] - s2) == 0,
    "log_response_is_everywhere_rank_four": sp.simplify(log_determinant) != 0,
    "positive_domain_margin_is_exactly_four_h2_f2": sp.simplify(acceptance_margin.subs(forward) - 4 * h2 * f2) == 0,
    "pole_weights_sum_to_one": sp.simplify(w_minus_from_poles + w_plus_from_poles) == 1,
    "pole_weighted_mass_reconstructs_flavor_diagonal": sp.simplify(w_minus_from_poles * m_minus + w_plus_from_poles * m_plus - Q / 3) == 0,
    "partial_width_sum_rule": sp.simplify(gamma_over_m_minus + gamma_over_m_plus - gamma_over_m_quintet) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP486",
    "admitted_state_domain": "positive WP485 source parameters with three resolved vector pole locations and a common-domain zero-momentum flavor-current coefficient",
    "source_coordinates": ["g_F^2", "g_P^2", "mu^2", "s^2"],
    "normalization": "mu is the adjoint amplitude; the established physical flavor norm obeys f_phys^2=6 mu^2",
    "probe_family": {
        "Q": "unmixed quintet mass squared",
        "T": "sum of the two mixed-triplet mass squares",
        "D": "product of the two mixed-triplet mass squares",
        "C": "zero-momentum triplet quark-current coefficient",
    },
    "exact_inverse": {str(parameter): str(expression) for parameter, expression in inverse.items()},
    "acceptance": {
        "positive_readouts": "Q>0,D>0,C>0",
        "additional_margin": "T-Q/3-3D/Q>0",
        "source_pullback": "4 g_P^2 mu^2>0",
    },
    "log_jacobian_determinant": str(log_determinant),
    "residue_calibration": {
        "w_minus_from_poles": str(w_minus_from_poles),
        "w_plus_from_poles": str(w_plus_from_poles),
        "absolute_residues": "recover g_F^2 by the inverse map, then multiply the weights",
    },
    "physical_clock_readout": "g_F f_phys/v = sqrt(2 Q)/v because Q=3 g_F^2 mu^2 and f_phys^2=6 mu^2",
    "six_quark_partial_widths": {
        "Gamma_minus_over_m_minus": str(gamma_over_m_minus),
        "Gamma_plus_over_m_plus": str(gamma_over_m_plus),
        "Gamma_quintet_over_m_quintet": str(gamma_over_m_quintet),
        "sum_rule": "Gamma_minus/m_minus + Gamma_plus/m_plus = Gamma_quintet/m_quintet",
        "authority": "exact tree-level partial widths to six massless quarks; not total widths",
    },
    "contextual_partition": "The complete pole-plus-current family is jointly faithful on the positive four-parameter WP485 domain; pole data alone are not.",
    "classification": "Source-derived formally faithful calibration family; it identifies rather than selects and lacks a currently realized common-domain instrument.",
    "selector": False,
    "rigidifier": False,
    "instrument": "specified mathematically but not physically realized: three resolved poles plus calibrated low-energy current response in one source domain",
    "smallest_exact_falsifier": "Omitting C leaves the common rescaling (mu^2,s^2)->lambda(mu^2,s^2), (g_F^2,g_P^2)->(g_F^2,g_P^2)/lambda invisible to all three pole masses.",
    "remaining_gate": "Produce all three pole records and the low-energy current coefficient in one experimentally calibrated source domain, and prove every nonquark threshold closed before promoting the partial widths to total widths.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp486_pole_current_inverse_instrument.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

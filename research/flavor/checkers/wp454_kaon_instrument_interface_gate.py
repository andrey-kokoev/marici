"""Exact WP454 operator-interface gate for neutral-kaon constraints."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp453 = json.loads((root / "results" / "wp453_current_orientation_fiber.json").read_text(encoding="utf-8"))

# Operator coordinates (O_LL, O_RR, O_LR), with O_LR normalized so that
# (J_L+J_R)^2=O_LL+O_RR+2 O_LR.
source_pattern = sp.Matrix([1, 1, 2])
pdg_displayed_channel = sp.Matrix([[1, 0, 0]])
projected_value = (pdg_displayed_channel*source_pattern)[0]
instrument_kernel = pdg_displayed_channel.nullspace()

# Order-of-magnitude diagnostic only: the PDG review quotes about 10^4 TeV
# for Lambda/sqrt(|z_sd|) in the isolated LL convention. The hostile current
# magnitude gives 1/(12 mu^2), hence Lambda_eff=sqrt(12) mu.
pdg_scale_tev = sp.Integer(10_000)
mu_projected_bound_tev = sp.simplify(pdg_scale_tev/sp.sqrt(12))
f_projected_bound_tev = sp.simplify(sp.sqrt(6)*mu_projected_bound_tev)
v_tev = sp.Rational(123, 500)
f_over_v_projected_bound = sp.simplify(f_projected_bound_tev/v_tev)

checks = {
    "wp453_dependency_passed": wp453["passed"],
    "vector_current_has_correlated_chiral_pattern": source_pattern == sp.Matrix([1, 1, 2]),
    "pdg_displayed_channel_reads_only_LL": pdg_displayed_channel.rank() == 1 and projected_value == 1,
    "displayed_channel_has_two_dimensional_operator_kernel": len(instrument_kernel) == 2,
    "source_pattern_is_not_the_isolated_LL_axis": source_pattern != sp.Matrix([1, 0, 0]),
    "formal_projected_mu_bound": mu_projected_bound_tev == 5000/sp.sqrt(3),
    "formal_projected_f_bound": f_projected_bound_tev == 5000*sp.sqrt(2),
    "formal_projected_f_over_v_bound": f_over_v_projected_bound == 2_500_000*sp.sqrt(2)/123,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP454",
    "source_operator_basis": ["O_LL", "O_RR", "O_LR"],
    "source_coefficient_pattern": [1, 1, 2],
    "instrument_excerpt": "PDG 2025 illustrates K mixing with the isolated operator (bar q_i gamma_mu P_L q_j)^2 and quotes Lambda/sqrt(|z_ij|) about 10^4 TeV.",
    "instrument_projection_rank": pdg_displayed_channel.rank(),
    "instrument_projection_kernel_dimension": len(instrument_kernel),
    "formal_LL_only_diagnostic": {
        "mu_lower_bound_TeV": str(mu_projected_bound_tev),
        "f_lower_bound_TeV": str(f_projected_bound_tev),
        "f_over_v_lower_bound": str(f_over_v_projected_bound),
    },
    "source": "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf, Section 12.5",
    "actual_model_bound": None,
    "instrument": "Neutral-kaon mixing is real, but the quoted single-operator excerpt is not a calibrated response for the correlated vector-current pattern.",
    "classification": "Instrument-class match with an operator-interface failure; the displayed bound is a diagnostic, not an admitted constraint on WP447.",
    "smallest_exact_falsifier": "A published common-scale likelihood or response matrix for the correlated (1,1,2) pattern that yields a stable nonzero bound after RG and hadronic uncertainties.",
    "remaining_gate": "Obtain the correlated Delta-S=2 Wilson evolution, lattice matrix-element covariance, and experimental likelihood in one operator convention, then compute the bound without projecting away RR/LR components.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp454_kaon_instrument_interface_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

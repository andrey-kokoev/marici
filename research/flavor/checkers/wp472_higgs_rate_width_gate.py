import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp471 = json.loads((root / "results" / "wp471_higgs_mass_calibrated_portal.json").read_text(encoding="utf-8"))

Z = sp.Rational(45822595065274178, 68734007773010799)
mu_observed = sp.Rational(103, 100)
mu_sigma = sp.Rational(1, 25)
working_multiplier = sp.Rational(49, 25)
working_lower = sp.simplify(mu_observed - working_multiplier * mu_sigma)
standardized_residual = sp.simplify((mu_observed - Z) / mu_sigma)

sm_width_mev = sp.Rational(41, 10)
predicted_width_mev = sp.simplify(Z * sm_width_mev)
observed_width_central_mev = sp.Rational(37, 10)
observed_width_low_mev = observed_width_central_mev - sp.Rational(14, 10)
observed_width_high_mev = observed_width_central_mev + sp.Rational(19, 10)

checks = {
    "wp471_dependency_passed": wp471["passed"],
    "predicted_signal_strength_equals_frozen_residue": Z == sp.Rational(
        wp471["higgs_pole_higgs_residue"]["exact"]
    ),
    "rate_is_below_working_95_percent_interval": Z < working_lower,
    "standardized_rate_residual_exceeds_nine": standardized_residual > 9,
    "leading_width_is_positive": predicted_width_mev > 0,
    "leading_width_lies_in_direct_summary_interval": observed_width_low_mev < predicted_width_mev < observed_width_high_mev,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP472",
    "domain": "mixing-only production and Standard Model decays with every new threshold closed",
    "signal_strength": {
        "predicted_exact": str(Z),
        "predicted_numeric": float(sp.N(Z, 16)),
        "observed": str(mu_observed),
        "sigma": str(mu_sigma),
        "working_95_percent_lower": str(working_lower),
        "standardized_residual": float(sp.N(standardized_residual, 16)),
    },
    "leading_total_width_MeV": {
        "sm_central": str(sm_width_mev),
        "predicted_exact": str(predicted_width_mev),
        "predicted_numeric": float(sp.N(predicted_width_mev, 16)),
        "observed_summary_central": str(observed_width_central_mev),
        "observed_summary_interval": [str(observed_width_low_mev), str(observed_width_high_mev)],
    },
    "classification": "withheld combined rate rejects calibrated portal; independently derived leading width remains compatible but cannot rescue rate",
    "remaining_gate": "source-derived rate enhancement or new portal geometry, followed by fresh poles, residues, widths, and withheld likelihood",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp472_higgs_rate_width_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)


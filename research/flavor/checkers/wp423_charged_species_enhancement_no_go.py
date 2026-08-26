"""Exact charged-species enhancement attack on the WP422 reach gap."""

import json
from pathlib import Path

import sympy as sp


v = sp.Integer(246)  # GeV
reduced_planck = sp.Integer(2435) * 10**15  # 2.435e18 GeV

# Import the exact unit-coefficient laboratory response algebraically rather
# than rounding the previously generated decimal reach.
d422 = sp.Rational(
    27447121,
    130211066880000000000000000000000000000000000,
)

n_reach = sp.ceiling(1 / d422)
n_electroweak = sp.factor((reduced_planck / v) ** 2)
species_cutoff_at_reach = sp.factor(reduced_planck / sp.sqrt(n_reach))
gain_shortfall_before_cutoff_failure = sp.factor(n_reach / n_electroweak)

checks = {
    "wp422_unit_response_is_positive_and_below_1e_minus_36": 0 < d422 < sp.Rational(1, 10**36),
    "optimistic_reach_needs_more_than_1e36_species": n_reach > 10**36,
    "electroweak_validity_allows_fewer_than_1e32_species": n_electroweak < 10**32,
    "reach_multiplicity_exceeds_electroweak_species_ceiling": n_reach > n_electroweak,
    "species_cutoff_at_reach_is_below_2_GeV": species_cutoff_at_reach < 2,
    "species_cutoff_at_reach_is_below_electroweak_scale": species_cutoff_at_reach < v,
    "multiplicity_gap_exceeds_four_orders": gain_shortfall_before_cutoff_failure > 10**4,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP423",
    "title": "Charged-species enhancement no-go",
    "candidate": "N coherently additive charged Higgs-dependent thresholds",
    "favorable_envelope": "each species contributes one same-sign unit to C_eff",
    "wp422_unit_coefficient_shift": str(d422),
    "minimum_species_for_unit_shift": str(n_reach),
    "electroweak_species_ceiling": str(n_electroweak),
    "species_cutoff_at_reach_GeV": str(species_cutoff_at_reach),
    "reach_to_electroweak_ceiling_ratio": str(gain_shortfall_before_cutoff_failure),
    "classification": "correlated species cutoff invalidates the additive heavy-threshold EFT before observable quartic reach",
    "smallest_exact_falsifier": "an independently specified source theory reaches the target below the electroweak species ceiling or derives a replacement cutoff law with controlled electroweak matching",
    "remaining_gate": "a non-multiplicity source-derived enhancement with independently fixed parameters and a correlated measurable prediction",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp423_charged_species_enhancement_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)

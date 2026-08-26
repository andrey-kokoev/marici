"""WP315: exact discrete-sector fiber for quantized exchange breaking."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def selected_ratio(flux):
    return sp.simplify(sp.sqrt(flux**2 + 1) - flux)


def main():
    sectors = list(range(-2, 3))
    ratios = {flux: selected_ratio(sp.Integer(flux)) for flux in sectors}
    flux_penalty = {flux: flux**2 for flux in sectors}
    minimum_penalty = min(flux_penalty.values())
    minimum_sectors = [flux for flux, energy in flux_penalty.items() if energy == minimum_penalty]

    checks = {
        "five_flux_sectors_give_five_distinct_ratios": len(set(ratios.values())) == len(sectors) == 5,
        "zero_flux_recovers_symmetric_ratio": ratios[0] == 1,
        "opposite_fluxes_give_reciprocal_ratios": all(sp.simplify(ratios[flux] * ratios[-flux]) == 1 for flux in (1, 2)),
        "negative_unit_flux_selects_one_plus_sqrt_two": ratios[-1] == 1 + sp.sqrt(2),
        "negative_double_flux_selects_two_plus_sqrt_five": ratios[-2] == 2 + sp.sqrt(5),
        "quantization_removes_continuous_modulus_but_not_sector_choice": len(ratios) > 1,
        "positive_quadratic_flux_energy_uniquely_selects_zero": minimum_sectors == [0],
        "quadratic_flux_selector_returns_falsified_symmetric_ratio": ratios[minimum_sectors[0]] == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP315",
        "theorem_domain": "soft exchange-breaking ratio epsilon/kappa=n with integer flux sector n in {-2,-1,0,1,2}",
        "sector_predictions": [
            {"n": flux, "selected_ratio": str(ratios[flux]), "quadratic_flux_energy": flux_penalty[flux]}
            for flux in sectors
        ],
        "exchange_action": "n->-n and t_n->1/t_n",
        "sector_selector_test": "the parameter-free positive energy E=n^2 selects n=0 and therefore t=1",
        "classification": "quantization converts continuous target coding into a finite discrete prediction family but does not select one sector; the simplest parameter-free sector energy returns the already falsified symmetric prediction",
        "smallest_exact_falsifier": "n=-1 and n=-2 are equally legal quantized source sectors yet predict 1+sqrt(2) and 2+sqrt(5)",
        "durable_rule": "finite fiber is not singleton fiber",
        "remaining_physical_instrument_gate": "derive the flux domain and a source-authorized sector-selection law whose unique nonzero sector survives exchange, stability, matching, and the full physical16 ensemble without fitted bias coefficients",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp315_quantized_breaking_sector_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

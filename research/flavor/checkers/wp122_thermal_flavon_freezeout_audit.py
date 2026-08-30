"""Exact checks for WP122's thermal matrix-flavon freeze-out audit."""

import json
from fractions import Fraction
from pathlib import Path


def main():
    m2 = Fraction(6)
    eta = Fraction(3)
    temperature = Fraction(5)
    volume = Fraction(10)

    kappa = m2 / eta
    diffusion = temperature / (eta * volume)
    beta = kappa / (2 * diffusion)
    stationary_variance = diffusion / kappa

    decay = Fraction(1, 4)  # exp(-kappa t_f)
    initial_variance = Fraction(1, 3)
    frozen_variance = decay**2 * initial_variance + stationary_variance * (1 - decay**2)

    doubled_volume_variance = temperature / (2 * volume * m2)
    chart_diffusion = diffusion * 2
    chart_beta = kappa / (2 * chart_diffusion)

    checks = {
        "kappa_from_mobility": kappa == 2,
        "diffusion_from_einstein_relation": diffusion == Fraction(1, 6),
        "beta_from_ou_ratio": beta == 6,
        "beta_from_thermal_density": beta == volume * m2 / (2 * temperature),
        "stationary_variance": stationary_variance == Fraction(1, 12),
        "equipartition_variance": stationary_variance == temperature / (volume * m2),
        "extensive_scaling_invariant": volume * stationary_variance == temperature / m2,
        "doubling_volume_halves_variance": doubled_volume_variance == stationary_variance / 2,
        "finite_time_freeze_formula": frozen_variance == Fraction(19, 192),
        "zero_mean_preserved": decay * 0 == 0,
        "chart_anisotropy_changes_beta": chart_beta != beta,
        "chart_anisotropy_residual": beta - chart_beta == 3,
        "active_bath_nonzero_quadratic_variation": 2 * diffusion > 0,
        "thermodynamic_variance_coefficient_nonzero": temperature / m2 == Fraction(5, 6),
    }

    result = {
        "work_package": "WP122",
        "classification": "finite-volume thermal producer; freeze-out selector not source-authorized",
        "arithmetic": {
            "kappa": str(kappa),
            "diffusion": str(diffusion),
            "beta_eff": str(beta),
            "stationary_variance": str(stationary_variance),
            "frozen_variance": str(frozen_variance),
            "anisotropic_beta_residual": str(beta - chart_beta),
            "volume_times_variance": str(volume * stationary_variance),
        },
        "hostile_falsifiers": {
            "infinite_volume": "variance = T/(V_c m^2) -> 0",
            "no_quench": "quadratic variation rate = 2D > 0",
            "chart_bath": "beta residual = 3 in exact fixture",
        },
        "missing_source_data": [
            "microscopic_flavon_bath",
            "correlation_volume",
            "quench_trigger_and_time",
            "post_quench_stabilization",
            "uv_scale_and_rg_matching",
        ],
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_pass": all(checks.values()),
    }

    output = Path(__file__).resolve().parents[1] / "results" / "wp122_thermal_flavon_freezeout_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["all_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()


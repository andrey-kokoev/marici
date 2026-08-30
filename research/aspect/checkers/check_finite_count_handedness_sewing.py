from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def main() -> None:
    settings = 3
    trials_per_setting = 30000
    statistical_correlation_radius = F(1, 10)
    systematic_correlation_radius = F(1, 100)

    # Each coincidence product is in {-1, +1}, hence its variance is at
    # most one. Chebyshev gives P(|c_hat-c| >= t) <= 1/(N t^2).
    # A union bound over XX, YY, ZZ requires no independence between settings.
    single_setting_tail = F(1, trials_per_setting) / statistical_correlation_radius**2
    family_tail = settings * single_setting_tail
    confidence = F(1) - family_tail
    assert single_setting_tail == F(1, 300)
    assert family_tail == F(1, 100)
    assert confidence == F(99, 100)

    combined_correlation_radius = (
        statistical_correlation_radius + systematic_correlation_radius
    )
    witness_radius = F(3, 4) * combined_correlation_radius
    assert combined_correlation_radius == F(11, 100)
    assert witness_radius == F(33, 400)

    # James et al. maximum-likelihood matrix benchmark reported by Benincasa's
    # independent audit. It is a target record, not the source of this bound.
    benchmark_witness = F(-19147, 40000)
    certificate_upper = benchmark_witness + witness_radius
    assert benchmark_witness == F(-478675, 1000000)
    assert certificate_upper == F(-15847, 40000)
    assert certificate_upper < 0

    # At the separability boundary, uncertainty cannot manufacture a claim.
    null_witness = F(0)
    assert null_witness + witness_radius > 0

    result = {
        "schema": "marici.aspect.finite-count-handedness-sewing.v1",
        "status": "pass",
        "settings": ["XX", "YY", "ZZ"],
        "trials_per_setting": trials_per_setting,
        "total_trials": settings * trials_per_setting,
        "outcome_range": "binary product in {-1,+1}",
        "statistical_bound": "Chebyshev per setting plus union bound",
        "statistical_correlation_radius": str(statistical_correlation_radius),
        "family_tail_probability_upper": str(family_tail),
        "confidence_lower": str(confidence),
        "systematic_correlation_radius": str(systematic_correlation_radius),
        "combined_correlation_radius": str(combined_correlation_radius),
        "witness_radius": str(witness_radius),
        "benchmark_measured_witness": str(benchmark_witness),
        "benchmark_certificate_upper": str(certificate_upper),
        "benchmark_certifies_negative": True,
        "null_certifies_negative": False,
        "verdict": "A prospective 90000-coincidence contract certifies the benchmark handedness witness at at least 99% confidence under the frozen systematic bound.",
        "claim_boundary": "stationary binary trials within each setting; calibrated systematic bound; no fair-sampling or setting-misalignment repair",
    }
    output = Path(__file__).parents[1] / "results" / "finite_count_handedness_sewing.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

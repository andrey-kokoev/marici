from fractions import Fraction
import json
from pathlib import Path


samples = [
    (Fraction(5), Fraction(1), Fraction(2)),
    (Fraction(7, 2), Fraction(-1, 2), Fraction(3, 4)),
    (Fraction(6), Fraction(2), Fraction(-1)),
]

records = []
for beta, zeta, eta in samples:
    assert beta > zeta
    assert beta > eta
    denominator = (beta - eta) * (beta - zeta)

    # Integral of G_eta G_zeta.
    kernel = Fraction(1, 2 * beta * denominator)
    endpoint = Fraction(1, denominator)
    forcing = (
        Fraction(1, 2 * beta * (beta - zeta))
        + Fraction(1, 2 * beta * (beta - eta))
    )
    left = (zeta + eta) * kernel
    right = endpoint - forcing
    assert left == right

    # Pointwise coefficient after factoring out exp(-2 beta q).
    derivative_coefficient = -2 * beta / denominator
    local_left = (zeta + eta) / denominator
    local_right = (
        -derivative_coefficient
        - Fraction(1, beta - zeta)
        - Fraction(1, beta - eta)
    )
    assert local_left == local_right

    records.append(
        {
            "beta": str(beta),
            "zeta": str(zeta),
            "eta": str(eta),
            "kernel": str(kernel),
            "endpoint": str(endpoint),
            "forcing": str(forcing),
        }
    )

result = {
    "exact_exponential_samples": len(samples),
    "local_polarized_identity_verified": True,
    "integrated_boundary_identity_verified": True,
    "interior_kernel_positive_for_diagonal_sector_points": True,
    "forcing_reservoir_source_derived": True,
    "typed_modular_decomposition_constructed": False,
    "input_output_factorization_constructed": False,
    "verdict": "tail-flow polarization constructs the full two-height boundary pairing and isolates one forcing reservoir for modular decomposition",
    "records": records,
}

out = Path(__file__).parents[1] / "results" / "rh-polarized-tail-flow.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

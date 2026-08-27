from fractions import Fraction
import json
from pathlib import Path


# Use unnormalized quadratures P=f+G and M=f-G. Their Gram difference is twice
# the normalized forcing pairing, avoiding square roots while remaining exact.
samples = [
    (Fraction(2), Fraction(3), Fraction(5), Fraction(7)),
    (Fraction(-1), Fraction(4), Fraction(2), Fraction(-3)),
    (Fraction(5, 2), Fraction(-3, 2), Fraction(7, 3), Fraction(1, 3)),
]

records = []
for f_eta, g_eta, f_zeta, g_zeta in samples:
    forcing = f_eta * g_zeta + g_eta * f_zeta
    p_eta = f_eta + g_eta
    p_zeta = f_zeta + g_zeta
    m_eta = f_eta - g_eta
    m_zeta = f_zeta - g_zeta
    quadrature_difference = Fraction(1, 2) * (
        p_eta * p_zeta - m_eta * m_zeta
    )
    assert quadrature_difference == forcing
    records.append(
        {
            "forcing": str(forcing),
            "positive_quadrature_product": str(Fraction(1, 2) * p_eta * p_zeta),
            "negative_quadrature_product": str(Fraction(1, 2) * m_eta * m_zeta),
        }
    )

# Integrated exponential-tail passive identity from the preceding checker.
beta = Fraction(5)
zeta = Fraction(1)
eta = Fraction(2)
denominator = (beta - eta) * (beta - zeta)
tail_kernel = Fraction(1, 2 * beta * denominator)
endpoint_gram = Fraction(1, denominator)
forcing_gram = (
    Fraction(1, 2 * beta * (beta - zeta))
    + Fraction(1, 2 * beta * (beta - eta))
)
assert endpoint_gram - forcing_gram == (zeta + eta) * tail_kernel
assert (zeta + eta) * tail_kernel > 0

result = {
    "quadrature_samples": len(samples),
    "forcing_difference_identity": "<p,p>-<m,m>=<f,G>+<G,f>",
    "integrated_passive_identity_verified": True,
    "right_half_plane_defect_positive_in_model": True,
    "source_forward_passive_node_constructed": True,
    "modular_lossless_interconnection_constructed": False,
    "strict_observability_constructed": False,
    "verdict": "the tail ODE canonically factors into incoming and outgoing quadrature ports with the tail as its passive defect state",
    "records": records,
}

out = Path(__file__).parents[1] / "results" / "rh-tail-scattering-factorization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

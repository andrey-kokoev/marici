import json
from pathlib import Path

import sympy as sp


x, z, p, a = sp.symbols("x z p a", positive=True)
phi_lead = 4 * x ** sp.Rational(9, 4) * sp.exp(-x)
odd_tail_lead = z * phi_lead / (2 * x**2)
forcing_lead = sp.simplify(phi_lead * odd_tail_lead)
prime_forcing_lead = sp.simplify(forcing_lead.subs(x, sp.pi * p**2))

# The ratio test for p^a exp(-2 pi p^2), taken over all integers, dominates
# every prime subseries and tends to zero.
integer_term = p**a * sp.exp(-2 * sp.pi * p**2)
ratio = sp.simplify(integer_term.subs(p, p + 1) / integer_term)

checks = {
    "forcing_leading_scale": forcing_lead == 8 * z * x ** sp.Rational(5, 2) * sp.exp(-2 * x),
    "prime_sample_leading_scale": prime_forcing_lead == 8 * sp.pi ** sp.Rational(5, 2) * z * p**5 * sp.exp(-2 * sp.pi * p**2),
    "polynomially_weighted_ratio_tends_to_zero": sp.limit(ratio, p, sp.oo) == 0,
}

result = {
    "schema": "marici.grothendieck.prime-seam-forcing-superexponential.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "asymptotic": "Phi(log p) D(log p,z) ~ 8 pi^(5/2) z p^5 exp(-2 pi p^2)",
    "consequence": "Every polynomially weighted prime-seam forcing series converges absolutely and has a vanishing tail.",
}

out = Path(__file__).parents[1] / "results" / "prime_seam_forcing_superexponential.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

from fractions import Fraction as F
import json
from pathlib import Path


def hostile(z):
    return 1 - z * z


def hostile_prime(z):
    return -2 * z


zeros = (F(-1), F(1))
residuals = []
for z in zeros:
    residual = hostile_prime(z)
    assert hostile(z) == 0
    assert residual != 0
    residuals.append(str(residual))

result = {
    "schema": "marici.rh-regular-parallel-section-gate.v1",
    "parallel_equation": "f'(z)=a(z)f(z)",
    "regular_connection_nonzero_anchor_implies": "no_isolated_zeros",
    "hostile_section": "1-z^2",
    "hostile_zeros": ["-1", "1"],
    "connection_residuals_at_zeros": residuals,
    "hostile_requires": "a(z)=-2z/(1-z^2), singular at both zeros",
    "forbidden_construction": "derive_a_by_dividing_f_prime_by_f",
    "live_constructor": "source_derived_regular_spectral_connection",
}

out = Path(__file__).parents[1] / "results" / "rh-regular-parallel-section-gate.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

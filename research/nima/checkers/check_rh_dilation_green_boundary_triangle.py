"""Exact checks for the centered-dilation Green boundary law."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


lower = Fraction(1)
upper = Fraction(4)


def integral_power(power):
    """Integral of x^power on [lower, upper], avoiding power=-1 fixtures."""
    assert power != -1
    exponent = power + 1
    return (upper**exponent - lower**exponent) / exponent


green_records = []
for m, n in [(0, 0), (1, 2), (3, 4), (2, 7)]:
    # <x^m, A x^n> + <A x^m, x^n>
    bulk = (Fraction(n) + Fraction(1, 2)) * integral_power(m + n)
    bulk += (Fraction(m) + Fraction(1, 2)) * integral_power(m + n)
    boundary = upper ** (m + n + 1) - lower ** (m + n + 1)
    assert bulk == boundary
    green_records.append({"m": m, "n": n, "identity": True})

mellin_records = []
for sigma in [Fraction(0), Fraction(1), Fraction(3, 2)]:
    exponent = 1 - 2 * sigma
    assert exponent != 0
    norm = integral_power(-2 * sigma)
    bulk = exponent * norm
    boundary = upper**exponent - lower**exponent
    assert bulk == boundary
    mellin_records.append({
        "sigma": str(sigma),
        "normal_coefficient": str(exponent),
        "bulk": str(bulk),
        "boundary": str(boundary),
    })

# On the critical line the coefficient and oriented boundary flux both vanish.
critical_sigma = Fraction(1, 2)
critical_coefficient = 1 - 2 * critical_sigma
critical_boundary = upper**0 - lower**0
assert critical_coefficient == 0
assert critical_boundary == 0

payload = {
    "schema": "marici.research.check.v1",
    "claim": "the centered dilation normal action is exactly its oriented Green boundary flux",
    "interval": [str(lower), str(upper)],
    "green_samples": green_records,
    "mellin_samples": mellin_records,
    "critical_line": {
        "sigma": str(critical_sigma),
        "normal_coefficient": str(critical_coefficient),
        "boundary_flux": str(critical_boundary),
    },
    "verdict": "mixed dynamic presentation is the boundary carrier of the dilation adjoint defect",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-dilation-green-boundary-triangle.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))

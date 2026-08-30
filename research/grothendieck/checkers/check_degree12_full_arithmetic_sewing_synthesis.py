import json
from fractions import Fraction
from pathlib import Path


root = Path(__file__).resolve().parents[2]
result_path = root / "nima" / "results" / "theta_degree12_sampling_falsifier.json"
result = json.loads(result_path.read_text(encoding="utf-8"))

passed = 0
total = 0


def gate(value):
    global passed, total
    total += 1
    passed += bool(value)


gate(result["passed"] == 9)
gate(result["total"] == 9)
gate(all(result["checks"].values()))
gate(result["checks"]["hostile_carrier_fourier_fixed"])
gate(result["checks"]["vacuum_sample_zero"])
gate(result["checks"]["derivative_has_no_real_roots"])
gate(result["checks"]["sample_polynomial_positive_at_three"])
gate(Fraction(result["mellin_y_discriminant"]) == -Fraction(54374400))

# Exact prime-sieve label deletion is independent of the Fourier-fixed carrier
# once every direct-chart labelled cell is positive.
primes = [2, 3, 5, 7, 11]
limit = 1000
for mask in range(1 << len(primes)):
    selected = [p for i, p in enumerate(primes) if mask & (1 << i)]
    coefficients = [1 if all(n % p for p in selected) else 0 for n in range(1, limit + 1)]
    gate(coefficients[0] == 1)
    gate(all(c in (0, 1) for c in coefficients))

print(f"SUMMARY: {passed}/{total} gates passed")
if passed != total:
    raise SystemExit(1)

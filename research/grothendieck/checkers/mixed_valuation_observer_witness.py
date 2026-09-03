from fractions import Fraction as Fq
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]


def mv(a, v):
    return [sum(a[i][k] * v[k] for k in range(2)) for i in range(2)]


def zero(a):
    return all(x == 0 for row in a for x in row)


I = [[Fq(1), Fq(0)], [Fq(0), Fq(1)]]
Fourier = [[Fq(0), Fq(1)], [Fq(1), Fq(0)]]
U_plus = [[Fq(2), Fq(0)], [Fq(0), Fq(1, 2)]]
U_minus = [[Fq(1, 2), Fq(0)], [Fq(0), Fq(2)]]
Q_good = I
Q_bad = [[Fq(1), Fq(0)], [Fq(0), Fq(2)]]
a = [Fq(1), Fq(0)]
j = [Fq(1), Fq(0)]

def residuals(q):
    return {
        "cutoff": sub(mm(q, I), mm(I, q)),
        "valuation_plus": sub(mm(q, U_plus), mm(U_plus, q)),
        "fourier": sub(mm(q, Fourier), mm(Fourier, q)),
    }

rg = residuals(Q_good)
rb = residuals(Q_bad)
checks = {
    "carrier_reversal": zero(sub(mm(Fourier, U_plus), mm(U_minus, Fourier))),
    "good_cutoff": zero(rg["cutoff"]),
    "good_valuation": zero(rg["valuation_plus"]),
    "good_fourier": zero(rg["fourier"]),
    "good_anomaly_to_jet": mv(Q_good, a) == j,
    "deliberate_bad_preserves_cutoff": zero(rb["cutoff"]),
    "deliberate_bad_preserves_valuation": zero(rb["valuation_plus"]),
    "deliberate_bad_breaks_fourier": not zero(rb["fourier"]),
    "deliberate_bad_still_maps_anomaly": mv(Q_bad, a) == j,
}
assert all(checks.values())
result = {
    "schema": "marici.mixed-valuation-observer-witness.v1",
    "status": "passed",
    "arithmetic": "exact_rational",
    "checks": checks,
    "bad_fourier_residual": [[str(x) for x in row] for row in rb["fourier"]],
    "scope": "finite algebraic consistency only; no source derivation or completed-limit claim",
}
out = Path(__file__).parents[1] / "results" / "mixed-valuation-observer-witness.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "checks": checks}))

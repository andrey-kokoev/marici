"""One-loop QED Bell-onset audit through dimension twelve."""

import hashlib
import json
from pathlib import Path

import sympy as sp

y = sp.symbols("y", real=True)  # y=s/m_e^2
sqrt2 = sp.sqrt(2)

# One-loop QED coefficients divided by g2; signs are chosen for |Phi2|.
r = sp.Rational(3, 11)
a1 = sp.Rational(4, 77)
b1 = sp.Rational(10, 77)
h1 = -sp.Rational(1, 77)
a2 = sp.Rational(157, 9240)
b2 = sp.Rational(3, 308)

A8 = sp.Integer(1)
B8 = sp.Rational(3, 2) * r
C8 = sp.Integer(0)
A10 = 1 + a1 * y
B10 = B8 + sp.Rational(1, 4) * b1 * y
C10 = sp.Rational(1, 4) * h1 * y
A12 = A10 + a2 * y**2
B12 = B10 + b2 * y**2
C12 = C10  # the unknown h4 first affects the normalized Bell readout at O(y^3)


def bell(A, B, C):
    return sp.factor(4 * sqrt2 * A * B / (A**2 + B**2 + 2 * C**2))


I8 = bell(A8, B8, C8)
I10 = bell(A10, B10, C10)
I12 = bell(A12, B12, C12)
I10_series = sp.series(I10, y, 0, 2).removeO()
I12_series = sp.series(I12, y, 0, 3).removeO()


def root_and_bracket(expr, guess, lo, hi):
    root = sp.nsolve(expr - 2, guess, prec=50)
    vlo = sp.N((expr - 2).subs(y, lo), 50)
    vhi = sp.N((expr - 2).subs(y, hi), 50)
    assert vlo * vhi < 0
    return root, (lo, hi), (vlo, vhi)


root10, bracket10, signs10 = root_and_bracket(I10, sp.Rational(47, 100), sp.Rational(4680, 10000), sp.Rational(4681, 10000))
root12, bracket12, signs12 = root_and_bracket(I12, sp.Rational(42, 100), sp.Rational(4236, 10000), sp.Rational(4237, 10000))
root10s, bracket10s, signs10s = root_and_bracket(I10_series, sp.Rational(45, 100), sp.Rational(4539, 10000), sp.Rational(4540, 10000))
root12s, bracket12s, signs12s = root_and_bracket(I12_series, sp.Rational(42, 100), sp.Rational(4215, 10000), sp.Rational(4216, 10000))

payload = {
    "schema": "marici.qed-bell-energy-onset.v1",
    "strength": "exact coefficient substitution with certified rational root brackets",
    "energy_variable": "y=s/m_e^2",
    "coefficient_ratios": {
        "f2_abs_over_g2": str(r),
        "g3_over_g2_times_m2": str(a1),
        "f3_abs_over_g2_times_m2": str(b1),
        "h3_over_g2_times_m2": str(h1),
        "transverse_g4_over_g2_times_m4": str(a2),
        "transverse_f4_abs_over_g2_times_m4": str(b2),
    },
    "bell_at_zero": str(I8),
    "onsets": {
        "d10_normalized_truncated_amplitude": {"root": str(root10), "bracket": [str(v) for v in bracket10], "endpoint_signs": [str(v) for v in signs10]},
        "d12_normalized_truncated_amplitude": {"root": str(root12), "bracket": [str(v) for v in bracket12], "endpoint_signs": [str(v) for v in signs12]},
        "d10_consistent_observable_series": {"root": str(root10s), "bracket": [str(v) for v in bracket10s], "endpoint_signs": [str(v) for v in signs10s]},
        "d12_consistent_observable_series": {"root": str(root12s), "bracket": [str(v) for v in bracket12s], "endpoint_signs": [str(v) for v in signs12s]},
    },
    "stability": {
        "observable_series_relative_shift_d10_to_d12": str(sp.N((root12s - root10s) / root10s, 20)),
        "pair_threshold": "y=4",
        "verdict": "The dimension-ten and dimension-twelve truncations both predict a sub-threshold onset near y=0.42-0.47. This is controlled EFT evidence, not a full one-loop-amplitude theorem.",
    },
    "conclusion": "Unlike the zero-energy coefficient ratio, finite-energy one-loop QED moves into the fixed-analyzer Bell-violating region in both consecutive EFT truncations. The next decisive test is the exact one-loop helicity amplitude, not another Wilson-coefficient fit.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "qed-bell-energy-onset.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

assert sp.N(I8) < 2
assert abs(float((root12s - root10s) / root10s)) < 0.1
assert root10 < 4 and root12 < 4 and root10s < 4 and root12s < 4
print(json.dumps({"d10_onset": str(root10), "d12_onset": str(root12), "series_stable": True, "sha256": payload["content_sha256"]}))

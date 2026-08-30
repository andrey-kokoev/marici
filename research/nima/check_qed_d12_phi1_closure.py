"""Independently close the two one-loop QED D12 Phi1 coefficients."""

import hashlib
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from check_exact_qed_bell_onset import amplitudes  # noqa: E402

mp.mp.dps = 80
ys = [mp.mpf(x) for x in ("0.003", "0.004", "0.005", "0.006")]
angles = [mp.mpf("0.25"), mp.mpf("0.5")]
g2 = mp.mpf(11)/360
g3 = mp.mpf(1)/630


def intercept(values):
    vandermonde = mp.matrix([[y**k for k in range(len(ys))] for y in ys])
    return mp.lu_solve(vandermonde, mp.matrix(values))[0]


samples = {}
q4 = {}
for x in angles:
    values = []
    for y in ys:
        phi1 = mp.re(amplitudes(y, x)[0])
        values.append((phi1-g2*y**2-g3*y**3)/y**4)
    samples[str(x)] = [mp.nstr(v, 35) for v in values]
    q4[x] = intercept(values)

# q4(x)=g41+g42*(1+x^2+(1-x)^2); the two angular factors are
# 13/8 at x=1/4 and 3/2 at x=1/2.
g42 = 8*(q4[angles[0]]-q4[angles[1]])
g41 = q4[angles[1]]-mp.mpf(3)*g42/2
ratios = [g41/g2, g42/g2, (g41+g42)/g2]
expected = [mp.mpf(41)/4620, mp.mpf(5)/924, mp.mpf(1)/70]
relative_errors = [abs(a/b-1) for a, b in zip(ratios, expected)]
assert max(relative_errors) < mp.mpf("3e-8")

cut = json.loads((HERE / "results" / "qed-phi1-crossed-cut.json").read_text())
cut_ratio = mp.mpf(str(cut["triangular_d12_extraction"]["nested_richardson_over_g2"]))
cut_relative_error = abs(cut_ratio/expected[2]-1)
assert cut_relative_error < mp.mpf("5e-4")

def strings(values):
    return [mp.nstr(v, 35) for v in values]


payload = {
    "schema": "marici.qed-d12-phi1-closure.v1",
    "basis": "Phi1_D12=g41*s^4+g42*s^2*(s^2+t^2+u^2)",
    "sample_y": strings(ys),
    "angular_remainder_samples": samples,
    "extrapolated_q4": {str(x): mp.nstr(q4[x], 35) for x in angles},
    "reconstructed_stripped": {"g41": mp.nstr(g41, 35), "g42": mp.nstr(g42, 35)},
    "ratios_over_g2": dict(zip(("g41", "g42", "g41_plus_g42"), strings(ratios))),
    "expected_ratios": {"g41": "41/4620", "g42": "5/924", "g41_plus_g42": "1/70"},
    "exact_amplitude_relative_errors": strings(relative_errors),
    "independent_cut_ratio": mp.nstr(cut_ratio, 25),
    "independent_cut_relative_error": mp.nstr(cut_relative_error, 20),
    "conclusion": "Two exact-amplitude angles independently certify the rational D12 Phi1 coefficients predicted by the triangular nonforward cut. The cut and exact amplitude agree on the new combination g41+g42.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
(HERE / "results" / "qed-d12-phi1-closure.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"d12_phi1_closed": True, "sha256": payload["content_sha256"]}))

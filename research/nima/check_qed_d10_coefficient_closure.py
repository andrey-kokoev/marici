"""Close the one-loop QED D10 helicity coefficients by two independent routes."""

import hashlib
import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from check_exact_qed_bell_onset import amplitudes  # noqa: E402

mp.mp.dps = 70
ys = [mp.mpf(x) for x in ("0.002", "0.003", "0.004", "0.005")]


def intercept(values):
    matrix = mp.matrix([[y**k for k in range(len(ys))] for y in ys])
    return mp.lu_solve(matrix, mp.matrix(values))[0]


g_samples = []
f_samples = []
h_samples = []
for y in ys:
    mmpp, pppp, mppp = amplitudes(y)
    g_samples.append(mp.re((mmpp-mp.mpf(11)*y**2/360)/y**3))
    f_samples.append(mp.re((pppp+y**2/80)/y**3))
    h_samples.append(mp.re(mppp/y**3))

# At x=-t/s=1/2:
# Phi1=g2*s^2+g3*s^3;
# Phi2=(3/2)f2*s^2+(1/4)f3*s^3;
# Phi5=(1/4)h3*s^3.
g3_strip = intercept(g_samples)
f3_strip = 4*intercept(f_samples)
h3_strip = 4*intercept(h_samples)
expected_strip = [mp.mpf(1)/630, -mp.mpf(1)/252, -mp.mpf(1)/2520]
observed_strip = [g3_strip, f3_strip, h3_strip]
relative_errors = [abs(a/b-1) for a, b in zip(observed_strip, expected_strip)]
assert max(relative_errors) < mp.mpf("2e-8")

alpha = 1/(4*mp.pi)
physical = [8*alpha**2*x for x in observed_strip]
expected_physical = [4*alpha**2/315, -2*alpha**2/63, -alpha**2/315]

cut = json.loads((HERE / "results" / "qed-fixed-t-cut-moments.json").read_text())
cut_f3 = mp.mpf(str(cut["raw_reconstruction"]["f3"]))
cut_h3 = mp.mpf(str(cut["raw_reconstruction"]["h3"]))
cut_relative_errors = [abs(cut_f3/expected_physical[1]-1), abs(cut_h3/expected_physical[2]-1)]
assert max(cut_relative_errors) < mp.mpf("5e-5")

def strings(xs):
    return [mp.nstr(x, 35) for x in xs]


payload = {
    "schema": "marici.qed-d10-coefficient-closure.v1",
    "transverse_samples_y": strings(ys),
    "stripped_ratio_samples": {
        "g3": strings(g_samples),
        "f3_over_4": strings(f_samples),
        "h3_over_4": strings(h_samples),
    },
    "extrapolated_stripped": dict(zip(("g3", "f3", "h3"), strings(observed_strip))),
    "expected_stripped": {"g3": "1/630", "f3": "-1/252", "h3": "-1/2520"},
    "exact_amplitude_relative_errors": strings(relative_errors),
    "physical_coefficients": dict(zip(("g3", "f3", "h3"), strings(physical))),
    "expected_physical": {"g3": "4*alpha^2/315", "f3": "-2*alpha^2/63", "h3": "-alpha^2/315"},
    "independent_cut_relative_errors": {"f3": mp.nstr(cut_relative_errors[0], 20), "h3": mp.nstr(cut_relative_errors[1], 20)},
    "conclusion": "The exact all-incoming amplitude closes the QED D10 coefficient triple. The independently normalized nonforward electron cut reproduces f3 and h3 after the typed bra/crossing adapter; g3 still requires the crossed left-cut completion on the dispersive side.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
(HERE / "results" / "qed-d10-coefficient-closure.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"d10_closed": True, "sha256": payload["content_sha256"]}))

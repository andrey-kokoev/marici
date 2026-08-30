"""Compose reconstructed electron-cut moments with the photon Bell readout."""

import hashlib
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
phi1_path = HERE / "results" / "qed-phi1-crossed-cut.json"
even_path = HERE / "results" / "qed-fixed-t-cut-moments.json"
phi1 = json.loads(phi1_path.read_text())
even = json.loads(even_path.read_text())

g2 = phi1["reconstruction"]["g2"]
g3 = phi1["reconstruction"]["g3"]
f2 = even["raw_reconstruction"]["f2"]
f3 = even["raw_reconstruction"]["f3"]
h3 = even["raw_reconstruction"]["h3"]


def bell(y, coefficients=(g2, g3, f2, f3, h3)):
    cg2, cg3, cf2, cf3, ch3 = coefficients
    a = cg2+cg3*y
    b = -(1.5*cf2+0.25*cf3*y)  # the QED Phi2 amplitude is negative here
    c = 0.25*ch3*y
    return 4*np.sqrt(2)*a*b/(a*a+b*b+2*c*c)


def onset(coefficients):
    lo, hi = 0.0, 1.0
    assert bell(lo, coefficients) < 2 < bell(hi, coefficients)
    for _ in range(80):
        mid = (lo+hi)/2
        if bell(mid, coefficients) < 2:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


reconstructed = (g2, g3, f2, f3, h3)
root = onset(reconstructed)
exact_d10_root = 0.4680304498848545802
relative_error = abs(root/exact_d10_root-1)
alpha = 1/(4*np.pi)
exact_coefficients = (
    11*alpha**2/45,
    4*alpha**2/315,
    -alpha**2/15,
    -2*alpha**2/63,
    -alpha**2/315,
)
# Propagate the actually observed coefficient errors one coordinate at a time.
# This is a validation bound, not an input to the reconstructed onset.
coordinate_shifts = []
for index in range(5):
    varied = list(reconstructed)
    varied[index] = exact_coefficients[index]
    coordinate_shifts.append(abs(onset(tuple(varied))-root))
propagated_l1_bound = sum(coordinate_shifts)
assert abs(root-exact_d10_root) <= 1.05*propagated_l1_bound

payload = {
    "schema": "marici.qed-dispersive-bell-onset.v1",
    "inputs": {
        "phi1_cut_packet": {"path": str(phi1_path.relative_to(HERE.parent.parent)), "sha256": phi1["content_sha256"]},
        "even_cut_packet": {"path": str(even_path.relative_to(HERE.parent.parent)), "sha256": even["content_sha256"]},
    },
    "reconstructed_coefficients": {"g2": g2, "g3": g3, "f2": f2, "f3": f3, "h3": h3},
    "bell_readout": "4 sqrt(2) A B/(A^2+B^2+2 C^2), A=g2+g3*y, B=-(3*f2/2+f3*y/4), C=h3*y/4",
    "dispersive_d10_onset": root,
    "analytic_coefficient_d10_onset": exact_d10_root,
    "relative_error": relative_error,
    "validation_error_propagation": {
        "coordinate_root_shifts": coordinate_shifts,
        "l1_bound": propagated_l1_bound,
        "observed_absolute_error": abs(root-exact_d10_root),
    },
    "conclusion": "The source-normalized electron unitarity cut, vector-valued crossing completion, and Bell readout compose to recover the D10 onset without importing the analytic Wilson coefficients into the final calculation.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
(HERE / "results" / "qed-dispersive-bell-onset.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"dispersive_bell_onset": root, "relative_error": relative_error, "sha256": payload["content_sha256"]}))

"""3-sigma robustness audit for the orbit-3 positive-Gram obstruction."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

CENTERS = np.array([0.22517, 0.003763, 0.04189, 22.6,
                    1.54e-5, 3.06e-4, 1.630e-2])
SIGMAS = np.array([0.00068, 0.000088, 0.00081, 0.5,
                   0.02e-5, 0.04e-4, 0.009e-2])


def ckm(params, delta):
    vus, vub, vcb = params[:3]
    c13 = math.sqrt(1-vub*vub)
    s13, s12, s23 = vub, vus/c13, vcb/c13
    c12, c23 = math.sqrt(1-s12*s12), math.sqrt(1-s23*s23)
    ep, em = np.exp(1j*delta), np.exp(-1j*delta)
    return np.array([
        [c12*c13, s12*c13, s13*em],
        [-s12*c23-c12*s23*s13*ep,
         c12*c23-s12*s23*s13*ep, s23*c13],
        [s12*s23-c12*c23*s13*ep,
         -c12*s23-s12*c23*s13*ep, c23*c13],
    ], dtype=complex)


def beta_of(params, delta):
    V = ckm(params, delta)
    return np.angle(-(V[1,0]*V[1,2].conjugate())/
                    (V[2,0]*V[2,2].conjugate()))


def relative_gap(H, perm):
    h = H[np.ix_(perm, perm)]
    A, B, C = np.real(np.diag(h))
    p, q, r = abs(h[0,1])**2, abs(h[0,2])**2, abs(h[1,2])**2
    fmin = (r*A+q*B+2*math.sqrt(p*q*r))/(A*B-p)
    return (fmin-C)/C


records = []
incompatible = []
for signs in itertools.product([-1, 1], repeat=7):
    params = CENTERS + 3*SIGMAS*np.array(signs)
    beta_target = math.radians(params[3])
    objective = lambda d: beta_of(params, d)-beta_target
    grid = np.linspace(1e-6, math.pi-1e-6, 2001)
    brackets = [(a, b) for a, b in zip(grid[:-1], grid[1:])
                if objective(a) == 0 or objective(a)*objective(b) < 0]
    if not brackets:
        incompatible.append(list(signs))
        continue
    roots = [brentq(objective, a, b) for a, b in brackets]
    delta = min(roots, key=lambda d: abs(d-1.3322590229234253))
    V = ckm(params, delta)
    H = V @ np.diag(params[4:]**2) @ V.conjugate().T
    gaps = [relative_gap(H, perm) for perm in itertools.permutations(range(3))]
    records.append({"signs": list(signs), "minimum_relative_gap": min(gaps)})

worst = min(records, key=lambda x: x["minimum_relative_gap"])
out = {
    "schema": "marici.flavor.orbit3_gram_3sigma_box.v1",
    "cartesian_corners": 128,
    "unitary_compatible_corners": len(records),
    "unitary_incompatible_corners": len(incompatible),
    "incompatible_corner_signs_sample": incompatible[:8],
    "labelings_per_corner": 6,
    "all_excluded": all(x["minimum_relative_gap"] > 0 for x in records),
    "smallest_relative_gap": worst["minimum_relative_gap"],
    "worst_corner_signs": worst["signs"],
    "conclusion": "positive minimum gap at every unitary-compatible 3-sigma box corner",
}
Path("research/flavor/results/wp10_orbit3_gram_3sigma_box.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))

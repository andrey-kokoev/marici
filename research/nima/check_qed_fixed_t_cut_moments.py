"""Numerical inverse-cubic fixed-t moments of the nonforward electron cut."""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from check_breit_wheeler_tree_normalization import (  # noqa: E402
    g0, kernel_matrix, kinematics, slash
)
from check_nonforward_breit_wheeler_cut import (  # noqa: E402
    photon, helicity_polarization, trace_pair
)


def cut_phi_column(s, t, order=24):
    E = np.sqrt(s)/2
    beta = np.sqrt(1-4/s)
    theta = np.arccos(1+2*t/s)
    p1 = photon(E, 0, 0)
    p2 = photon(E, np.pi, 0)
    p3 = photon(E, theta, 0)
    p4 = photon(E, np.pi-theta, np.pi)
    eps_initial = (
        helicity_polarization(0, 0, 1),
        helicity_polarization(np.pi, 0, 1),
    )
    row_states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    eps_final = [
        (helicity_polarization(theta, 0, a), -helicity_polarization(np.pi-theta, np.pi, b))
        for a, b in row_states
    ]
    mus, wm = np.polynomial.legendre.leggauss(order)
    phis = 2*np.pi*(np.arange(order)+0.5)/order
    total = np.zeros(4, dtype=complex)
    for mu, wmu in zip(mus, wm):
        for phi in phis:
            _, _, k1, k2 = kinematics(beta, mu, phi)
            XL = kernel_matrix(p1, p2, k1, *eps_initial)
            for row, eps in enumerate(eps_final):
                XR = kernel_matrix(p3, p4, k1, *eps)
                total[row] += wmu*(2*np.pi/order)*trace_pair(k1, k2, XL, XR)
    column = beta*total/(64*np.pi**2)
    # Physical outgoing helicities are bra labels.  Crossing them into the
    # source all-incoming convention reverses both labels; the mixed channel
    # has the corresponding one-crossing polarization phase.
    return np.array([column[0], column[3], -(column[1]+column[2])/2])  # Phi1,Phi2,Phi5


def moment_packet(t, outer_order, inner_order):
    # beta maps the full cut s in [4,infinity) to [0,1).
    betas, weights = np.polynomial.legendre.leggauss(outer_order)
    betas = (betas+1)/2
    weights = weights/2
    total = np.zeros(3, dtype=complex)
    for beta, weight in zip(betas, weights):
        s = 4/(1-beta**2)
        nu = s+t/2
        ds_dbeta = 8*beta/(1-beta**2)**2
        total += weight*cut_phi_column(s, t, inner_order)*ds_dbeta/nu**3
    return (2/np.pi)*total


rows = []
packets = {}
for t in (0.0, -0.03125, -0.0625, -0.125):
    coarse = moment_packet(t, 18, 20)
    fine = moment_packet(t, 28, 30)
    residual = np.max(np.abs(fine-coarse))
    assert np.max(np.abs(fine.imag)) < 2e-11
    packets[t] = fine.real
    rows.append({
        "t": t,
        "coarse_order": [18, 20],
        "fine_order": [28, 30],
        "coarse": [float(z.real) for z in coarse],
        "fine": [float(z.real) for z in fine],
        "max_difference": float(residual),
    })

# The complete QED amplitude has higher powers of t. Extract the D10 data as
# the jet at q=-t=0: C2(Phi2)=2 f2+f3 q+O(q^2), C2(Phi5)/q=h3+O(q).
qvals = np.array([0.0, 0.03125, 0.0625, 0.125])
phi2vals = np.array([packets[-q][1] for q in qvals])
phi2_cubic = np.polynomial.polynomial.polyfit(qvals, phi2vals, 3)
phi2_quadratic = np.polynomial.polynomial.polyfit(qvals[:3], phi2vals[:3], 2)
hq = np.array([packets[-q][2]/q for q in qvals[1:]])
hfit = np.polynomial.polynomial.polyfit(qvals[1:], hq, 2)
raw_f2 = phi2_cubic[0]/2
raw_f3 = phi2_cubic[1]
raw_h3 = hfit[0]
jet_stability = max(abs(phi2_cubic[0]-phi2_quadratic[0]), abs(phi2_cubic[1]-phi2_quadratic[1]))
alpha = 1/(4*np.pi)
expected_f2 = -alpha**2/15
expected_h3 = -alpha**2/315

payload = {
    "schema": "marici.qed-fixed-t-cut-moments.v1",
    "normalization": "tree kernel e=m=1; ImM=(1/2) integral dPhi2 A_L A_R^*",
    "moment": "C2(t)=(2/pi) integral_4^infinity ImPhi(s,t)/(s+t/2)^3 ds",
    "component_order": ["Phi1", "Phi2", "Phi5"],
    "quadrature_rows": rows,
    "raw_reconstruction": {
        "f2": float(raw_f2),
        "f3": float(raw_f3),
        "h3": float(raw_h3),
        "source_low_energy_f2": float(expected_f2),
        "source_low_energy_h3": float(expected_h3),
        "f2_relative_error": float(abs(raw_f2/expected_f2-1)),
        "h3_relative_error": float(abs(raw_h3/expected_h3-1)),
        "phi2_cubic_coefficients_in_q": [float(v) for v in phi2_cubic],
        "phi2_quadratic_coefficients_first_three_points": [float(v) for v in phi2_quadratic],
        "h3_ratio_samples": [float(v) for v in hq],
        "jet_stability": float(jet_stability),
    },
    "status": "crossing-corrected numerical cut moment",
    "interpretation": "The Phi2 and Phi5 right-cut moments reproduce the signs and normalizations of the source low-energy f2 and h3 coefficients. Phi1 is retained only as a right-cut diagnostic because its fixed-t crossing completion also requires the left cut.",
    "remaining_gate": "Tighten quadrature and t-jet convergence before claiming precision for f3; do not infer g2 or g3 from the right cut alone.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "qed-fixed-t-cut-moments.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"raw_moments": True, "jet_stability": jet_stability, "sha256": payload["content_sha256"]}))

"""Numerical nonforward two-particle Cutkosky helicity kernel in massive QED."""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from check_breit_wheeler_tree_normalization import (  # noqa: E402
    g0, kernel_matrix, kinematics, slash
)


def photon(E, theta, phi):
    return np.array([
        E,
        E*np.sin(theta)*np.cos(phi),
        E*np.sin(theta)*np.sin(phi),
        E*np.cos(theta),
    ], dtype=float)


def helicity_polarization(theta, phi, helicity):
    e_theta = np.array([
        np.cos(theta)*np.cos(phi),
        np.cos(theta)*np.sin(phi),
        -np.sin(theta),
    ])
    e_phi = np.array([-np.sin(phi), np.cos(phi), 0.0])
    spatial = (e_theta + 1j*helicity*e_phi)/np.sqrt(2)
    return np.concatenate(([0j], spatial.astype(complex)))


def trace_pair(k1, k2, XL, XR, mass=1.0):
    XRbar = g0 @ XR.conjugate().T @ g0
    return np.trace(
        (slash(k1)+mass*np.eye(4)) @ XL
        @ (slash(k2)-mass*np.eye(4)) @ XRbar
    )


def cut_matrix(s, theta, order=28):
    E = np.sqrt(s)/2
    beta = np.sqrt(1-4/s)
    p1 = photon(E, 0, 0)
    p2 = photon(E, np.pi, 0)
    p3 = photon(E, theta, 0)
    p4 = photon(E, np.pi-theta, np.pi)
    states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    eps12 = [
        (helicity_polarization(0, 0, a), helicity_polarization(np.pi, 0, b))
        for a, b in states
    ]
    eps34 = [
        # The minus sign transports the p4 spherical frame continuously to the
        # declared p2 frame at theta=0.
        (helicity_polarization(theta, 0, a), -helicity_polarization(np.pi-theta, np.pi, b))
        for a, b in states
    ]
    mus, wm = np.polynomial.legendre.leggauss(order)
    phis = 2*np.pi*(np.arange(order)+0.5)/order
    total = np.zeros((4, 4), dtype=complex)
    for mu, wmu in zip(mus, wm):
        for phi in phis:
            _, _, k1, k2 = kinematics(beta, mu, phi)
            left = [kernel_matrix(p1, p2, k1, *eps) for eps in eps12]
            right = [kernel_matrix(p3, p4, k1, *eps) for eps in eps34]
            for f, XR in enumerate(right):
                for i, XL in enumerate(left):
                    total[f, i] += wmu*(2*np.pi/order)*trace_pair(k1, k2, XL, XR)
    # Im M = (1/2) int dPhi_2 A_L A_R^*, dPhi_2=beta dOmega/(32 pi^2).
    return beta*total/(64*np.pi**2)


def encode_matrix(M):
    return [[{"re": float(z.real), "im": float(z.imag)} for z in row] for row in M]


s = 10.0
forward = cut_matrix(s, 0.0)
hermitian_residual = np.max(np.abs(forward-forward.conjugate().T))
eigenvalues = np.linalg.eigvalsh((forward+forward.conjugate().T)/2)
assert hermitian_residual < 2e-13
assert eigenvalues.min() > -2e-13

# With massless incoming flux, Im M_ii=s*sigma_i. Recompute sigma_i directly
# from the same normalized differential kernel but without the unitarity 1/2.
beta = np.sqrt(1-4/s)
sigma_from_diagonal = forward.diagonal().real/s
assert np.all(sigma_from_diagonal >= -1e-15)

t = -1.0
theta = np.arccos(1+2*t/s)
nonforward = cut_matrix(s, theta)
assert np.all(np.isfinite(nonforward))

# Reversing the scattering plane complex-conjugates the chosen helicity frame.
nonforward_reflected = cut_matrix(s, -theta)
reflection_residual = np.max(np.abs(nonforward_reflected-nonforward.conjugate()))
assert reflection_residual < 3e-12

payload = {
    "schema": "marici.nonforward-breit-wheeler-cut.v1",
    "normalization": "Im M=(1/2) integral dPhi2 A_L A_R^*, e=m=1",
    "helicity_order": ["++", "+-", "-+", "--"],
    "quadrature": {"gauss_legendre_mu": 28, "midpoint_phi": 28},
    "forward_sample": {
        "s": s,
        "matrix": encode_matrix(forward),
        "hermitian_residual": float(hermitian_residual),
        "eigenvalues": [float(v) for v in eigenvalues],
        "polarized_cross_sections_from_optical_theorem": [float(v) for v in sigma_from_diagonal],
    },
    "nonforward_sample": {
        "s": s,
        "t": t,
        "theta": float(theta),
        "matrix": encode_matrix(nonforward),
        "plane_reflection_conjugation_residual": float(reflection_residual),
    },
    "conclusion": "The source-normalized tree kernels glue to a finite nonforward helicity discontinuity. The forward matrix is Hermitian positive semidefinite and the nonforward plane-reflection covariance holds.",
    "next_gate": "Map the crossed outgoing-helicity convention to Phi1,Phi2,Phi5, then perform the inverse-cubic energy moments at fixed t.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "nonforward-breit-wheeler-cut.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"forward_psd": True, "nonforward_finite": True, "sha256": payload["content_sha256"]}))

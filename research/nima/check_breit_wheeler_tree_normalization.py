"""Dirac-trace Breit-Wheeler kernel with Ward and total-rate normalization gates."""

import hashlib
import json
from pathlib import Path

import mpmath as mp
import numpy as np


mp.mp.dps = 30
I2 = np.eye(2, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]])
gammas = [g0]
for sigma in (sx, sy, sz):
    gammas.append(np.block([[Z2, sigma], [-sigma, Z2]]))


def slash(v):
    return gammas[0] * v[0] - gammas[1] * v[1] - gammas[2] * v[2] - gammas[3] * v[3]


def dot(a, b):
    return a[0]*b[0] - np.dot(a[1:], b[1:])


def kernel_matrix(p1, p2, k1, eps1, eps2, mass=1.0):
    d1 = -2 * dot(k1, p1)
    d2 = -2 * dot(k1, p2)
    return (
        slash(eps1) @ (slash(k1-p1) + mass*np.eye(4)) @ slash(eps2) / d1
        + slash(eps2) @ (slash(k1-p2) + mass*np.eye(4)) @ slash(eps1) / d2
    )


def spin_sum(p1, p2, k1, k2, eps1, eps2, mass=1.0):
    X = kernel_matrix(p1, p2, k1, eps1, eps2, mass)
    Xbar = g0 @ X.conjugate().T @ g0
    return float(np.trace((slash(k1)+mass*np.eye(4)) @ X @ (slash(k2)-mass*np.eye(4)) @ Xbar).real)


def kinematics(beta, mu, phi=0.0, mass=1.0):
    E = mass / np.sqrt(1-beta**2)
    p = beta * E
    st = np.sqrt(max(0.0, 1-mu**2))
    p1 = np.array([E, 0, 0, E], dtype=float)
    p2 = np.array([E, 0, 0, -E], dtype=float)
    k1 = np.array([E, p*st*np.cos(phi), p*st*np.sin(phi), p*mu], dtype=float)
    k2 = np.array([E, -k1[1], -k1[2], -k1[3]], dtype=float)
    return p1, p2, k1, k2


def unpolarized_msq(beta, mu):
    p1, p2, k1, k2 = kinematics(beta, mu)
    ex = np.array([0, 1, 0, 0], dtype=float)
    ey = np.array([0, 0, 1, 0], dtype=float)
    return sum(spin_sum(p1, p2, k1, k2, e1, e2) for e1 in (ex, ey) for e2 in (ex, ey)) / 4


def numerical_sigma(beta):
    mass = mp.mpf(1)
    s = 4*mass**2/(1-mp.mpf(beta)**2)
    angular = 2*mp.pi*mp.quad(lambda z: unpolarized_msq(float(beta), float(z)), [-1, 0, 1])
    return mp.mpf(beta) * angular / (64*mp.pi**2*s)


def exact_sigma(beta):
    # e=1 in the trace kernel, hence alpha=e^2/(4*pi)=1/(4*pi).
    b = mp.mpf(beta)
    alpha = 1/(4*mp.pi)
    return (mp.pi*alpha**2/2) * (1-b**2) * ((3-b**4)*mp.log((1+b)/(1-b)) - 2*b*(2-b**2))


ward_rows = []
for beta, mu in ((0.3, -0.4), (0.7, 0.2)):
    p1, p2, k1, k2 = kinematics(beta, mu)
    ey = np.array([0, 0, 1, 0], dtype=float)
    w1 = spin_sum(p1, p2, k1, k2, p1, ey)
    w2 = spin_sum(p1, p2, k1, k2, ey, p2)
    assert abs(w1) < 1e-12 and abs(w2) < 1e-12
    ward_rows.append({"beta": beta, "mu": mu, "replace_eps1_by_p1": w1, "replace_eps2_by_p2": w2})

rate_rows = []
for beta in (mp.mpf("0.2"), mp.mpf("0.6"), mp.mpf("0.9")):
    got = numerical_sigma(beta)
    want = exact_sigma(beta)
    rel = abs((got-want)/want)
    assert rel < mp.mpf("2e-12")
    rate_rows.append({"beta": str(beta), "numerical": str(got), "analytic": str(want), "relative_error": str(rel)})

payload = {
    "schema": "marici.breit-wheeler-tree-normalization.v1",
    "conventions": "metric +---; m=1; e=1; incoming photon average 1/4; dSigma/dOmega=beta |M|^2/(64 pi^2 s)",
    "ward_checks": ward_rows,
    "total_rate_checks": rate_rows,
    "conclusion": "The Dirac-trace tree kernel satisfies both photon Ward identities and reproduces the analytic unpolarized Breit-Wheeler total cross section.",
    "next_use": "Source-normalized integrand for the nonforward two-particle Cutkosky phase-space pairing.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "breit-wheeler-tree-normalization.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"ward": True, "rates": True, "sha256": payload["content_sha256"]}))

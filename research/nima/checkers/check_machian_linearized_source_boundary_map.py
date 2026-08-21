#!/usr/bin/env python3
"""Exact linearized Einstein source/boundary decomposition."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

ETA = (-1, 1, 1, 1)


def dot(a, b):
    return sum((ETA[i] * a[i] * b[i] for i in range(4)), Fraction(0))


def lower(v):
    return tuple(ETA[i] * v[i] for i in range(4))


def outer(a, b):
    return tuple(tuple(a[i] * b[j] for j in range(4)) for i in range(4))


def madd(*matrices):
    return tuple(tuple(sum((m[i][j] for m in matrices), Fraction(0))
                       for j in range(4)) for i in range(4))


def mscale(c, matrix):
    return tuple(tuple(c * matrix[i][j] for j in range(4)) for i in range(4))


def trace_cov(matrix):
    return sum((ETA[i] * matrix[i][i] for i in range(4)), Fraction(0))


def trace_reverse_inverse(hbar):
    tr = trace_cov(hbar)
    return tuple(tuple(hbar[i][j] - (ETA[i] if i == j else 0) * tr / 2
                       for j in range(4)) for i in range(4))


def divergence_cov(k_contra, matrix_cov):
    return tuple(sum((k_contra[mu] * matrix_cov[mu][nu] for mu in range(4)),
                     Fraction(0)) for nu in range(4))


def gauge_delta(k_cov, xi_cov):
    return tuple(tuple(k_cov[mu] * xi_cov[nu] + k_cov[nu] * xi_cov[mu]
                       for nu in range(4)) for mu in range(4))


def fourier_riemann(h, k_cov):
    # Overall Fourier sign is conventional and irrelevant to the tests.
    return tuple(tuple(tuple(tuple(
        (
            -k_cov[rho] * k_cov[nu] * h[mu][sig]
            -k_cov[sig] * k_cov[mu] * h[nu][rho]
            +k_cov[sig] * k_cov[nu] * h[mu][rho]
            +k_cov[rho] * k_cov[mu] * h[nu][sig]
        ) / 2
        for sig in range(4)) for rho in range(4)) for nu in range(4)) for mu in range(4))


def tensor_equal(a, b):
    return a == b


def tensor_nonzero(a):
    return any(a[mu][nu][rho][sig] != 0
               for mu in range(4) for nu in range(4)
               for rho in range(4) for sig in range(4))


# Off-shell Fourier source mode: k^2 != 0.
k = (Fraction(0), Fraction(1), Fraction(2), Fraction(0))
k2 = dot(k, k)
assert k2 == 5
e = (Fraction(0), Fraction(2), Fraction(-1), Fraction(0))
t = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
z = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))
source = madd(outer(e, e), mscale(Fraction(2), outer(t, t)), outer(z, z))
assert divergence_cov(k, source) == (0, 0, 0, 0)

# Harmonic-gauge particular solution; the omitted 16 pi G is a common scale.
hbar = mscale(Fraction(1, 5), source)
assert divergence_cov(k, hbar) == (0, 0, 0, 0)
h = trace_reverse_inverse(hbar)
r_source = fourier_riemann(h, lower(k))
assert tensor_nonzero(r_source)

# Pure gauge changes h but not the curvature.
xi = (Fraction(3), Fraction(-2), Fraction(5), Fraction(7))
hg = madd(h, gauge_delta(lower(k), xi))
assert tensor_equal(fourier_riemann(hg, lower(k)), r_source)

# Independent homogeneous radiative data: q^2=0, TT, nonzero curvature.
q = (Fraction(1), Fraction(0), Fraction(0), Fraction(1))
assert dot(q, q) == 0
wave = (
    (0, 0, 0, 0),
    (0, Fraction(1), 0, 0),
    (0, 0, Fraction(-1), 0),
    (0, 0, 0, 0),
)
assert divergence_cov(q, wave) == (0, 0, 0, 0)
assert trace_cov(wave) == 0
r_wave = fourier_riemann(wave, lower(q))
assert tensor_nonzero(r_wave)

packet = {
    "schema": "marici.machian-linearized-source-boundary.v1",
    "status": "pass",
    "claims": {
        "conserved_source": "k^mu T_mu_nu=0 gives a harmonic-compatible particular solution",
        "gauge_descent": "adding k_(mu xi_nu) leaves linearized curvature unchanged",
        "boundary_independence": "a source-free null TT mode has nonzero curvature",
        "conclusion": "T_mu_nu alone does not determine local curvature; radiative boundary/homogeneous data is independent input",
        "scope": "linearized Fourier-mode theorem packet; nonlinear Einstein localization remains open",
    },
    "source_k_squared": str(k2),
    "source_curvature_nonzero": True,
    "homogeneous_wave_q_squared": str(dot(q, q)),
    "homogeneous_curvature_nonzero": True,
}
canonical = json.dumps(packet, indent=2, sort_keys=True) + "\n"
packet["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
out = Path(__file__).resolve().parents[1] / "results" / "machian-linearized-source-boundary.json"
out.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"passed": True, "output": str(out)}))

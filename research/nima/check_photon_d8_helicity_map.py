"""Exact dimension-eight photon EFT operator-to-helicity map.

The checker expands the two quartic field-strength operators multilinearly,
uses physical COM helicity vectors, and verifies Ward, Bose/parity data and
the source-normalized helicity ratios. Overall S-matrix normalization is fixed
by Phi1 = g2*s^2.
"""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

c, h, g2, f2 = sp.symbols("c h g2 f2", real=True)
I = sp.I
sqrt2 = sp.sqrt(2)
eta = sp.diag(1, -1, -1, -1)


def dot4(a, b):
    return (a.T * eta * b)[0]


def pol(e_theta, e_phi, helicity):
    spatial = (e_theta + I * helicity * e_phi) / sqrt2
    return sp.Matrix([0, spatial[0], spatial[1], spatial[2]])


def field_strength(k, eps):
    # Covariant antisymmetric tensor F_{mu nu}.
    kc = eta * k
    ec = eta * eps
    return kc * ec.T - ec * kc.T


def raise2(F):
    return eta * F * eta


def contract(F, G):
    return sp.simplify(sum(F[i, j] * raise2(G)[i, j] for i in range(4) for j in range(4)))


def dual_upper(F):
    # tilde F^{mu nu} = 1/2 epsilon^{mu nu rho sigma} F_{rho sigma}, epsilon^{0123}=+1.
    out = sp.zeros(4)
    for mu, nu, rho, sig in itertools.product(range(4), repeat=4):
        out[mu, nu] += sp.LeviCivita(mu, nu, rho, sig) * F[rho, sig] / 2
    return out


def pseudo_contract(F, G):
    dG = dual_upper(G)
    return sp.simplify(sum(F[i, j] * dG[i, j] for i in range(4) for j in range(4)))


def quartic(Fs):
    pairings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    ss = sum(contract(Fs[a], Fs[b]) * contract(Fs[d], Fs[e]) for (a, b), (d, e) in pairings)
    pp = sum(pseudo_contract(Fs[a], Fs[b]) * pseudo_contract(Fs[d], Fs[e]) for (a, b), (d, e) in pairings)
    # Multilinear coefficient of the declared L8 operators.
    return sp.simplify((g2 + f2) * ss / 2 + (g2 - f2) * pp / 2)


# Physical momenta, E=1; outgoing legs are crossed into the all-incoming tensor.
p1 = sp.Matrix([1, 0, 0, 1])
p2 = sp.Matrix([1, 0, 0, -1])
p3 = sp.Matrix([1, h, 0, c])
p4 = sp.Matrix([1, -h, 0, -c])
ks = [p1, p2, -p3, -p4]

ex, ey = sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0])
eth = sp.Matrix([c, 0, -h])
emth = sp.Matrix([c, 0, -h])

def eps_physical(leg, helicity):
    if leg == 0:
        return pol(ex, ey, helicity)
    if leg == 1:
        return pol(-ex, ey, helicity)
    if leg == 2:
        return sp.conjugate(pol(eth, ey, helicity))
    return sp.conjugate(pol(emth, -ey, helicity))


def amplitude(hs):
    Fs = [field_strength(ks[i], eps_physical(i, hs[i])) for i in range(4)]
    return sp.factor(quartic(Fs).subs(h**2, 1-c**2))


amps = {"".join("+" if q == 1 else "-" for q in hs): amplitude(hs) for hs in itertools.product((1, -1), repeat=4)}

# Fix the common contact normalization against source Phi1=g2*s^2, s=4.
raw_phi1 = amps["++++"]
normalizer = sp.simplify(16 * g2 / raw_phi1)
normalized = {name: sp.factor(value * normalizer) for name, value in amps.items()}

smand = sp.Integer(4)
tmand = sp.simplify(-2 * (1-c))
umand = sp.simplify(-2 * (1+c))
expected_phi1 = g2 * smand**2
expected_phi2 = sp.expand(f2 * (smand**2 + tmand**2 + umand**2))

# Ward tests replace one polarization by its crossed momentum.
ward = []
for leg in range(4):
    eps = [eps_physical(i, 1) for i in range(4)]
    eps[leg] = ks[leg]
    ward.append(sp.simplify(quartic([field_strength(ks[i], eps[i]) for i in range(4)])))

residuals = {
    "Phi1": sp.simplify(normalized["++++"] - expected_phi1),
    "Phi2": sp.simplify(normalized["++--"] - expected_phi2),
    "Phi5_left": sp.simplify(normalized["+++-"]),
    "Phi5_right": sp.simplify(normalized["++-+"]),
    "parity_Phi1": sp.simplify(normalized["++++"] - normalized["----"]),
    "parity_Phi2": sp.simplify(normalized["++--"] - normalized["--++"]),
    "mixed_exchange": sp.simplify(normalized["+++-"] - normalized["++-+"]),
}

payload = {
    "schema": "marici.photon-d8-helicity-map.v1",
    "strength": "exact quartic field-strength contraction",
    "lagrangian": "(g2+f2)/16*(F.F)^2 + (g2-f2)/16*(F.Fdual)^2",
    "mandelstam": {"s": str(smand), "t": str(tmand), "u": str(umand)},
    "raw_phi1": str(raw_phi1),
    "source_normalizer": str(normalizer),
    "normalized_fixed_incoming_pp": {
        "Phi1": str(normalized["++++"]),
        "Phi5_left": str(normalized["+++-"]),
        "Phi5_right": str(normalized["++-+"]),
        "Phi2": str(normalized["++--"]),
    },
    "expected": {"Phi1": str(expected_phi1), "Phi2": str(expected_phi2), "Phi5": "0"},
    "ward_residuals": [str(v) for v in ward],
    "symmetry_and_source_residuals": {k: str(v) for k, v in residuals.items()},
    "coefficient_plane_rank": 2,
    "marici_typing": "two-dimensional parity-even quartic Ward-cohomology coefficient fiber; no canonical ray is supplied by the current carrier packet",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "photon-d8-helicity-map.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

assert all(v == 0 for v in ward)
assert all(v == 0 for v in residuals.values())
print(json.dumps({"ward": True, "symmetry": True, "source_map": True, "sha256": payload["content_sha256"]}))

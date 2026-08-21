"""Power audit of every one-loop QED helicity prefactor at fixed spacelike t."""

import hashlib
import json
from pathlib import Path

import sympy as sp


S, tau = sp.symbols("S tau", positive=True)
xs, xt, xu = S, -tau, -S + tau

def degree_at_infinity(expr):
    num, den = [sp.Poly(q, S) for q in sp.fraction(sp.cancel(expr))]
    return sp.Rational(num.degree() - den.degree())

def root2_poly(x):
    return sp.expand(x * (x - 4))

def root3_poly(i, j, k):
    return sp.expand(i * j * (i * j + 4 * k))

def root_degree(poly):
    return sp.Rational(sp.Poly(poly, S).degree(), 2)

def r8(i, j, k):
    return 2 * (i * j + 2 * k) / k

def r9(i, j, k):
    return (i - 4) * (i - j) / k

def r10(i, j, k):
    return 1 - 4 / i - 2 * j * k / i**2

def r11(i, j, k):
    return 4 - 2 * i - j * k + 2 * j * k * (j * k + 4 * i) / i**2

triples = [(xs, xt, xu), (xt, xu, xs), (xu, xs, xt)]
rows = []

def add(name, rational, root_poly=None):
    rational_degree = degree_at_infinity(rational)
    rd = root_degree(root_poly) if root_poly is not None else sp.Integer(0)
    net = sp.simplify(rational_degree - rd)
    rows.append({"term": name, "rational_degree": str(rational_degree), "root_degree": str(rd), "net_power": str(net)})
    assert net <= 0

# M++++: one f6/root3 for each labelled permutation.
for idx, tri in enumerate(triples):
    add(f"M++++ f6 permutation {idx}", 1, root3_poly(*tri))

# M-+++: the common f4 coefficient and each r8*f6/root3 term.
add("M-+++ sum_f4", 2 * (1/xs + 1/xt + 1/xu))
for idx, tri in enumerate(triples):
    add(f"M-+++ r8 f6 permutation {idx}", r8(*tri), root3_poly(*tri))

# M--++ terms in the exact representation.
add("M--++ r9(t,u,s) f2/root2(t)", r9(xt, xu, xs), root2_poly(xt))
add("M--++ r9(u,t,s) f2/root2(u)", r9(xu, xt, xs), root2_poly(xu))
add("M--++ r10 f4", r10(xs, xt, xu))
add("M--++ (s-2) f6/root3(s,t,u)", 2*(xs-2), root3_poly(xs, xt, xu))
add("M--++ (s-2) f6/root3(u,s,t)", 2*(xs-2), root3_poly(xu, xs, xt))
add("M--++ r11 f6/root3(t,u,s)", r11(xs, xt, xu), root3_poly(xt, xu, xs))

max_power = max(sp.Rational(r["net_power"]) for r in rows)
assert max_power == 0

payload = {
    "schema": "marici.qed-fixed-t-subtraction-gate.v1",
    "limit": "s=S->infinity, t=-tau fixed, u=-S+tau",
    "prefactor_audit": rows,
    "maximum_net_power": str(max_power),
    "master_growth": "The one-loop master basis has GPL weight at most two; its large-argument growth is at most logarithm squared after analytic continuation.",
    "amplitude_bound": "M_lambda=O(log^2|nu|) at fixed spacelike t in the explicit one-loop representation.",
    "contour_consequence": "M_lambda/nu^3 has a vanishing large-circle contribution, so the nu^2 Taylor coefficient has no independent subtraction polynomial at one loop.",
    "scope": "One-loop massive-fermion QED helicity amplitudes. This does not automatically establish the same bound nonperturbatively or at arbitrary loop order.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
out = Path(__file__).parent / "results" / "qed-fixed-t-subtraction-gate.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"maximum_net_power": str(max_power), "sha256": payload["content_sha256"]}))

"""Swapped orbit-3 Gram criterion at the source central flavor point.

The down support is anti-diagonal, so work in the down-mass basis.  The up
support is the six-link zero-diagonal texture.  Its necessary-and-sufficient
Gram inequality is the same intrinsic scalar criterion as the original
orientation, now applied to H_u = V^dagger diag(y_u^2,y_c^2,y_t^2) V.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 80

A, B, C, p, q, r, y = sp.symbols("A B C p q r y", positive=True)
f = r/(B-p/y) + q/(A-y)
f_min = sp.factor((r*A + q*B + 2*sp.sqrt(p*q*r))/(A*B-p))
y_star = sp.factor((sp.sqrt(r*p)*A + sp.sqrt(q)*p) /
                   (sp.sqrt(q)*B + sp.sqrt(r*p)))
assert sp.simplify(sp.diff(f, y).subs(y, y_star)) == 0
assert sp.simplify(f.subs(y, y_star)-f_min) == 0

Vus, Vub, Vcb = map(mp.mpf, ["0.22517", "0.003763", "0.04189"])
beta_target = mp.radians(mp.mpf("22.6"))
yu, yc, yt = map(mp.mpf, ["7.04e-6", "3.56e-3", "0.967"])
c13 = mp.sqrt(1-Vub**2)
s13 = Vub
s12 = Vus/c13
s23 = Vcb/c13
c12 = mp.sqrt(1-s12**2)
c23 = mp.sqrt(1-s23**2)


def ckm(delta):
    ep, em = mp.e**(1j*delta), mp.e**(-1j*delta)
    return mp.matrix([
        [c12*c13, s12*c13, s13*em],
        [-s12*c23-c12*s23*s13*ep,
         c12*c23-s12*s23*s13*ep, s23*c13],
        [s12*s23-c12*c23*s13*ep,
         -c12*s23-s12*c23*s13*ep, c23*c13],
    ])


def beta(delta):
    V = ckm(delta)
    return mp.arg(-(V[1,0]*mp.conj(V[1,2])) /
                  (V[2,0]*mp.conj(V[2,2])))


def scalar_data(H):
    return (mp.re(H[0,0]), mp.re(H[1,1]), mp.re(H[2,2]),
            abs(H[0,1])**2, abs(H[0,2])**2, abs(H[1,2])**2)


def gap(vals):
    aa, bb, cc, pp, qq, rr = vals
    if not pp/bb < aa:
        return mp.inf
    return (rr*aa+qq*bb+2*mp.sqrt(pp*qq*rr))/(aa*bb-pp)-cc


delta = mp.findroot(lambda d: beta(d)-beta_target,
                    (mp.mpf("1.0"), mp.mpf("1.4")))
V = ckm(delta)
H0 = V.transpose_conj()*mp.diag([yu**2, yc**2, yt**2])*V

audits = []
for perm in itertools.permutations(range(3)):
    H = mp.matrix(3)
    for i in range(3):
        for j in range(3):
            H[i,j] = H0[perm[i],perm[j]]
    vals = scalar_data(H)
    g = gap(vals)
    audits.append({
        "down_basis_permutation": list(perm),
        "minimum_minus_C": mp.nstr(g, 30),
        "relative_gap": mp.nstr(g/vals[2], 30),
        "criterion_satisfied": bool(g <= 0),
    })

out = {
    "schema": "marici.flavor.wp10_swapped_orbit3_gram_criterion.v1",
    "status": "proved_symbolic_reduction_high_precision_central_audit",
    "masks": {"u": 238, "d": 84},
    "physical_gram": "V^dagger diag(yu^2,yc^2,yt^2) V",
    "closed_realisability_inequality":
        "C*(A*B-p) >= r*A+q*B+2*sqrt(p*q*r)",
    "central_reconstruction": {
        "delta_radians": mp.nstr(delta, 30),
        "beta_radians": mp.nstr(beta(delta), 30),
    },
    "basis_label_audits": audits,
    "any_label_satisfies": any(a["criterion_satisfied"] for a in audits),
    "conclusion":
        "swapped orbit 3 is excluded at the source central flavor point iff all gaps are positive",
}
Path("research/flavor/results/wp10_swapped_orbit3_gram_criterion.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))

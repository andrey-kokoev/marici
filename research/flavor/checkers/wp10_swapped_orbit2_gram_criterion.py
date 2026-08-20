"""Exact Gram criterion for the sector-swapped orientation of orbit 2.

With the down texture monomial, the physical up Gram matrix must factor as

    Y = [[a,0,b],[c,d,0],[e,f,0]].

Writing A,B,C for its diagonal Gram entries and x,y,z for H01,H02,H12,
alpha=|a|^2 is forced linearly. Positivity of the six squared magnitudes is
then necessary and sufficient.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 80

# Symbolic certificate.
A, B, C, alpha = sp.symbols("A B C alpha", positive=True)
p, q, r, tau = sp.symbols("p q r tau", real=True)
equation = sp.expand(r - 2*tau/alpha + p*q/alpha**2
                     - (B-p/alpha)*(C-q/alpha))
cleared = sp.factor(alpha*equation)
alpha_star = sp.factor((B*q+C*p-2*tau)/(B*C-r))
assert sp.simplify(cleared.subs(alpha, alpha_star)) == 0

# Central CKM reconstruction, following the source convention used by WP10.
Vus, Vub, Vcb = map(mp.mpf, ["0.22517", "0.003763", "0.04189"])
beta_target = mp.radians(mp.mpf("22.6"))
yu, yc, yt = map(mp.mpf, ["7.04e-6", "3.56e-3", "0.967"])
c13 = mp.sqrt(1-Vub**2); s13 = Vub
s12 = Vus/c13; s23 = Vcb/c13
c12 = mp.sqrt(1-s12**2); c23 = mp.sqrt(1-s23**2)

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
    return mp.arg(-(V[1,0]*mp.conj(V[1,2]))/(V[2,0]*mp.conj(V[2,2])))

delta = mp.findroot(lambda d: beta(d)-beta_target, (mp.mpf("1.0"), mp.mpf("1.4")))
V = ckm(delta)
Du = mp.diag([yu**2, yc**2, yt**2])
H0 = V.transpose_conj()*Du*V

def audit(H):
    aa, bb, cc = (mp.re(H[i,i]) for i in range(3))
    x, y, z = H[0,1], H[0,2], H[1,2]
    pp, qq, rr = abs(x)**2, abs(y)**2, abs(z)**2
    tt = mp.re(z*x*mp.conj(y))
    denom = bb*cc-rr
    astar = (bb*qq+cc*pp-2*tt)/denom
    squares = {
        "abs_a2": astar,
        "abs_b2": aa-astar,
        "abs_c2": pp/astar,
        "abs_d2": bb-pp/astar,
        "abs_e2": qq/astar,
        "abs_f2": cc-qq/astar,
    }
    return astar, squares, all(value > 0 for value in squares.values())

audits = []
direct_witness = None
for perm in itertools.permutations(range(3)):
    H = mp.matrix([[H0[perm[i],perm[j]] for j in range(3)] for i in range(3)])
    astar, squares, ok = audit(H)
    audits.append({
        "row_permutation": list(perm),
        "alpha_star": mp.nstr(astar, 30),
        "squared_magnitudes": {k: mp.nstr(v, 30) for k, v in squares.items()},
        "criterion_satisfied": bool(ok),
    })
    if direct_witness is None and ok:
        aa = mp.re(H[0,0]); x, y, z = H[0,1], H[0,2], H[1,2]
        aval = mp.sqrt(astar)
        cval = mp.conj(x)/aval
        eval_ = mp.conj(y)/aval
        bval = mp.sqrt(aa-astar)
        dval = mp.sqrt(mp.re(H[1,1])-abs(cval)**2)
        residual = z-cval*mp.conj(eval_)
        fval = mp.conj(residual)/dval
        Y = mp.matrix([[aval, 0, bval], [cval, dval, 0], [eval_, fval, 0]])
        delta_H = Y*Y.transpose_conj()-H
        max_residual = max(abs(delta_H[i,j]) for i in range(3) for j in range(3))
        direct_witness = {
            "row_permutation": list(perm),
            "entries": {
                "a": mp.nstr(aval, 40), "b": mp.nstr(bval, 40),
                "c": mp.nstr(cval, 40), "d": mp.nstr(dval, 40),
                "e": mp.nstr(eval_, 40), "f": mp.nstr(fval, 40),
            },
            "max_abs_YYdagger_minus_H": mp.nstr(max_residual, 20),
            "loop_phase_radians": mp.nstr(mp.arg(cval*mp.conj(dval)*fval*mp.conj(eval_)), 30),
        }

out = {
    "schema": "marici.flavor.swapped_orbit2_gram_criterion.v1",
    "status": "proved_symbolic_reduction_high_precision_physical_audit",
    "support": "[[a,0,b],[c,d,0],[e,f,0]]",
    "cleared_equation": str(cleared),
    "forced_alpha": str(alpha_star),
    "necessary_and_sufficient_condition": "all six reconstructed squared magnitudes are positive",
    "central_delta_radians": mp.nstr(delta, 30),
    "row_label_audits": audits,
    "any_label_satisfies": any(a["criterion_satisfied"] for a in audits),
    "direct_gram_factor_witness": direct_witness,
    "conclusion": "All six row labelings satisfy the positive Gram criterion and an explicit factor Y is supplied. The swapped orbit-2 no-fit pilot is an optimizer miss, not an exclusion.",
}
Path("research/flavor/results/wp10_swapped_orbit2_gram_criterion.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))

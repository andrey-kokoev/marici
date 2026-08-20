"""Orbit-3 exact Gram criterion and high-precision physical-point audit.

For Y=[[0,a,b],[c,0,d],[e,f,0]], write
 A=H00=x+y, B=H11=z+w, C=H22=v+t,
 p=|H01|^2=y*w, q=|H02|^2=x*t, r=|H12|^2=z*v.
Eliminating x,z,w,v,t leaves
 C = r/(B-p/y) + q/(A-y), p/B < y < A.
This is necessary and sufficient for positive entry magnitudes.  We derive
the scalar reduction symbolically and test every row labeling at the source
central CKM point with high precision.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 80

# Exact symbolic elimination certificate.
A, B, C, p, q, r, y = sp.symbols("A B C p q r y", positive=True)
x = A - y
w = p / y
z = B - w
t = q / x
v = r / z
criterion = sp.factor(v + t - C)
cleared = sp.factor(criterion * y * (A-y) * (B*y-p))
assert sp.simplify(criterion - (r/(B-p/y) + q/(A-y) - C)) == 0
f = r/(B-p/y) + q/(A-y)
f_second = sp.factor(sp.diff(f, y, 2))
f_second_positive = 2*r*p*B/(B*y-p)**3 + 2*q/(A-y)**3
assert sp.simplify(f_second-f_second_positive) == 0
alpha, beta_s = sp.sqrt(r*p), sp.sqrt(q)
y_star = sp.factor((alpha*A + beta_s*p)/(beta_s*B + alpha))
f_min_closed = sp.factor((r*A + q*B + 2*sp.sqrt(p*q*r))/(A*B-p))
assert sp.simplify(sp.diff(f, y).subs(y, y_star)) == 0
assert sp.simplify(f.subs(y, y_star) - f_min_closed) == 0

# Central CKM reconstruction.  The three quoted magnitudes set the PDG
# angles; delta is fixed by the quoted beta through its invariant quartet.
Vus = mp.mpf("0.22517")
Vub = mp.mpf("0.003763")
Vcb = mp.mpf("0.04189")
beta_target = mp.radians(mp.mpf("22.6"))
yd, ys, yb = map(mp.mpf, ["1.54e-5", "3.06e-4", "1.630e-2"])
c13 = mp.sqrt(1-Vub**2)
s13 = Vub
s12 = Vus/c13
s23 = Vcb/c13
c12 = mp.sqrt(1-s12**2)
c23 = mp.sqrt(1-s23**2)


def ckm(delta):
    epos, eneg = mp.e**(1j*delta), mp.e**(-1j*delta)
    return mp.matrix([
        [c12*c13, s12*c13, s13*eneg],
        [-s12*c23-c12*s23*s13*epos,
         c12*c23-s12*s23*s13*epos, s23*c13],
        [s12*s23-c12*c23*s13*epos,
         -c12*s23-s12*c23*s13*epos, c23*c13],
    ])


def beta(delta):
    V = ckm(delta)
    return mp.arg(-(V[1,0]*mp.conj(V[1,2]))/(V[2,0]*mp.conj(V[2,2])))


delta = mp.findroot(lambda d: beta(d)-beta_target, (mp.mpf("1.0"), mp.mpf("1.4")))
V = ckm(delta)
D = mp.diag([yd**2, ys**2, yb**2])
H0 = V*D*V.transpose_conj()


def scalar_data(H):
    return (mp.re(H[0,0]), mp.re(H[1,1]), mp.re(H[2,2]),
            abs(H[0,1])**2, abs(H[0,2])**2, abs(H[1,2])**2)


def fmin_gap(vals):
    aa, bb, cc, pp, qq, rr = vals
    lo, hi = pp/bb, aa
    if not lo < hi:
        return mp.inf, None
    root_rp, root_q = mp.sqrt(rr*pp), mp.sqrt(qq)
    xm = (root_rp*aa + root_q*pp)/(root_q*bb + root_rp)
    closed_min = (rr*aa + qq*bb + 2*mp.sqrt(pp*qq*rr))/(aa*bb-pp)
    return closed_min-cc, xm


audits = []
for perm in itertools.permutations(range(3)):
    H = mp.matrix(3)
    for i in range(3):
        for j in range(3):
            H[i,j] = H0[perm[i],perm[j]]
    vals = scalar_data(H)
    gap, ymin = fmin_gap(vals)
    audits.append({
        "row_permutation": list(perm),
        "minimum_minus_C": mp.nstr(gap, 30),
        "relative_gap": mp.nstr(gap/vals[2], 30),
        "criterion_satisfied": bool(gap <= 0),
        "minimizer_y": None if ymin is None else mp.nstr(ymin, 30),
    })

out = {
    "schema": "marici.flavor.orbit3_gram_criterion.v1",
    "status": "proved_symbolic_reduction_high_precision_physical_audit",
    "cleared_scalar_polynomial": str(cleared),
    "strict_convexity_second_derivative": "2*r*p*B/(B*y-p)^3 + 2*q/(A-y)^3 > 0 on p/B<y<A",
    "unique_minimizer": str(y_star),
    "closed_minimum": str(f_min_closed),
    "closed_realisability_inequality": "C*(A*B-p) >= r*A+q*B+2*sqrt(p*q*r)",
    "central_reconstruction": {
        "delta_radians": mp.nstr(delta, 30),
        "beta_radians": mp.nstr(beta(delta), 30),
    },
    "row_label_audits": audits,
    "any_label_satisfies": any(a["criterion_satisfied"] for a in audits),
    "conclusion": "zero-diagonal down texture is excluded at the central point iff every minimum_minus_C is positive",
}
target = Path("research/flavor/results/wp10_orbit3_gram_criterion.json")
target.write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))

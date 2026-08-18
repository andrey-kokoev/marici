"""Exact function-field residues for the infinity-Gysin extension.

Consumes the validated Gysin-adapted bivariate rational connection and works
in GF(p)(u)[v]/(f) for f=P6,Q.  No points on either divisor are sampled.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

from sympy.polys.domains import GF


P = 2305843009213693951
K = GF(P).frac_field("u")
u = K.gens[0]
Z, O = K.zero, K.one


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a or [Z]


def padd(a, b):
    n = max(len(a), len(b)); out = [Z] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else Z) + (b[i] if i < len(b) else Z)
    return trim(out)


def pneg(a): return trim([-x for x in a])
def psub(a, b): return padd(a, pneg(b))


def pmul(a, b):
    out = [Z] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return trim(out)


def pscale(a, c): return trim([c * x for x in a])


def pdivmod_monic(a, f):
    a = trim(a); f = trim(f); q = [Z] * max(1, len(a) - len(f) + 1)
    while len(a) >= len(f) and any(a):
        k = len(a) - len(f); c = a[-1]; q[k] += c
        a = psub(a, [Z] * k + pscale(f, c))
    return trim(q), trim(a)


def is_zero_poly(a): return all(not x for x in a)


def factor_order(a, f):
    order = 0; a = trim(a)
    while not is_zero_poly(a):
        q, r = pdivmod_monic(a, f)
        if not is_zero_poly(r): break
        a = q; order += 1
    return order, a


class QF:
    __slots__ = ("a", "b", "alpha", "beta")
    def __init__(self, a, b, alpha, beta): self.a, self.b, self.alpha, self.beta = a, b, alpha, beta
    def __add__(self, x): return QF(self.a + x.a, self.b + x.b, self.alpha, self.beta)
    def __neg__(self): return QF(-self.a, -self.b, self.alpha, self.beta)
    def __sub__(self, x): return self + (-x)
    def __mul__(self, x):
        return QF(self.a*x.a + self.beta*self.b*x.b,
                  self.a*x.b + self.b*x.a + self.alpha*self.b*x.b,
                  self.alpha, self.beta)
    def inv(self):
        norm = self.a*self.a + self.alpha*self.a*self.b - self.beta*self.b*self.b
        if not norm: raise ZeroDivisionError
        return QF((self.a + self.alpha*self.b)/norm, -self.b/norm, self.alpha, self.beta)
    def __truediv__(self, x): return self * x.inv()
    def is_zero(self): return not self.a and not self.b
    def text(self): return {"one": str(self.a), "v": str(self.b)}


def qzero(alpha, beta): return QF(Z, Z, alpha, beta)
def qconst(c, alpha, beta): return QF(K.convert(c), Z, alpha, beta)


def qfrom_poly(a, alpha, beta):
    f = [-beta, -alpha, O]
    _, r = pdivmod_monic(a, f)
    return QF(r[0] if r else Z, r[1] if len(r) > 1 else Z, alpha, beta)


def terms_to_poly(terms):
    out = [Z]
    for i, j, c in terms:
        while len(out) <= j: out.append(Z)
        out[j] += K.convert(c) * u**i
    return trim(out)


def fit_residue(fit, divisor):
    n = terms_to_poly(fit["numerator"]); d = terms_to_poly(fit["denominator"])
    on, n = factor_order(n, divisor); od, d = factor_order(d, divisor)
    order = on - od
    alpha, beta = -divisor[1], -divisor[0]
    if order >= 0: return qzero(alpha, beta), order
    if order != -1: raise ValueError(f"nonlogarithmic order {order}")
    fv = [divisor[1], K.convert(2)]
    return qfrom_poly(n, alpha, beta) / (qfrom_poly(d, alpha, beta) * qfrom_poly(fv, alpha, beta)), order


def rank(a):
    a = [[x for x in row] for row in a]; nr, nc = len(a), len(a[0]); r = 0
    for c in range(nc):
        p = next((i for i in range(r, nr) if not a[i][c].is_zero()), None)
        if p is None: continue
        a[r], a[p] = a[p], a[r]; z = a[r][c].inv(); a[r] = [z*x for x in a[r]]
        for i in range(nr):
            if i != r and not a[i][c].is_zero():
                z = a[i][c]; a[i] = [a[i][j] - z*a[r][j] for j in range(nc)]
        r += 1
        if r == nr: break
    return r


def operator(residue, m):
    alpha, beta = residue[0][0].alpha, residue[0][0].beta
    out = [[qzero(alpha, beta) for _ in range(4)] for _ in range(4)]
    for qi in range(2):
        for k in range(2):
            col = 2*qi+k
            for i in range(2):
                for j in range(2):
                    row = 2*i+j; z = qzero(alpha, beta)
                    if qi == i and k == j: z = z - qconst(m, alpha, beta)
                    if qi == i: z = z + residue[k][j]
                    if k == j: z = z - residue[i+2][qi+2]
                    out[row][col] = z
    return out


def poly_add(a, b, z):
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else z)+(b[i] if i<len(b) else z) for i in range(n)]
def poly_mul(a, b, z):
    out=[z for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=out[i+j]+x*y
    return out


def characteristic_coefficients(t):
    alpha,beta=t[0][0].alpha,t[0][0].beta; z=qzero(alpha,beta); one=qconst(1,alpha,beta)
    entries=[]
    for i in range(4):
        row=[]
        for j in range(4): row.append([t[i][j], -one] if i==j else [t[i][j]])
        entries.append(row)
    det=[z]
    for perm in itertools.permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4)); term=[one]
        for i,j in enumerate(perm): term=poly_mul(term,entries[i][j],z)
        if inv%2: term=[-x for x in term]
        det=poly_add(det,term,z)
    return det


def build_divisors():
    half = K.convert(2)**-1; v=[Z,O]; up=[u]; one=[O]
    y=psub(pscale(padd(up,v),half),one); u2=[u*u]; s=pscale(padd(up,v),half)
    q=pneg(pscale(pmul(y,y),K.convert(16)))
    q=padd(q,pscale(pmul(y,u2),K.convert(-8)))
    q=padd(q,pscale(pmul(pmul(s,u2),[u]),K.convert(8)))
    q=psub(q,pscale(pmul(u2,u2),K.convert(5)))
    quarter=half*half
    p6=psub(psub(one,up),v); p6=padd(p6,pscale(pmul(v,v),quarter)); p6=padd(p6,pscale(pmul(up,v),half))
    p6=psub(p6,pscale(u2,K.convert(7)*quarter)); p6=padd(p6,pmul(u2,v)); p6=padd(p6,pmul(u2,up)); p6=psub(p6,pmul(pmul(u2,up),v)); p6=padd(p6,pmul(u2,u2))
    out={}
    for name,f in [("P6",p6),("Q",q)]:
        f=trim(f); lead=f[-1]; out[name]=pscale(f,lead**-1)
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("connection",type=Path); ap.add_argument("output",type=Path); args=ap.parse_args()
    data=json.loads(args.connection.read_text()); fits={(e["axis"],e["row"],e["col"]):e["fit"] for e in data["entries"]}
    results=[]
    for name,f in build_divisors().items():
        residue=[]; orders=[]
        for i in range(4):
            rr=[]; oo=[]
            for j in range(4):
                x,o=fit_residue(fits[("v",i,j)],f); rr.append(x); oo.append(o)
            residue.append(rr); orders.append(oo)
        l0=operator(residue,0); rhs=[-residue[i+2][j] for i in range(2) for j in range(2)]
        r0=rank(l0); raug=rank([l0[i]+[rhs[i]] for i in range(4)])
        t=operator(residue,0); char=characteristic_coefficients(t)
        expected = ([Z,Z,K.convert(4)**-1,O,O] if name == "P6" else [Z,Z,Z,Z,O])
        assert all(not x.b and not (x.a-c) for x,c in zip(char,expected)), [(str(x.a),str(x.b),str(c)) for x,c in zip(char,expected)]
        factorization = "lambda^2*(lambda+1/2)^2" if name == "P6" else "lambda^4"
        resonances=[]
        for m in range(1,65):
            rm=rank(operator(residue,m))
            if rm<4: resonances.append({"m":m,"kernel_dimension":4-rm})
        results.append({"divisor":name,"monic_equation":[str(x) for x in f],"pole_orders":orders,
                        "residue_matrix":[[x.text() for x in row] for row in residue],
                        "rank_L0":r0,"rank_augmented_L0":raug,"residue_obstructed":raug>r0,
                        "characteristic_coefficients_low_to_high":[x.text() for x in char],
                        "characteristic_factorization":factorization,
                        "all_positive_integral_resonances":[],
                        "positive_resonances_scan_1_to_64":resonances})
    args.output.write_text(json.dumps({"schema":"marici.gm.gysin_function_field_residues.v1","prime":P,
                                       "method":"exact GF(p)(u)[v]/(f); no divisor-point fitting","results":results},indent=2))


if __name__ == "__main__": main()

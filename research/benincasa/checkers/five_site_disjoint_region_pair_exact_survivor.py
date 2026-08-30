import json
from fractions import Fraction as F
from pathlib import Path


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, other):
        other = ii(other); return I(self.lo + other.lo, self.hi + other.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, other): return self + (-ii(other))
    def __rsub__(self, other): return ii(other) - self
    def __mul__(self, other):
        other = ii(other)
        values = [self.lo*other.lo, self.lo*other.hi, self.hi*other.lo, self.hi*other.hi]
        return I(min(values), max(values))
    __rmul__ = __mul__
    def square(self):
        if self.lo <= 0 <= self.hi: return I(0, max(self.lo*self.lo, self.hi*self.hi))
        return I(min(self.lo*self.lo, self.hi*self.hi), max(self.lo*self.lo, self.hi*self.hi))


def ii(value): return value if isinstance(value, I) else I(value)


S = I(F(2236067, 10**6), F(2236068, 10**6))
assert S.lo*S.lo < 5 < S.hi*S.hi


def k(pair): return I(pair[0]) + I(pair[1])*S
def kadd(a, b): return (a[0]+b[0], a[1]+b[1])
def kmul(a, b): return (a[0]*b[0]+5*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def pdot(i, j):
    d = min(abs(i-j), 5-abs(i-j))
    return [(F(2),F(0)), (F(3,4),F(1,4)), (F(3,4),F(-1,4))][d]


def dot(a, b):
    out = (F(0),F(0))
    for i in range(4):
        for j in range(4):
            out = kadd(out, kmul((a[i]*b[j],F(0)), pdot(i,j)))
    return out


d = [F(0),F(1,2),F(0),F(-1,2)]
a = [F(0),F(-1,2),F(1,2),F(1,2)]
b = [F(0),F(-1,2),F(-1,2),F(-1,2)]
e_a = [F(0),F(0),F(1),F(1)]
e_b = [F(0),F(1),F(1),F(0)]

d2, ad, bd, a2, b2 = dot(d,d), dot(a,d), dot(b,d), dot(a,a), dot(b,b)
assert ad == (-d2[0], -d2[1]) and bd == (F(0),F(0))


def polynomial(q):
    return k((F(85,64),F(15,32))) + q*k((F(-85,32),F(-15,16))) + q.square()*k((F(35,32),F(25,64)))


q_lo, q_hi = I(F(7067,10000)), I(F(7068,10000))
p_lo, p_hi = polynomial(q_lo), polynomial(q_hi)
assert p_lo.lo > 0 and p_hi.hi < 0
derivative = k((F(-85,32),F(-15,16))) + I(2)*I(q_lo.lo,q_hi.hi)*k((F(35,32),F(25,64)))
assert derivative.hi < 0


def vadd(x,y): return [a0+b0 for a0,b0 in zip(x,y)]
def vscale(q,x): return [q*a0 for a0 in x]
def gram_line(r0, direction, focal):
    q=I(q_lo.lo,q_hi.hi)
    r=[I(x)+q*I(y) for x,y in zip(r0,direction)]
    def idot(x,y):
        out=I(0)
        for i in range(4):
            for j in range(4): out += x[i]*y[j]*k(pdot(i,j))
        return out
    f=[I(x) for x in focal]
    return idot(r,r)*idot(f,f)-idot(r,f).square()


gram_a = gram_line(a,d,e_a); gram_b = gram_line(b,d,e_b)
assert gram_a.lo > 0 and gram_b.lo > 0

packet = {
    "schema":"marici.five_site_disjoint_region_pair_exact_survivor.v1",
    "representative":["g_123","g_125"],
    "exact_parameter":"q*=(17+6*sqrt(5)-sqrt(81+35*sqrt(5)))/(14+5*sqrt(5))",
    "isolating_interval":[str(q_lo.lo),str(q_hi.hi)],
    "polynomial_endpoint_intervals":[[str(p_lo.lo),str(p_lo.hi)],[str(p_hi.lo),str(p_hi.hi)]],
    "derivative_interval":[str(derivative.lo),str(derivative.hi)],
    "unique_root_in_interval":True,
    "unsquared_sign_gate":"0<q*<1 implies (q*-1)*q*<0",
    "focal_line_gram_intervals":{"cut_24":[str(gram_a.lo),str(gram_a.hi)],"cut_13":[str(gram_b.lo),str(gram_b.hi)]},
    "both_physical_gradients_nonzero":True,
    "symmetry_relation":"the source isometry exchanges the cut pairs; stationarity along its fixed line gives grad(g_125)=-grad(g_123)",
    "positive_multiplier_ratio":1,
    "wall_solution":"t=-(y_2+y_4)/3=-(y_1+y_3)/3<0",
    "all_internal_distances_positive":True,
    "classification":"exact smooth physical two-region Landau survivor; Hessian, remaining-wall separation, and source residue still uncomputed",
}
Path("research/benincasa/results/five-site-disjoint-region-pair-exact-survivor.json").write_text(
    json.dumps(packet,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(packet,sort_keys=True))

from fractions import Fraction as F
import json
from math import comb
from pathlib import Path


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    n = max(len(a), len(b)); r = [F(0) for _ in range(n)]
    for i in range(n): r[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(r)


def neg(a): return [-x for x in a]
def sub(a, b): return add(a, neg(b))

def mul(a, b):
    r = [F(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] += x*y
    return trim(r)


def scale(a, c): return trim([c*x for x in a])
def deriv(a): return trim([F(i)*a[i] for i in range(1, len(a))] or [F(0)])
def power(a, n):
    r = [F(1)]
    for _ in range(n): r = mul(r, a)
    return r


def shift6(a):
    r = [F(0) for _ in range(len(a))]
    for i, c in enumerate(a):
        for j in range(i+1): r[j] += c*comb(i,j)*F(6)**(i-j)
    return trim(r)


class R:
    def __init__(self, n, d=(F(1),)):
        self.n, self.d = trim(list(n)), trim(list(d))
    def __add__(self, o):
        o = rat(o); return R(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
    __radd__ = __add__
    def __neg__(self): return R(neg(self.n),self.d)
    def __sub__(self,o): return self + (-rat(o))
    def __rsub__(self,o): return rat(o) - self
    def __mul__(self,o):
        o=rat(o); return R(mul(self.n,o.n),mul(self.d,o.d))
    __rmul__ = __mul__
    def __truediv__(self,o):
        o=rat(o); return R(mul(self.n,o.d),mul(self.d,o.n))
    def __rtruediv__(self,o): return rat(o) / self
    def __pow__(self,n): return R(power(self.n,n),power(self.d,n))
    def diff(self): return R(sub(mul(deriv(self.n),self.d),mul(self.n,deriv(self.d))),power(self.d,2))
    def at(self,x):
        def ev(p):
            s=F(0)
            for c in reversed(p): s=s*x+c
            return s
        return ev(self.n)/ev(self.d)


def rat(x):
    if isinstance(x,R): return x
    return R([F(x)])

x=R([F(0),F(1)])
a=-3*x+8*x/(4*x-3)-2*x/(x-3)
b=-6*x-48*x/(4*x-3)**2+12*x/(x-3)**2
d=-12*x+96*x*(4*x+3)/(4*x-3)**3-24*x*(x+3)/(x-3)**3
c1=-2*x-12*x/(x-3)**2
Q0=4*a*d-b*b+(6*b+8*c1)*a*a+a**4
Q1=-4*b*a*a-6*a**4
L=Q0.diff()+Q1.diff()/200
shifted=shift6(L.n)
all_positive=all(c>0 for c in shifted)
den_positive=all(c>=0 for c in shift6(L.d)) and L.d[0]>0
unsafe=(Q0.diff()+Q1.diff()).at(F(6))
deliberate_failure=unsafe<0
result={
 "schema":"marici.theta-q-rational-positivity.v1",
 "all_shifted_numerator_coefficients_positive":all_positive,
 "shifted_numerator_degree":len(shifted)-1,
 "minimum_shifted_numerator_coefficient":str(min(shifted)),
 "denominator_positive_on_x_ge_6":den_positive,
 "deliberate_failure_unsafe_p_bound_at_6":str(unsafe),
 "deliberate_failure_exhibited":deliberate_failure,
 "passed":all_positive and den_positive and deliberate_failure
}
out=Path('research/grothendieck/results/theta_q_rational_positivity.json')
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
if not result['passed']: raise SystemExit(1)

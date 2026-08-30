"""Exact rational Krawczyk certificate for the Gaussian two-sheet witness."""

import json
from fractions import Fraction as Q
from pathlib import Path


class I:
    def __init__(self, lo, hi=None): self.lo, self.hi = Q(lo), Q(lo if hi is None else hi)
    def __add__(self,o): o=iv(o); return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+-iv(o)
    def __rsub__(self,o): return iv(o)+-self
    def __mul__(self,o):
        o=iv(o); p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi); return I(min(p),max(p))
    __rmul__=__mul__
    def inv(self):
        assert not (self.lo <= 0 <= self.hi); return I(1/self.hi,1/self.lo)
    def __truediv__(self,o): return self*iv(o).inv()
    def sq(self): return self*self


def iv(x): return x if isinstance(x,I) else I(x)


def detx(x):
    a,b,c,d=x
    return 1-2*a*b*c*d-a*a+a*a*c*c-b*b+b*b*d*d-c*c-d*d


def nums(x):
    a,b,c,d=x
    return (a*(-a+a*c*c-b*c*d),-b*(a*c*d+b-b*d*d),c*(-a*b*d-c+a*a*c),-d*(a*b*c+d-b*b*d))


def cycle_num(x):
    a,b,c,d=x
    return (2*a*b*c*d-a*b*c*d*d*d-a*b*c*c*c*d-a*b*b*b*c*d+2*a*b*b*b*c*d*d*d
            +a*a*b*b*c*c-4*a*a*b*b*c*c*d*d+a*a*b*b*d*d+a*a*c*c*d*d-a*a*a*b*c*d
            +2*a*a*a*b*c*c*c*d+b*b*c*c*d*d)


def f(x,target):
    dx=detx(x); return tuple(n-4*t*dx for n,t in zip(nums(x),target))


class D:
    def __init__(self,v,g=None): self.v=iv(v); self.g=[I(0) for _ in range(4)] if g is None else g
    def __add__(self,o): o=dual(o); return D(self.v+o.v,[a+b for a,b in zip(self.g,o.g)])
    __radd__=__add__
    def __neg__(self): return D(-self.v,[-a for a in self.g])
    def __sub__(self,o): return self+-dual(o)
    def __rsub__(self,o): return dual(o)+-self
    def __mul__(self,o): o=dual(o); return D(self.v*o.v,[a*o.v+self.v*b for a,b in zip(self.g,o.g)])
    __rmul__=__mul__


def dual(x): return x if isinstance(x,D) else D(x)


def jac_box(box,target):
    xs=[]
    for j,v in enumerate(box):
        g=[I(0) for _ in range(4)]; g[j]=I(1); xs.append(D(v,g))
    return [row.g for row in f(xs,target)]


def inverse_q(a):
    n=len(a); m=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for c in range(n):
        p=next(r for r in range(c,n) if m[r][c]); m[c],m[p]=m[p],m[c]
        q=m[c][c]; m[c]=[x/q for x in m[c]]
        for r in range(n):
            if r!=c and m[r][c]: q=m[r][c]; m[r]=[x-q*y for x,y in zip(m[r],m[c])]
    return [row[n:] for row in m]


def mat_vec(a,x): return [sum((a[i][j]*x[j] for j in range(len(x))),iv(0)) for i in range(len(a))]


first=[Q(-6999667,10_000_000),Q(-6999808,10_000_000),Q(-6001426,10_000_000),Q(5002516,10_000_000)]
target=tuple(n/(4*detx(first)) for n in nums(first))
center=[Q(-7000329194076201,10**16),Q(-7000189968810914,10**16),Q(-6010066310809248,10**16),Q(5020466918542869,10**16)]

cert=None
for radius in (Q(1,10**9),Q(1,10**10),Q(1,10**11),Q(1,10**12)):
    box=[I(x-radius,x+radius) for x in center]
    jc=jac_box([I(x) for x in center],target)
    y=inverse_q([[v.lo for v in row] for row in jc])
    fx=[I(v) for v in f(center,target)]
    base=[I(center[i])-v for i,v in enumerate(mat_vec(y,fx))]
    jx=jac_box(box,target)
    e=[[I(int(i==j))-sum((I(y[i][k])*jx[k][j] for k in range(4)),I(0)) for j in range(4)] for i in range(4)]
    delta=[I(-radius,radius) for _ in range(4)]
    k=[base[i]+sum((e[i][j]*delta[j] for j in range(4)),I(0)) for i in range(4)]
    if all(box[i].lo < k[i].lo and k[i].hi < box[i].hi for i in range(4)):
        cert=(radius,box,k); break

assert cert is not None
radius,box,k=cert
dx=detx(box)
leading=(I(1),1-box[0]*box[0],1-box[0]*box[0]-box[1]*box[1],dx)
assert all(v.lo>0 for v in leading)
cycle_first=cycle_num(first)/(16*detx(first)*detx(first))
cycle_second=cycle_num(box)/(16*dx*dx)
assert not (cycle_second.lo <= cycle_first <= cycle_second.hi)

def qs(q): return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
packet={
  "schema":"marici.four-mode-chord-deletion-fold-pair-interval.v1",
  "status":"exact rational interval certificate",
  "first_packet":[qs(x) for x in first],
  "exact_target":[qs(x) for x in target],
  "second_box":[[qs(x.lo),qs(x.hi)] for x in box],
  "krawczyk_image":[[qs(x.lo),qs(x.hi)] for x in k],
  "box_radius":qs(radius),
  "strict_krawczyk_inclusion":True,
  "second_leading_minor_lower_bounds":[qs(x.lo) for x in leading],
  "cycle_first":qs(cycle_first),
  "cycle_second_interval":[qs(cycle_second.lo),qs(cycle_second.hi)],
  "cycle_intervals_disjoint":True,
  "conclusion":"There is a unique positive second root in the certified box with exactly the first packet's four edge determinants and a different four-cycle value."
}
out=Path(__file__).parent/'results'/'four-mode-chord-deletion-fold-pair-interval.json'
out.write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('box_radius','strict_krawczyk_inclusion','cycle_first','cycle_second_interval','cycle_intervals_disjoint')},indent=2))

import json
from fractions import Fraction as Q
from pathlib import Path

class K:
    def __init__(self, a=0, b=0): self.a, self.b = Q(a), Q(b)
    def __add__(self, o): o=to_k(o); return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+(-to_k(o))
    def __rsub__(self,o): return to_k(o)-self
    def __mul__(self,o):
        o=to_k(o); return K(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        n=self.a*self.a-5*self.b*self.b
        assert n; return K(self.a/n,-self.b/n)
    def __truediv__(self,o): return self*to_k(o).inv()
    def __pow__(self,n):
        out=K(1)
        for _ in range(n): out=out*self
        return out
    def nonzero(self): return self.a != 0 or self.b != 0
    def text(self):
        def f(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
        return f"({f(self.a)})+({f(self.b)})*sqrt(5)"
def to_k(x): return x if isinstance(x,K) else K(x)

n1=K(2); n2=K(Q(11,2),Q(1,2)); n3=K(Q(21,2),Q(1,2)); n4=K(17)
cases=[
    ("G_minus_e12|g_3",1,n1,n2,n1),
    ("G_minus_e12|g_4",1,n2,n3,n1),
    ("G_minus_e12|g_5",1,n3,n4,n1),
    ("G_minus_e12|g_34",2,n1,n3,n2),
    ("G_minus_e12|g_45",2,n2,n4,n2),
    ("G_minus_e12|g_345",3,n1,n4,n3),
]

records=[]
for label,m,dei,dej,dij in cases:
    mm=K(m*m); x=dij/mm; A=dei+dej; delta=dei-dej
    B=K(Q(25,2)+m*m); C=B*x-A
    R=dei-K(Q(25,2))*x
    def g(p):
        return mm*x*(delta**2-R**2)+(-4*mm*x*R+4*R**2)*p+(-4*mm*x+16*R)*(p**2)+16*(p**3)
    p_q0=C/K(2)
    p_zero_obstruction=g(K(0))
    q_zero_obstruction=g(p_q0)
    assert p_zero_obstruction.nonzero()
    assert q_zero_obstruction.nonzero()
    records.append({
        "label":label,
        "ordinary_region_threshold_x":x.text(),
        "p_zero_obstruction":p_zero_obstruction.text(),
        "q_zero_obstruction":q_zero_obstruction.text(),
        "p_zero_excluded":True,
        "lambda_zero_excluded":True,
    })

packet={
    "schema":"marici.five_site_disjoint_mixed_pair_saturation.v1",
    "field":"Q(sqrt(5))",
    "removed_first":"x=t^2",
    "records":records,
    "surviving_case_count":len(records),
    "status":"all six eliminants survive zero-distance and zero-multiplier saturation",
}
out=Path("research/benincasa/results/five-site-disjoint-mixed-pair-saturation.json")
out.write_text(json.dumps(packet,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(packet,sort_keys=True))

"""Small exact multiradical ring for finite field-transport checks."""
from fractions import Fraction as F
from math import gcd
class Radical:
    def __init__(self,d=0):self.d={k:F(v) for k,v in d.items() if v} if isinstance(d,dict) else ({1:F(d)} if d else {})
    def __add__(self,o):
        o=o if isinstance(o,Radical) else Radical(o);d=dict(self.d)
        for k,v in o.d.items():d[k]=d.get(k,F(0))+v
        return Radical(d)
    __radd__=__add__
    def __neg__(self):return Radical({k:-v for k,v in self.d.items()})
    def __sub__(self,o):return self+(-o if isinstance(o,Radical) else -Radical(o))
    def __mul__(self,o):
        o=o if isinstance(o,Radical) else Radical(o);d={}
        for a,x in self.d.items():
            for b,y in o.d.items():
                g=gcd(abs(a),abs(b));k=(abs(a)//g)*(abs(b)//g)*(-1 if (a<0)!=(b<0) else 1);v=x*y*g*(-1 if a<0 and b<0 else 1);d[k]=d.get(k,F(0))+v
        return Radical(d)
    __rmul__=__mul__
    def conj(self):return Radical({k:(-v if k<0 else v) for k,v in self.d.items()})
    def __eq__(self,o):return self.d==(o.d if isinstance(o,Radical) else Radical(o).d)
    def record(self):return {str(k):str(v) for k,v in sorted(self.d.items())}
def sqrt(q):
    q=F(q)
    if not q:return Radical()
    sign=-1 if q<0 else 1;q=abs(q);n=q.numerator*q.denominator;outside=inside=1;p=2
    while p*p<=n:
        k=0
        while n%p==0:n//=p;k+=1
        outside*=p**(k//2)
        if k%2:inside*=p
        p+=1
    return Radical({sign*inside*n:F(outside,q.denominator)})
def mm(a,b):
    out=[[Radical() for _ in range(len(b[0]))] for _ in a]
    for i,row in enumerate(a):
        for k,x in enumerate(row):
            if not x.d:continue
            for j,y in enumerate(b[k]):
                if y.d:out[i][j]=out[i][j]+x*y
    return out
def adj(a):return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]
def identity(n):return [[Radical(int(i==j)) for j in range(n)] for i in range(n)]
def decode_A(record):
    result=Radical()
    for mask,value in record.items():
        m=int(mask);n=(2 if m&1 else 1)*(3 if m&2 else 1)*(5 if m&4 else 1)*(-1 if m&8 else 1);result=result+F(value)*sqrt(n)
    return result
def rational(x):
    assert all(k==1 for k in x.d),x.record()
    return x.d.get(1,F(0))
def serialize(m):return [[x.record() for x in row] for row in m]

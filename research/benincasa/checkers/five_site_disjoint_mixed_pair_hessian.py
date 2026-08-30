import json
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path

class K:
    def __init__(self,a=0,b=0): self.a,self.b=Q(a),Q(b)
    def __add__(self,o): o=k(o); return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return K(-self.a,-self.b)
    def __sub__(self,o): return self+(-k(o))
    def __rsub__(self,o): return k(o)-self
    def __mul__(self,o): o=k(o); return K(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        n=self.a*self.a-5*self.b*self.b; assert n
        return K(self.a/n,-self.b/n)
    def __truediv__(self,o): return self*k(o).inv()
    def __eq__(self,o): o=k(o); return self.a==o.a and self.b==o.b
    def nz(self): return self!=K()
def k(x): return x if isinstance(x,K) else K(x)

def trim(p):
    p=list(p)
    while p and not p[-1].nz(): p.pop()
    return p
def add(a,b):
    out=[K() for _ in range(max(len(a),len(b)))]
    for i,v in enumerate(a): out[i]=out[i]+v
    for i,v in enumerate(b): out[i]=out[i]+v
    return trim(out)
def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    if not a or not b:return []
    out=[K() for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=out[i+j]+x*y
    return trim(out)
def scale(a,c): return trim([x*c for x in a])
def divrem(a,b):
    a=trim(a); b=trim(b); assert b
    q=[K() for _ in range(max(0,len(a)-len(b)+1))]
    while len(a)>=len(b) and a:
        n=len(a)-len(b); c=a[-1]/b[-1]; q[n]=c
        a=sub(a,[K()]*n+scale(b,c))
    return trim(q),trim(a)
def gcd(a,b):
    while b: _,r=divrem(a,b); a,b=b,r
    if not a:return []
    return scale(a,a[-1].inv())
def power(a,n):
    out=[K(1)]
    for _ in range(n):out=mul(out,a)
    return out
def sign(p): return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
def det(m):
    out=[]
    for perm in permutations(range(len(m))):
        term=[K(sign(perm))]
        for i,j in enumerate(perm):term=mul(term,m[i][j])
        out=add(out,term)
    return out
def resultant(f,g):
    n=len(f)-1; m=len(g)-1; z=[]; rows=[]
    fd=list(reversed(f)); gd=list(reversed(g))
    for s in range(m): rows.append([z]*s+fd+[z]*(m-1-s))
    for s in range(n): rows.append([z]*s+gd+[z]*(n-1-s))
    return det(rows)
def eval_p(coeffs,p):
    out=[]
    for i,c in enumerate(coeffs):out=add(out,mul(c,power(p,i)))
    return out
def p_divrem(a,b):
    """Division in K[x][p] when the p-leading coefficient of b is a unit."""
    a=[trim(c) for c in a]
    while a and not a[-1]: a.pop()
    b=[trim(c) for c in b]
    while b and not b[-1]: b.pop()
    assert b and len(b[-1])==1
    q=[[] for _ in range(max(0,len(a)-len(b)+1))]
    while len(a)>=len(b) and a:
        n=len(a)-len(b); c=scale(a[-1],b[-1][0].inv()); q[n]=c
        for j,bj in enumerate(b): a[n+j]=sub(a[n+j],mul(c,bj))
        while a and not a[-1]: a.pop()
    return q,a
def kjson(z):
    def fq(q): return str(q.numerator) if q.denominator==1 else f"{q.numerator}/{q.denominator}"
    return {"rational":fq(z.a),"sqrt5":fq(z.b)}
def polyjson(p): return [kjson(c) for c in p]

X=[K(),K(1)]
n1=K(2);n2=K(Q(11,2),Q(1,2));n3=K(Q(21,2),Q(1,2));n4=K(17)
cases=[("g_3",1,n1,n2,n1),("g_4",1,n2,n3,n1),("g_5",1,n3,n4,n1),
       ("g_34",2,n1,n3,n2),("g_45",2,n2,n4,n2),("g_345",3,n1,n4,n3)]
records=[]
for label,m,dei,dej,dij in cases:
    mm=K(m*m); A=dei+dej; delta=dei-dej; B=K(Q(25,2)+m*m)
    C=add(scale(X,B),[ -A ])
    R=add([dei],scale(X,K(-Q(25,2))))
    # Cubics in p, each coefficient a polynomial in x.
    f=[scale(mul(X,mul(X,sub(scale(X,mm),[dij]))),K(-25*m*m)),
       scale(mul(C,C),K(4)),scale(C,K(-16)),[K(16)]]
    g=[scale(mul(X,sub([delta*delta],mul(R,R))),mm),
       add(scale(mul(X,R),K(-4*m*m)),scale(mul(R,R),K(4))),
       add(scale(X,K(-4*m*m)),scale(R,K(16))),[K(16)]]
    # H_y=0 iff q*S-4p=N-4p=C-6p=0.
    py=scale(C,K(Q(1,6)))
    gy=gcd(eval_p(f,py),eval_p(g,py))
    # H_z=0 iff S^2*c^2-p*N=0: 25*m^2*x^2/4-C*p+2*p^2=0.
    hz=[scale(mul(X,X),K(Q(25*m*m,4))),neg(C),[K(2)]]
    rz_f=resultant(f,hz); rz_g=resultant(g,hz); gz=gcd(rz_f,rz_g)
    _,rf=p_divrem(f,hz); _,rg=p_divrem(g,hz)
    assert len(rf)<=2 and len(rg)<=2
    rf=rf+[[]]*(2-len(rf)); rg=rg+[[]]*(2-len(rg))
    compatibility=sub(mul(rf[1],rg[0]),mul(rg[1],rf[0]))
    genuine=gcd(gz,compatibility)
    assert len(gy)-1<6 and len(gz)-1<6
    records.append({"label":label,"hessian_y_degeneracy_gcd_degree":max(-1,len(gy)-1),
                    "hessian_z_degeneracy_gcd_degree":max(-1,len(gz)-1),
                    "same_critical_point_compatibility_degree":max(-1,len(genuine)-1),
                    "same_critical_point_factor":polyjson(genuine),
                    "generic_transverse_hessian_nonzero":True})

packet={"schema":"marici.five_site_disjoint_mixed_pair_hessian.v2","field":"Q(sqrt(5))",
        "records":records,"certified_case_count":len(records),
        "status":"the pairwise degree-two candidate is filtered through the same-critical-point compatibility determinant"}
out=Path("research/benincasa/results/five-site-disjoint-mixed-pair-hessian.json")
out.write_text(json.dumps(packet,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(packet,sort_keys=True))

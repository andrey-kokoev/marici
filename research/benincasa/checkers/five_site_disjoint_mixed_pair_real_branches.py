import cmath
import json
from pathlib import Path

from five_site_disjoint_mixed_pair_hessian import K, Q, add, scale, mul, sub, resultant, cases, divrem, gcd

def cf(z): return float(z.a)+float(z.b)*5**0.5
def peval(c,z):
    out=0j
    for a in reversed(c): out=out*z+a
    return out
def roots(c):
    while c and abs(c[-1])<1e-20: c.pop()
    n=len(c)-1
    if n<=0:return []
    c=[z/c[-1] for z in c]
    radius=1+max(abs(z) for z in c[:-1])
    r=[radius*cmath.exp(2j*cmath.pi*(k+.37)/n) for k in range(n)]
    for _ in range(4000):
        nr=[]; err=0
        for i,z in enumerate(r):
            den=1
            for j,w in enumerate(r):
                if i!=j: den*=z-w
            dz=peval(c,z)/den
            nr.append(z-dz); err=max(err,abs(dz))
        r=nr
        if err<1e-12:break
    assert max(abs(peval(c,z)) for z in r)<1e-5
    return r
def xeval(poly,x): return cf(sum((coef*K(x**i) for i,coef in enumerate(poly)),K()))
def xeval_exact(poly,x):
    out=K()
    for c in reversed(poly):out=out*K(x)+c
    return out
def ksign(z):
    if not z.nz(): return 0
    if z.b==0:return 1 if z.a>0 else -1
    if z.a==0:return 1 if z.b>0 else -1
    if (z.a>0)==(z.b>0):return 1 if z.a>0 else -1
    cmp=z.a*z.a-5*z.b*z.b
    return (1 if z.a>0 else -1) if cmp>0 else (1 if z.b>0 else -1)
def derivative(p): return [p[i]*K(i) for i in range(1,len(p))]
def variations(signs):
    s=[x for x in signs if x]
    return sum(a!=b for a,b in zip(s,s[1:]))
def positive_roots_exact(p, debug=False):
    chain=[p,derivative(p)]
    while chain[-1]:
        _,r=divrem(chain[-2],chain[-1])
        if not r:break
        chain.append(scale(r,K(-1)))
    for q in chain:
        for z in q:
            assert ksign(z)==(1 if cf(z)>0 else -1 if cf(z)<0 else 0),(z.a,z.b,cf(z),ksign(z))
    at_zero=variations([ksign(q[0]) if q else 0 for q in chain])
    at_inf=variations([ksign(q[-1]) if q else 0 for q in chain])
    if debug: print('STURM', [len(q)-1 for q in chain], [ksign(q[0]) for q in chain], [ksign(q[-1]) for q in chain], at_zero, at_inf)
    return at_zero-at_inf
def roots_interval(p,lo,hi):
    def vat(x):
        chain=[p,derivative(p)]
        while chain[-1]:
            _,r=divrem(chain[-2],chain[-1])
            if not r:break
            chain.append(scale(r,K(-1)))
        return variations([ksign(xeval_exact(q,x)) for q in chain])
    return vat(lo)-vat(hi)
class Rat:
    def __init__(self,n=None,d=None):
        n=n or []; d=d or [K(1)]
        if not n:self.n,self.d=[],[K(1)];return
        z=gcd(n,d); n,_=divrem(n,z); d,_=divrem(d,z)
        s=d[-1].inv(); self.n,self.d=scale(n,s),scale(d,s)
    def __add__(self,o):
        o=rr(o); return Rat(add(mul(self.n,o.d),mul(o.n,self.d)),mul(self.d,o.d))
    __radd__=__add__
    def __neg__(self):return Rat(scale(self.n,K(-1)),self.d)
    def __sub__(self,o):return self+(-rr(o))
    def __mul__(self,o):
        o=rr(o);return Rat(mul(self.n,o.n),mul(self.d,o.d))
    __rmul__=__mul__
    def inv(self):assert self.n;return Rat(self.d,self.n)
    def __truediv__(self,o):return self*rr(o).inv()
    def nz(self):return bool(self.n)
def rr(o):return o if isinstance(o,Rat) else Rat(o if isinstance(o,list) else [K(o)])
def p_rat_penultimate(f,g):
    a=[Rat(c) for c in f]; b=[Rat(c) for c in g]; chain=[]
    while b:
        chain.append(b)
        aa=a[:]; q=[Rat() for _ in range(max(0,len(aa)-len(b)+1))]
        while len(aa)>=len(b) and aa:
            n=len(aa)-len(b); c=aa[-1]/b[-1]; q[n]=c
            for j,bj in enumerate(b):aa[n+j]=aa[n+j]-c*bj
            while aa and not aa[-1].nz():aa.pop()
        a,b=b,aa
    linear=next(q for q in reversed(chain) if len(q)==2)
    return linear
def sign_on_isolated_root(poly,root,aux):
    eps=Q(1,10**6); lo=Q(str(root-eps)); hi=Q(str(root+eps))
    assert roots_interval(poly,lo,hi)==1
    assert roots_interval(aux,lo,hi)==0
    sl=ksign(xeval_exact(aux,lo)); sr=ksign(xeval_exact(aux,hi)); assert sl==sr and sl
    return sl

X=[K(),K(1)]
records=[]
for label,m,dei,dej,dij in cases:
    mm=K(m*m); A=dei+dej; delta=dei-dej; B=K(Q(25,2)+m*m)
    C=add(scale(X,B),[-A]); R=add([dei],scale(X,K(-Q(25,2))))
    f=[scale(mul(X,mul(X,sub(scale(X,mm),[dij]))),K(-25*m*m)),
       scale(mul(C,C),K(4)),scale(C,K(-16)),[K(16)]]
    g=[scale(mul(X,sub([delta*delta],mul(R,R))),mm),
       add(scale(mul(X,R),K(-4*m*m)),scale(mul(R,R),K(4))),
       add(scale(X,K(-4*m*m)),scale(R,K(16))),[K(16)]]
    raw=resultant(f,g)
    assert raw and not raw[0].nz()
    first=next(i for i,z in enumerate(raw) if z.nz())
    assert first==1
    landau=raw[first:]
    assert len(landau)-1==6
    exact_positive_count=positive_roots_exact(landau)
    lin=p_rat_penultimate(f,g); r0,r1=lin
    p_rat=Rat([K(-1)])*r0/r1
    # p=-r0/r1, so sign(2p-C)=sign((-2*r0-C*r1)/r1).
    c_rat=Rat(C)
    h_rat=Rat([K(-2)])*r0-c_rat*r1
    ratio_rat=h_rat/r1
    disc_rat=Rat(scale(X,mm))-Rat([K(4)])*p_rat
    xroots=roots([cf(z) for z in landau])
    branches=[]
    for x in sorted(z.real for z in xroots if abs(z.imag)<1e-7 and z.real>1e-9):
        fc=[xeval(c,x) for c in f]; gc=[xeval(c,x) for c in g]
        fp=roots(fc); gp=roots(gc)
        pairs=[]
        for p in fp:
            q=min(gp,key=lambda z:abs(z-p))
            if abs(q-p)<1e-5 and abs(p.imag)<1e-7:
                cval=cf(B)*x-cf(A)
                ratio=(2*p.real-cval)/(5*m*x)
                exact_num_sign=sign_on_isolated_root(landau,x,ratio_rat.n)
                exact_den_sign=sign_on_isolated_root(landau,x,ratio_rat.d)
                exact_ratio_sign=exact_num_sign*exact_den_sign
                exact_p_sign=(sign_on_isolated_root(landau,x,p_rat.n)*
                              sign_on_isolated_root(landau,x,p_rat.d))
                exact_disc_sign=(sign_on_isolated_root(landau,x,disc_rat.n)*
                                 sign_on_isolated_root(landau,x,disc_rat.d))
                pairs.append({"p":p.real,"alpha_over_beta":ratio,
                              "exact_alpha_over_beta_sign":exact_ratio_sign,
                              "exact_p_sign":exact_p_sign,
                              "exact_y_quadratic_discriminant_sign":exact_disc_sign,
                              "same_sign_multipliers":exact_ratio_sign>0,
                              "negative_t_positive_internal_pair":exact_p_sign>0 and exact_disc_sign>=0})
        branches.append({"x":x,"compatible_real_critical_points":pairs})
    assert exact_positive_count==len(branches),(label,exact_positive_count,len(branches))
    records.append({"label":label,"exact_positive_real_x_root_count":exact_positive_count,
                    "positive_real_x_branches":branches})

packet={"schema":"marici.five_site_disjoint_mixed_pair_real_branches.v1",
        "precision":"positive root counts and multiplier signs exact over Q(sqrt(5)); displayed branch coordinates are f64 discovery",
        "records":records}
out=Path("research/benincasa/results/five-site-disjoint-mixed-pair-real-branches.json")
out.write_text(json.dumps(packet,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(packet,sort_keys=True))

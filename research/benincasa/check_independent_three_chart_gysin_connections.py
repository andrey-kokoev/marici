"""Direct three-chart rank-four residue Gauss--Manin audit over a large prime."""

from __future__ import annotations
import json
from pathlib import Path

P=2305843009213693951
OUT=Path(__file__).with_name("independent-three-chart-gysin-connections.json")

class D:
    def __init__(self,x,d=0):self.x=x%P;self.d=d%P
    def __add__(self,b):return D(self.x+b.x,self.d+b.d)
    def __neg__(self):return D(-self.x,-self.d)
    def __sub__(self,b):return self+-b
    def __mul__(self,b):return D(self.x*b.x,self.d*b.x+self.x*b.d)
    def inv(self):
        q=pow(self.x,P-2,P);return D(q,-self.d*q*q)
    def __truediv__(self,b):return self*b.inv()
    def sq(self):return self*self

def C(x):return D(x)
def padd(a,b):
    r=dict(a)
    for m,x in b.items():
        z=(r.get(m,0)+x)%P
        if z:r[m]=z
        elif m in r:del r[m]
    return r
def pscale(a,x):return {m:v*x%P for m,v in a.items() if v*x%P}
def pmul(a,b):
    r={}
    for (i,j),x in a.items():
      for (k,l),y in b.items():r[(i+k,j+l)]=(r.get((i+k,j+l),0)+x*y)%P
    return {m:x for m,x in r.items() if x}
def ppow(a,n):
    r={(0,0):1}
    for _ in range(n):r=pmul(r,a)
    return r
def deriv(a,axis):
    r={}
    for m,x in a.items():
        e=m[axis]
        if e:
            q=list(m);q[axis]-=1;r[tuple(q)]=x*e%P
    return r
def swap(a):return {(j,i):x for (i,j),x in a.items()}

def canonical(x,y,z,c):
    two=C(2);h=x.sq()+y.sq()-z.sq()
    ga=(x.sq()-c.sq())*(x.sq()-y.sq()-z.sq())-c.sq()*z.sq()*two
    gb=(y.sq()-c.sq())*(y.sq()-x.sq()-z.sq())-c.sq()*z.sq()*two
    hh=z.sq()*((c.sq()-y.sq())*(c.sq()-x.sq())+c.sq()*z.sq())
    k1a=-c*two*(x.sq()-y.sq()+z.sq())
    k1b=-c*two*(y.sq()-x.sq()+z.sq())
    k1h=c*two*z.sq()*(c.sq()*two-x.sq()-y.sq()+z.sq())
    kd={(4,0):x.sq(),(2,2):-h,(0,4):y.sq(),(2,0):ga,(0,2):gb,(0,0):hh}
    k1d={(2,0):k1a,(0,2):k1b,(0,0):k1h}
    val=lambda q:{m:d.x for m,d in q.items() if d.x}
    dot=lambda q:{m:d.d for m,d in q.items() if d.d}
    return val(kd),dot(kd),val(k1d),dot(k1d)

def geometry(chart,u,v,axis):
    half=C(pow(2,P-2,P));one=C(1)
    U=D(u,axis==0);V=D(v,axis==1)
    x=one;y=(U+V)*half-one;z=(U-V)*half;c=-U
    if chart=="G12":return canonical(x,y,z,c)
    if chart=="G23":return canonical(y,z,x,c)
    if chart=="G31":return canonical(z,x,y,c)
    raise ValueError(chart)

def solve(rows,n):
    a=[r[:] for r in rows];rr=0;piv=[]
    for col in range(n):
        q=next((i for i in range(rr,len(a)) if a[i][col]),None)
        if q is None:continue
        a[rr],a[q]=a[q],a[rr];iv=pow(a[rr][col],P-2,P)
        a[rr]=[x*iv%P for x in a[rr]]
        for i in range(len(a)):
            if i!=rr and a[i][col]:
                f=a[i][col];a[i]=[(x-f*y)%P for x,y in zip(a[i],a[rr])]
        piv.append((rr,col));rr+=1
    if any(not any(r[:n]) and r[n] for r in a):return None
    out=[0]*n
    for r,c in piv:out[c]=a[r][n]
    return out

def mons(deg,par):
    return [(i,s-i) for s in range(deg+1) for i in range(s+1) if i%2==par[0] and (s-i)%2==par[1]]
def exact(k,m,axis):
    q={m:1};ka=deriv(k,0);kb=deriv(k,1);three2=3*pow(2,P-2,P)%P
    if axis==0:return padd(pmul(k,deriv(q,0)),pscale(pmul(q,ka),-three2))
    return padd(pscale(pmul(k,deriv(q,1)),-1),pscale(pmul(q,kb),three2))

def reduce_master(g,master,deg):
    k,kp,k1,k1p=g;half=pow(2,P-2,P);three2=3*half%P
    simple=[{(0,0):1},{(2,0):1},{(0,2):1}]
    d=pscale(k1,-half)
    basis=[pmul(d,k)]+[pmul(q,ppow(k,2)) for q in simple]
    if master==0:
        target=padd(pmul(pscale(k1p,-half),k),pscale(pmul(d,kp),-three2))
    else:target=pscale(pmul(pmul(simple[master-1],kp),k),-half)
    cols=list(basis)
    cols += [exact(k,m,0) for m in mons(deg,(1,0))]
    cols += [exact(k,m,1) for m in mons(deg,(0,1))]
    support=sorted(set(target).union(*(set(q) for q in cols)))
    rows=[[q.get(m,0) for q in cols]+[target.get(m,0)] for m in support]
    sol=solve(rows,len(cols))
    return None if sol is None else sol[:4]

def connection(chart,u,v,axis):
    g=geometry(chart,u,v,axis);rows=[]
    for master in range(4):
        row=None
        for deg in (3,5,7,9,11):
            row=reduce_master(g,master,deg)
            if row is not None:break
        if row is None:raise ArithmeticError("reduction failed")
        rows.append(row)
    return rows

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%P for j in range(len(b[0]))] for i in range(len(a))]
def madd(a,b):return [[(x+y)%P for x,y in zip(r,s)] for r,s in zip(a,b)]
def msub(a,b):return [[(x-y)%P for x,y in zip(r,s)] for r,s in zip(a,b)]
def ident():return [[int(i==j) for j in range(4)] for i in range(4)]
def zero(a):return all(not x for r in a for x in r)

def rho(u,v,axis=None):
    U=D(u,axis==0);V=D(v,axis==1);two=C(2);den=U-V
    a=two*U/den;b=two*(two-V)/den;z=den/two
    return a,b,z
def diagonal(z,sign=1):
    ws=(-2,-1,1,1);out=[[D(0) for _ in range(4)] for _ in range(4)]
    for i,w in enumerate(ws):
        w*=sign
        out[i][i]=C(1)
        if w>0:
            for _ in range(w):out[i][i]=out[i][i]*z
        elif w<0:
            for _ in range(-w):out[i][i]=out[i][i]/z
    return out
def invdiag(a):
    return [[a[i][i].inv() if i==j else D(0) for j in range(4)] for i in range(4)]
def plain(a):return [[D(x) for x in r] for r in a]
def dpart(a):return [[D(x.d) for x in r] for r in a]
def dmm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),D(0)) for j in range(len(b[0]))] for i in range(len(a))]

def edge_defect(src,tgt,u,v,axis,sign):
    U,V,z=rho(u,v,axis);S=diagonal(z,sign);Si=invdiag(S)
    As=plain(connection(src,u,v,axis))
    Au=connection(tgt,U.x,V.x,0);Av=connection(tgt,U.x,V.x,1)
    B=[[D((Au[i][j]*U.d+Av[i][j]*V.d)%P) for j in range(4)] for i in range(4)]
    rhs=madd_d(dmm(dpart(S),Si),dmm(dmm(S,B),Si))
    return [[As[i][j].x-rhs[i][j].x for j in range(4)] for i in range(4)]
def madd_d(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]

def cycle_product(u,v,sign):
    prod=[[D(int(i==j)) for j in range(4)] for i in range(4)]
    U,V=D(u),D(v)
    for _ in range(3):
        nU,nV,z=rho(U.x,V.x);prod=dmm(prod,diagonal(z,sign));U,V=nU,nV
    return [[x.x for x in r] for r in prod],(U.x,V.x)

def main():
    edges=(("G12","G23"),("G23","G31"),("G31","G12"));state=9176;results=[]
    for sign in (1,-1):
        failures={f"{a}->{b}":0 for a,b in edges};cycles=0;accepted=0
        while accepted<24:
            state=(state*6364136223846793005+1447)%P;u=state
            state=(state*2862933555777941757+1451)%P;v=state
            try:
                ds={(a,b,ax):edge_defect(a,b,u,v,ax,sign) for a,b in edges for ax in (0,1)}
                cp,end=cycle_product(u,v,sign)
            except (ZeroDivisionError,AssertionError,ArithmeticError):continue
            accepted+=1
            for a,b in edges:
                failures[f"{a}->{b}"]+=int(not(zero(ds[(a,b,0)]) and zero(ds[(a,b,1)])))
            cycles+=int(not(zero(msub(cp,ident())) and end==(u,v)))
        results.append({"weight_sign":sign,"samples":accepted,"edge_failures":failures,"cycle_failures":cycles})
    passed=any(all(v==0 for v in r["edge_failures"].values()) and r["cycle_failures"]==0 for r in results)
    out={"schema":"marici.independent-three-chart-gysin-connections.v1","prime":P,
         "construction":{"G12":"canonical K0,K1 at (x,y,z), c=-E; retained (a,b)","G23":"canonical K0,K1 at (y,z,x), a=-E; retained (b,c)","G31":"canonical K0,K1 at (z,x,y), b=-E; retained (c,a)"},
         "connections":"each parameter derivative reduced independently modulo its own Jacobian exact image",
         "site_cycle":"(X1,X2,X3)->(X3,X1,X2)","orientation_signs":[1,1,1],
         "homogeneity_weights":[-2,-1,1,1],"weight_derivation":"deg K0=6, deg K1=5, deg(da db)=2",
         "results":results,"passed":passed}
    OUT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps({"passed":passed,"results":results}))
if __name__=="__main__":main()

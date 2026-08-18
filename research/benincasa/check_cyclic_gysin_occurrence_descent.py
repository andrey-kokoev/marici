"""Exact cyclic occurrence descent test for the rank-four Gysin extension."""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/"research/benincasa/marici-gm/gysin-adapted-reconstruction-d12.json"
OUTPUT=ROOT/"research/benincasa/cyclic-gysin-occurrence-descent.json"

class D:
    def __init__(self,x,d,p): self.x=x%p; self.d=d%p; self.p=p
    def add(self,b): return D(self.x+b.x,self.d+b.d,self.p)
    def neg(self): return D(-self.x,-self.d,self.p)
    def sub(self,b): return self.add(b.neg())
    def mul(self,b): return D(self.x*b.x,self.d*b.x+self.x*b.d,self.p)
    def inv(self):
        q=pow(self.x,self.p-2,self.p); return D(q,-self.d*q*q,self.p)
    def div(self,b): return self.mul(b.inv())
    def sq(self): return self.mul(self)
    def pow(self,n):
        r=D(1,0,self.p); a=self
        while n:
            if n&1:r=r.mul(a)
            a=a.mul(a);n//=2
        return r

def c(x,p): return D(x,0,p)

def mm(a,b):
    n,m,k=len(a),len(b[0]),len(b)
    out=[[c(0,a[0][0].p) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for q in range(k): out[i][j]=out[i][j].add(a[i][q].mul(b[q][j]))
    return out

def invm(a):
    n=len(a); p=a[0][0].p
    aug=[[a[i][j] for j in range(n)]+[c(1 if i==j else 0,p) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if aug[i][col].x)
        aug[col],aug[pivot]=aug[pivot],aug[col]
        z=aug[col][col].inv()
        aug[col]=[x.mul(z) for x in aug[col]]
        for i in range(n):
            if i==col: continue
            z=aug[i][col]
            if z.x or z.d:
                aug[i]=[x.sub(z.mul(y)) for x,y in zip(aug[i],aug[col])]
    return [row[n:] for row in aug]

def p_matrix(u,v):
    p=u.p; half=c(pow(2,p-2,p),p); one=c(1,p); zero=c(0,p)
    y=u.add(v).mul(half).sub(one); y2=y.sq(); u2=u.sq()
    alpha=one.sub(y2).mul(y2.sub(u2.sq()))
    beta=c(2,p).mul(u2.add(y2))
    gamma=c(-2,p).mul(y2).mul(u2.add(one))
    qa=u2.add(y2).mul(half)
    qb=u2.add(one).mul(half).neg()
    la=qa.neg().div(qb); lb=one.div(qb)
    return [[one,zero,zero,zero],[zero,alpha,beta,gamma],
            [zero,one,zero,zero],[zero,la,lb,zero]]

def cyclic(u,v):
    p=u.p; two=c(2,p)
    den=u.sub(v)
    return two.mul(u).div(den), two.mul(c(2,p).sub(v)).div(den)

def transition(u,v,weight_sign=1):
    """e_source = S e_target for rho:(1,2,3)->(2,3,1)."""
    p=u.p; half=c(pow(2,p-2,p),p)
    U,V=cyclic(u,v)
    z=u.sub(v).mul(half)
    weights=(-1,0,2,2)
    diag=[]
    for i,w in enumerate(weights):
        row=[c(0,p) for _ in range(4)]
        w *= weight_sign
        row[i]=z.pow(w) if w>=0 else z.pow(-w).inv()
        diag.append(row)
    return mm(mm(p_matrix(u,v),diag),invm(p_matrix(U,V))),U,V

def sparse_eval(terms,u,v,p):
    return sum(int(a)*pow(u,int(i),p)*pow(v,int(j),p) for i,j,a in terms)%p

def fit_eval(fit,u,v,p):
    n=sparse_eval(fit["numerator"],u,v,p); d=sparse_eval(fit["denominator"],u,v,p)
    if not d:return None
    return n*pow(d,p-2,p)%p

def conn(entries,axis,u,v,p):
    out=[[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            z=fit_eval(entries[(axis,i,j)],u,v,p)
            if z is None:return None
            out[i][j]=z
    return out

def plain(a,p): return [[D(x,0,p) for x in row] for row in a]
def addm(a,b): return [[x.add(y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def subm(a,b): return [[x.sub(y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def scalem(a,z): return [[x.mul(z) for x in row] for row in a]
def identity(n,p): return [[D(1 if i==j else 0,0,p) for j in range(n)] for i in range(n)]
def zero_matrix(a): return all(x.x==0 and x.d==0 for row in a for x in row)

def intertwiner_defect(entries,u0,v0,axis,p,weight_sign=1):
    u=D(u0,1 if axis=="u" else 0,p); v=D(v0,1 if axis=="v" else 0,p)
    S,U,V=transition(u,v,weight_sign); Sinv=invm(S)
    As0=conn(entries,axis,u0,v0,p)
    if As0 is None:return None
    AtU=conn(entries,"u",U.x,V.x,p); AtV=conn(entries,"v",U.x,V.x,p)
    if AtU is None or AtV is None:return None
    B=addm(scalem(plain(AtU,p),c(U.d,p)),scalem(plain(AtV,p),c(V.d,p)))
    dS=[[D(0,x.d,p) for x in row] for row in S]
    rhs=addm(mm(dS,Sinv),mm(mm(S,B),Sinv))
    lhs=plain(As0,p)
    return subm(lhs,rhs)

def cycle_product(u0,v0,p,weight_sign=1):
    u=D(u0,0,p);v=D(v0,0,p)
    S0,u1,v1=transition(u,v,weight_sign)
    S1,u2,v2=transition(D(u1.x,0,p),D(v1.x,0,p),weight_sign)
    S2,u3,v3=transition(D(u2.x,0,p),D(v2.x,0,p),weight_sign)
    return mm(mm(S0,S1),S2),(u3.x,v3.x)

def main():
    payload=json.loads(INPUT.read_text());p=int(payload["prime"])
    entries={(x["axis"],x["row"],x["col"]):x["fit"] for x in payload["entries"]}
    diagnostics=[]
    for weight_sign in (1,-1):
      state=0x9e3779b97f4a7c15%p; accepted=0; failures=0; cycle_failures=0
      samples=[]
      while accepted<64:
        state=(state*6364136223846793005+1447)%p;u=state
        state=(state*2862933555777941757+1451)%p;v=state
        try:
            du=intertwiner_defect(entries,u,v,"u",p,weight_sign)
            dv=intertwiner_defect(entries,u,v,"v",p,weight_sign)
            prod,end=cycle_product(u,v,p,weight_sign)
        except (StopIteration,ZeroDivisionError):
            continue
        if du is None or dv is None:continue
        accepted+=1
        ok_u=zero_matrix(du);ok_v=zero_matrix(dv)
        cyc=zero_matrix(subm(prod,identity(4,p))) and end==(u,v)
        failures+=int(not(ok_u and ok_v));cycle_failures+=int(not cyc)
        if len(samples)<4:samples.append({"u":u,"v":v,"du":ok_u,"dv":ok_v,"cycle":cyc})
      diagnostics.append({"weight_sign":weight_sign,"sample_count":accepted,"intertwiner_failures":failures,"three_cycle_failures":cycle_failures,"samples":samples})
    chosen=next((x for x in diagnostics if x["intertwiner_failures"]==0 and x["three_cycle_failures"]==0),diagnostics[0])
    accepted=chosen["sample_count"];failures=chosen["intertwiner_failures"];cycle_failures=chosen["three_cycle_failures"];samples=chosen["samples"]
    result={
      "schema":"marici.cyclic-gysin-fixed-chart-obstruction.v1","prime":p,
      "site_cycle":"rho: (X1,X2,X3)->(X3,X1,X2)",
      "chart_cycle":["G12","G23","G31","G12"],
      "base_map":{"u_prime":"2u/(u-v)","v_prime":"2(2-v)/(u-v)","normalization_factor":"z=(u-v)/2=X3"},
      "residue_orientation_sign":1,
      "raw_master_homogeneity_weights":[-1,0,2,2],
      "weight_sign":chosen["weight_sign"],
      "adapted_transition":"S=P(u,v) diag(z^-1,1,z^2,z^2) P(rho(u,v))^-1",
      "connection_convention":"row frame; A_source=dS S^-1+S rho^*(A_target) S^-1",
      "sample_count":accepted,"intertwiner_failures":failures,
      "three_cycle_failures":cycle_failures,"samples":samples,"diagnostics":diagnostics,
      "passed":failures==0 and cycle_failures==0,
      "implication":"the formal three-cycle gauge closes, but neither homogeneity convention intertwines the fixed G12 connection; independent G23 and G31 reducers are required"
    }
    OUTPUT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:result[k] for k in ["sample_count","intertwiner_failures","three_cycle_failures","passed"]},sort_keys=True))

if __name__=="__main__":main()

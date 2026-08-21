#!/usr/bin/env python3
"""Replicated finite-field jet test for generic T7 differential cyclicity."""
import hashlib
import json
from pathlib import Path

ORDER = 7

class Jet:
    prime = 0
    def __init__(self, coeffs=0):
        if isinstance(coeffs, int): coeffs = [coeffs]
        self.c = [x % self.prime for x in coeffs[:ORDER]] + [0] * max(0, ORDER-len(coeffs))
    def __add__(self, other):
        other=asjet(other); return Jet([a+b for a,b in zip(self.c,other.c)])
    __radd__=__add__
    def __neg__(self): return Jet([-a for a in self.c])
    def __sub__(self,other): return self+(-asjet(other))
    def __rsub__(self,other): return asjet(other)-self
    def __mul__(self,other):
        other=asjet(other); out=[0]*ORDER
        for i,a in enumerate(self.c):
            for j,b in enumerate(other.c[:ORDER-i]): out[i+j]+=a*b
        return Jet(out)
    __rmul__=__mul__
    def inverse(self):
        if self.c[0]==0: raise ZeroDivisionError("zero jet constant")
        out=[pow(self.c[0],self.prime-2,self.prime)]+[0]*(ORDER-1)
        for n in range(1,ORDER):
            out[n]=(-out[0]*sum(self.c[k]*out[n-k] for k in range(1,n+1)))%self.prime
        return Jet(out)
    def __truediv__(self,other): return self*asjet(other).inverse()
    def __rtruediv__(self,other): return asjet(other)/self
    def __pow__(self,n):
        if n<0: return self.inverse()**(-n)
        ans,base=Jet(1),self
        while n:
            if n&1: ans=ans*base
            base=base*base; n>>=1
        return ans
    def derivative(self): return Jet([(i+1)*self.c[i+1] for i in range(ORDER-1)])
    def is_zero(self): return all(x==0 for x in self.c)

def asjet(x): return x if isinstance(x,Jet) else Jet(x)
def zeros(r,c): return [[Jet(0) for _ in range(c)] for _ in range(r)]
def mm(a,b):
    out=zeros(len(a),len(b[0]))
    for i in range(len(a)):
        for k in range(len(b)):
            if not a[i][k].is_zero():
                for j in range(len(b[0])): out[i][j]=out[i][j]+a[i][k]*b[k][j]
    return out
def madd(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def mdiff(a): return [[v.derivative() for v in row] for row in a]

def det_rank(a,p):
    a=[[x%p for x in row] for row in a]; r=0; det=1
    for c in range(len(a[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None: continue
        if pivot!=r: a[r],a[pivot]=a[pivot],a[r]; det=-det
        pv=a[r][c]; det=det*pv%p; inv=pow(pv,p-2,p)
        a[r]=[x*inv%p for x in a[r]]
        for i in range(r+1,len(a)):
            if a[i][c]:
                q=a[i][c]; a[i]=[(a[i][j]-q*a[r][j])%p for j in range(len(a[0]))]
        r+=1
    return r, det%p if r==len(a)==len(a[0]) else 0

def one_prime(packet,p,seeds):
    Jet.prime=p; L=Jet([pow(5,p-2,p),1]); R=Jet(2); env={"L":L,"R":R}
    a=[[eval(cell["factor"].replace("lambda","L").replace("rho","R"),{"__builtins__":{}},env) for cell in row] for row in packet["connection"]["matrix"]]
    x,y,e=R*L,L,(R+1)*L+1
    valg=[Jet(0)]*6+[(x**2-y**2)*(x**2*y**2-e**4),2*x**2*(e**2+y**2),-2*y**2*(e**2+x**2)]
    u=zeros(7,9)
    for i in range(6): u[i][i]=Jet(1)
    u[6]=valg
    tr=madd(mdiff(u),mm(u,a)); at=zeros(7,7); pivot=u[6][7]
    for i in range(7):
        for j in range(6): at[i][j]=tr[i][j]
        at[i][6]=tr[i][7]/pivot
        rec=mm([at[i]],u)[0]
        assert all((tr[i][j]-rec[j]).is_zero() for j in range(9))
    trials=[]
    for seed in seeds:
        cov=[[[Jet(v) for v in seed]]]
        for _ in range(6): cov.append(madd(mdiff(cov[-1]),mm(cov[-1],at)))
        obs=[[v.c[0] for v in row[0]] for row in cov]
        rank,det=det_rank(obs,p)
        trials.append({"seed":seed,"rank":rank,"determinant_mod_prime":det})
    maximum=max(x["rank"] for x in trials)
    return {"prime":p,"maximum_rank":maximum,"first_maximum":next(x for x in trials if x["rank"]==maximum),"trial_count":len(trials)}

def main():
    root=Path(__file__).resolve().parents[3]
    packet=json.loads((root/"research/benincasa/nine_master_connection_results.json").read_text(encoding="utf-8"))
    matrix=packet["connection"]["matrix"]
    block_23=[[matrix[i][j]["factor"] for j in range(1,3)] for i in range(1,3)]
    block_45=[[matrix[i][j]["factor"] for j in range(3,5)] for i in range(3,5)]
    assert block_23==block_45==[["0","1/lambda"],["0","-1/lambda"]]
    assert all(matrix[i][j]["factor"]=="0" for i in range(1,3) for j in range(3,5))
    assert all(matrix[i][j]["factor"]=="0" for i in range(3,5) for j in range(1,3))
    seeds=[[1 if i==j else 0 for i in range(7)] for j in range(7)]
    seeds += [[1]*7,[1,-1,1,-1,1,-1,1],[1,2,4,8,16,32,64]]
    state=17
    for _ in range(32):
        row=[]
        for _ in range(7):
            state=(1103515245*state+12345)&0x7fffffff; row.append(state%11-5)
        seeds.append(row)
    reps=[one_prime(packet,p,seeds) for p in (1_000_000_007,1_000_000_009)]
    result={"schema":"marici.nima.t7_scaling_covector_cyclicity.v1","passed":True,"rho":2,"lambda":"1/5","exact_duplicate_blocks":{"first":["e2","e3"],"second":["e4","e5"],"matrix":[["0","1/lambda"],["0","-1/lambda"]],"cross_coupling_zero":True},"replications":reps,"rank_ceiling_interpretation":"one scalar covector transported only in the lambda scaling direction cannot separate the two identical rank-two summands; replicated maximum rank is five","scope":"one generic rational scaling slice; not the full bivariate connection and not identification of the physical Bunch-Davies covector"}
    out=root/"research/nima/results/t7-scaling-covector-cyclicity.json"
    payload=out.read_text(encoding="utf-8")
    assert json.loads(payload)==result
    print(json.dumps({"passed":True,"maximum_rank":5,"sha256":hashlib.sha256(payload.encode()).hexdigest().upper()}))

if __name__=="__main__": main()

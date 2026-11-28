"""LP proposes certificates; accept only exact rational inequalities."""
from r37_structural_weights import weights,cores,combinations,F,Counter
from scipy.optimize import linprog
import numpy as np
from collections import defaultdict

def certify(R,keys):
    G=defaultdict(list)
    for r,k in zip(R,keys):G[k].append(r)
    A=np.array([[6*sum(not s&r for r in L)-len(L) for L in G.values()] for s in R]);m,n=A.shape
    res=linprog(np.ones(n),A_ub=-A,b_ub=-np.ones(m),method='highs');pos=res.success
    if not pos:
        res=linprog(np.zeros(m),A_ub=A.T,b_ub=np.zeros(n),A_eq=[np.ones(m)],b_eq=[1],method='highs');assert res.success
    def exact(x):
        if min(x)<0 or not any(x):return False
        mat=A if pos else -A.T
        vals=[sum(int(a)*v for a,v in zip(row,x) if v) for row in mat];return min(vals)>0 if pos else min(vals)>=0
    for den in (1000,100000,100000000):
        x=[F(float(t)).limit_denominator(den) for t in res.x]
        if exact(x):return pos,len(G),[(i,str(t)) for i,t in enumerate(x) if t]
    return None,len(G),[]
if __name__=='__main__':
    out=Counter()
    for idx,rec in enumerate(cores):
        a=rec['core'];R=sorted(sum(1<<i for i in t) for t in combinations(range(16),5) if all(not a[i]>>j&1 for i,j in combinations(t,2)));ws=weights(set(R));faces=Counter(r^(1<<i) for r in R for i in range(16) if r>>i&1);keys=[[ws[0][r] for r in R],[tuple(sorted(faces[r^(1<<i)] for i in range(16) if r>>i&1)) for r in R],[ws[2][r] for r in R]]
        for name,key in zip(('size','face profile','squares','joint'),[*keys,list(zip(*keys))]):
            ok,n,cert=certify(R,key);out[name,ok]+=1
            if idx==0:print(name,ok,n,'witness',[(R[i],v) for i,v in cert] if ok==False else len(cert),flush=True)
    print(out)

"""Prefer exact pair obstruction; give rank and risk rules extra information."""
from r37_shared_triple import *
from fractions import Fraction

def block(R,K,ids):
    A=np.zeros((len(R),len(ids)),dtype=int);G=defaultdict(list)
    for q,k in zip(R,K):G[k].append(q)
    for k,L in G.items():A[:,ids[k]]=[6*sum(not s&q for q in L)-len(L) for s in R]
    return A

def evidence(A):
    n,m=A.shape;sol=linprog(np.ones(m),A_ub=-A,b_ub=-np.ones(n));
    if sol.success:
        x=np.rint(sol.x*10**7).astype('int64');assert min(x)>=0 and min(A@x)>0;return True
    assert sol.status==2;dual=linprog(np.zeros(n),A_ub=A.T,b_ub=np.zeros(m),A_eq=[np.ones(n)],b_eq=[1]);assert dual.success
    for bound in (10000,10**8):
        y=[(i,F(float(t)).limit_denominator(bound)) for i,t in enumerate(dual.x) if t>1e-10];
        if sum(t for i,t in y)>0 and all(sum(int(A[i,j])*t for i,t in y)<=0 for j in range(m)):return False
    raise ValueError('no exact dual')
if __name__=='__main__':
 ds=[data(c['core']) for c in cores];eligible=[i for i,(R,K,z) in enumerate(ds) if certify(R,K)[0]];ids={k:i for i,k in enumerate(sorted({k for R,K,z in ds for k in K}))};B={};stats=Counter()
 for i in eligible:
    R,K,risk=ds[i];B[i]=block(R,K,ids);scores=[sum(F(1,t) for t in k) for k in K];levels=sorted(set(scores));# monotone weights are nonnegative sums of upper-tail indicators
    A=np.array([[sum(6*(not r&q)-1 for q,v in zip(R,scores) if v>=s) for s in levels] for r in R]);stats['best monotone rank',evidence(A)]+=1
    if risk:stats['in-core risk',margin(R,[risk[k] for k in K])[0]>0]+=1
 for i,j in combinations([33,35,36],2):print('pair',i,j,evidence(np.vstack([B[i],B[j]])))
 for i,j in combinations(eligible,2):
    if not evidence(np.vstack([B[i],B[j]])):
        print('first incompatible pair',i,j);break
 else:print('all pairs compatible')
 print(stats)

"""Retain which triples meet at a vertex, not its label. Check ties vs ordering."""
from r37_profile_stress import *

def split(R,K):
 T=[[t for t in combinations([i for i in range(16) if r>>i&1],3)] for r in R];C=Counter(t for L in T for t in L)
 return [(k,tuple(sorted(tuple(sorted(C[t] for t in L if i in t)) for i in range(16) if r>>i&1))) for r,k,L in zip(R,K,T)]

def pool(ds,I,common):
 keys=[split(ds[i][0],ds[i][1]) for i in I];sets=list(map(set,keys));allkeys=set.union(*sets);sel=set.intersection(*sets) if common else allkeys;ids={k:j for j,k in enumerate(sorted(allkeys))};J=[ids[k] for k in sel];A=np.vstack([block(ds[i][0],K,ids) for i,K in zip(I,keys)]);return len(sel),evidence(A[:,J]) if J else False

if __name__=='__main__':
 ds=[data(c['core']) for c in cores];stats=Counter()
 for R,K,risk in ds:
    if not certify(R,K)[0]:continue
    scores=[sum(F(1,t) for t in k) for k in K];ok,n,_=certify(R,scores);stats['unrestricted rarity',ok]+=1
    z=[risk[k] for k in K];levels=sorted(set(z));A=np.array([[sum(6*(not r&q)-1 for q,v in zip(R,z) if v>=s) for s in levels] for r in R]);stats['monotone in-core risk',evidence(A)]+=1
 for I in ([6,9],[33,35,36]):print(I,'all split keys',pool(ds,I,False),'shared keys alone',pool(ds,I,True))
 print(stats)

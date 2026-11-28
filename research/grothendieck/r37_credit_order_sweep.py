"""Freeze union-of-credits semantics, vary witness size; no miss labels in proxy construction."""
from r37_profile_stress import cores,combinations,evidence,np,Counter
from functools import reduce
from operator import or_
mask=lambda v:sum(1<<i for i in v);stats=Counter();levels={}
for idx,rec in enumerate(cores):
 a=rec['core'];V=[s for s in combinations(range(16),5) if all(not(a[i]>>j&1) for i,j in combinations(s,2))];R=list(map(mask,V));passes=[]
 for k in range(1,6):
    groups={}
    for s,r in zip(V,R):
        for t in combinations(s,k):groups[t]=groups.get(t,0)|r
    forbid=[[groups[t] for t in combinations(s,k)] for s in V];A=np.array([[6*any(not u&q for u in L)-1 for q in R] for L in forbid]);ok=evidence(A)
    if ok:levels[idx]=k;break
 assert idx in levels
print('first sufficient order',Counter(levels.values()),'pair failures',[i for i,k in levels.items() if k>2]);
from r37_core19_pairs import R,V,G,tight
for key,rows in G.items():
 hits=[mask(s) for s in rows if all(mask(s)&q for q in tight)]
 if not hits:continue
 P={t for s in rows for t in combinations(s,2)};cand=[s for s in combinations(range(16),5) if all(t in P for t in combinations(s,2))];mins=[next(k for k in range(1,6) if any(all(mask(t)&q for q in tight) for t in combinations([j for j in range(16) if r>>j&1],k))) for r in hits];print('hit rows',hits,'min hit sizes',mins,'class vs clique counts',len(rows),len(cand))

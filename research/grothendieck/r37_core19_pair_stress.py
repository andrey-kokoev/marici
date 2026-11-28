from r37_core19_pairs import R,V,G,d,tight,combinations
mask=lambda v:sum(1<<i for i in v)
v=V[R.index(9349)];triples=[mask(t) for t in combinations(v,3)]
for k in range(1,15):
    sols=[S for S in combinations(tight,k) if all(any(not s&t for s in S) for t in triples)]
    if sols:print('minimum negative certificates',k,'example',sols[0]);break
rows=G[tuple(sorted(d[j] for j in v))];P={t for row in rows for t in combinations(row,2)};possible=[list(s) for s in combinations(range(16),5) if all(t in P for t in combinations(s,2))];print('positive pair cliques',possible);assert possible==sorted(rows)
for s in possible:print('row',mask(s),'private sites',[i for i in s if sum(i in t for t in rows)==1],'all hit',all(mask(s)&q for q in tight))
# Even allowing the best pair per individual row, only positive proxy credits count.
credits={mask(t):{q for q in R if all(not(q&r) for r in R if mask(t)&r==mask(t))} for t in combinations(range(16),2) if any(mask(t)&r==mask(t) for r in R)}
U={r:set.union(*(credits[mask(t)] for t in combinations(s,2))) for r,s in zip(R,V)};print('empty pooled rows',sum(not u for u in U.values()),'worst size',min(map(len,U.values())))
from r37_profile_stress import evidence,np
A=np.array([[6*int(q in U[r])-1 for q in R] for r in R]);print('pooled certificate exists',evidence(A),'eligible cells',sum(map(len,U.values())),'actual miss cells',sum(not(r&q) for r in R for q in R))

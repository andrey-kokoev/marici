"""Audit published witnesses; seek finite-distance failure even with arbitrary column swaps."""
from itertools import combinations
from pathlib import Path
from collections import Counter,deque,defaultdict
import json
cores=json.loads((Path(__file__).resolve().parents[1]/'voevodsky/results/ramsey_37_catalogue_free.json').read_text())['certificates']
for idx in [0,6,25]:
 a=cores[idx]['core'];R=sorted(sum(1<<i for i in t) for t in combinations(range(16),5) if all(not a[i]>>j&1 for i,j in combinations(t,2)));M={r:{q for q in R if not q&r} for r in R};V={r:sum(1<<(3*i) for i in range(16) if r>>i&1) for r in R};target=sum((6-v.bit_count())<<(3*i) for i,v in enumerate(a))
 if idx==0:
    A={r:[q for q in R if (q^r).bit_count()==2] for r in R};dist={}
    for r in R:
        Q=deque([r]);dist[r,r]=0
        while Q:
            v=Q.popleft()
            for q in A[v]:
                if (r,q) not in dist:dist[r,q]=dist[r,v]+1;Q.append(q)
    B=defaultdict(list)
    for t in combinations(R,3):B[sum(V[r] for r in t)].append(t)
    def witness():
        for k,L in B.items():
            for t in L:
                for s in B.get(target-k,[]):
                    if t[-1]>=s[0]:continue
                    T=t+s;P=list(combinations(T,2));d=min(dist.get(p,999) for p in P);near=[p for p in P if dist.get(p,999)==d];far=[(p,min(M[p[0]]&M[p[1]])) for p in P if M[p[0]]&M[p[1]] and p in dist]
                    if d<999 and far and all(not M[x]&M[y] for x,y in near):return T,d,near,far[0],dist[far[0][0]]
    print('all swaps',witness())
 elif idx==6:
    T=[4156,5056,28684,33925,34890,36608];assert sum(V[r] for r in T)==target
    h=Counter(sum(q in M[r] for r in T) for q in R);print('miss histogram',h)
    for name,w in [('miss opportunities',{q:1+len(M[q]) for q in R}),('hit opportunities',{q:1+len(R)-len(M[q]) for q in R})]:print(name,sum(w[q] for r in T for q in M[r]),sum(w.values()))
 else:
    T=[12449,16978,28720,33925,34827,35648];r,s,t,u=16978,34827,33362,18443;assert sum(V[x] for x in T)==target==sum(V[x] for x in set(T)-{r,s}|{t,u});
    print('square aligned, mixed',[(x,y,sorted(M[x]&M[y])) for x,y in [(r,s),(t,u),(r,u),(t,s)]])

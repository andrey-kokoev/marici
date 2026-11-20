"""Test for one global ground-label transport on independently generated 11-step paths, not prescribed mirror partners. Align both half-paths from the same pole. Compare S6 and the geometric S4 subgroup. Separate gate evidence from full interior evidence and residual closure."""
from itertools import permutations,combinations
from collections import Counter
from ramsey_strip_prism_proof import X,P,T,r
s,t=0,29
N=[set() for _ in r]
for i,d in enumerate(P):
 for j,m in enumerate(T,15):
    if d in m:N[i].add(j);N[j].add(i)
paths=[]
def walk(p):
 if len(p)==12:
    if p[-1]==t:paths.append(p)
    return
 if p[-1]!=t:
    for y in N[p[-1]]-set(p):walk(p+(y,))
walk((s,));tet={tuple(X.index(tuple(sorted(p[i] for i in x))) for x in X) for p in permutations(range(4))};acts=[]
for p in permutations(range(6)):
 tr=lambda d:tuple(sorted(p[i] for i in d));a=tuple([P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,m)))) for m in T]);
 if a[s]==s and a[t]==t:acts.append((a,p in tet))
print('endpoint stabilizers S6,S4',len(acts),sum(k for a,k in acts));H=Counter();prefix=Counter();bad=[]
for p,q in combinations(paths,2):
 if not set(p[1:-1]).isdisjoint(q[1:-1]):continue
 gate=p[1]==r[q[1]] and p[-2]==r[q[-2]];exact=tuple(r[v] for v in p)==q;hs=[(a,k) for a,k in acts if all(a[x]==y for x,y in zip(p,q))];H[gate,exact,bool(hs)]+=1
 if gate and not exact:bad.append({i for i in range(2,10) if r[p[i]]!=q[i]})
 if exact:
    candidates=[a for a,k in acts];trace=[]
    for x,y in zip(p[1:-1],q[1:-1]):candidates=[a for a in candidates if a[x]==y];trace.append(len(candidates))
    assert candidates==[tuple(r)];prefix[tuple(trace[:3])]+=1
print('gate matches, exact swap, any S6 transport',H,'exact prefix counts',prefix)
for k in range(9):
 tests=[I for I in combinations(range(2,10),k) if all(set(I)&b for b in bad)]
 if tests:break
print('minimal extra interior checkpoints given both gates',tests)

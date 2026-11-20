"""Test nonbacktracking directly against both joins in all frames; count sites at which predecessor's cut side disambiguates arrival. Do not assume the strip's B is a graph vertex or a particular block."""
from ramsey_37_middle_support_recovery import V,E,pairs,D
from itertools import combinations
from collections import Counter
import json
N={v:{x for x in V if tuple(sorted((v,x))) in E} for v in V};assert all(len(n)==2 for n in N.values());circuits=[];remaining=set(V)
while remaining:
    a=min(remaining);b=min(N[a]);c=[a];u,v=a,b
    while v!=a:
        c.append(v);u,v=v,next(iter(N[v]-{u}))
    remaining.difference_update(c);circuits.append(c)
count=0
for pair in pairs:
    for F,G in (pair,pair[::-1]):
        mate={next(t for t in G if not s&t):s for s in F};step={s:mate[next(t for t in G if len(s&t)==1)] for s in F}
        for s in F:
            q=s
            for _ in range(4):
                q=step[q];u,=s&q;v,=step[s]&step[q];w,=step[step[s]]&step[step[q]]
                if v in N[u]:assert N[v]-{u}=={w};count+=1
hist=Counter(sum(len(N[v]&set(A))==1 for v in V) for A in combinations(V,3));out=dict(circuits=circuits,joined=count,resolved_sites_hist=dict(hist));print(out);(D/'ramsey_37_strip_arrival_bit.json').write_text(json.dumps(out,indent=2)+'\n')

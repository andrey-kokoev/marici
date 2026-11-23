"""Minimal-support geodesic criterion pilot at the exceptional Exoo deletion. Detect the bridge in endpoint difference coordinates and validate majority control."""
from exoo39_symbolic_relations import edges
from itertools import combinations
from pathlib import Path
from functools import reduce
from operator import and_,or_
import json
D=Path(__file__).parent;E=edges();H=[sum(1<<j for j in range(39) if tuple(sorted((i,j))) in E) for i in range(39)];I=[0]
for i,h in enumerate(H):
    if i!=37:I.extend([s|1<<i for s in I if not s&h]);
T=[s for s in I if s.bit_count()==9];B={s for s in I if all(s&t for t in T)};fixed=reduce(and_,B);V=reduce(or_,B)^fixed;B={s^fixed for s in B};ls=lambda s:[i for i in range(39) if s>>i&1];mins=lambda Z:sorted(s for s in Z if not any(t!=s and t&s==t for t in Z));M=mins(B);rows=mins({t&V for t in T if not t&fixed});paths={};exception=[]
for p,q in combinations(M,2):
    if p|q in B:
        route=[p];z=p
        for i in ls(q&~p)+ls(p&~q):z^=1<<i;route.append(z)
    else:
        r,=[m for m in M if m not in (p,q) and not m&~(p|q) and (m|p) in B and (m|q) in B];route=[p,p|r,r,q|r,q];exception.append(dict(start=ls(p),destination=ls(q),bridge=ls(r),path=list(map(ls,route))))
    assert all(s in B for s in route) and all((a^b).bit_count()==1 for a,b in zip(route,route[1:])) and len(route)-1==(p^q).bit_count();paths[p,q]=route;paths[q,p]=route[::-1]
# Lift the support proof to every ordered pair by fixing the common part throughout.
for s in B:
 for t in B:
    p=next(k for k in M if k&s==k);q=next(k for k in M if k&t==k);c=s&t;route=[s];z=s
    for i in ls(s&~(c|p)):z^=1<<i;route.append(z)
    for v in paths.get((p,q),[p]):
        if v|c!=route[-1]:route.append(v|c)
    z=route[-1]
    for i in ls(t&~z):z^=1<<i;route.append(z)
    assert all(v in B for v in route) and route[-1]==t and all((a^b).bit_count()==1 for a,b in zip(route,route[1:])) and len(route)-1==(s^t).bit_count()
bad=next(((a,b,c) for a,b,c in combinations(M,3) if (a&b|a&c|b&c) not in B),None);r=dict(states=len(B),fixed=ls(fixed),minimal_rows=list(map(ls,rows)),minimum_supports=list(map(ls,M)),exception=exception,verified_ordered_pairs=len(B)**2,majority_counterexample=list(map(ls,bad)) if bad else None);print(r);(D/'ramsey_exoo37_support_bridge.json').write_text(json.dumps(r,indent=2)+'\n')

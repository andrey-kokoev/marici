"""Resolve the six-label duad wiring into five synthemes covering K6; test its ternary readout and dihedral cyclic compression."""
from itertools import combinations,permutations,product
from collections import Counter,defaultdict
from pathlib import Path
import json
D=Path(__file__).parent
P=list(combinations(range(6),2));T=[t for t in combinations(range(15),3) if len(set(x for i in t for x in P[i]))==6];pent=next(t for t in combinations(range(15),5) if len({v for j in t for v in T[j]})==15);W=[]
def dfs(q,mask):
    if len(q)==15:W.append(tuple(q));return
    for v in T[len(q)]:
        if not mask>>v&1:dfs(q+[v],mask|1<<v)
dfs([],0);assert len(W)==288
proj=lambda w,t:tuple(w[i] for i in t);g=defaultdict(list)
for w in W:g[proj(w,pent)].append(w)
# Minimal fixed number of additional partition probes after the five.
rest=[j for j in range(15) if j not in pent];extra=next(t for n in range(11) for t in combinations(rest,n) if all(len({proj(w,t) for w in a})==len(a) for a in g.values()));minimal=next(t for n in range(6,16) for t in combinations(range(15),n) if len({proj(w,t) for w in W})==288)
# Test whether distinguishing a global symmetry frame changes the picture.
cyc=next(p for p in permutations(range(6)) if sum(i==v for i,v in enumerate(p))==1 and all(p[p[p[p[p[i]]]]]==i for i in range(6)) and {tuple(sorted(P.index(tuple(sorted((p[a],p[b])))) for a,b in [P[v] for v in T[j]])) for j in pent}=={T[j] for j in pent});act=[P.index(tuple(sorted((cyc[a],cyc[b])))) for a,b in P];dest=[T.index(tuple(sorted(act[v] for v in t))) for t in T];inv=[w for w in W if all(w[dest[j]]==act[w[j]] for j in range(15))];out={'pentad':[[P[v] for v in T[j]] for j in pent],'histogram':dict(Counter(map(len,g.values()))),'codes':len(g),'extra':extra,'first_minimal_ternary_list':[T[j] for j in minimal],'minimal_count':len(minimal),'cycle':cyc,'invariant_wirings':len(inv),'invariant_codes':len({proj(w,pent) for w in inv})};print(out);(D/'ramsey_pentad_readout.json').write_text(json.dumps(out)+'\n')

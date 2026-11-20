"""Minimum certificate menu. A signature covers the clique (including loops) on types supporting it. Remove contained supports, then exhaust every way to cover a least-choice uncovered pair, at increasing depth. Input: iteration 5 exceptions + corresponding aligned old adjacency. No edge-color completion oracle."""
from itertools import combinations,combinations_with_replacement
from functools import lru_cache
from pathlib import Path
import json
H=Path(__file__).parent;load=lambda name:json.loads((H/name).read_text());hosts={(h['record'],tuple(h['order'])):h['N'] for h in load('ramsey_strict_aligned_hosts.json')};out=[]
for row in load('ramsey_signature_core.json'):
    N=hosts[row['record'],tuple(row['order'])];T=row['partners'];V=range(16);supports={}
    for five in combinations(V,5):
        F=sum(1<<x for x in five)
        if any(N[x]&F for x in five):continue
        for r in V:
            mask=sum(1<<i for i,(a,b,_) in enumerate(T) if any(s>>r&1 and not s&F for s in (a,b)))
            if mask:supports.setdefault(mask,(r,five))
    maximal=[m for m in supports if not any(m!=k and m&k==m for k in supports)];pairs=list(combinations_with_replacement(range(len(T)),2));cov=[sum(1<<k for k,(i,j) in enumerate(pairs) if m>>i&m>>j&1) for m in maximal];opts=sorted(([i for i,c in enumerate(cov) if c>>k&1],k) for k in range(len(pairs)));opts.sort(key=lambda x:len(x[0]));assert all(o for o,k in opts);full=(1<<len(pairs))-1
    @lru_cache(None)
    def choose(rem,d):
        if not rem:return ()
        if d==0:return None
        o=next(o for o,k in opts if rem>>k&1)
        for i in sorted(o,key=lambda j:-(cov[j]&rem).bit_count()):
            t=choose(rem&~cov[i],d-1)
            if t is not None:return (i,)+t
    for d in range(1,len(cov)+1):
        t=choose(full,d)
        if t is not None:break
    assert len(t)==d and all(any(cov[i]>>k&1 for i in t) for k in range(len(pairs)));menu=[supports[maximal[i]] for i in t];assert all(any(all(any(s>>r&1 and not any(s>>x&1 for x in f) for s in T[j][:2]) for j in pair) for r,f in menu) for pair in pairs)
    out.append(dict(record=row['record'],center=row['center'],partners=len(T),maximal_supports=len(cov),minimum=d,menu=menu));print(row['record'],len(T),len(cov),d)
(H/'ramsey_certificate_menu.json').write_text(json.dumps(out,indent=2)+'\n')

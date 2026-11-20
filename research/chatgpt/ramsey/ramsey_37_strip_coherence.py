"""Tests of two specified interpretations only. Input is unmarked graph data, not an observed strip order. Search fixed-point-free automorphisms of order 2; independently match blue pairs certified by a common red neighbor. Null: mean fraction of certified pairs for a uniformly random pairing."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
import json
H=Path(__file__).parent;rows=[]
for idx,line in enumerate((H/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines(),1):
    bits=''.join(f'{ord(x)-63:06b}' for x in line[1:]);V=range(22);N=[set() for i in V];pairs=list(combinations(V,2))
    for i,j in pairs:
        if bits[j*(j-1)//2+i]=='1':N[i].add(j);N[j].add(i)
    sig=[(len(n),sorted(len(N[i]) for i in n)) for n in N]
    def sym(left,p):
        if not left:return p
        opts=[([j for j in left if i!=j and sig[i]==sig[j] and all((a in N[i])==(b in N[j]) for a,b in p.items())],i) for i in left];js,i=min(opts,key=lambda z:len(z[0]))
        for j in js:
            r=sym(left-{i,j},p|{i:j,j:i})
            if r:return r
    p=sym(set(V),{});good={ (i,j):min(N[i]&N[j]) for i,j in pairs if N[i]&N[j]};assert all(j not in N[i] for i,j in good)
    @lru_cache(None)
    def match(left):
        if not left:return ()
        i=left[0]
        for j in left[1:]:
            if (i,j) in good:
                m=match(tuple(x for x in left[1:] if x!=j))
                if m is not None:return ((i,j,good[i,j]),)+m
    m=match(tuple(V));rows.append(dict(record=idx,swap=p,matching=m,certified=len(good)))
print('swap',sum(bool(x['swap']) for x in rows),'matching',sum(bool(x['matching']) for x in rows),'mean random certified pairs',sum(x['certified'] for x in rows)/(21*len(rows)));(H/'ramsey_37_strip_coherence.json').write_text(json.dumps(rows,separators=(',',':'))+'\n')

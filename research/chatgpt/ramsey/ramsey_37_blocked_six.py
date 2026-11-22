"""All ordered-count collisions: test blocked independent six on losing side. Diagnose remaining failures by the smallest jointly un-hittable family up to size two; distinguish directly red queried pairs."""
from pathlib import Path
from itertools import combinations, product
from collections import Counter
import csv,json
D=Path(__file__).parent

def core(name):
    with (D/f'ramsey_3_7_{name}_22.csv').open() as f:m=list(csv.reader(f));m=[list(map(int,row)) for row in m]
    o=[0]+sorted(range(1,21),key=lambda i:(-m[0][i],i));h=[sum(m[i][v]<<j for j,v in enumerate(o)) for i in o];I=[0]
    for v,r in enumerate(h):I.extend([s|1<<v for s in I if not s&r]);
    T=[s for s in I if s.bit_count()==6];B=[s for s in I if all(s&t for t in T)];assert len(B)==1;return h,I,T,B[0]

def labels(s):return [i for i in range(21) if s>>i&1]
G=[core(n) for n in ('pair_rotation','target_two_rings')];records=[];cert={}
for (a,b),(c,d) in product(combinations(range(1,7),2),combinations(range(7,21),2)):
    q=1<<a|1<<c;ans=[s&q==q for h,I,T,s in G];reads=[[(h[a]>>c&1)+(h[b]>>d&1),(h[a]>>d&1)+(h[b]>>c&1)] for h,I,T,s in G]
    if ans[0]==ans[1] or reads[0]!=reads[1]:continue
    side=ans.index(False);h,I,T,s=G[side];key=f'{side}:{a},{c}';blocked=[t for t in T if not t&~(h[a]|h[c])];direct=bool(h[a]>>c&1);case='both' if blocked and direct else 'six' if blocked else 'edge' if direct else 'neither';entry=dict(case=case,blocked_count=len(blocked),six=labels(blocked[0]) if blocked else None);assert not any(not t&~(G[1-side][0][a]|G[1-side][0][c]) for t in G[1-side][2]);
    if case=='neither':
        S=[x for x in I if x&q==q];U=(1<<len(S))-1;hit={t:sum(1<<j for j,x in enumerate(S) if x&t) for t in T};cover=next(((t,u) for t,u in combinations(T,2) if not hit[t]&hit[u]),None);entry.update(two_rows=[labels(t) for t in cover] if cover else None,candidate_neighborhoods=len(S))
    cert[key]=entry;records.append(dict(layout=[a,b,c,d],key=key))
assert len(records)==24;r=dict(layouts=records,certificates=cert,counts=dict(Counter(cert[x['key']]['case'] for x in records)));print(r['counts'],cert);D.joinpath('ramsey_37_blocked_six.json').write_text(json.dumps(r,indent=2)+'\n')

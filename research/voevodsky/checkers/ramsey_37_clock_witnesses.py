"""Freeze probe: red adjacency to the same slot one clock tick away. Compare both signs, both poles, both tick lengths and all rotation-compatible transversals."""
from pathlib import Path
import json,sys
from collections import Counter
H=Path(__file__).resolve().parents[1];D=H/'results';g=json.loads((D/'ramsey_37_dual_stars.json').read_text());a=json.loads((D/'ramsey_37_star_addresses.json').read_text());sys.path.insert(0,str(H.parent/'chatgpt/ramsey'));import check_ramsey_six_direction_bitransversals as w
rows=g['rows'];r=list(range(22));
for row in rows:
    for k,u in enumerate(row):r[u]=row[(k+1)%5]
def step(u,k):
    for _ in range(k%5):u=r[u]
    return u
E={tuple(e) for e in g['red_edges']};edge=lambda u,v:tuple(sorted((u,v))) in E
checks=[]
for pole in ('pole0','pole6'):
    for i,star in enumerate(a[pole]):
        for d,u in zip(a['powers'],star):
            observed=[edge(u,step(u,k)) for k in (1,-1,2,-2)];assert observed==[abs(d)==2]*2+[abs(d)==1]*2;checks.append(dict(pole=pole,frame=i,address=d,vertex=u,red_at_ticks=observed))
patterns=Counter()
for deleted in w.enumerate_transversals():
    A=w.graph(deleted);red=lambda u,v:(A[u]>>v)&1
    if not all(red(u,v)==red(r[u],r[v]) for u in range(22) for v in range(u)):continue
    patterns[str(tuple(tuple(red(row[0],row[k]) for k in (1,2)) for row in rows[1:3]))]+=1
out=dict(ticks=[1,-1,2,-2],checks=checks,all_rotating_examples_side_then_diagonal_patterns=patterns);(D/'ramsey_37_clock_witnesses.json').write_text(json.dumps(out,indent=2)+'\n');print(patterns)

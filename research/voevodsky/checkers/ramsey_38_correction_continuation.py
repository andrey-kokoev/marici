"""No-reuse correction sequences = matchings in Z x W. Compare terminal parity with one-step counts, maximum future depth, and the lengths at which choices can get stuck. Test all residual states, not just the first turn. Reuse of the hub is permitted."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'ramsey_38_disk_routes_layer.json').read_text());E=set(map(tuple,json.loads((D/'ramsey_38_root_glue.json').read_text())['witness']['plus_edges']));red=lambda a,b:tuple(sorted((a,b))) in E
out=[]
for row in rows:
    Z=sorted(row['layer']);h=row['hub'];W=sorted(set(range(27))-set(Z+row['ring']+row['poles']+[h]));L=(1<<len(Z))-1;R=(1<<len(W))-1
    adj=[sum(1<<j for j,w in enumerate(W) if not red(z,w)) for z in Z];assert all(red(h,z) for z in Z) and not any(red(h,w) for w in W)
    def moves(a,b):return [(i,j) for i in range(len(Z)) if a>>i&1 for j in range(len(W)) if adj[i]&b&(1<<j)]
    @lru_cache(None)
    def terminal_depths(a,b):
        m=moves(a,b);return frozenset(d+1 for i,j in m for d in terminal_depths(a^(1<<i),b^(1<<j))) if m else frozenset([0])
    initial=moves(L,R);first=[]
    for i,j in initial:
        a,b=L^(1<<i),R^(1<<j);first.append(dict(move=[Z[i],W[j]],next_count=len(moves(a,b)),terminal_depths=sorted(terminal_depths(a,b))))
    out.append(dict(poles=row['poles'],ring=row['ring'],Z=Z,W=W,unused_external=[w for j,w in enumerate(W) if not any(k==j for _,k in initial)],terminal_depths=sorted(terminal_depths(L,R)),first=first));terminal_depths.cache_clear()
print('terminal length sets',Counter(tuple(o['terminal_depths']) for o in out));print('all choices full max',sum(all(max(f['terminal_depths'])==len(o['Z'])-1 for f in o['first']) for o in out));print('distinct next counts',Counter(len({f['next_count'] for f in o['first']}) for o in out));print('first example',[(v,next(f['move'] for f in out[0]['first'] if f['next_count']==v)) for v in sorted({f['next_count'] for f in out[0]['first']})]);print('unused external',Counter(len(o['unused_external']) for o in out));(D/'ramsey_38_correction_continuation.json').write_text(json.dumps(out,indent=2)+'\n')

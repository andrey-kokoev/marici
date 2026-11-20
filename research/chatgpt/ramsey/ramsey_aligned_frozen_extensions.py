"""Exhaust all one-pair extensions of each previously saved intermediate host, holding every old pair fixed. Read only that stage's edges in solve(); no target witness or catalogue. Positive-control check on deletion of final pair, not used to construct the input stages."""
from pathlib import Path
from itertools import combinations
import json
H=Path(__file__).parent

def solve(n,edges):
    N=[0]*n
    for i,j in edges:N[i]|=1<<j;N[j]|=1<<i
    A=[0]
    for i in range(n):A += [s|1<<i for s in A if not s&N[i]]
    assert max(x.bit_count() for x in A)<=6
    fives=[s for s in A if s.bit_count()==5];sixes=[s for s in A if s.bit_count()==6];ans={'blue':0,'red':0};hit=0;example=None
    for s in A:
        if any(not s&f for f in sixes):continue
        hit+=1;t=((s&0x555555)<<1)|((s&0xaaaaaa)>>1)
        for name,ok in [('red',not s&t),('blue',all(f&(s|t) for f in fives))]:
            if not ok:continue
            ans[name]+=1
            if example is None:example=dict(pair=name,S=[i for i in range(n) if s>>i&1]);
    return dict(n=n,independent_hitting_sets=hit,attachments=ans,first=example)
rows=json.loads((H/'ramsey_aligned_blind.json').read_text());out=[solve(r['n'],r['edges']) for r in rows[:-1]];last=rows[-1];control=solve(20,[e for e in last['edges'] if max(e)<20]);assert sum(control['attachments'].values())>=1
for r in out+[control]:print(r['n'],r['independent_hitting_sets'],r['attachments'])
(H/'ramsey_aligned_frozen_extensions.json').write_text(json.dumps(dict(stages=out,deletion_control=control),indent=2)+'\n')

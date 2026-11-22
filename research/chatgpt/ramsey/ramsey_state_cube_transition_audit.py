"""Replay transition claims directly on saved probe-ordered states, including signed-permutation determinant (distance preservation alone allows reflections)."""
from pathlib import Path
from collections import defaultdict,Counter
from itertools import combinations
import json
D=Path(__file__).parent;r=json.loads((D/'ramsey_nine_frame_readout.json').read_text());W=r['coordinate_ordered_wirings'];P=r['actions'];dist=defaultdict(Counter)
for a,b in combinations(range(8),2):dist[(a^b).bit_count()][(W[a]^W[b]).bit_count()]+=1
for p in P:
    c=p[0];axis=[p[1<<i]^c for i in range(3)];assert set(axis)=={1,2,4} and (sum(a>b for a,b in combinations(axis,2))+c.bit_count())%2==0;assert all(p[s]==c^sum(axis[i] for i in range(3) if s>>i&1) for s in range(8))
assert len(set(map(tuple,P)))==24;r=dict(distances={k:dict(v) for k,v in dist.items()},proper_rotations=len(P),translations=[p[0] for p in P if all(p[i]==i^p[0] for i in range(8))]);print(r);Path(__file__).with_suffix('.json').write_text(json.dumps(r)+'\n')

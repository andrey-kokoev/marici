"""Which orientation flags follow just from typed stage words, vertex memberships and two shared-leg supports? Do not treat candidate reordered windows as source operations."""
from itertools import permutations,product
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];W=json.loads((D/'results/pne_kind_index_projection.json').read_text())['windows'];types=['CMC','MCM','MCC'];choices=[[p for p in permutations(w) if ''.join(s[0] for s in p)==t] for w,t in zip(W,types)];rows=[]
for ws in product(*choices):
 edges=[list(zip(w,w[1:])) for w in ws];ans=[]
 for a,b in zip(edges,edges[1:]):
  pairs=[(x,y) for x in a for y in b if set(x)==set(y)]
  if len(pairs)!=1:break
  x,y=pairs[0];ans.append('same' if x==y else 'opposite')
 if len(ans)==2:rows.append(dict(words=ws,outer=ans))
assert len({tuple(r['outer']) for r in rows})==len(rows)==4;o=dict(scope='typed words + named sites + shared leg supports only',actual=W,candidates=rows);print(rows);(D/'results/pne_window_order_provenance.json').write_text(json.dumps(o,indent=2)+'\n')

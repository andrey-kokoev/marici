"""Act on all ordered distinct Ramsey source labels, without fitting a target edge. Compare orbit size with eight directed M edges, then test the stronger endpoint reversal condition forced by A=stay."""
from pathlib import Path
from itertools import permutations
import json
D=Path(__file__).resolve().parents[1];A=(1,0,3,2,4,5,6);B=(1,0,2,3,5,4,6);C=(0,1,4,5,2,3,6);gs=[A,B,C];act=lambda g,p:tuple(g[i] for i in p);remain=set(permutations(range(7),2));rows=[]
while remain:
 q=[min(remain)]
 for p in q:
  for g in gs:
   t=act(g,p)
   if t not in q:q.append(t)
 remain.difference_update(q); rows.append(dict(orbit=q,size=len(q),reversed_by_A=sum(act(A,p)==p[::-1] for p in q)))
raw=json.loads((D/'results/pne_m_site_transport.json').read_text());
for row in raw:
 M=row['by']['M0'];T=row['by']['M1'];edges={(x,r['to']) for x,rs in M.items() for r in rs};assert len(edges)==8 and all((b,a) in edges and any(s['cell']==r['cell'] and s['to']==a for s in T[b]) for a,rs in M.items() for r in rs for b in [r['to']])
print([(r['orbit'][0],r['size'],r['reversed_by_A']) for r in rows]);(D/'results/ramsey_pne_ordered_pair_orbits.json').write_text(json.dumps(rows,indent=2)+'\n')

"""Fix the first PN entry before any exit decision. On the previously validated five-tick spine NE is a branch, not the reader's successor. Select its early/late address independently at each tick. Count marked contact events (not all incidental links among packets)."""
import itertools,json
from collections import Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';load=lambda k:json.loads((D/(k+'.json')).read_text());rows=load('pne_four_cover_realizations');hist=[Counter(),Counter()];examples=[];total=0
for r in rows:
 if r['late']:continue
 l=next(s for s in rows if s['late'] and (r['perm'],r['prep'])==(s['perm'],s['prep']));a,b=r['contacts'],l['contacts'];assert a[::2]==b[::2];entry=a[0]
 for mask in range(32):
  cs=[(b if j%2 and (mask>>(j//2))&1 else a)[j] for j in range(10)];total+=1;views=[]
  for v in (0,1):
   targets=[''.join(t) for t in itertools.combinations(sorted(set('01234')-set(entry[v])),2)];hits={k:[j for j,c in enumerate(cs) if c[v]==k] for k in targets};hist[v][tuple(sorted(map(len,hits.values())))]+=1;views.append(hits)
  if r is rows[0] and mask in (0,1,2,3,31):examples.append(dict(mask=mask,entry=entry,views=views))
assert total==load('pne_same_period_incidence')['valid'];out=dict(total=total,multiplicities=[{str(k):n for k,n in h.items()} for h in hist],examples=examples);print(out);(D/'pne_center_address_occurrences.json').write_text(json.dumps(out,indent=2)+'\n')

"""Test shifts of the whole reachable pair-relation dictionary, not trajectories. Allow independent coefficient renamings in the two views and optional exchange. Preserve contact kind and every offered ordered pair of addresses."""
import json,itertools,math,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'pne_contact_orbit_incidence.json').read_text())['rows'];pairs=[''.join(v) for v in itertools.combinations('abcde',2)];idx=pairs.index
rel={(r['k'],idx(r['pair'][0]),idx(r['pair'][1])) for r in rows};assert len(rel)==20
perms=[[''.join(sorted(p[ord(c)-97] for c in a)) for a in pairs] for p in itertools.permutations('abcde')];maps=[[idx(a) for a in p] for p in perms];hist=collections.Counter();best=None;keys=sorted(rel)
for swap in (0,1):
 for f,g in itertools.product(maps,repeat=2):
  def act(row):
   k,a,b=row;return (k,f[b],g[a]) if swap else (k,f[a],g[b])
  if not all(act(row) in rel for row in keys):continue
  unseen=set(keys);cycles=[]
  while unseen:
   v=min(unseen);c=[]
   while v in unseen:unseen.remove(v);c.append(v);v=act(v)
   cycles.append(c)
  order=math.lcm(*(len(c) for c in cycles));hist[swap,order]+=1
  if best is None or max(map(len,cycles))>best:best=max(map(len,cycles))
out=dict(addressPairs=len(rel),automorphisms=sum(hist.values()),orders={str(k):n for k,n in hist.items()},maxCycle=best);print(out);(D/'pne_contact_relation_symmetries.json').write_text(json.dumps(out,indent=2)+'\n')

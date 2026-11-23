"""Drop the one-exit-per-tick prescription. Select any five of ten offered contacts; do both native label views cover all pairs once? Check graph validity separately."""
import json,itertools,functools,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';load=lambda n:json.loads((D/(n+'.json')).read_text());data=load('pne_contact_pair_views');masks=load('ramsey_37_exit_phase_controls');base=[(x['swapped'],x['held']) for x in data[0]['contacts']];assert all([(x['swapped'],x['held']) for x in r['contacts']]==base for r in data);entries=base[::2];early=base[1::2];offers=[v for p in early for v in (p,p[::-1])];assert len(set(offers))==10;assert all(early[i][1]==early[i-1][0] for i in range(5));pairs={''.join(x) for x in itertools.combinations('01234',2)}
def alpha(C):
 adj=[0]*22
 def link(i,j):adj[i]|=1<<j;adj[j]|=1<<i
 link(20,21)
 for i in range(5):link(20,10+i);link(21,15+i);link(10+i,15+i)
 for i,(p,q) in enumerate(C):
  for j in p:link(i,10+int(j))
  for j in q:link(i,15+int(j))
  for j,(u,v) in enumerate(C[:i]):
   if set(p).isdisjoint(u) and set(q).isdisjoint(v):link(i,j)
 assert not any(adj[i]&adj[j] for i in range(22) for j in range(i) if adj[i]>>j&1)
 @functools.lru_cache(None)
 def a(m):
  if not m:return 0
  v=(m&-m).bit_length()-1;r=m^(1<<v);return max(a(r),1+a(r&~adj[v]))
 return a((1<<22)-1)
rows=[]
for ix in itertools.combinations(range(10),5):
 C=entries+[offers[j] for j in ix];x,y=(set(col)==pairs for col in zip(*C));rows.append(dict(offers=ix,one_per_tick=len({j//2 for j in ix})==5,swapped_cover=x,held_cover=y,alpha=alpha(C)))
assert all((x['swapped_cover'] and x['held_cover'])==(x['alpha']==6) for x in rows if x['one_per_tick']);print(collections.Counter((x['swapped_cover'],x['held_cover'],x['alpha']) for x in rows));print([x for x in rows if x['alpha']==6]);(D/'ramsey_37_dual_cover_closure.json').write_text(json.dumps(rows,indent=2)+'\n')

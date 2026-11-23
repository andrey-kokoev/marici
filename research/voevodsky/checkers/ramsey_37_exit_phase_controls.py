"""Hold the entry contact fixed; choose the exit before/after N advance independently at each of five ticks. Swap/hold pairs at the later offer exchange roles by native phase permutation. Test the completed graph, not just labels: triangle and maximum independent set, retaining counterexamples."""
import json,itertools,collections,functools
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';load=lambda n:json.loads((D/(n+'.json')).read_text());data=load('pne_contact_pair_views');native=load('pne_exit_predecessor_search')['edges']['N'];assert all([p[1],p[4]]==[3,2] and [p[2],p[3]]==[4,1] for k,_,p in native if k.endswith('phase-advance'))

def audit(C):
 adj=[0]*22
 def link(i,j):adj[i]|=1<<j;adj[j]|=1<<i
 # 0..9 chronological contacts; 10..14 and 15..19 paired label copies; 20,21 poles.
 link(20,21)
 for i in range(5):link(20,10+i);link(21,15+i);link(10+i,15+i)
 for i,(a,b) in enumerate(C):
  for x in a:link(i,10+int(x))
  for x in b:link(i,15+int(x))
  for j,(u,v) in enumerate(C[:i]):
   if set(a).isdisjoint(u) and set(b).isdisjoint(v):link(i,j)
 tri=next(((i,j,k) for i,j,k in itertools.combinations(range(22),3) if adj[i]>>j&adj[j]>>k&adj[k]>>i&1),None)
 @functools.lru_cache(None)
 def ind(m):
  if not m:return ()
  v=(m&-m).bit_length()-1;m^=1<<v;return max(ind(m),(v,)+ind(m&~adj[v]),key=len)
 witness=ind((1<<22)-1);return dict(edges=sum(x.bit_count() for x in adj)//2,triangle=tri,alpha=len(witness),independent=witness)
out=[];cache={}
for r in data:
 base=[(c['swapped'],c['held']) for c in r['contacts']];cases=[]
 for mask in range(32):
  C=tuple((b,a) if i%2 and mask>>(i//2)&1 else (a,b) for i,(a,b) in enumerate(base));
  if C not in cache:cache[C]=audit(C)
  changes=sum(((mask>>i)^(mask>>((i+1)%5)))&1 for i in range(5));assert cache[C]['alpha']==6+changes//2 and cache[C]['edges']==66-changes and cache[C]['triangle'] is None
  relabel=None
  if mask in (0,31):
   relabel=next(''.join(p) for p in itertools.permutations('01234') if {tuple(''.join(sorted(p[int(x)] for x in side)) for side in c) for c in base}==set(C))
  cases.append(dict(mask=mask,changes=changes,uniform_relabelling=relabel,unique_first=len({a for a,b in C}),**cache[C]))
 out.append(dict(seed=r['perm'],move=r['move'],cases=cases))
print(collections.Counter((x['mask'].bit_count(),x['edges'],x['alpha'],bool(x['triangle'])) for x in out[0]['cases']));assert all(x['cases']==out[0]['cases'] for x in out);(D/'ramsey_37_exit_phase_controls.json').write_text(json.dumps(out,indent=2)+'\n')

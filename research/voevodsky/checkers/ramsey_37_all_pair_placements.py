"""All bijections between the two pair charts, keeping the matching and double-disjointness rule fixed. Overlap p intersect f(p) immediately gives a red triangle via the matching. Test surviving graphs for a blue seven, classify successes by simultaneous label permutation and pole exchange."""
import json,itertools,collections
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';P=list(itertools.combinations(range(5),2));dis=lambda a,b:set(P[a]).isdisjoint(P[b]);allp=[]
def gen(f):
 if len(f)==10:allp.append(tuple(f));return
 for j in range(10):
  if j not in f and dis(len(f),j):gen(f+[j])
gen([]);success=[];fails=collections.Counter()
for f in allp:
 N=[0]*22
 def link(i,j):N[i]|=1<<j;N[j]|=1<<i
 link(20,21)
 for i in range(5):link(20,i);link(21,5+i);link(i,5+i)
 for i,j in enumerate(f):
  for k in P[i]:link(10+i,k)
  for k in P[j]:link(10+i,5+k)
  for h in range(i):
   if dis(i,h) and dis(j,f[h]):link(10+i,10+h)
 if any(N[i]&N[j] for i in range(22) for j in range(i) if N[i]>>j&1):fails['triangle']+=1;continue
 def seven(mask,k):
  if not k:return True
  while mask.bit_count()>=k:
   b=mask&-mask;mask^=b
   if seven(mask&~N[b.bit_length()-1],k-1):return True
  return False
 if seven((1<<22)-1,7):fails['seven']+=1
 else:success.append(f)
left=set(success);orbits=[]
while left:
 f=min(left);orbit=set()
 for perm in itertools.permutations(range(5)):
  g=[P.index(tuple(sorted(perm[k] for k in p))) for p in P];v=tuple(g[f[g.index(i)]] for i in range(10));orbit.add(v);orbit.add(tuple(v.index(i) for i in range(10)))
 assert orbit<=left;left-=orbit;orbits.append(dict(size=len(orbit),representative=f))
out=dict(disjointBijections=len(allp),failures=fails,successes=len(success),orbits=orbits);print(out);(D/'ramsey_37_all_pair_placements.json').write_text(json.dumps(out,indent=2)+'\n')

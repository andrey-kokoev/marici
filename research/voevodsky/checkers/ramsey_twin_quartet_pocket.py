"""If the two exceptional quartets agree, the root and both cells are a blue three with four common red neighbors. By the global codegree-four bound their three private sets are disjoint blue fours. These 12 vertices exhaust the pocket blue to the four shared labels under unsaturation. Four are omitted newcomers U; the other eight are the four singleton cells on U and four distinct pair/triple cells (repeated triples forbidden with singletons). Test all labeled pocket patterns up to permuting U and the two private groups. No core constraints beyond this necessary induced graph unless stated."""
import itertools,json,collections
from pysat.solvers import Solver
from ramsey_retention_slice import D
P=D.parent;comb=itertools.combinations;perms=[[sum(1<<p[i] for i in range(4) if s>>i&1) for s in range(16)] for p in itertools.permutations(range(4))];out=[];mult=collections.Counter()
for extra in comb([s for s in range(16) if s.bit_count() in (2,3)],4):
 if tuple(sorted(extra))!=min(tuple(sorted(p[s] for s in extra)) for p in perms):continue
 m=(1,2,4,8)+extra;st=[p for p in perms if set(p[s] for s in extra)==set(extra)];seen=set()
 for left in comb(m,4):
  left=tuple(sorted(left));right=tuple(sorted(set(m)-set(left)))
  if left in seen:continue
  seen.update(tuple(sorted(p[s] for s in t)) for p in st for t in (left,right));v=left+right;mult['marked']+=1
  if min(sum(s.bit_count() for s in t) for t in (left,right))<7:continue
  mult['budget']+=1;fixed=[0]*12;E={}
  for i,s in enumerate(v,4):
   for j in range(4):
    if s>>j&1:fixed[i]|=1<<j;fixed[j]|=1<<i
   if i>=8:
    for j,t in enumerate(left,4):
     if not s&t:E[j,i]=len(E)+1
  cs=[]
  for xs in comb(range(12),5):
   if not any(fixed[i]>>j&1 for i,j in comb(xs,2)):cs.append([E[e] for e in comb(xs,2) if e in E])
  # Any triangles would require a shared U label, already excluded on candidate cross edges.
  with Solver(name='cadical195',bootstrap_with=cs) as sl:
   if sl.solve():out.append(dict(left=left,right=right));
print(mult,len(out));(P/'ramsey_twin_quartet_pocket.json').write_text(json.dumps(dict(counts=mult,survive=out))+'\n')

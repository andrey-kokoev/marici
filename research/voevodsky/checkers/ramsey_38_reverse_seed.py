"""Reverse the support test from one genuine degree-seven root. Retain all old edges and grow its 19-core by one. Exhaust all red neighborhoods of the new vertex. Test 5+6 demands separately from full legality."""
import json,itertools,collections
from ramsey_retention_slice import D,decode,check
P=D.parent;g=decode(next(r['graph6'] for r in json.loads(D.read_text()) if (r['l'],r['k'])==(3,8)));F=(1<<27)-1
assert check(g,F,3,8);x=next(i for i,t in enumerate(g) if t.bit_count()==7);J=g[x];C=F^(J|1<<x);ind=[0]
for i in range(27):
 if C>>i&1:ind += [q|1<<i for q in ind if not q&g[i]]
e=sum((t&C).bit_count() for i,t in enumerate(g) if C>>i&1)//2;by=collections.Counter();best=None
for t in ind: # new vertex blue to root, red to t in core. S is red neighborhood in J, constrained by no red triangle.
 newq=[q for q in ind if not q&t];
 if any(q.bit_count()==6 for q in newq) or not 45<=e+t.bit_count()<=49:continue
 by['candidate_core_extensions']+=1;avail=J
 for i in range(27):
  if t>>i&1:avail&=~g[i]
 # Using all available red edges to J maximizes hits simultaneously; J has no red edges.
 bad=[];profile=collections.Counter()
 for q in newq:
  hit=avail
  for i in range(27):
   if q>>i&1:hit|=g[i]&J
  size=q.bit_count()+1
  if hit.bit_count()<size:bad.append(size);profile[size]+=1
 if not any(k>=5 for k in bad):by['pass56']+=1
 if not bad:by['full']+=1
 score=(sum(profile[k] for k in (5,6)),len(bad));
 if best is None or score<best[0]:best=(score,dict(red_core=t,red_neighbors=avail,edge_count=e+t.bit_count(),failed_cliques=dict(profile)))
print(x,e,by,best);(P/'ramsey_38_reverse_seed.json').write_text(json.dumps(dict(root=x,core_mask=C,neighbor_mask=J,core_edges=e,counts=by,best=best),indent=1)+'\n')

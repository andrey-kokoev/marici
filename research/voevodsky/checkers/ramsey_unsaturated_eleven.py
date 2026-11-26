"""Test 8 singletons + exactly 11 pairs (>=12 already classified). Seven remaining cells carry 26 incidences; each has size 3..5, hence at least two triples. Mark an unordered pair of triples, enumerate all pair-graph and marked orbits, and screen induced demands + residual degree budget. Never count timeout as exclusion."""
from ramsey_unsaturated_skeleton_budget import *
from concurrent.futures import ProcessPoolExecutor
path=P/'ramsey_unsaturated_eleven.json';sizes=[s for s in range(256) if 3<=s.bit_count()<=5];trips=[s for s in sizes if s.bit_count()==3]
def fixed(e):return tuple(single+[1<<i|1<<j for i,j in e])
def group(e):return [[sum(1<<p[i] for i in V if s>>i&1) for s in range(256)] for p in ig.Graph(8,e).get_automorphisms_vf2()]
def tests(e):
 f=fixed(e);z=dict(edges=e,base=local(f));
 if not z['base']:return z
 G=group(e);opts=[];seen=set();unknown=0
 for s in trips:
  if s in seen:continue
  orb={p[s] for p in G};seen.update(orb);v=budget(f+(s,));unknown+=v is None
  if v is not False:opts.extend(orb)
 ps=sorted({min(tuple(sorted((p[a],p[b]))) for p in G) for a,b in itertools.combinations_with_replacement(opts,2)});ok=[]
 for a,b in ps:
  v=budget(f+(a,b));unknown+=v is None
  if v is not False:ok.append((a,b))
 z.update(triples=sorted(opts),pair_types=len(ps),pairs=ok,unknown=unknown);return z
if __name__=='__main__':
 gs=graphs(11);print(len(gs),flush=True);out=[]
 with ProcessPoolExecutor(8) as ex:
  for j,z in enumerate(ex.map(tests,gs)):out.append(z);path.write_text(json.dumps(out)+'\n');print(j,z['base'],z.get('pair_types'),len(z.get('pairs',[])),flush=True)

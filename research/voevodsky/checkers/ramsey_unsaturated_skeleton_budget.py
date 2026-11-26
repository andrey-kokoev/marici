"""Missing six cells have TOTAL core degree 24. An induced core on the retained cells must already contain at least 52 red edges; after fixing an extra cell use its known degree to sharpen the bound. Screen masks by orbit including clique demands up to 5 labels, before selecting the remaining cells."""
from ramsey_unsaturated_pair_graphs import *
def budget(m,level=5):
 N=len(m);E={p:i+1 for i,p in enumerate(p for p in pairs(range(N),2) if not m[p[0]]&m[p[1]])};cs=[];n=len(E)
 for t in range(256):
  vs=[i for i,x in enumerate(m) if not x&~t];k=t.bit_count()
  if len(vs)>cap[k]:return False
  if k<=level:
   for s in pairs(vs,k+1):
    c=[E[p] for p in pairs(s,2) if p in E];
    if not c:return False
    cs.append(c)
 for x in pairs(range(N),3):
  es=list(pairs(x,2));
  if all(p in E for p in es):cs.append([-E[p] for p in es])
 for i,s in enumerate(m):
  xs=[v for p,v in E.items() if i in p];d=8-s.bit_count()
  for fn,k in [(CardEnc.atmost,min(d,len(xs))),(CardEnc.atleast,max(0,d-26+N))]:
   b=fn(xs,k,top_id=n);cs+=b.clauses;n=max(n,b.nv)
 b=CardEnc.atleast(list(E.values()),sum(8-s.bit_count() for s in m)-76,top_id=n);cs+=b.clauses
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  sl.conf_budget(150000);return sl.solve_limited()
if __name__=='__main__':
 from concurrent.futures import ProcessPoolExecutor
 data=json.loads((P/'ramsey_unsaturated_pair_graphs.json').read_text());out=[]
 for z in data[:2]:
  es=z['edges'];f=tuple(single+[1<<i|1<<j for i,j in es]);g=ig.Graph(8,es);aut=g.get_automorphisms_vf2();orbs={}
  for s in range(1,256):
   if not local(f+(s,)):continue
   rep=min(sum(1<<p[i] for i in V if s>>i&1) for p in aut);orbs.setdefault(rep,[]).append(s)
  obs=[()]+[(s,) for s in orbs];
  with ProcessPoolExecutor(8) as ex:rs=list(ex.map(budget,[f+t for t in obs]));
  out.append(dict(edges=es,base=rs[0],orbits=[dict(rep=s,masks=v,ok=r) for (s,v),r in zip(orbs.items(),rs[1:])]));print(rs,flush=True);(P/'ramsey_unsaturated_skeleton_budget.json').write_text(json.dumps(out)+'\n')

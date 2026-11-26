"""Explain a two-region conflict with independently switchable primitive constraints. Test constraint families across all stored unsaturated joint-beam nodes. No timeouts counted as exclusions."""
from ramsey_incidence_first35 import P,json,itertools,CardEnc,Solver
from collections import Counter
from functools import reduce
pairs=itertools.combinations;nodes=json.loads((P/'ramsey_incidence_joint_beam.json').read_text())['nodes'];base=json.loads((P/'ramsey_unsaturated_joint_core.json').read_text());T=base['five_masks'];ts=[t for t in range(256) if t.bit_count()==4]
def setup(m,ts5):
 E={p:k+1 for k,p in enumerate(p for p in pairs(range(26),2) if not m[p[0]]&m[p[1]])};n=len(E);cs=[];groups={}
 def group(name,clauses):
  nonlocal n
  n+=1;groups[n]=name;cs.extend([[-n]+c for c in clauses])
 for i,s in enumerate(m):
  xs=[w for p,w in E.items() if i in p];d=8-s.bit_count()
  for name,fn in [('upper',CardEnc.atmost),('lower',CardEnc.atleast)]:
   b=fn(xs,d,top_id=n);n=max(n,b.nv);group((name,i),b.clauses)
 for x in pairs(range(26),3):
  es=list(pairs(x,2));
  if all(p in E for p in es):group(('triangle',*x),[[-E[p] for p in es]])
 seen=set()
 for t in sorted(range(256),key=int.bit_count):
  k=t.bit_count()
  if k>4 and t not in ts5:continue
  for xs in pairs([i for i,s in enumerate(m) if not s&~t],k+1):
   c=tuple(E[p] for p in pairs(xs,2) if p in E)
   key=(t if k==5 else None,c) # Keep each independently switchable region complete.
   if key not in seen:group(('cover',t,*xs),[list(c)]);seen.add(key)
 return cs,groups

def trace(m):
 cs,gs=setup(m,T)
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  a=list(gs);assert not sl.solve(assumptions=a);core=sl.get_core();
  for x in sorted(core,key=lambda x:gs[x][0] not in ('lower','upper')):
   if x not in core:continue
   test=[i for i in core if i!=x]
   if not sl.solve(assumptions=test):core=sl.get_core()
  assert not sl.solve(assumptions=core) and all(sl.solve(assumptions=[i for i in core if i!=x]) for x in core)
 return [gs[x] for x in core]
if __name__=='__main__':
 m=nodes[base['node']]['m'];c=trace(m);print(Counter(g[0] for g in c));print(c[:30]);(P/'ramsey_unsaturated_conflict_trace.json').write_text(json.dumps(dict(m=m,core=c))+'\n')

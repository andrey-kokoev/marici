"""No fixed cube rows or prescribed incidence multiset. Exact rooted (3,9) feasibility via lazy independent-set cuts. Budget exhaustion leaves the question open. Seed archive models are separate lower-level controls, never constraints on this search."""
import json,itertools,sys,time,collections
from ramsey_incidence_first35 import P,CardEnc,Solver
from ramsey_retention_slice import decode
C=range(26);L=range(26,34);pairs=itertools.combinations;root=34;ts=[sum(1<<j for j in s) for s in pairs(range(8),4)]
def profile(m):return [sum(not s&t for s in m) for t in ts]
def independent(g):
 a=[0]
 for i,v in enumerate(g):a.extend([s|1<<i for s in a if not s&v and s.bit_count()<9]);
 return a

def run(budget,rounds):
 z=json.loads((P/'ramsey_incidence35_endpoint.json').read_text());a=decode(z['graph6']);control=[]
 for r in range(35):
  labs=[i for i in range(35) if a[r]>>i&1];h=profile([sum((a[i]>>j&1)<<l for l,j in enumerate(labs)) for i in range(35) if i!=r and i not in labs]);control.append([max(h),h.count(9)])
 src=json.loads((P/'ramsey_incidence_joint_beam.json').read_text());best=None
 for i,z in enumerate(src['nodes']):
  m=z['m'];h=profile(m)
  if max(h)>8:continue
  g=[0]*26
  for u,v in z['edges']:g[u]|=1<<v;g[v]|=1<<u
  assert all(x.bit_count()+s.bit_count()==8 for x,s in zip(g,m)) and all(sum(s>>l&1 for s in m)==7 for l in range(8));assert all(not(m[u]&m[v] or g[u]&g[v]) for u,v in z['edges']);bad=set()
  for s in independent(g):
   mask=0
   for j in C:
    if s>>j&1:mask|=m[j]
   if s.bit_count()>mask.bit_count():bad.add(mask)
  assert min(b.bit_count() for b in bad)>=5;v=dict(node=i,maximum=max(h),five_regions_passed=sum(not any(not b&~t for b in bad) for t in range(256) if t.bit_count()==5));
  if best is None or v['five_regions_passed']>best['five_regions_passed']:best=v
 E={(i,j):k+1 for k,(i,j) in enumerate((i,j) for i in C for j in range(i+1,34))};n=len(E);cs=[]
 def card(xs,k,eq=True):
  nonlocal n
  b=(CardEnc.equals if eq else CardEnc.atmost)(xs,k,top_id=n);n=max(n,b.nv);cs.extend(b.clauses)
 for i in range(34):card([w for p,w in E.items() if i in p],8-int(i>=26))
 for p in pairs(range(34),3):
  es=list(pairs(p,2));
  if all(e in E for e in es):cs.append([-E[e] for e in es])
 for t in ts:
  xs=[]
  for i in C:n+=1;xs.append(n);cs.append([n]+[E[i,j] for j in L if t>>(j-26)&1])
  card(xs,8,False)
 # By separate label and cell permutations the first row may hit precisely the first seven cells.
 cs.extend([[E[i,26] if i<7 else -E[i,26]] for i in C]);history=[];out=dict(control=collections.Counter(map(str,control)),archive_control=best,history=history);path=P/'ramsey_unanchored_saturation.json'
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for it in range(rounds):
   sl.conf_budget(budget);ok=sl.solve_limited();out['status']={True:'relaxed',False:'excluded',None:'unknown'}[ok];
   if ok is not True:break
   sol=set(sl.get_model());g=[0]*35
   for (i,j),w in E.items():
    if w in sol:g[i]|=1<<j;g[j]|=1<<i
   for j in L:g[j]|=1<<34;g[34]|=1<<j
   h=profile([v>>26 for v in g[:26]]);assert max(h)<=8 and all(v.bit_count()==8 for v in g);bad=[s for s in independent(g) if s.bit_count()==9];history.append(dict(round=it,blue_nines=len(bad),maximum=max(h)));out['last_graph']=g;path.write_text(json.dumps(out)+'\n');
   if not bad:out['status']='witness';break
   for s in bad:sl.add_clause([v for (i,j),v in E.items() if s>>i&1 and s>>j&1])
 path.write_text(json.dumps(out)+'\n');print(out['status'],best,history[-3:])
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]))

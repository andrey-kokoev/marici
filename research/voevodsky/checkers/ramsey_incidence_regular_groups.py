"""Blind order-eight regular label-action census. All five groups, unconstrained core completion. Nonempty masks since core degrees <=7; size<=5 since core red degree >=3 (26-1-22). Multiplicity <=mask size by blue shortage. Orbit multiplicities constrained only by 26 cells/56 incidences. Isomorphism dedup of colored incidence graph; deterministic local propagation and SAT checks for any survivor. No witness or cube inputs."""
import itertools,functools,collections,json,subprocess,sys,igraph as ig
from ramsey_incidence_first35 import P,solve

def mult(g,i,j):
 if g=='C8':return (i+j)%8
 if g=='C2^3':return i^j
 a,b=i%4,i//4;c,d=j%4,j//4
 return ((a+(c if g=='C4xC2' or not b else -c)+(2*b*d if g=='Q8' else 0))%4)+4*(b^d)

def key(m):
 edges=[(i,26+j) for i,s in enumerate(m) for j in range(8) if s>>j&1];g=ig.Graph(34,edges);p=g.canonical_permutation(color=[1]*26+[2]*8);return tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(p).get_edgelist()))
classes={};results={}
actions={group:[[mult(group,i,j) for j in range(8)] for i in range(8)] for group in ('C8','C4xC2','D8','Q8','C2^3')};actions.update({f'min32-{i}':g for i,g in enumerate(json.loads((P/'ramsey_transitive8_gate.json').read_text())['nonregular'])})
for group,perm in actions.items():
 table=set(map(tuple,perm));assert all(tuple(p[q[i]] for i in range(8)) in table for p,q in itertools.product(perm,repeat=2)) and len({p[0] for p in perm})==8;orbits={}
 for s in range(1,256):
  if s.bit_count()>5:continue
  o=tuple(sorted({sum(1<<t[i] for i in range(8) if s>>i&1) for t in perm}));orbits[o]=None
 O=sorted(orbits);nk=[(len(o),o[0].bit_count()) for o in O];types=set();raw=0
 @functools.cache
 def count(i,n,d):
  if n<0 or d<n or d>5*n:return 0
  if i==len(O):return int(n==d==0)
  l,k=nk[i];return sum(count(i+1,n-l*j,d-l*k*j) for j in range(k+1))
 def gen(i,n,d,m):
  global raw
  if i==len(O):
   assert len(m)==26 and all(sum(s>>v&1 for s in m)==7 for v in range(8));raw+=1;h=key(m);types.add(h);r=classes.setdefault(h,dict(m=m,groups=[]));
   if group not in r['groups']:r['groups'].append(group)
   return
  l,k=nk[i]
  for j in range(k+1):
   if count(i+1,n-l*j,d-l*k*j):gen(i+1,n-l*j,d-l*k*j,m+list(O[i])*j)
 gen(0,26,56,[]);assert raw==count(0,26,56);results[group]=dict(raw=raw,types=len(types));print(group,results[group],flush=True)
rs=list(classes.values());gate=subprocess.check_output([sys.argv[1],'8'],input=''.join(' '.join(map(str,r['m']))+'\n' for r in rs),text=True).splitlines()
for r,l in zip(rs,gate,strict=True):
 r['gate'],r['rounds']=map(int,l.split())
 if not r['gate']:r['solve']=solve(r['m'],False)
out=dict(groups=results,classes=rs);print(len(rs),'gate survivors',sum(not r['gate'] for r in rs),collections.Counter(r['solve']['status'] for r in rs if not r['gate']));(P/'ramsey_incidence_transitive_groups.json').write_text(json.dumps(out,separators=(',',':'))+'\n')

"""Close one-fully-doubled-side K3,3 templates without any catalogue on the other side. The only open edges go from three opposite roots and three private doubles to the 17-core. Enforce exact degrees, triangle-free attachments; audit nine-cliques by exhaustive model separation. Codegree constraints on opposite side follow from general theorems (each B pair can share <=1 additional vertex). Unknowns are retained."""
import itertools,json,collections,sys
from ramsey_retention_slice import D,check
from pysat.card import CardEnc
from pysat.solvers import Solver
P=D.parent;C=itertools.combinations

def build(z):
 i,es,w=z;g=[0]*35
 def add(i,j):g[i]|=1<<j;g[j]|=1<<i
 for i in range(3):
  for j in range(3,6):add(i,j)
  for j in range(3):add(i,6+3*i+j)
  for j in range(3):
   if j!=i:add(i,15+j)
 for j,x in enumerate(w['X']):
  for k in range(j):
   if x>>k&1:add(6+j,6+k)
 for j,s in enumerate(w['S']):
  for k in range(17):
   if s>>k&1:add(6+j,18+k)
 for a,b in es:add(18+a,18+b)
 return g

def run(z):
 g=build(z);U=[3,4,5,15,16,17];V=range(18,35);E={(i,j):v+1 for v,(i,j) in enumerate((i,j) for i in U for j in V if not g[i]&g[j])};n=len(E);cs=[]
 if any((a&b).bit_count()>4 for a,b in C(g,2)) or any((a&b&c).bit_count()>3 for a,b,c in C(g,3)):return 'codegree',0
 for i,row in enumerate(g):
  xs=[w for e,w in E.items() if i in e];d=8-row.bit_count()
  if not 0<=d<=len(xs):return 'degree',0
  if xs:b=CardEnc.equals(xs,d,top_id=n);cs+=b.clauses;n=max(n,b.nv)
 for i in U:
  for a,b in C(V,2):
   if g[a]>>b&1 and (i,a) in E and (i,b) in E:cs.append([-E[i,a],-E[i,b]])
 for j,k in C((3,4,5),2):
  for a,b in C(V,2):
   p=[(j,a),(k,a),(j,b),(k,b)]
   if all(e in E for e in p):cs.append([-E[e] for e in p])
 for a in V:
  p=[(j,a) for j in (3,4,5)]
  if all(e in E for e in p):cs.append([-E[e] for e in p])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for it in range(200):
   if not sl.solve():return 'unsat',it
   sol=set(sl.get_model());a=g[:]
   for (i,j),w in E.items():
    if w in sol:a[i]|=1<<j;a[j]|=1<<i
   assert all(s.bit_count()==8 for s in a);I=[0];cut=set()
   for j,s in enumerate(a):
    for q in I[:]:
     if q&s:continue
     u=q|1<<j
     if u.bit_count()==9:
      c=tuple(w for (i,v),w in E.items() if u>>i&1 and u>>v&1)
      if not c:return 'fixed_nine',it+1
      cut.add(c)
     else:I.append(u)
   if not cut:assert check(a,(1<<35)-1,3,9);return 'witness',a
   for c in cut:sl.add_clause(c)
 return 'unknown',200
if __name__=='__main__':
 from concurrent.futures import ProcessPoolExecutor
 R=json.loads((P/'ramsey_k33_three_spokes.json').read_text());ss=json.loads((P/'ramsey_k33_spoke_join.json').read_text());tasks=[(z['i'],R[z['i']]['h'],w) for z in ss for w in z['alive']];
 with ProcessPoolExecutor(8) as ex:rs=list(ex.map(run,tasks,chunksize=5));print(collections.Counter(r[0] for r in rs),flush=True);(P/'ramsey_k33_spoke_finish.json').write_text(json.dumps(rs)+'\n')

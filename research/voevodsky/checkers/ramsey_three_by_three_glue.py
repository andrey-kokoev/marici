"""Glue marked (3,6) cores along their common neutral cells in a K3,3 hypothetical endpoint. Initially (a,b)=(3,3): both catalogued sides order 17 and five shared neutral vertices. Keep only bijections realizing exactly the neutral red degrees and the same total cross-edge budget. Any remaining edges are confined to the X by Y block. SAT enforces exact degrees, triangles and no blue nines (lazy); unknowns not exclusions."""
from ramsey_retention_slice import CAT,D,decode
import itertools,collections,json,sys
from pysat.card import CardEnc
from pysat.solvers import Solver
P=D.parent;comb=itertools.combinations

def nodes(h,w):
 z=[i for i in range(len(h)) if not any(s>>i&1 for s in w)];x=[i for i in range(len(h)) if i not in z];return x,z

def glue(h,w,l,v,cnt):
 x,z=nodes(h,w);y,t=nodes(l,v);cnt['side_pairs']+=1
 if sum(8-sum(s>>i&1 for s in w)-h[i].bit_count() for i in x)!=sum(8-sum(s>>i&1 for s in v)-l[i].bit_count() for i in y):return
 cnt['balanced']+=1
 for perm in itertools.permutations(t):
  if any(((h[i]>>j)&1)!=((l[k]>>m)&1) for (i,k),(j,m) in comb(zip(z,perm),2)):continue
  cnt['isomorphic_Z']+=1
  if any(h[i].bit_count()+l[k].bit_count()-sum(h[i]>>j&1 for j in z)!=8 for i,k in zip(z,perm)):continue
  cnt['degree_Z']+=1;g=[0]*35
  def red(i,j):g[i]|=1<<j;g[j]|=1<<i
  for i in range(3):
   for j in range(3,6):red(i,j)
  for old,sets,cells,zold,idx,offset in ((h,w,x,z,0,6),(l,v,y,perm,3,6+len(x))):
   mp={c:offset+i for i,c in enumerate(cells)}|{c:6+len(x)+len(y)+i for i,c in enumerate(zold)}
   for i,j in comb(range(len(old)),2):
    if old[i]>>j&1:red(mp[i],mp[j])
   for j,s in enumerate(sets):
    for i in cells:
     if s>>i&1:red(idx+j,mp[i])
  if any((s&t).bit_count()>4 for s,t in comb(g,2)):continue
  if any((s&t&u).bit_count()>3 for s,t,u in comb(g,3)):continue
  cnt['partial_common']+=1;E={(i,j):1+k for k,(i,j) in enumerate((i,j) for i in range(6,6+len(x)) for j in range(6+len(x),6+len(x)+len(y)) if not g[i]&g[j])};yield g,E

def solve(g,E):
 n=len(E);cs=[]
 for i,row in enumerate(g):
  xs=[v for p,v in E.items() if i in p];k=8-row.bit_count()
  if k>len(xs) or k<0:return 'degree'
  if xs:b=CardEnc.equals(xs,k,top_id=n);cs+=b.clauses;n=max(n,b.nv)
 for q in comb(range(35),3):
  es=list(comb(q,2));
  if all(g[i]>>j&1 or (i,j) in E for i,j in es):cs.append([-E[p] for p in es if p in E])
 # All blue nines in the minimum red graph are demands; collect clauses with a shared fixed prefix.
 I=[0];cuts=set()
 for i,row in enumerate(g):
  for s in I[:]:
   if s&row:continue
   q=s|1<<i
   if q.bit_count()==9:
    c=tuple(v for (i,j),v in E.items() if (q>>i)&1 and (q>>j)&1)
    if not c:return 'fixed_nine'
    cuts.add(c)
   else:I.append(q)
 with Solver(name='cadical195',bootstrap_with=cs+list(cuts)) as sl:
  ok=sl.solve();return 'witness' if ok else 'unsat'
if __name__=='__main__':
 H=list(map(decode,(CAT/'r36_17.g6').read_text().splitlines()));rows=json.loads((P/'ramsey_three_by_three_proj_17.json').read_text());ss=[(r['ix'],w) for r in rows for w in r['ss']];cnt=collections.Counter();wins=[]
 for (i,w),(j,v) in itertools.combinations_with_replacement(ss,2):
  for g,E in glue(H[i],w,H[j],v,cnt):
   r=solve(g,E);cnt[r]+=1
   if r=='witness':wins.append((i,w,j,v))
 print(cnt,wins);(P/'ramsey_three_by_three_glue_33.json').write_text(json.dumps(dict(counts=cnt,wins=wins))+'\n')

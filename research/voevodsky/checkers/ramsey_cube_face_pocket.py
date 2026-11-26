"""Four erased corners of a face. Four retained newcomers are jointly blue to an order-13 (3,5) pocket (nine completely unhit core cells and four erased newcomers). Use the complete order-13 catalogue and the orbits of its blue fours. Freeze pocket edges up to isomorphism, not by assuming cube. All 17 outer cells may change their red attachments and mutual edges. Essential coverage constraints from small fixed-outer blue cliques, plus exact degrees, triangles, and row nonrestoration. Bounded decisions are explicitly unknown."""
import itertools,json,sys,collections,time,concurrent.futures as cf
from pysat.solvers import Solver
from pysat.card import CardEnc
import igraph as ig
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;lines=(CAT/'r35_13.g6').read_text().splitlines();assert len(lines)==1;a=decode(lines[0]);E13=[(i,j) for i in range(13) for j in range(i) if a[i]>>j&1];g=ig.Graph(13,E13);aut=g.get_automorphisms_vf2();I=[0]
for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
Q=[s for s in I if s.bit_count()==4];orbit=lambda q:{sum(1<<p[i] for i in range(13) if q>>i&1) for p in aut};rep=sorted({min(orbit(q)) for q in Q});assert len(rep)==2
M=[sum(1<<i for i in range(8) if i&k==v) for k in range(1,8) for v in range(8) if not v&~k];h=[v>>4 for v in M if v>>4];old=[v&15 for v in M if v>>4];assert len(h)==17;groups=[[i for i,s in enumerate(h) if s==t] for t in set(h)];goodpairs=[(s,t) for s in I for t in I if all(q&(s|t) for q in Q)];assert all(not s&t for s,t in goodpairs)

def run(item):
 q,budget=item;# indices: 0..12 pocket, 13..29 exterior, 30..33 retained, 34 root
 hidden=[i for i in range(13) if q>>i&1];fixed=[0]*35;poss={};n=0;cs=[]
 def add(i,j):fixed[i]|=1<<j;fixed[j]|=1<<i
 def var(i,j):return poss.get(tuple(sorted((i,j))))
 for i,j in E13:add(i,j)
 for j in hidden+list(range(30,34)):add(34,j)
 for i,s in enumerate(h,13):
  for j in range(4):
   if s>>j&1:add(i,30+j)
  for j in range(i):
   if j>=13 and h[j-13]&s:continue
   n+=1;poss[j,i]=n
 for i,v in enumerate(fixed):
  xs=[w for p,w in poss.items() if i in p];d=8-v.bit_count()
  if xs:f=CardEnc.equals(xs,d,top_id=n);cs+=f.clauses;n=max(n,f.nv)
  else:assert d==0
 for t in itertools.combinations(range(35),3):
  pairs=list(itertools.combinations(t,2));
  if all(fixed[i]>>j&1 or var(i,j) for i,j in pairs):cs.append([-var(i,j) for i,j in pairs if var(i,j)])
 for b in groups:
  if h[b[0]].bit_count()!=1:continue
  assert len(b)==2;x,y=[13+i for i in b];
  for s in Q:cs.append([var(i,j) for i in (x,y) for j in range(13) if s>>j&1]);
  for j in range(13):cs.append([-var(x,j),-var(y,j)])
 # Compare N(i), a blue eight, to a blue eight containing all four retained labels. Every absent retained label needs a distinct red neighbor of i seeing that label. For i in P choose Q=N_P(i), shared by both blue eights. For an exterior i use Hall on its independent core neighbors, disjoint from its incident labels (or use the blue-clique label-union condition).
 for i in range(30):
  absent=15 if i<13 else 15^h[i-13]
  for L in range(1,16):
   if L&~absent:continue
   xs=[var(i,13+j) for j,s in enumerate(h) if s&L and var(i,13+j)];bound=L.bit_count()-int(i in hidden)
   if bound>0:
    b=CardEnc.atleast(xs,bound,top_id=n);cs+=b.clauses;n=max(n,b.nv)
 # Complete blue-nine clauses with <=3 of the seventeen open vertices. Prefix is fixed triangle-free 13 plus retained newcomers and root.
 st=[0]
 for j in list(range(13))+list(range(30,35)):st.extend([s|1<<j for s in st if not s&fixed[j]]);
 # For each blue clique in fixed region bound total common blue neighbors by previous Ramsey maxima. Auxiliary vars indicate an exterior vertex misses the whole clique.
 maxima={1:27,2:22,3:17,4:13,5:8,6:5,7:2,8:0};I_fixed=sum(1<<i for i in set(range(35))-set(range(13,30)));miss={}
 for s in st:
  if not s:continue
  un=0
  for i in range(35):
   if s>>i&1:un|=fixed[i]
  candidates=[x for x in range(13,30) if not un>>x&1];bound=maxima[s.bit_count()]-(I_fixed&~(s|un)).bit_count()
  if len(candidates)<=bound:continue
  xs=[]
  for x in candidates:
   lits=tuple(var(x,j) for j in range(13) if s>>j&1)
   if not lits:bound-=1;continue
   if len(lits)==1:xs.append(-lits[0]);continue
   if lits not in miss:n+=1;miss[lits]=n;cs.append([n,*lits])
   xs.append(miss[lits])
  if bound<0:cs.append([])
  elif bound<len(xs):b=CardEnc.atmost(xs,bound,top_id=n);n=max(n,b.nv);cs+=b.clauses
 for size in (1,2,3):
  pre=[s for s in st if s.bit_count()==9-size]
  for xs in itertools.combinations(range(13,30),size):
   forbid=0
   for x in xs:forbid|=fixed[x]
   for s in pre:
    if forbid&s:continue
    cs.append([v for i,j in itertools.combinations(xs,2) if (v:=var(i,j))]+[var(x,j) for x in xs for j in range(13) if s>>j&1])
 # Under five-anchor theorem any row restoring cube is already classified. All four hidden rows have four pocket hits and three exterior hits.
 blocked=set()
 for l in range(4):
  for parts in itertools.product(*(itertools.combinations(b,sum(old[i]>>l&1 for i in b)) for b in groups)):blocked.add(tuple(sorted(itertools.chain.from_iterable(parts))))
 for j in hidden:
  for row in blocked:cs.append([-var(13+i,j) for i in row])
 # Pair ordering of cells with the same retained label mask, lex by their pocket neighborhoods. One can always relabel these cells to satisfy this.
 for b in groups:
  if len(b)!=2:continue
  x,y=[13+i for i in b];prev=None
  for j in range(13):
   p1,p2=var(j,x),var(j,y);esc=[] if prev is None else [-prev];cs.append(esc+[-p1,p2]);n+=1;cs.extend([esc+[p1,p2,n],esc+[-p1,-p2,n]]);prev=n
 t=time.perf_counter();models=[]
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for it in range(12):
   sl.conf_budget(budget);ok=sl.solve_limited();
   if ok!=True:break
   sol=set(sl.get_model());graph=fixed[:]
   for (i,j),v in poss.items():
    if v in sol:graph[i]|=1<<j;graph[j]|=1<<i
   assert all(v.bit_count()==8 for v in graph);sets=[0]
   for i,v in enumerate(graph):sets.extend([s|1<<i for s in sets if not s&v and s.bit_count()<9]);
   bad=[s for s in sets if s.bit_count()==9];models.append(len(bad));
   if not bad:assert check(graph,(1<<35)-1,3,9);break
   for s in bad:sl.add_clause([v for (i,j),v in poss.items() if s>>i&1 and s>>j&1])
  else:ok=None
  conf=sl.accum_stats()['conflicts']
 return dict(q=q,orbit=len(orbit(q)),masks=[sum((a[i]>>j&1)<<k for k,j in enumerate(hidden)) for i in range(13) if i not in hidden],ok=ok,models=models,endpoint=graph if ok else None,seconds=time.perf_counter()-t,conflicts=conf)
if __name__=='__main__':
 budget=int(sys.argv[1]);out=[];print('pocket orbits',[len(orbit(q)) for q in rep],'unordered compatible pairs',len(goodpairs)//2,flush=True)
 with cf.ProcessPoolExecutor(2) as ex:
  for f in cf.as_completed([ex.submit(run,(q,budget)) for q in rep]):out.append(f.result());print(out[-1],flush=True);(P/f'ramsey_cube_face_pocket_{budget}.json').write_text(json.dumps(out)+'\n')

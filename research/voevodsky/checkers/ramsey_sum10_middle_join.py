"""Enumerate induced 12-overlaps for each stored 17 type against the marked 24. Test joins until first SAT per type or all matches exhausted."""
import json,itertools,collections,networkx as nx
from pysat.card import CardEnc
from pysat.solvers import Solver
from ramsey_retention_slice import D,CAT,decode,has,check
P=D.parent;h=decode(json.loads(D.read_text())[-1]['graph6']);refs=[decode(s) for s in (CAT/'r36_17.g6').read_text().splitlines()];hosts=json.loads((P/'ramsey_sum10_seed_types.json').read_text());by=collections.defaultdict(list)
def graph(a,t):
 G=nx.Graph();G.add_nodes_from(t);G.add_edges_from((i,j) for i,j in itertools.combinations(t,2) if a[i]>>j&1);return G
def sig(G):return tuple(sorted((len(G[i]),tuple(sorted(len(G[j]) for j in G[i]))) for i in G))
cs=[[-i-1,-j-1,-k-1] for i,j,k in itertools.combinations(range(24),3) if h[i]>>j&h[i]>>k&h[j]>>k&1];
with Solver(name='g4',bootstrap_with=cs+CardEnc.atleast(list(range(1,25)),12).clauses) as sl:
 while sl.solve():
  t=[i-1 for i in sl.get_model() if 1<=i<=24];assert len(t)==12;sl.add_clause([-i-1 for i in t]);H=graph(h,t);by[sig(H)].append(H)
import sys
from ramsey_sum10_screen import screen
scan='--screen' in sys.argv
cores=[];screens=[]
def join(g,t,key):
 adj=[0]*29;groups=[]
 for a,seed,start in [(g,t,12),(h,key,17)]:
  order=list(seed)+[i for i in range(len(a)) if i not in seed];slots=list(range(12))+list(range(start,start+len(a)-12));groups.append(slots[12:]);
  for (i,u),(j,v) in itertools.combinations(zip(slots,order),2):
   if a[u]>>v&1:adj[i]|=1<<j;adj[j]|=1<<i
 cs=[]
 for k,col in [(4,1),(6,0)]:
  A=adj if col else [~v for v in adj];parts=[]
  for group in groups:
   seq=[]
   for n in range(1,k):
    for u in itertools.combinations(group,n):
     if any(not(A[i]>>j&1) for i,j in itertools.combinations(u,2)):continue
     p=4095
     for i in u:p&=A[i]
     seq.append((u,p))
   parts.append(seq)
  for (u,p),(v,q) in itertools.product(*parts):
   r=k-len(u)-len(v)
   if r>=0 and has(A,p&q,r):cs.append([(-1 if col else 1)*(1+12*(i-12)+j-17) for i in u for j in v])
 with Solver(name='g4',bootstrap_with=cs) as sl:
  if scan:
   result,rounds,forced=screen(cs);pivot=None
   if result=='open':pivot=next((i for i in range(1,61) if all(screen(cs+[[v]])[0]!='open' for v in (i,-i))),None)
   ok=sl.solve();assert (result=='open' and pivot is None) or not ok;screens.append(dict(type=refs.index(g)+1,t=t,key=key,screen=result,rounds=rounds,forced=forced,pivot=pivot,sat=ok));return None
  if not sl.solve():
   if g==refs[0]:
    # Keep an inclusion-minimal set of constraints, not necessarily a smallest one.
    sel=list(range(61,61+len(cs)))
    with Solver(name='g4',bootstrap_with=[[-i]+c for i,c in zip(sel,cs)]) as s:
     assert not s.solve(assumptions=sel);ids=s.get_core()
     for i in ids.copy():
      trial=[j for j in ids if j!=i]
      if not s.solve(assumptions=trial):ids=trial
    c=[cs[i-61] for i in ids];threshold=None
    for width in range(1,1+max(map(len,c))):
     with Solver(name='g4',bootstrap_with=[cl for cl in cs if len(cl)<=width]) as test:
      if not test.solve():threshold=width;break
    sel=[i for i in sel if len(cs[i-61])<=threshold]
    with Solver(name='g4',bootstrap_with=[[-i]+cs[i-61] for i in sel]) as s:
     assert not s.solve(assumptions=sel);ids=s.get_core()
     for i in ids.copy():
      trial=[j for j in ids if j!=i]
      if not s.solve(assumptions=trial):ids=trial
    c=[cs[i-61] for i in ids];cores.append(dict(seed17=t,seed24=key,clauses=c,first_unsat_width=threshold));print('core size / first unsat width',len(c),threshold,flush=True)
   return None
  pos=set(sl.get_model());
  for i,j in itertools.product(*groups):
   if 1+12*(i-12)+j-17 in pos:adj[i]|=1<<j;adj[j]|=1<<i
 assert check(adj,(1<<29)-1,4,6) and check(adj,(1<<17)-1,3,6) and check(adj,4095|(((1<<12)-1)<<17),4,5);return adj
out=[]
for typ,g in enumerate(refs,1):
 rec=dict(type=typ,hosts=sum(str(typ) in row for row in hosts),tested=0);out.append(rec)
 for t in itertools.combinations(range(17),12):
  G=graph(g,t);targets=by.get(sig(G),[])
  for H in targets:
   for m in nx.isomorphism.GraphMatcher(G,H).isomorphisms_iter():
    key=[m[i] for i in t];rec['tested']+=1;b=join(g,t,key)
    if b:rec.update(seed17=t,seed24=key,red_masks=b);break
   if 'red_masks' in rec:break
  if 'red_masks' in rec:break
 print(typ,rec['tested'],'red_masks' in rec,flush=True)
if scan:
 (P/'ramsey_sum10_screen.json').write_text(json.dumps(screens,indent=1)+'\n');print(collections.Counter((r['type'],r['screen'],r['sat']) for r in screens));sys.exit()
(P/'ramsey_sum10_type1_cores.json').write_text(json.dumps(cores,indent=1)+'\n')
(P/'ramsey_sum10_middle_join.json').write_text(json.dumps(dict(subsets24=sum(map(len,by.values())),types=out),indent=1)+'\n')

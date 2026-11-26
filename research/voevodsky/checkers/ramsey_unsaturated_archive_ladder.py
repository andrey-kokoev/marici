"""Classify archived rooted mask multisets (modulo cell order only) at successive exact SAT gates. Four-label maximum <=8 is a filter, not an assumption of nonextendibility. First failure witnesses suffice. No bounded solve used. Search for genuinely higher-order failures among compatible subfamilies if no full-pattern survivor."""
from ramsey_incidence_first35 import P,json,CardEnc,Solver,itertools,collections
from concurrent.futures import ProcessPoolExecutor
from functools import lru_cache
import random,sys
pairs=itertools.combinations
@lru_cache(None)
def profile(m):return max(sum(not s&t for s in m) for t in range(256) if t.bit_count()==4)
def archive():
 seen={}
 def walk(x):
  if isinstance(x,list):
   for y in x:walk(y)
  elif isinstance(x,dict):
   m=x.get('m',x.get('masks'))
   if isinstance(m,list) and len(m)==26 and all(type(i)==int and 0<i<256 for i in m):
    k=tuple(sorted(m));
    if k not in seen and all(sum(s>>j&1 for s in k)==7 for j in range(8)) and profile(k)<=8:seen[k]=f.name
   for y in x.values():
    if isinstance(y,(dict,list)):walk(y)
 for f in sorted(P.glob('ramsey_incidence*.json')):walk(json.loads(f.read_text()))
 return list(seen)
def run(m):
 E={p:i+1 for i,p in enumerate(p for p in pairs(range(26),2) if not m[p[0]]&m[p[1]])};n=len(E);rg={};cs=[]
 for t in sorted(range(256),key=int.bit_count):
  k=t.bit_count();guard=[]
  if k>5:break
  if k==5:n+=1;rg[t]=n;guard=[-n]
  for xs in pairs([i for i,s in enumerate(m) if not s&~t],k+1):
   c=[E[p] for p in pairs(xs,2) if p in E];
   if not c and k<=4:return ['forced4',t]
   cs.append(guard+c)
 for i,s in enumerate(m):
  b=CardEnc.equals([w for p,w in E.items() if i in p],8-s.bit_count(),top_id=n);n=max(n,b.nv);cs+=b.clauses
 for x in pairs(range(26),3):
  p=list(pairs(x,2));
  if all(v in E for v in p):cs.append([-E[v] for v in p])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  ass=lambda ts:[rg[t] for t in ts]
  if not sl.solve():return ['unsat4']
  for t in rg:
   if not sl.solve(assumptions=[rg[t]]):return ['single',t]
  for u,v in pairs(rg,2):
   if not sl.solve(assumptions=ass((u,v))):return ['pair',u,v]
  if sl.solve(assumptions=ass(rg)):return ['sat5']
  core=sl.get_core()
  for x in core[:]:
   if x in core and not sl.solve(assumptions=[y for y in core if x!=y]):core=sl.get_core()
  return ['higher',*[t for t in rg if rg[t] in core]]
if __name__=='__main__':
 ms=archive();print(len(ms),flush=True)
 with ProcessPoolExecutor(6) as ex:out=list(ex.map(run,ms,chunksize=8))
 print(collections.Counter(x[0] for x in out));(P/'ramsey_unsaturated_archive_ladder.json').write_text(json.dumps([dict(m=m,gate=z) for m,z in zip(ms,out)])+'\n')

"""Forget two label neighborhoods, keep six cube incidences only. Release every core edge. Order missing-bit pairs within cells with identical retained masks (legitimate vertex relabeling); enumerate row choices, not edge colorings. Lazy exact blue clique cuts: for blue Q, degree k>7 requires some internal red edge; otherwise must hit each complement of k-1 labels. Use a restricted small-label clause base plus violated full clauses from each SAT completion. No solver timeout is reported as an exclusion."""
import itertools,json,collections,sys,time
from pysat.card import CardEnc
from pysat.solvers import Solver
from ramsey_incidence_first35 import P
from ramsey_retention_slice import check

def run(dist,stage,probe=False):
 free=(0,(1<<dist)-1) if isinstance(dist,int) else tuple(dist);fnum=len(free);fm=sum(1<<v for v in free);m=[sum(1<<i for i in range(8) if i&k==v) for k in range(1,8) for v in range(8) if not v&~k];h=[s&~fm for s in m];groups=[[i for i,s in enumerate(h) if s==k] for k in sorted(set(h))];var=lambda i,j:1+i+26*j;E={(i,j):26*fnum+1+k for k,(i,j) in enumerate(itertools.combinations(range(26),2)) if not h[i]&h[j]};top=max(E.values());cs=[]
 for i,j,k in itertools.combinations(range(26),3):
  if (i,j) in E and (j,k) in E and (i,k) in E:cs.append([-E[i,j],-E[j,k],-E[i,k]])
 for (i,j),e in E.items():
  for b in range(fnum):cs.append([-e,-var(i,b),-var(j,b)])
 for g in groups:
  for i,j in zip(g,g[1:]):
   for a,b in itertools.product(range(1<<fnum),repeat=2):
    if a>b:cs.append([var(v,k)*(-1 if val>>k&1 else 1) for v,val in [(i,a),(j,b)] for k in range(fnum)])
 for xs,k in [([v for e,v in E.items() if i in e]+[var(i,j) for j in range(fnum)],8-s.bit_count()) for i,s in enumerate(h)]+[([var(i,j) for i in range(26)],7) for j in range(fnum)]:
  f=CardEnc.equals(xs,k,top_id=top);top=max(top,f.nv);cs.extend(f.clauses)
 def clause(q,t):return [E[e] for e in itertools.combinations(q,2) if e in E]+[var(i,j) for j,l in enumerate(free) if not t>>l&1 for i in q]
 # Only exact retained union needed: if a bad clique exists, a subset of size |T|+1 suffices; include nonexact unions too for propagation.
 for t in range(256):
  k=t.bit_count()
  if k>stage:continue
  for q in itertools.combinations([i for i,s in enumerate(h) if not s&~t],k+1):cs.append(clause(q,t))
 def canonical(nums):
  w=[0]*26
  for g in groups:
   for i,x in zip(g,sorted(nums[j] for j in g)):w[i]=x
  return tuple(w)
 expected={canonical([sum(((s>>l)&1)<<j for j,l in enumerate(f)) for s in m]) for f in itertools.permutations(free)};ans=[];cuts=0;models=0;start=time.perf_counter();path=P/(f'ramsey_cube_missing_two_{dist}.json' if fnum==2 else 'ramsey_cube_missing_more_'+''.join(map(str,free))+'.json')
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  if probe:
   for nums in expected:sl.add_clause([-var(i,j) for i,x in enumerate(nums) for j in range(fnum) if x>>j&1]);
   return dict(case=dist,stage=stage,admits_other=sl.solve())
  while sl.solve():
   model=set(sl.get_model());nums=[sum((var(i,j) in model)<<j for j in range(fnum)) for i in range(26)]; masks=[s|sum(((x>>j)&1)<<l for j,l in enumerate(free)) for s,x in zip(h,nums)];edges=[e for e,v in E.items() if v in model];a=[sum(1<<j for j in range(26) if tuple(sorted((i,j))) in edges) for i in range(26)];I=[((),0,0)]
   for i,v in enumerate(a):I.extend([(q+(i,),b|1<<i,u|masks[i]) for q,b,u in I if not b&v]);
   bad=[(q,u) for q,b,u in I if len(q)>min(7,u.bit_count())];models+=1
   if bad:
    for q,t in bad:
     if len(q)>=8:sl.add_clause([E[e] for e in itertools.combinations(q[:8],2) if e in E]);
     else:sl.add_clause(clause(q[:t.bit_count()+1],t))
    cuts+=len(bad);continue
   graph=a+[0]*9
   for j in range(8):
    v=26+j;s=sum(1<<i for i,t in enumerate(masks) if t>>j&1);graph[v]=s|1<<34;graph[34]|=1<<v
    for i in range(26):graph[i]|=(s>>i&1)<<v
   assert check(graph,(1<<35)-1,3,9);ans.append(dict(nums=nums,edges=edges));sl.add_clause([-var(i,j) for i,x in enumerate(nums) for j in range(fnum) if x>>j&1]);
 assert expected<=set(tuple(r['nums']) for r in ans);res=dict(distance=dist,free=free,stage=stage,models=models,cuts=cuts,expected=len(expected),nonstandard=sum(tuple(r['nums']) not in expected for r in ans),solutions=ans,seconds=time.perf_counter()-start);path.write_text(json.dumps(res)+'\n');return dist,len(ans),res['nonstandard'],models,cuts
if __name__=='__main__':
 import concurrent.futures as cf
 with cf.ProcessPoolExecutor(3) as ex:
  for f in cf.as_completed([ex.submit(run,i,int(sys.argv[1])) for i in (1,2,3)]):print(f.result(),flush=True)

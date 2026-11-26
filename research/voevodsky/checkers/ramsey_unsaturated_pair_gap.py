"""Maximum compatible regional families under pairwise versus simultaneous feasibility. Exact SAT cardinality, all core edges remain variable. If a maximum pairwise family fails jointly, extract an inclusion-minimal conflict of size >=3 and independently solve each deletion."""
from ramsey_unsaturated_conflict_trace import nodes,P,json,setup,Solver,CardEnc
from concurrent.futures import ProcessPoolExecutor
prior=json.loads((P/'ramsey_unsaturated_switches.json').read_text());T=[t for t in range(256) if t.bit_count()==5]
def best(cs,tags):
 n=max(abs(x) for c in cs for x in c);lo=0;hi=len(tags)+1;winner=[]
 while lo+1<hi:
  k=(hi+lo)//2;bounds=CardEnc.atleast(list(tags.values()),k,top_id=n)
  with Solver(name='cadical195',bootstrap_with=cs+bounds.clauses) as sl:
   if sl.solve():lo=k;s=set(sl.get_model());winner=[t for t,i in tags.items() if i in s];lo=max(lo,len(winner))
   else:hi=k
 return winner

def run(r):
 i=r['idx'];tags={t:j+1 for j,t in enumerate(T)};paircs=[[-tags[t]] for t in r['individually_failed']]+[[-tags[a],-tags[b]] for a,b,*_ in r['switch']+r['other']];pairwin=best(paircs,tags);cs,gs=setup(nodes[i]['m'],T);n=max(gs);tags={t:n+j+1 for j,t in enumerate(T)}
 for v,g in gs.items():cs.append([v] if g[0]!='cover' or g[1].bit_count()<5 else [-tags[g[1]],v])
 # setup deduplicates clauses across five-regions: a repeated edge clause can be necessary under either activation! Reinsert full independent regional demands, leaving dedup implication valid.
 import itertools
 m=nodes[i]['m'];E={e:k+1 for k,e in enumerate(e for e in itertools.combinations(range(26),2) if not m[e[0]]&m[e[1]])}
 for t in T:
  for xs in itertools.combinations([j for j,s in enumerate(m) if not s&~t],6):cs.append([-tags[t]]+[E[p] for p in itertools.combinations(xs,2) if p in E])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  a=[tags[t] for t in pairwin];core=[]
  if not sl.solve(assumptions=a):
   core=sl.get_core()
   for x in core[:]:
    if x in core and not sl.solve(assumptions=[y for y in core if x!=y]):core=sl.get_core()
   assert len(core)>=3 and all(sl.solve(assumptions=[y for y in core if y!=x]) for x in core)
 joint=best(cs,tags) if core else pairwin
 return dict(i=i,pairwise=len(pairwin),joint=len(joint),pairwin=pairwin,jointwin=joint,higher=[t for t in tags if tags[t] in core])
if __name__=='__main__':
 out=[]
 with ProcessPoolExecutor(4) as ex:
  for z in ex.map(run,prior):out.append(z);print(z['i'],z['pairwise'],z['joint'],z['higher'],flush=True);(P/'ramsey_unsaturated_pair_gap.json').write_text(json.dumps(out)+'\n')

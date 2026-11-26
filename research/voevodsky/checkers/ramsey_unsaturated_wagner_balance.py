"""Census balanced Wagner completions using five-label partial-screen survivors (retain unknown). Six masks of size 4 with each label used three times. Remind: actual core masks have size <=5 from common-blue (3,7) bound. Thus any unbalanced case must contain equally many triples and quintuples."""
from ramsey_unsaturated_pair_graphs import *
from concurrent.futures import ProcessPoolExecutor
if __name__=='__main__':
 z=json.loads((P/'ramsey_unsaturated_skeleton_budget.json').read_text())[1];opts=[s for r in z['orbits'] if r['ok'] is not False for s in r['masks'] if s.bit_count()==4];f=tuple(single+[1<<i|1<<j for i,j in z['edges']]);G=[[sum(1<<p[i] for i in V if x>>i&1) for x in range(256)] for p in ig.Graph(8,z['edges']).get_automorphisms_vf2()];code=lambda s:sum(8**i for i in V if s>>i&1);target=3*code(255);B=collections.defaultdict(list)
 for t in itertools.combinations_with_replacement(sorted(opts),3):B[sum(code(s) for s in t)].append(t)
 seen=set();ts=[];total=0
 for u,ls in B.items():
  for a in ls:
   for b in B.get(target-u,[]):
    if a[-1]>b[0]:continue
    t=a+b;total+=1
    if t in seen:continue
    seen.update(tuple(sorted(p[s] for s in t)) for p in G);ts.append(t)
 assert len(seen)==total
 with ProcessPoolExecutor(8) as ex:rs=list(ex.map(run,[f+t for t in ts],chunksize=8));
 h=collections.Counter(r[0] for r in rs);print(total,len(ts),h);(P/'ramsey_unsaturated_wagner_balance.json').write_text(json.dumps(dict(total=total,types=len(ts),counts=h,surv=[dict(t=t,r=r) for t,r in zip(ts,rs) if r[0] not in ('unsat4','forced4')]))+'\n')

"""Unbalanced Wagner completions have a triple in a single orbit. Fix rep 13. Screen every companion by induced five-label and degree-budget test; retain timeouts. Fill five remaining positions by exact 2+3 meet-in-the-middle. Enumeration fixes a marked triple, not distinct unmarked types."""
from ramsey_unsaturated_skeleton_budget import *
from concurrent.futures import ProcessPoolExecutor
if __name__=='__main__':
 z=json.loads((P/'ramsey_unsaturated_skeleton_budget.json').read_text())[1];opts=[s for r in z['orbits'] if r['ok'] is not False for s in r['masks'] if 3<=s.bit_count()<=5];f=tuple(single+[1<<i|1<<j for i,j in z['edges']]);q=13;code=lambda s:sum(8**i for i in V if s>>i&1);target=3*code(255)-code(q);B=collections.defaultdict(list)
 with ProcessPoolExecutor(8) as ex:
  rs=list(ex.map(budget,[f+(q,s) for s in opts]));alive=sorted(s for s,r in zip(opts,rs) if r is not False);print('companions',len(alive),'unknown',rs.count(None),flush=True)
  for t in itertools.combinations_with_replacement(alive,2):B[sum(code(s) for s in t)].append(t)
  ts=[(q,)+a+b for b in itertools.combinations_with_replacement(alive,3) for a in B.get(target-sum(code(s) for s in b),[]) if a[-1]<=b[0]];print('full',len(ts),flush=True);ans=list(ex.map(run,[f+t for t in ts],chunksize=8));h=collections.Counter(r[0] for r in ans);print(h);(P/'ramsey_unsaturated_wagner_triple.json').write_text(json.dumps(dict(q=q,tests=list(zip(opts,rs)),count=len(ts),status=h,surv=[dict(t=t,r=r) for t,r in zip(ts,ans) if r[0] not in ('unsat4','forced4')]))+'\n')

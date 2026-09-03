import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def leq(K,L):return all(a<=b for a,b in zip(K,L))
cases=0;intervals=0;obstruction=None
for r in range(k-1):
 if obstruction:break
 for T in itertools.combinations(range(k),r):
  if obstruction:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   raw=dict(source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,)))));cases+=1;total=sum(raw.values());o=1 if total>0 else -1;vals={K:o*v for K,v in raw.items()};positive=[K for K,v in vals.items() if v>0]
   for K in positive:
    for L in positive:
     if K==L or not leq(K,L):continue
     intervals+=1;members=[M for M in vals if leq(K,M) and leq(M,L)];res=sum(vals[M] for M in members)
     if res<0:
      obstruction={'base':T,'i':i,'j':j,'minimum':K,'maximum':L,'member_count':len(members),'members':members,'residual':str(res)};break
    if obstruction:break
   if obstruction:break
result={'schema':'marici.strominger.rh_quarter_gale_positive_corner_interval_sums.v1','status':'failed' if obstruction else 'passed','terminal_cases_reached':cases,'positive_corner_intervals_tested':intervals,'first_obstruction':obstruction,'verdict':'Positive-corner Gale intervals do not universally have nonnegative terminal-oriented sum.' if obstruction else 'Every fixed-eight positive-corner Gale interval has nonnegative terminal-oriented sum.','checks':{'nontrivial_intervals_tested':intervals>0,'universal_positive_corner_interval_sum':obstruction is None}}
(base/'results'/'rh_quarter_gale_positive_corner_interval_sums.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def covers(K):
 for a in range(len(K)):
  L=list(K);L[a]+=1
  if L[a]<k and (a+1==len(L) or L[a]<L[a+1]):yield tuple(L)
cases=0;chains=0;obstruction=None
for r in range(k-1):
 if obstruction:break
 for T in itertools.combinations(range(k),r):
  if obstruction:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   vals={K:v for K,v in source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))))};cases+=1;total=sum(vals.values());o=1 if total>0 else -1
   for K0 in vals:
    for K1 in covers(K0):
     if K1 not in vals:continue
     for K2 in covers(K1):
      if K2 not in vals:continue
      chains+=1;vs=[o*vals[K] for K in (K0,K1,K2)];res=sum(vs)
      if res<0:
       obstruction={'base':T,'i':i,'j':j,'chain':[K0,K1,K2],'oriented_values':list(map(str,vs)),'residual':str(res)};break
     if obstruction:break
    if obstruction:break
   if obstruction:break
result={'schema':'marici.strominger.rh_quarter_gale_three_term_chain_rescue.v1','status':'failed' if obstruction else 'passed','terminal_cases_reached':cases,'nonzero_two_cover_chains_tested':chains,'first_obstruction':obstruction,'verdict':'Three-term Gale parity blocks do not universally have terminal-total-positive residual.' if obstruction else 'Every fixed-eight nonzero two-cover Gale chain has nonnegative terminal-oriented three-term residual.','checks':{'chains_tested':chains>0,'universal_three_term_rescue':obstruction is None}}
(base/'results'/'rh_quarter_gale_three_term_chain_rescue.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

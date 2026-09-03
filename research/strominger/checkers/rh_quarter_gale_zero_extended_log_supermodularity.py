import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def move(K,a):
 L=list(K);L[a]+=1
 return tuple(L) if L[a]<k and (a+1==len(L) or L[a]<L[a+1]) else None
cases=0;diamonds=0;boundary=0;violation=None
for r in range(k-1):
 if violation:break
 allK=list(itertools.combinations(range(k),r+1))
 for T in itertools.combinations(range(k),r):
  if violation:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   weights={K:abs(v) for K,v in source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))))};cases+=1
   for K in allK:
    for a,b in itertools.combinations(range(len(K)),2):
     Ka,Kb=move(K,a),move(K,b)
     if Ka is None or Kb is None:continue
     Kab=move(Ka,b)
     if Kab is None or Kab!=move(Kb,a):continue
     diamonds+=1;vals=[weights.get(X,0) for X in (K,Ka,Kb,Kab)]
     if not all(vals):boundary+=1
     lhs=vals[0]*vals[3];rhs=vals[1]*vals[2]
     if lhs<rhs:
      violation={'base':T,'i':i,'j':j,'meet':K,'left_cover':Ka,'right_cover':Kb,'join':Kab,'weights':list(map(str,vals)),'lhs':str(lhs),'rhs':str(rhs),'residual_lhs_minus_rhs':str(lhs-rhs)};break
    if violation:break
   if violation:break
result={'schema':'marici.strominger.rh_quarter_gale_zero_extended_log_supermodularity.v1','status':'failed' if violation else 'passed','terminal_cases_reached':cases,'diamonds_tested':diamonds,'boundary_diamonds_tested':boundary,'first_violation':violation,'verdict':'Zero-extended source weights fail Gale log-supermodularity at an exact support-boundary obstruction.' if violation else 'Zero-extended source weights satisfy fixed-eight Gale log-supermodularity.','checks':{'boundary_test_executed':boundary>0,'no_violation':violation is None}}
(base/'results'/'rh_quarter_gale_zero_extended_log_supermodularity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

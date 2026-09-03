import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def move(K,a):
 L=list(K);L[a]+=1
 return tuple(L) if L[a]<k and (a+1==len(L) or L[a]<L[a+1]) else None
cases=0;diamonds=0;violation=None
for r in range(k-1):
 if violation:break
 for T in itertools.combinations(range(k),r):
  if violation:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));weights={K:abs(v) for K,v in source_terms(R,S) if v};cases+=1
   for K,w0 in weights.items():
    for a,b in itertools.combinations(range(len(K)),2):
     Ka,Kb=move(K,a),move(K,b)
     if Ka is None or Kb is None:continue
     Kab=move(Ka,b)
     if Kab is None or Kab!=move(Kb,a):continue
     if Ka not in weights or Kb not in weights or Kab not in weights:continue
     diamonds+=1;lhs=w0*weights[Kab];rhs=weights[Ka]*weights[Kb]
     if lhs<rhs:
      violation={'base':T,'i':i,'j':j,'meet':K,'left_cover':Ka,'right_cover':Kb,'join':Kab,'lhs':str(lhs),'rhs':str(rhs),'residual_lhs_minus_rhs':str(lhs-rhs)};break
    if violation:break
   if violation:break
result={'schema':'marici.strominger.rh_quarter_gale_weight_log_supermodularity.v1','status':'failed' if violation else 'passed','terminal_cases_reached':cases,'nonzero_diamonds_tested':diamonds,'first_violation':violation,'verdict':'Absolute source weights are not Gale log-supermodular.' if violation else 'All fixed-eight nonzero Gale diamonds satisfy log-supermodularity.','checks':{'diamond_test_executed':diamonds>0,'no_violation':violation is None}}
(base/'results'/'rh_quarter_gale_weight_log_supermodularity.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

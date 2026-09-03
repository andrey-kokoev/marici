import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')))
source_terms,k=g['source_terms'],g['k']
orders={'lex':lambda K:K,'reverse_lex':lambda K:tuple(-x for x in K),'sum_then_lex':lambda K:(sum(K),K),'reverse_sum_then_lex':lambda K:(-sum(K),K)}
stats={n:{'cases_with_prefix_deficit':0,'first_deficit':None} for n in orders};cases=0
for r in range(k-1):
 for T in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   R=tuple(sorted(T+(i,)));S=tuple(sorted(T+(j,)));et=(-1)**(j-i+1) if i<j else (-1)**(i-j);expected=et*(-1)**(sum(x>i for x in T)+sum(x>j for x in T));terms=source_terms(R,S);cases+=1
   for name,key in orders.items():
    acc=0;bad=None
    for K,v in sorted(terms,key=lambda kv:key(kv[0])):
     acc+=expected*v
     if acc<0 and bad is None:bad={'base':T,'i':i,'j':j,'K':K,'prefix_residual':str(acc)}
    if bad:
     stats[name]['cases_with_prefix_deficit']+=1
     if stats[name]['first_deficit'] is None:stats[name]['first_deficit']=bad
successful=[n for n,s in stats.items() if s['cases_with_prefix_deficit']==0]
result={'schema':'marici.strominger.rh_quarter_fixed_eight_signed_mass_transport.v1','status':'passed' if successful else 'failed','verdict':'A natural label order certifies positive-to-negative mass transport only if every oriented prefix is nonnegative in all terminal cases.','terminal_case_count':cases,'successful_orders':successful,'order_statistics':stats,'checks':{'all_terminal_cases_visited':cases==3584,'natural_order_certificate_found':bool(successful)}}
(base/'results'/'rh_quarter_fixed_eight_signed_mass_transport.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

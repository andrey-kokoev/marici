import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def covers(K):
 for a in range(len(K)):
  L=list(K);L[a]+=1
  if L[a]<k and (a+1==len(L) or L[a]<L[a+1]):yield tuple(L)
cases=0;covers_tested=0;obstruction=None
for r in range(k-1):
 if obstruction:break
 for T in itertools.combinations(range(k),r):
  if obstruction:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   vals={K:v for K,v in source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))))};cases+=1;total=sum(vals.values());orientation=1 if total>0 else -1
   for K,v in vals.items():
    for L in covers(K):
     if L not in vals:continue
     covers_tested+=1;a=orientation*v;b=orientation*vals[L]
     positive=abs(a) if a>0 else abs(b);negative=abs(a) if a<0 else abs(b)
     if positive<negative:
      obstruction={'base':T,'i':i,'j':j,'lower':K,'upper':L,'oriented_values':[str(a),str(b)],'positive_magnitude':str(positive),'negative_magnitude':str(negative),'residual_positive_minus_negative':str(positive-negative)};break
    if obstruction:break
   if obstruction:break
result={'schema':'marici.strominger.rh_quarter_gale_parity_cover_dominance.v1','status':'failed' if obstruction else 'passed','terminal_cases_reached':cases,'nonzero_covers_tested':covers_tested,'first_obstruction':obstruction,'verdict':'Local Gale-cover dominance toward the total-positive parity fails exactly.' if obstruction else 'Every fixed-eight nonzero Gale cover is dominated by its total-positive endpoint.','checks':{'covers_tested':covers_tested>0,'universal_positive_cover_dominance':obstruction is None}}
(base/'results'/'rh_quarter_gale_parity_cover_dominance.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

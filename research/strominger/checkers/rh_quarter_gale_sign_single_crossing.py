import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
def covers(K):
 for a in range(len(K)):
  L=list(K);L[a]+=1
  if L[a]<k and (a+1==len(L) or L[a]<L[a+1]):yield tuple(L)
cases=0;two_steps=0;obstruction=None
for r in range(k-1):
 if obstruction:break
 for T in itertools.combinations(range(k),r):
  if obstruction:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   vals={K:v for K,v in source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))))};cases+=1
   for K0,v0 in vals.items():
    for K1 in covers(K0):
     if K1 not in vals:continue
     for K2 in covers(K1):
      if K2 not in vals:continue
      two_steps+=1;s=[1 if vals[K]>0 else -1 for K in (K0,K1,K2)]
      if s[0]==s[2] and s[0]!=s[1]:
       obstruction={'base':T,'i':i,'j':j,'chain':[K0,K1,K2],'signs':s,'values':[str(vals[K]) for K in (K0,K1,K2)]};break
     if obstruction:break
    if obstruction:break
   if obstruction:break
result={'schema':'marici.strominger.rh_quarter_gale_sign_single_crossing.v1','status':'failed' if obstruction else 'passed','terminal_cases_reached':cases,'nonzero_two_cover_chains_tested':two_steps,'first_sign_interlacing':obstruction,'verdict':'Terminal source signs are not single-crossing along Gale chains.' if obstruction else 'No fixed-eight two-change sign interlacing occurs along nonzero Gale two-cover chains.','checks':{'chains_tested':two_steps>0,'no_sign_interlacing':obstruction is None}}
(base/'results'/'rh_quarter_gale_sign_single_crossing.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

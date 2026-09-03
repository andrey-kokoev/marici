import itertools,json,runpy
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name('rh_quarter_hurwitz_terminal_minor_source_formula.py')));source_terms,k=g['source_terms'],g['k']
cases=0;terms=0;plus_cases=0;minus_cases=0;obstruction=None
for r in range(k-1):
 if obstruction:break
 for T in itertools.combinations(range(k),r):
  if obstruction:break
  rem=[x for x in range(k) if x not in T]
  for i,j in itertools.permutations(rem,2):
   xs=source_terms(tuple(sorted(T+(i,))),tuple(sorted(T+(j,))));cases+=1;terms+=len(xs)
   chars={(1 if v>0 else -1)*((-1)**sum(K)) for K,v in xs}
   if len(chars)!=1:
    first=next(iter(chars));bad=next((K,v) for K,v in xs if (1 if v>0 else -1)*((-1)**sum(K))!=first)
    obstruction={'base':T,'i':i,'j':j,'twisted_characters':sorted(chars),'bad_label':bad[0],'bad_value':str(bad[1])};break
   c=next(iter(chars));plus_cases+=c==1;minus_cases+=c==-1
result={'schema':'marici.strominger.rh_quarter_gale_sign_parity_character.v1','status':'failed' if obstruction else 'passed','terminal_cases_reached':cases,'nonzero_terms_tested':terms,'case_character_counts':{'+1':plus_cases,'-1':minus_cases},'first_obstruction':obstruction,'verdict':'Every fixed-eight terminal source sign is a case-dependent constant times (-1)^{sum K}.' if not obstruction else 'The checkerboard parity character has an exact obstruction.','checks':{'all_cases':cases==3584,'terms_tested':terms>0,'universal_casewise_parity':obstruction is None}}
(base/'results'/'rh_quarter_gale_sign_parity_character.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

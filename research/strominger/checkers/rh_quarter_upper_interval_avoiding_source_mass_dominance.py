import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_terminal_minor_source_formula.py")))
source_terms,k=g["source_terms"],g["k"]
cases=0;coherent=0;first_failure=None;max_ratio=F(-1);max_case=None;by_base={}
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.combinations(rem,2):
   if any(i<q<j for q in S):continue
   R=tuple(sorted(S+(i,)));Q=tuple(sorted(S+(j,)));expected=(-1)**(j-i+1+sum(x>i for x in S)+sum(x>j for x in S));vals=[expected*z for _,z in source_terms(R,Q)];pos=sum(z for z in vals if z>0);neg=-sum(z for z in vals if z<0);cases+=1;by_base[str(r)]=by_base.get(str(r),0)+1
   if neg==0:coherent+=1
   if not pos>neg and first_failure is None:first_failure={"base":S,"i":i,"j":j,"positive_mass":str(pos),"negative_mass":str(neg)}
   ratio=neg/pos
   if ratio>max_ratio:max_ratio=ratio;max_case={"base":S,"i":i,"j":j,"positive_mass":str(pos),"negative_mass":str(neg),"negative_to_positive_ratio":str(ratio)}
checks={"all_769_upper_interval_avoiding_cases_checked":cases==769,"all_oriented_positive_source_mass_strictly_dominates_negative_mass":first_failure is None,"mixed_sign_cases_present":coherent<cases,"worst_case_ratio_strictly_below_one":max_ratio<1}
result={"schema":"marici.strominger.rh_quarter_upper_interval_avoiding_source_mass_dominance.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For every upper-oriented interval-avoiding terminal source expansion, total correctly oriented source mass strictly exceeds oppositely oriented mass. This exactly isolates cancellation as a positive-mass domination inequality; termwise coherence occurs only in a bounded subset. The maximizing ratio identifies the sharpest finite stress case but does not establish an all-order bound.","case_count":cases,"sign_coherent_case_count":coherent,"case_count_by_base_size":by_base,"first_failure":first_failure,"maximum_negative_to_positive_ratio":str(max_ratio),"maximum_ratio_case":max_case,"checks":checks}
(base/"results"/"rh_quarter_upper_interval_avoiding_source_mass_dominance.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_terminal_bordered_schur_signs.py")))
C,dm,k=g["C"],g["dm"],g["k"]
def P(T):T=list(T);return dm(T,T)
def D(T,i,j):T=list(T);return dm(T+[i],T+[j])
reducible=0;upper_reinforcing=0;lower_competing=0;irreducible=0;first_identity_failure=None;first_classification_failure=None;irreducible_by_base_size={}
for r in range(k-1):
 for S in itertools.combinations(range(k),r):
  rem=[x for x in range(k) if x not in S]
  for i,j in itertools.permutations(rem,2):
   internal=[q for q in S if min(i,j)<q<max(i,j)]
   if not internal:
    irreducible+=1;irreducible_by_base_size[str(r)]=irreducible_by_base_size.get(str(r),0)+1;continue
   q=internal[0];T=tuple(x for x in S if x!=q);lhs=D(S,i,j)*P(T);first=P(S)*D(T,i,j);second=D(T,q,j)*D(T,i,q);reducible+=1
   if lhs!=first-second and first_identity_failure is None:first_identity_failure={"base":S,"i":i,"j":j,"pivot":q,"residual":str(lhs-first+second)}
   full=D(S,i,j)
   if i<j and first*full>0 and second*full<0:upper_reinforcing+=1
   elif i>j and first*full>0 and second*full>0:lower_competing+=1
   elif first_classification_failure is None:first_classification_failure={"base":S,"i":i,"j":j,"pivot":q,"full":str(full),"principal_term":str(first),"cross_term":str(second)}
checks={"all_3584_oriented_cases_partitioned":reducible+irreducible==3584,"all_internal_pivot_condensation_identities_exact":first_identity_failure is None,"all_internal_cases_split_into_upper_reinforcing_and_lower_competing":upper_reinforcing+lower_competing==reducible and first_classification_failure is None,"irreducible_interval_avoiding_frontier_nonempty":irreducible>0}
result={"schema":"marici.strominger.rh_quarter_terminal_dodgson_condensation_source_induction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Desnanot-Jacobi gives D(S;i,j)P(T)=P(S)D(T;i,j)-D(T;q,j)D(T;i,q) for T=S\\{q}. An internal q makes every upper-oriented cross product oppose the target, so subtraction reinforces it and yields noncircular sign induction. The paired lower-oriented cross product has the target sign and still requires magnitude control. Interval-avoiding bases admit no internal reduction.","internally_reducible_case_count":reducible,"upper_reinforcing_case_count":upper_reinforcing,"lower_competing_case_count":lower_competing,"interval_avoiding_case_count":irreducible,"interval_avoiding_by_base_size":irreducible_by_base_size,"first_identity_failure":first_identity_failure,"first_classification_failure":first_classification_failure,"checks":checks}
(base/"results"/"rh_quarter_terminal_dodgson_condensation_source_induction.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

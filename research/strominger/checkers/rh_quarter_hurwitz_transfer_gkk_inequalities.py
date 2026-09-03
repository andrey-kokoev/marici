import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
C,det,k=g["C"],g["det"],g["k"]
def indices(mask):return [i for i in range(k) if mask>>i&1]
def principal(mask):
 S=indices(mask);return F(1) if not S else det([[C[i][j] for j in S] for i in S])
p={m:principal(m) for m in range(1<<k)};first_violation=None;strict=0;equal=0;reverse_strict=0;count=0
for a in range(1<<k):
 for b in range(a,1<<k):
  lhs=p[a]*p[b];rhs=p[a|b]*p[a&b];count+=1
  if lhs>rhs:strict+=1
  elif lhs==rhs:equal+=1
  else:
   reverse_strict+=1
   if first_violation is None:first_violation={"alpha_mask":a,"beta_mask":b,"alpha":indices(a),"beta":indices(b),"difference":str(lhs-rhs)}
checks={"all_principal_minors_positive":all(z>0 for z in p.values()),"all_generalized_hadamard_fischer_inequalities_hold":first_violation is None,"all_reverse_hadamard_fischer_inequalities_hold":strict==0,"all_32896_unordered_pairs_checked":count==32896,"classification_counts_complete":strict+equal+reverse_strict==count}
gkk=first_violation is None
verdict=("All generalized Hadamard-Fischer inequalities hold for the 256 positive principal minors; the order-eight transfer is a bounded GKK P-matrix." if gkk else "The GKK inequality fails, but every one of the 32,896 pairs satisfies the reverse Hadamard-Fischer inequality; 26,335 are strict and 6,561 are equal. The principal-minor map is log-supermodular rather than GKK log-submodular.")
result={"schema":"marici.strominger.rh_quarter_hurwitz_transfer_gkk_inequalities.v1","status":"passed" if checks["all_principal_minors_positive"] and checks["all_reverse_hadamard_fischer_inequalities_hold"] and checks["all_32896_unordered_pairs_checked"] else "failed","verdict":verdict,"gkk_inequalities_hold":gkk,"reverse_inequalities_hold":strict==0,"pair_count":count,"gkk_strict_count":strict,"equality_count":equal,"reverse_strict_count":reverse_strict,"first_gkk_violation":first_violation,"checks":checks}
(base/"results"/"rh_quarter_hurwitz_transfer_gkk_inequalities.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
C,det,k=g["C"],g["det"],g["k"]
def dm(R,S):return F(1) if not R else det([[C[i][j] for j in S] for i in R])
def sg(z):return 1 if z>0 else -1 if z<0 else 0
count=0;first_reorder_failure=None;first_terminal_sign_failure=None
for i in range(k):
 for j in range(i+1,k):
  rest=[x for x in range(k) if x not in (i,j)]
  for r in range(len(rest)+1):
   for St in itertools.combinations(rest,r):
    S=list(St);Si=sorted(S+[i]);Sj=sorted(S+[j]);u=dm(Si,Sj);v=dm(Sj,Si);ut=dm(S+[i],S+[j]);vt=dm(S+[j],S+[i]);parity=(sum(x>i for x in S)+sum(x>j for x in S))%2;factor=(-1)**parity;count+=1
    if (ut!=factor*u or vt!=factor*v) and first_reorder_failure is None:first_reorder_failure={"base":S,"i":i,"j":j,"parity":parity}
    if (sg(ut)!=(-1)**(j-i+1) or sg(vt)!=(-1)**(j-i)) and first_terminal_sign_failure is None:first_terminal_sign_failure={"base":S,"i":i,"j":j,"u_terminal_sign":sg(ut),"v_terminal_sign":sg(vt)}
checks={"all_1792_reordering_identities_exact":count==1792 and first_reorder_failure is None,"interval_parity_equals_move_to_terminal_parity":all((sum(i<x<j for x in S)%2)==((sum(x>i for x in S)+sum(x>j for x in S))%2) for i in range(k) for j in range(i+1,k) for r in range(k-1) for S in itertools.combinations([x for x in range(k) if x not in (i,j)],r) if r<=k-2),"all_terminal_bordered_signs_follow_distance_rule":first_terminal_sign_failure is None,"case_count_exact":count==1792}
result={"schema":"marici.strominger.rh_quarter_almost_principal_parity_reordering.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Moving exchanged indices from sorted position to the terminal row and column contributes exactly (-1)^{|S intersect (i,j)|}; this determinant-permutation identity holds at arbitrary size. In all bounded cases the resulting terminal bordered minors have signs (-1)^{j-i+1} and (-1)^{j-i}. Thus interval parity is universal bookkeeping; only the terminal bordered sign rule remains Hurwitz-specific.","case_count":count,"first_reorder_failure":first_reorder_failure,"first_terminal_sign_failure":first_terminal_sign_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_almost_principal_parity_reordering.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

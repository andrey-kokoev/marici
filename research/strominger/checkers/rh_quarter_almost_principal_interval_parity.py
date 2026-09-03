import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
C,det,k=g["C"],g["det"],g["k"]
def dm(R,S):return F(1) if not R else det([[C[i][j] for j in S] for i in R])
def sg(z):return 1 if z>0 else -1 if z<0 else 0
count=0;first_u_failure=None;first_v_failure=None;pair_rules={}
for i in range(k):
 for j in range(i+1,k):
  base_u=sg(C[i][j]);base_v=sg(C[j][i]);rest=[x for x in range(k) if x not in (i,j)];pair_rules[f"{i},{j}"]={"base_u_sign":base_u,"base_v_sign":base_v,"base_signs_opposite":base_u*base_v==-1}
  for r in range(len(rest)+1):
   for St in itertools.combinations(rest,r):
    S=sorted(St);Si=sorted(S+[i]);Sj=sorted(S+[j]);parity=sum(i<x<j for x in S)%2;pred_u=base_u*((-1)**parity);pred_v=base_v*((-1)**parity);u=dm(Si,Sj);v=dm(Sj,Si);count+=1
    if sg(u)!=pred_u and first_u_failure is None:first_u_failure={"base":S,"i":i,"j":j,"observed":sg(u),"predicted":pred_u}
    if sg(v)!=pred_v and first_v_failure is None:first_v_failure={"base":S,"i":i,"j":j,"observed":sg(v),"predicted":pred_v}
checks={"all_1792_first_minor_signs_follow_interval_parity":count==1792 and first_u_failure is None,"all_1792_paired_minor_signs_follow_interval_parity":first_v_failure is None,"all_empty_base_signs_opposite":all(x["base_signs_opposite"] for x in pair_rules.values()),"empty_base_u_sign_is_distance_parity":all(pair_rules[f"{i},{j}"]["base_u_sign"]==(-1)**(j-i+1) for i in range(k) for j in range(i+1,k)),"all_twenty_eight_pair_rules_classified":len(pair_rules)==28}
result={"schema":"marici.strominger.rh_quarter_almost_principal_interval_parity.v1","status":"passed" if all(checks.values()) else "failed","verdict":"All 1,792 almost-principal pairs obey one exact sign law. For i<j, the first sign is (-1)^(j-i+1+|S intersect (i,j)|), and the paired minor has the opposite sign. Therefore every paired product is negative by interval parity, explaining the bounded anti-sign-symmetry without casewise orientation choices.","case_count":count,"first_u_failure":first_u_failure,"first_v_failure":first_v_failure,"pair_rules":pair_rules,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_almost_principal_interval_parity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

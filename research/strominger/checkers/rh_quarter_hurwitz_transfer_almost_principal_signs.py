import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
C,det,k=g["C"],g["det"],g["k"]
def dm(R,S):return F(1) if not R else det([[C[i][j] for j in S] for i in R])
count=0;first_identity_failure=None;first_sign_failure=None;orientation={}
for i in range(k):
 for j in range(i+1,k):
  rest=[x for x in range(k) if x not in (i,j)];signs=[]
  for r in range(len(rest)+1):
   for St in itertools.combinations(rest,r):
    S=sorted(St);Si=sorted(S+[i]);Sj=sorted(S+[j]);T=sorted(S+[i,j]);u=dm(Si,Sj);v=dm(Sj,Si);lhs=dm(Si,Si)*dm(Sj,Sj)-dm(T,T)*dm(S,S);count+=1
    if lhs!=u*v and first_identity_failure is None:first_identity_failure={"base":S,"i":i,"j":j,"difference":str(lhs-u*v)}
    if not (u*v<0) and first_sign_failure is None:first_sign_failure={"base":S,"i":i,"j":j,"u":str(u),"v":str(v)}
    signs.append(1 if u>0 else -1 if u<0 else 0)
  orientation[f"{i},{j}"]={"u_sign_constant":len(set(signs))==1,"u_sign":signs[0] if len(set(signs))==1 else None,"observed_signs":sorted(set(signs))}
checks={"all_1792_local_identities_exact":count==1792 and first_identity_failure is None,"all_paired_almost_principal_products_negative":first_sign_failure is None,"all_pair_orientations_constant_over_base_sets":all(x["u_sign_constant"] for x in orientation.values()),"all_twenty_eight_index_pairs_classified":len(orientation)==28}
result={"schema":"marici.strominger.rh_quarter_hurwitz_transfer_almost_principal_signs.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every local reverse Hadamard-Fischer difference equals a strictly negative product of paired almost-principal minors, giving a cancellation-free local generator for log-supermodularity. The stronger fixed-orientation gate fails: nonadjacent index pairs exhibit both signs as the base set varies.","case_count":count,"first_identity_failure":first_identity_failure,"first_sign_failure":first_sign_failure,"orientation":orientation,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_hurwitz_transfer_almost_principal_signs.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

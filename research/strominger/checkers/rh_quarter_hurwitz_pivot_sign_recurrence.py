import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_terminal_bordered_schur_signs.py")))
C,k,inv=g["C"],g["k"],g["inv"]
def schur(T):
 T=list(T);R=[x for x in range(k) if x not in T]
 if not T:return R,{(i,j):C[i][j] for i in R for j in R}
 AI=inv([[C[i][j] for j in T] for i in T]);M={}
 for i in R:
  for j in R:M[i,j]=C[i][j]-sum(C[i][T[a]]*AI[a][b]*C[T[b]][j] for a in range(len(T)) for b in range(len(T)))
 return R,M
cache={T:schur(T) for r in range(k+1) for T in itertools.combinations(range(k),r)}
interior=0;exterior=0;first_interior_failure=None;first_exterior_failure=None;first_update_failure=None
for r in range(k-2):
 for T in itertools.combinations(range(k),r):
  R,M=cache[T]
  for i,j in itertools.combinations(R,2):
   for p in R:
    if p in (i,j):continue
    term=M[i,p]*M[p,j]/M[p,p];updated=M[i,j]-term;Tp=tuple(sorted(T+(p,)));target=cache[Tp][1][i,j]
    if updated!=target and first_update_failure is None:first_update_failure={"base":T,"i":i,"j":j,"pivot":p}
    if i<p<j:
     interior+=1
     if not (M[i,j]*term<0) and first_interior_failure is None:first_interior_failure={"base":T,"i":i,"j":j,"pivot":p}
    else:
     exterior+=1
     if not (M[i,j]*term>0 and abs(M[i,j])>abs(term)) and first_exterior_failure is None:first_exterior_failure={"base":T,"i":i,"j":j,"pivot":p,"difference_of_magnitudes":str(abs(M[i,j])-abs(term))}
checks={"all_one_pivot_updates_exact":first_update_failure is None,"all_interior_pivots_reinforce_by_opposite_sign":first_interior_failure is None,"all_exterior_pivots_preserve_sign_by_strict_dominance":first_exterior_failure is None,"both_pivot_classes_nonempty":interior>0 and exterior>0}
result={"schema":"marici.strominger.rh_quarter_hurwitz_pivot_sign_recurrence.v1","status":"passed" if all(checks.values()) else "failed","verdict":"One-pivot Schur updates split into two mechanisms. A pivot strictly between i and j contributes the opposite sign and reinforces the target entry automatically. An exterior pivot contributes the same sign, so preservation requires the strict magnitude inequality |M_ij|>|M_ip M_pj/M_pp|. Every bounded update satisfies its exact class condition. Sign data alone therefore close only interior elimination; exterior dominance is the remaining quantitative invariant.","interior_update_count":interior,"exterior_update_count":exterior,"first_update_failure":first_update_failure,"first_interior_failure":first_interior_failure,"first_exterior_failure":first_exterior_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_hurwitz_pivot_sign_recurrence.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

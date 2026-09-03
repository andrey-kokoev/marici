import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def coeff(a,i):return a[i] if 0<=i<len(a) else F(0)
records=[];first_failure=None;tested=0
for n in range(2,9):
 for s in range(3):
  A=mu(D(n-2,s+2),D(n,s));R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));S=[coeff(A,i)+2*coeff(R,i) for i in range(max(len(A),len(R)))]
  for k in range(len(A)):
   m=2*k;w=[coeff(A,i)*coeff(S,m-i) for i in range(m+1)];shell=[w[k]]+[w[k-d]+w[k+d] for d in range(1,k+1)];mono=all(shell[d]>=shell[d+1] for d in range(len(shell)-1));alt=sum(((-1)**d)*z for d,z in enumerate(shell));positive=alt>0;rec={"n":n,"shift":s,"k":k,"shell_count":len(shell),"shells_nonincreasing":mono,"alternating_shell_sum_positive":positive,"first_increase":next((d for d in range(len(shell)-1) if shell[d]<shell[d+1]),None)};records.append(rec);tested+=1
   if not mono and first_failure is None:first_failure=rec
checks={"all_even_coefficients_profiled":tested==len(records) and tested>0,"alternating_shell_sums_positive":all(r["alternating_shell_sum_positive"] for r in records),"shell_monotonicity_classified":first_failure is not None or all(r["shells_nonincreasing"] for r in records)}
result={"schema":"marici.strominger.rh_quarter_D_even_shell_matching.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Centering each even reflected convolution at k rewrites its desired signed coefficient as an alternating sum of symmetric shells. Nonincreasing shells would give an immediate adjacent-shell injection; exact classification determines whether that sufficient condition holds.","profile_count":tested,"first_shell_monotonicity_failure":first_failure,"nonmonotone_profile_count":sum(not r["shells_nonincreasing"] for r in records),"records":records,"checks":checks}
(base/"results"/"rh_quarter_D_even_shell_matching.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"profile_count":tested,"first_failure":first_failure,"nonmonotone":result["nonmonotone_profile_count"],"checks":checks},indent=2))

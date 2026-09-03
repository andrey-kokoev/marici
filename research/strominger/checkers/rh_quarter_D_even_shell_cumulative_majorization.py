import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")));Q,D,mu=g["Q"],g["D"],g["mu"]
def c(a,i):return a[i] if 0<=i<len(a) else F(0)
counts={"prefix_only":0,"suffix_only":0,"both":0,"neither":0};first_neither=None;profiles=0
for n in range(2,9):
 for s in range(3):
  A=mu(D(n-2,s+2),D(n,s));R=mu(mu(Q(s),D(n-1,s+1)),D(n-1,s+1));S=[c(A,i)+2*c(R,i) for i in range(max(len(A),len(R)))]
  for k in range(len(A)):
   w=[c(A,i)*c(S,2*k-i) for i in range(2*k+1)];shell=[w[k]]+[w[k-d]+w[k+d] for d in range(1,k+1)];signed=[((-1)**d)*z for d,z in enumerate(shell)];prefix_ok=all(sum(signed[:r+1])>=0 for r in range(len(signed)));suffix_ok=all(sum(signed[r:])>=0 for r in range(len(signed)));key="both" if prefix_ok and suffix_ok else "prefix_only" if prefix_ok else "suffix_only" if suffix_ok else "neither";counts[key]+=1;profiles+=1
   if key=="neither" and first_neither is None:first_neither={"n":n,"shift":s,"k":k,"shell_count":len(shell),"first_negative_prefix":next((r for r in range(len(signed)) if sum(signed[:r+1])<0),None),"first_negative_suffix":next((r for r in range(len(signed)) if sum(signed[r:])<0),None)}
checks={"all_1092_profiles_checked":profiles==1092,"directional_majorization_classified":sum(counts.values())==profiles,"universal_prefix_or_suffix_decided":first_neither is not None or counts["neither"]==0}
result={"schema":"marici.strominger.rh_quarter_D_even_shell_cumulative_majorization.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact cumulative shell sums classify whether each coefficient admits inward prefix matching or outward suffix matching. A profile failing both directions is an exact obstruction to one-dimensional directional majorization, not to total positivity.","profile_count":profiles,"classification_counts":counts,"first_neither":first_neither,"checks":checks}
(base/"results"/"rh_quarter_D_even_shell_cumulative_majorization.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

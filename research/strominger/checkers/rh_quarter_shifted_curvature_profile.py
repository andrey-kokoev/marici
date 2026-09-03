import json,math
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def R(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*R(n-1,a)*R(n-1,a+2)-q(a,0)*R(n-1,a+1)**2)/R(n-2,a+2)
profiles=[]
for a in range(7):
 rows=[]
 for n in range(2,23):
  C=R(n-1,a+1)**2/(R(n-1,a)*R(n-1,a+2));theta=q(a,0)*C/q(a,n-1)
  rows.append({"n":n,"n_theta":float(n*theta),"n2_theta":float(n*n*theta),"balance":math.log(float(C))-2*math.log(n)})
 late=rows[-5:];v1=[r["n_theta"] for r in late];v2=[r["n2_theta"] for r in late];rel1=(max(v1)-min(v1))/(sum(v1)/5);rel2=(max(v2)-min(v2))/(sum(v2)/5)
 profiles.append({"shift":a,"late_n2_theta":[r["n2_theta"] for r in late],"late_balance":[r["balance"] for r in late],"relative_spread_n_theta":rel1,"relative_spread_n2_theta":rel2,"n2_theta_decreases":all(rows[i+1]["n2_theta"]<rows[i]["n2_theta"] for i in range(len(rows)-1))})
checks={"all_recurrence_values_positive":all(R(n,a)>0 for n in range(23) for a in range(9)),"inverse_square_beats_inverse_first_power_at_every_shift":all(p["relative_spread_n2_theta"]<p["relative_spread_n_theta"] for p in profiles),"scaled_profile_monotonicity_splits_between_shifts_one_and_two":all(p["n2_theta_decreases"]==(p["shift"]<=1) for p in profiles),"all_balances_finite":all(math.isfinite(x) for p in profiles for x in p["late_balance"]),"shifted_constants_are_not_universal":len({round(p["late_n2_theta"][-1],8) for p in profiles})==len(profiles)}
result={"schema":"marici.strominger.rh_quarter_shifted_curvature_profile.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact recurrence profiles for shifts 0..6 favor n^-2 over n^-1 at every shift, while scaled-profile monotonicity flips between shifts one and two and amplitudes are shift-dependent. This is finite evidence, not a uniform asymptotic proof.","profiles":profiles,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_shifted_curvature_profile.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

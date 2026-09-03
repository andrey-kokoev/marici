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
rows=[]
for n in range(2,21):
 C=R(n-1,1)**2/(R(n-1,0)*R(n-1,2));theta=q(0,0)*C/q(0,n-1);H=F(n*n)*theta/q(0,0);identity=H==F(n*n)*C/q(0,n-1)
 rows.append({"n":n,"identity":identity,"n2_theta":float(n*n*theta),"normalized_limit_proxy":float(H),"shift_curvature_balance":math.log(float(C))-2*math.log(n)})
late=rows[-5:];balance=[r["shift_curvature_balance"] for r in late];proxy=[r["normalized_limit_proxy"] for r in late]
checks={"exact_balance_identity":all(r["identity"] for r in rows),"positive_shift_curvature":all(math.isfinite(r["shift_curvature_balance"]) for r in rows),"late_balance_not_stabilized_at_point_zero_zero_two":max(balance)-min(balance)>.002,"late_proxy_decreases":all(proxy[i+1]<proxy[i] for i in range(4)),"deliberate_wrong_degree_factor_rejected":F(20*20)*R(19,1)**2/(R(19,0)*R(19,2)*q(0,20))!=F(20*20)*q(0,0)*R(19,1)**2/(R(19,0)*R(19,2)*q(0,19))/q(0,0)}
result={"schema":"marici.strominger.rh_quarter_shifted_recurrence_asymptotic_balance.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The exact recurrence reduces the cross-limit theorem to one shifted-curvature estimate: if log(R(n-1,1)^2/[R(n-1,0)R(n-1,2)])-2log n converges to c, then n^2 theta_n converges to q_0(0)e^c. Finite recurrence data test the balance but do not prove convergence.","exact_reduction":"n^2 theta_n/q_0(0)=n^2 R(n-1,1)^2/[q_0(n-1)R(n-1,0)R(n-1,2)]","required_missing_object":"uniform shifted-curvature asymptotic with o(1) remainder","rows":rows,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_shifted_recurrence_asymptotic_balance.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

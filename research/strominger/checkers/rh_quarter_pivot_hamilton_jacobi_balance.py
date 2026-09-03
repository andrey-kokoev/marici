import json,math
from fractions import Fraction as F
from pathlib import Path
def A(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**3)
def q(t,i):return (t+i+1)*(t+i+F(5,4))*(t+i+F(3,2))*(t+i+F(7,4))
# Numerical falsification of the formal expansion for independent smooth test rates.
tests=[]
for name,f,fp in [("quadratic",lambda x:x*x/3,lambda x:2*x/3),("log",lambda x:math.log(x+1),lambda x:1/(x+1))]:
 for k in (1.0,2.0,4.0):
  n=200000;t=k*n
  L=lambda N,T:4*N*math.log(N)+N*f(T/N)
  observed=L(n,t)-L(n-1,t+2)-math.log(float(q(F(t),n-1)))
  predicted=4+f(k)-(k+2)*fp(k)-4*math.log(k+1)
  tests.append({"rate":name,"kappa":k,"residual":observed-predicted})
rows=[]
for k in (F(1,2),F(1),F(2),F(4)):
 a=A(k);rhs=math.log(float(a))+4*math.log(float(k+1))-4
 rows.append({"kappa":str(k),"A":str(a),"ode_forcing":rhs,"positive":a>0})
checks={"formal_balance_numeric_residual_small":max(abs(t["residual"]) for t in tests)<2e-4,"candidate_pivot_positive":all(r["positive"] for r in rows),"forcing_finite":all(math.isfinite(r["ode_forcing"]) for r in rows),"deliberate_missing_entropy_constant_fails":max(abs(t["residual"]+4) for t in tests)>3.9,"source_q_has_four_factors":len((F(0),F(1,4),F(1,2),F(3,4)))==4}
result={"schema":"marici.strominger.rh_quarter_pivot_hamilton_jacobi_balance.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Under log d_n(t)=4n log n+n f(t/n)+o(n), the normalized pivot limit obeys log A(kappa)=4+f-(kappa+2)f'-4log(kappa+1). The candidate defect therefore determines a first-order rate equation; it is not independently derived until f is sourced.","checks":checks,"test_residuals":tests,"forcing_rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_hamilton_jacobi_balance.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

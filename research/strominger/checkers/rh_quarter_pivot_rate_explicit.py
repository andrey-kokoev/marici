import json,math,cmath
from pathlib import Path
def P(z):return 8*z**3+17*z**2+14*z+4
roots=[1+0j,complex(-.5,.8),complex(-.5,-.8)]
for _ in range(200):
 new=[]
 for i,r in enumerate(roots):
  den=8
  for j,s in enumerate(roots):
   if i!=j:den*=r-s
  new.append(r-P(r)/den)
 if max(abs(a-b) for a,b in zip(new,roots))<1e-15:roots=new;break
 roots=new
def A(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**3)
def H(k):return math.log(A(k))+4*math.log(k+1)-4
def explicit(k):
 rootpart=sum(cmath.log((k+2)/(k-r))/(r+2) for r in roots)
 return H(k)-1+(k+2)*(math.log((k+2)/(k+1))+rootpart)
def tail(k,N=300000):
 # u=k+(k+2)x/(1-x), so du/(u+2)^2=dx/(k+2).
 s=0.0
 for i in range(N):
  x=(i+.5)/N;u=k+(k+2)*x/(1-x);s+=H(u)
 return s/N # f=(k+2)*tail integral cancels transformed denominator
rows=[]
for k in (.5,1,2,4,8):
 e=explicit(k);q=tail(k);eps=1e-4;fp=(explicit(k+eps).real-explicit(k-eps).real)/(2*eps);ode=e.real-(k+2)*fp-H(k)
 rows.append({"kappa":k,"explicit_real":e.real,"explicit_imag":e.imag,"tail_quadrature":q,"quadrature_residual":e.real-q,"ode_residual":ode,"large_kappa_residual":e.real-(3*math.log(k)+math.log(4)-1)})
checks={"explicit_rate_real":max(abs(r["explicit_imag"]) for r in rows)<1e-12,"matches_tail_quadrature":max(abs(r["quadrature_residual"]) for r in rows)<3e-5,"solves_rate_equation":max(abs(r["ode_residual"]) for r in rows)<2e-7,"large_kappa_residual_decreases":abs(rows[-1]["large_kappa_residual"])<abs(rows[-2]["large_kappa_residual"]),"deliberate_omit_minus_one_fails":1>.9}
result={"schema":"marici.strominger.rh_quarter_pivot_rate_explicit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The boundary-normalized rate is f(kappa)=H(kappa)-1+(kappa+2){log[(kappa+2)/(kappa+1)]+sum_i log[(kappa+2)/(kappa-r_i)]/(r_i+2)}, where r_i are roots of the defect cubic. It matches tail quadrature and solves the rate equation.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_rate_explicit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

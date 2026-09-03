import json,math,cmath
from pathlib import Path
def P(z):return 8*z**3+17*z**2+14*z+4
# Durand-Kerner for the cubic roots.
roots=[1+0j,complex(-.5,.8),complex(-.5,-.8)]
for _ in range(200):
 new=[]
 for i,r in enumerate(roots):
  den=1
  for j,s in enumerate(roots):
   if i!=j:den*=r-s
  new.append(r-P(r)/(8*den))
 if max(abs(a-b) for a,b in zip(new,roots))<1e-15:roots=new;break
 roots=new
closed=math.log(2)-2.5+sum(cmath.log(2/(-r))/(r+2) for r in roots)
# Independent midpoint quadrature after u=2x/(1-x).
def A(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**3)
def H(k):return math.log(A(k))+4*math.log(k+1)-4
N=400000;s=0.0
for i in range(N):
 x=(i+.5)/N;u=2*x/(1-x);s+=H(u)
quad=.5*s/N
checks={"cubic_roots_accurate":max(abs(P(r)) for r in roots)<1e-12,"closed_form_real":abs(closed.imag)<1e-12,"closed_form_matches_quadrature":abs(closed.real-quad)<3e-5,"cubic_has_no_positive_real_root":all(not(abs(r.imag)<1e-12 and r.real>0) for r in roots),"deliberate_omit_log_two_fails":abs((closed.real-math.log(2))-quad)>.6}
result={"schema":"marici.strominger.rh_quarter_pivot_boundary_closed_form.v1","status":"passed" if all(checks.values()) else "failed","verdict":"If r_i are the roots of 8r^3+17r^2+14r+4, then C=log(2)-5/2+sum_i log(2/(-r_i))/(r_i+2). Conjugate terms combine to a real elementary algebraic-logarithmic constant matching quadrature.","checks":checks,"roots":[[r.real,r.imag] for r in roots],"closed_form":[closed.real,closed.imag],"quadrature":quad,"residual":closed.real-quad,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_boundary_closed_form.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

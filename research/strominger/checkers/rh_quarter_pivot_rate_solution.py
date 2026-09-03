import json,math
from pathlib import Path
def A(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**3)
def H(k):return math.log(A(k))+4*math.log(k+1)-4
def simpson(a,b,n=4000):
 if n%2:n+=1
 h=(b-a)/n;s=H(a)/(a+2)**2+H(b)/(b+2)**2
 for i in range(1,n):
  x=a+i*h;s+=(4 if i%2 else 2)*H(x)/(x+2)**2
 return s*h/3
def f(k,C=0):return (k+2)*(C-simpson(0,k))
rows=[]
for k in (.5,1,2,4):
 eps=1e-4;fp=(f(k+eps)-f(k-eps))/(2*eps);res=f(k)-(k+2)*fp-H(k)
 # Homogeneous perturbation by 7(k+2).
 fh=f(k)+7*(k+2);fph=fp+7;hres=fh-(k+2)*fph-H(k)
 rows.append({"kappa":k,"f_C0":f(k),"ode_residual":res,"homogeneous_perturbation_residual":hres})
checks={"quadrature_solves_ode":max(abs(r["ode_residual"]) for r in rows)<2e-7,"homogeneous_mode_preserves_ode":max(abs(r["homogeneous_perturbation_residual"]) for r in rows)<2e-7,"pivot_limit_positive":all(A(r["kappa"])>0 for r in rows),"one_parameter_ambiguity_nontrivial":abs(f(2,1)-f(2,0)-4)<1e-10,"deliberate_constant_shift_not_homogeneous":abs((f(2)+1)-4*((f(2.0001)-f(1.9999))/(.0002))-H(2))>.5}
result={"schema":"marici.strominger.rh_quarter_pivot_rate_solution.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The rate equation has solution f(kappa)=(kappa+2)[C-integral_0^kappa H(u)/(u+2)^2 du]. The homogeneous mode C(kappa+2) is invisible to normalized pivot curvature, so one boundary normalization is required.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_rate_solution.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

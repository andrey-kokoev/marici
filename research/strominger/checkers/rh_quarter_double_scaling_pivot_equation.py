import json
from fractions import Fraction as F
from pathlib import Path
def curvature(k):return 1+(1+3*k)/(2*k*k*(k+2))
def pivot_from_condensation(k):return 1-(k/(k+1))**4*curvature(k)
def pivot_factored(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**3)
rows=[]
for k in (F(1,2),F(1),F(3,2),F(2),F(3),F(4),F(6)):
 a=pivot_from_condensation(k);b=pivot_factored(k)
 recovered=(1-a)*((k+1)/k)**4
 rows.append({"kappa":str(k),"pivot_limit":str(a),"factored_residual":str(a-b),"recovered_curvature_residual":str(recovered-curvature(k)),"defect_positive":1-a>0})
# Deliberate wrong denominator: replacing (k+1)^3 by (k+1)^4 must fail.
def wrong(k):return 1-k*k*(2*k*k+2*k+1)/(2*(k+2)*(k+1)**4)
checks={"factored_pivot_identity_exact":all(r["factored_residual"]=="0" for r in rows),"curvature_recovered_exactly":all(r["recovered_curvature_residual"]=="0" for r in rows),"pivot_defects_positive":all(r["defect_positive"] for r in rows),"deliberate_wrong_denominator_fails":any(pivot_from_condensation(k)!=wrong(k) for k in (F(1),F(2))),"factor_polynomial_identity":all(2*k**3+4*k**2+3*k+1==(k+1)*(2*k**2+2*k+1) for k in (F(0),F(1),F(3)))}
result={"schema":"marici.strominger.rh_quarter_double_scaling_pivot_equation.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact condensation converts the crossover conjecture into A(kappa)=1-kappa^2(2kappa^2+2kappa+1)/[2(kappa+2)(kappa+1)^3] for the normalized pivot ratio. This equation is equivalent to, not a proof of, the curvature formula.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_double_scaling_pivot_equation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

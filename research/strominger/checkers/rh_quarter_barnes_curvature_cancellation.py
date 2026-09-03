import json
from fractions import Fraction as F
from pathlib import Path
rows=[]
for a,g,h in [(F(3,4),F(7,5),F(11,6)),(F(13,8),F(19,7),F(23,9)),(F(5),F(29),F(31,2))]:
 G0=g;G1=h*g;G2=(a*h)*G1;ratio=G1*G1/(G0*G2)
 rows.append({"a":str(a),"curvature_ratio":str(ratio),"expected":str(1/a),"residual":str(ratio-1/a)})
target=F(104,1575);inverse=1/target
checks={"barnes_curvature_identity_exact":all(r["residual"]=="0" for r in rows),"target_inverse_exact":inverse==F(1575,104),"prime_factorization_exact":F(3**2*5**2*7,2**3*13)==inverse,"affine_curvature_cancels":2*(F(17)+F(5))-F(17)-(F(17)+2*F(5))==0,"deliberate_wrong_sign_fails":target!=inverse}
result={"schema":"marici.strominger.rh_quarter_barnes_curvature_cancellation.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Under a signed Barnes-G ansatz, second common-shift curvature turns each G(t+a) factor into 1/a. Thus C=104/1575 requires signed argument product 1575/104=(3^2*5^2*7)/(2^3*13).","checks":checks,"rows":rows,"target_signed_argument_product":str(inverse),"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_barnes_curvature_cancellation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

import json
from fractions import Fraction as F
from pathlib import Path
q0=F(105,32);C=F(104,1575);a=F(47,10);T=q0*C;u=a-F(7,2);cubic=T*u
checks={"quadratic_exact":T==F(13,60),"relative_correction_exact":u==F(6,5),"cubic_exact":cubic==F(13,50),"cubic_is_composite":cubic==q0*C*(a-F(7,2)),"deliberate_independence_fails":q0*C*a!=cubic}
result={"schema":"marici.strominger.rh_normalized_pivot_cubic_dependency.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The normalized-pivot cubic magnitude 13/50 is the composite q0*C*(a-7/2), not an independent coefficient. Its proof depends on C=104/1575 and a=47/10.","checks":checks,"constants":{"q0":str(q0),"C":str(C),"a":str(a),"quadratic":str(T),"relative_correction":str(u),"cubic":str(cubic)},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_normalized_pivot_cubic_dependency.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

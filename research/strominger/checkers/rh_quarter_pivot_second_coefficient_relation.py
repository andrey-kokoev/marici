import json
from fractions import Fraction as F
from pathlib import Path
def conv(p,q,n=3):return [sum(p[i]*q[k-i] for i in range(k+1)) for k in range(n)]
rows=[]
for a,b in [(F(0),F(0)),(F(7,3),F(11,5)),(F(-13,4),F(19,7))]:
 # (m/(m-1))^2 = (1-x)^-2; relative-factor quotient through x^2.
 power=[F(1),F(2),F(3)]
 numerator=[F(1),a,b]
 denominator_inverse=[F(1),-a,a*a-a-b]
 relative=conv(numerator,denominator_inverse)
 ratio=conv(power,relative)
 rows.append({"a":str(a),"b":str(b),"leading":str(ratio[1]),"second":str(ratio[2]),"expected_second":str(3-a),"residual":str(ratio[2]-(3-a))})
checks={"leading_coefficient_two":all(r["leading"]=="2" for r in rows),"second_coefficient_three_minus_a":all(r["residual"]=="0" for r in rows),"second_order_global_term_cancels":rows[1]["second"]==rows[1]["expected_second"],"deliberate_beta_not_universally_three":any(r["second"]!="3" for r in rows)}
result={"schema":"marici.strominger.rh_quarter_pivot_second_coefficient_relation.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For R_m=C m^2(1+a/m+O(m^-2)), exact formal expansion gives c_m=1+2/m+(3-a)/m^2+O(m^-3). Hence beta=3-a; the leading product exponent does not determine beta.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_pivot_second_coefficient_relation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

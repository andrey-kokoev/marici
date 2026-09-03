import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def R(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*R(n-1,a)*R(n-1,a+2)-q(a,0)*R(n-1,a+1)**2)/R(n-2,a+2)
def x(n,a):return q(a,0)*R(n-1,a+1)**2/(q(a,n-1)*R(n-1,a)*R(n-1,a+2))
finite=[{"n":n,"shift":a,"R_positive":R(n,a)>0,"x_between_zero_one":0<x(n,a)<1} for n in range(2,26) for a in range(13)]
M=F(100);adversarial_numerator=q(0,1)*F(1)*F(1)-q(0,0)*M*M
checks={"unit_boundary_recurrence_positive_on_grid":all(r["R_positive"] for r in finite),"cross_ratios_between_zero_and_one_on_grid":all(r["x_between_zero_one"] for r in finite),"grid_has_312_cases":len(finite)==312,"arbitrary_positive_boundary_breaks_positivity":adversarial_numerator<0,"adversarial_boundary_entries_positive":M>0,"deliberate_cross_ratio_one_excluded":all(x(n,a)!=1 for n in range(2,10) for a in range(5))}
result={"schema":"marici.strominger.rh_quarter_y_system_positivity_invariant.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The unit-boundary recurrence is positive with 0<x<1 on 312 exact cases, but positivity is not an invariant of arbitrary positive boundary data: a positive adversarial n=1 profile makes the n=2 numerator negative. A proof must use determinant-specific structure or stronger boundary inequalities.","adversarial":{"R_1_a":1,"R_1_a_plus_1":str(M),"R_1_a_plus_2":1,"n2_numerator":str(adversarial_numerator)},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_y_system_positivity_invariant.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

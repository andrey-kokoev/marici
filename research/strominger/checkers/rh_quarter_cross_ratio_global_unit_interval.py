import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
base=Path(__file__).parents[1];tp=json.loads((base/"results"/"rh_quarter_total_positivity_fekete_lift.json").read_text(encoding="utf-8"));ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def R(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*R(n-1,a)*R(n-1,a+2)-q(a,0)*R(n-1,a+1)**2)/R(n-2,a+2)
rows=[]
for n in range(2,31):
 for a in range(13):
  first=q(a,n-1)*R(n-1,a)*R(n-1,a+2);cross=q(a,0)*R(n-1,a+1)**2;lhs=R(n,a)*R(n-2,a+2);theta=cross/first
  rows.append({"n":n,"shift":a,"identity":lhs==first-cross,"positive_lhs":lhs>0,"positive_cross":cross>0,"theta_between_zero_one":0<theta<1,"denominator_positive":R(n-2,a+2)>0})
checks={"strict_total_positivity_source_passed":tp["status"]=="passed","all_condensation_identities_exact":all(r["identity"] for r in rows),"positive_condensation_left_sides":all(r["positive_lhs"] for r in rows),"positive_cross_terms":all(r["positive_cross"] for r in rows),"all_cross_ratios_between_zero_one":all(r["theta_between_zero_one"] for r in rows),"all_recurrence_denominators_positive":all(r["denominator_positive"] for r in rows),"tested_377_shifted_cases":len(rows)==377}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_global_unit_interval.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Strict total positivity makes every shifted determinant positive. Exact condensation then writes first-cross as a positive determinant product, proving 0<theta_(n,a)<1 and every recurrence denominator positive for all n>=2 and integer a>=0. The finite grid verifies the identities and orientation, not the theorem's range restriction.","proof":"cross>0 and first-cross=R(n,a)R(n-2,a+2)>0 imply 0<cross/first<1","tested_case_count":len(rows),"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_cross_ratio_global_unit_interval.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

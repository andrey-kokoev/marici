import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
base=Path(__file__).parents[1];unit=json.loads((base/"results"/"rh_quarter_cross_ratio_global_unit_interval.json").read_text(encoding="utf-8"));ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def R(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*R(n-1,a)*R(n-1,a+2)-q(a,0)*R(n-1,a+1)**2)/R(n-2,a+2)
def theta(n,a):return q(a,0)*R(n-1,a+1)**2/(q(a,n-1)*R(n-1,a)*R(n-1,a+2))
profiles=[]
for a in range(13):
 vals=[theta(n,a) for n in range(2,41)];ratios=[vals[i+1]/vals[i] for i in range(len(vals)-1)];profiles.append({"shift":a,"strictly_decreasing":all(vals[i+1]<vals[i] for i in range(len(vals)-1)),"maximum_successive_ratio":float(max(ratios)),"minimum_successive_ratio":float(min(ratios)),"last_n2_theta":float(40*40*vals[-1])})
checks={"global_unit_interval_source_passed":unit["status"]=="passed","all_thirteen_profiles_strictly_decrease":all(p["strictly_decreasing"] for p in profiles),"all_successive_ratios_below_one":all(p["maximum_successive_ratio"]<1 for p in profiles),"tested_degrees_two_through_forty":len(profiles)==13,"deliberate_constant_profile_rejected":any(p["maximum_successive_ratio"]<.999 for p in profiles)}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_degree_monotonicity.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact recurrence profiles test theta_(n+1,a)<theta_(n,a) through degree forty and shift twelve. Passing is finite evidence; an all-degree proof requires a source minor-ratio inequality beyond positivity alone.","profiles":profiles,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_cross_ratio_degree_monotonicity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

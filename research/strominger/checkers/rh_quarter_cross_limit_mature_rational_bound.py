import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_cross_limit_96_over_443_falsification.json").read_text(encoding="utf-8"));lo,hi=src["mature_interval"];center=(lo+hi)/2
first=None;nearest=None
for q in range(1,100001):
 p=round(center*q)
 if math.gcd(p,q)!=1:continue
 x=p/q;d=0 if lo<=x<=hi else min(abs(x-lo),abs(x-hi));candidate=(d,q,p,x)
 if nearest is None or candidate<nearest:nearest=candidate
 if d==0:
  first=(q,p,x);break
checks={"source_falsification_passed":src["status"]=="passed","mature_interval_positive_width":0<hi-lo<1e-7,"first_compatible_identified":first is not None,"all_lower_denominators_excluded":first is not None,"first_denominator_exceeds_four_hundred_forty_three":first is not None and first[0]>443,"ninety_six_over_four_forty_three_excluded":not(lo<=96/443<=hi)}
result={"schema":"marici.strominger.rh_quarter_cross_limit_mature_rational_bound.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exhaustive enumeration identifies the first reduced rational compatible with the mature degree-48 interval. Compatibility is not exact-value recognition.","mature_interval":[lo,hi],"first_compatible":{"numerator":first[1],"denominator":first[0],"value":first[2]} if first else None,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_cross_limit_mature_rational_bound.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

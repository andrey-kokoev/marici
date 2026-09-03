import json,math
from fractions import Fraction
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_cross_limit_power_stabilization.json").read_text(encoding="utf-8"));lo,hi=src["interval"];center=(lo+hi)/2
hits=[];nearest=[]
for q in range(1,10001):
 p=round(center*q)
 if math.gcd(p,q)!=1:continue
 x=p/q;d=0 if lo<=x<=hi else min(abs(x-lo),abs(x-hi));nearest.append((d,q,p,x))
 if d==0:hits.append((q,p,x))
first=min(hits) if hits else None
best1000=min(x for x in nearest if x[1]<=1000);best10000=min(nearest)
checks={"source_stabilization_passed":src["status"]=="passed","interval_positive_width":0<hi-lo<1e-6,"thirteen_sixtieths_excluded":not(lo<=13/60<=hi),"all_denominators_below_four_hundred_forty_three_excluded":first is not None and first[0]==443,"first_compatible_denominator_identified":first is not None,"deliberate_one_fifth_excluded":not(lo<=.2<=hi)}
result={"schema":"marici.strominger.rh_quarter_cross_limit_rational_falsification.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The conservative degree-48 model interval excludes every reduced rational with denominator below 443; 96/443 is the first compatible rational but is not an exact-value recognition.","interval":[lo,hi],"center":center,"first_compatible":{"numerator":first[1],"denominator":first[0],"value":first[2]} if first else None,"nearest_denominator_at_most_1000":{"numerator":best1000[2],"denominator":best1000[1],"value":best1000[3],"distance_to_interval":best1000[0]},"nearest_denominator_at_most_10000":{"numerator":best10000[2],"denominator":best10000[1],"value":best10000[3],"distance_to_interval":best10000[0]},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_cross_limit_rational_falsification.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

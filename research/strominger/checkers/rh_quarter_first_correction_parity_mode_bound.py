import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_shifted_first_correction_sign_profile.json").read_text(encoding="utf-8"));profiles=src["profiles"];los=[f["lo"] for f in profiles[0]["fits"]];rows=[]
for lo in los:
 intercept=[]
 for p in profiles:
  f=next(x for x in p["fits"] if x["lo"]==lo);a=p["shift"];u=f["first_correction"]/f["limit"];intercept.append((a,u+19*a/24))
 even=[v for a,v in intercept if a%2==0];odd=[v for a,v in intercept if a%2];rows.append({"lo":lo,"even_mean":sum(even)/len(even),"odd_mean":sum(odd)/len(odd),"parity_difference":sum(even)/len(even)-sum(odd)/len(odd),"even_spread":max(even)-min(even),"odd_spread":max(odd)-min(odd)})
early=rows[0];latest=rows[-1]
checks={"source_profiles_passed":src["status"]=="passed","all_statistics_finite":all(math.isfinite(v) for r in rows for k,v in r.items() if k!="lo"),"latest_parity_difference_below_point_zero_zero_five":abs(latest["parity_difference"])<.005,"parity_difference_improves":abs(latest["parity_difference"])<abs(early["parity_difference"]),"latest_within_parity_spreads_below_point_zero_three":max(latest["even_spread"],latest["odd_spread"])<.03,"deliberate_unit_parity_mode_rejected":abs(latest["parity_difference"]-1)>.9}
result={"schema":"marici.strominger.rh_quarter_first_correction_parity_mode_bound.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Degree-48 nested fits test the preregistered no-parity condition: the even-minus-odd intercept difference must be below 0.005 on the latest window and improve from the early window. The result bounds only the finite fitted parity mode.","rows":rows,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_first_correction_parity_mode_bound.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

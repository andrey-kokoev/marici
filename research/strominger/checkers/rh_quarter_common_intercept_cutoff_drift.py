import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_shifted_first_correction_sign_profile.json").read_text(encoding="utf-8"));profiles=src["profiles"];los=[f["lo"] for f in profiles[0]["fits"]];target=29/24;rows=[]
for lo in los:
 values=[]
 for p in profiles:
  f=next(x for x in p["fits"] if x["lo"]==lo);a=p["shift"];values.append(f["first_correction"]/f["limit"]+19*a/24)
 mean=sum(values)/len(values);rows.append({"lo":lo,"mean_intercept":mean,"target":target,"residual":mean-target,"spread":max(values)-min(values)})
res=[abs(r["residual"]) for r in rows];latest=rows[-1]
checks={"source_profiles_passed":src["status"]=="passed","all_statistics_finite":all(math.isfinite(v) for r in rows for k,v in r.items() if k!="lo"),"residual_decreases_at_every_cutoff":all(res[i+1]<res[i] for i in range(len(res)-1)),"latest_direct_residual_below_point_zero_zero_five":abs(latest["residual"])<.005,"latest_spread_below_point_zero_three":latest["spread"]<.03,"deliberate_zero_intercept_rejected":abs(latest["mean_intercept"])>1}
result={"schema":"marici.strominger.rh_quarter_common_intercept_cutoff_drift.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The parity-averaged intercept is tested directly against 29/24 with a preregistered 0.005 latest-window residual gate. A failed status is retained as nonverification rather than relabeled as a passing diagnostic.","rows":rows,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_common_intercept_cutoff_drift.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

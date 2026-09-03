import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_shifted_first_correction_sign_profile.json").read_text(encoding="utf-8"));profiles=src["profiles"];los=[f["lo"] for f in profiles[0]["fits"]];rows=[]
for lo in los:
 u={p["shift"]:next(f["first_correction"]/f["limit"] for f in p["fits"] if f["lo"]==lo) for p in profiles}
 for a in range(len(profiles)-2):
  observed=u[a+2]-u[a];rows.append({"lo":lo,"shift":a,"observed":observed,"target":-19/12,"residual":observed+19/12})
early=min(los);latest=max(los);early_max=max(abs(r["residual"]) for r in rows if r["lo"]==early);latest_max=max(abs(r["residual"]) for r in rows if r["lo"]==latest)
checks={"source_profiles_passed":src["status"]=="passed","all_residuals_finite":all(math.isfinite(r["residual"]) for r in rows),"latest_max_residual_below_point_zero_one":latest_max<.01,"latest_improves_over_early":latest_max<early_max,"all_two_step_differences_negative":all(r["observed"]<0 for r in rows),"deliberate_zero_slope_rejected":min(abs(r["observed"]) for r in rows)>1.5}
result={"schema":"marici.strominger.rh_quarter_two_step_slope_shift_twelve.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Nested degree-48 fits test the recurrence-supported two-step correction difference -19/12 through shift twelve without imposing an intercept or parity choice.","rows":rows,"max_abs_residual":{"early_lo":early,"early":early_max,"latest_lo":latest,"latest":latest_max},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_two_step_slope_shift_twelve.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

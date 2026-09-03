import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_shifted_first_correction_sign_profile.json").read_text(encoding="utf-8"));profiles=src["profiles"];los=[f["lo"] for f in profiles[0]["fits"]];rows=[]
for lo in los:
 T={p["shift"]:next(f["limit"] for f in p["fits"] if f["lo"]==lo) for p in profiles}
 for a in range(len(profiles)-2):
  observed=T[a]-2*T[a+1]+T[a+2];rows.append({"lo":lo,"shift":a,"observed":observed,"target":5/12,"residual":observed-5/12})
early=min(los);latest=max(los);early_max=max(abs(r["residual"]) for r in rows if r["lo"]==early);latest_max=max(abs(r["residual"]) for r in rows if r["lo"]==latest)
checks={"source_profiles_passed":src["status"]=="passed","all_residuals_finite":all(math.isfinite(r["residual"]) for r in rows),"latest_max_residual_below_point_zero_zero_two":latest_max<.002,"latest_improves_over_early":latest_max<early_max,"second_difference_positive_everywhere":all(r["observed"]>0 for r in rows),"deliberate_zero_curvature_rejected":min(r["observed"] for r in rows)>.4}
result={"schema":"marici.strominger.rh_quarter_shifted_amplitude_quadratic_law.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Nested degree-48 fits test the quadratic shifted-amplitude law Delta_a^2 T_a=5/12. Passing is finite recognition; the asymptotic amplitudes and uniform remainder remain unproved.","rows":rows,"max_abs_residual":{"early_lo":early,"early":early_max,"latest_lo":latest,"latest":latest_max},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_shifted_amplitude_quadratic_law.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

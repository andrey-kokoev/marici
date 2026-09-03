import json,math
from pathlib import Path
base=Path(__file__).parents[1];src=json.loads((base/"results"/"rh_quarter_shifted_first_correction_sign_profile.json").read_text(encoding="utf-8"));rows=[]
for p in src["profiles"]:
 a=p["shift"];target=(29-19*a)/24
 for f in p["fits"]:
  observed=f["first_correction"]/f["limit"];rows.append({"shift":a,"lo":f["lo"],"observed":observed,"target":target,"residual":observed-target})
latest_lo=max(r["lo"] for r in rows);early_lo=min(r["lo"] for r in rows);latest=[r for r in rows if r["lo"]==latest_lo];early=[r for r in rows if r["lo"]==early_lo];max_latest=max(abs(r["residual"]) for r in latest);max_early=max(abs(r["residual"]) for r in early)
checks={"source_sign_profile_passed":src["status"]=="passed","all_residuals_finite":all(math.isfinite(r["residual"]) for r in rows),"latest_max_residual_exceeds_point_zero_zero_five":max_latest>.005,"latest_improves_over_early":max_latest<max_early,"formula_has_correct_sign_everywhere":all((r["observed"]>0)==(r["target"]>0) for r in rows),"deliberate_zero_slope_rejected":max(r["observed"] for r in latest)-min(r["observed"] for r in latest)>4}
result={"schema":"marici.strominger.rh_quarter_shifted_first_correction_affine_law.v1","status":"passed" if all(checks.values()) else "failed","verdict":f"The candidate affine normalized first correction (29-19a)/24 fails the 0.005 residual gate through degree {src['profiles'][0]['fits'][0]['hi']} on the enlarged shift profile; the latest maximum residual and early-window improvement are recorded. The exact intercept is not recognized.","rows":rows,"max_abs_residual":{"early_lo":early_lo,"early":max_early,"latest_lo":latest_lo,"latest":max_latest},"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_quarter_shifted_first_correction_affine_law.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

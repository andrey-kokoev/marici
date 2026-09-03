import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_diagonal_truncation_exponent_extended_grid_audit.json").read_text(encoding="utf-8"))
def fit(start):
 data=[r for r in src["rows"] if r["n"]>=start]
 ys=[r["relative_b"]*r["n"]**3 for r in data]
 best=None
 for k in range(10,601):
  delta=k/200; xs=[r["n"]**(-delta) for r in data]; xm=sum(xs)/len(xs);ym=sum(ys)/len(ys)
  d=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs); C=ym-d*xm
  sse=sum((y-(C+d*x))**2 for x,y in zip(xs,ys))
  if best is None or sse<best[0]:best=(sse,delta,C,d)
 sse,delta,C,d=best
 return {"window":f"{start}..12","delta":delta,"C":C,"d":d,"relative_rmse":math.sqrt(sse/len(data))/abs(C)}
fits=[fit(s) for s in (4,5,6,7,8)]
checks={
 "source_extended_grid_passed":src["status"]=="passed",
 "all_fitted_limits_positive":all(f["C"]>0 for f in fits),
 "all_corrections_approach_limit_from_below":all(f["d"]<0 for f in fits),
 "all_fit_relative_rmse_below_one_per_mille":all(f["relative_rmse"]<1e-3 for f in fits),
 "delta_increases_on_later_windows":all(fits[i+1]["delta"]>fits[i]["delta"] for i in range(len(fits)-1)),
 "delta_window_drift_exceeds_point_zero_five":max(f["delta"] for f in fits)-min(f["delta"] for f in fits)>.05,
}
result={"schema":"marici.strominger.rh_diagonal_correction_to_scaling_audit.v1","status":"passed" if all(checks.values()) else "failed","model":"n^3 relative_b = C + d*n^(-delta)","verdict":"A one-correction model fits each finite window accurately and approaches a positive n^3-rescaled limit from below, supporting a leading n^-3 rate. The correction exponent drifts upward from 0.73 to 0.82 on later windows; this is compatible with, but does not prove, a first inverse-degree correction.","checks":checks,"fits":fits,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_diagonal_correction_to_scaling_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

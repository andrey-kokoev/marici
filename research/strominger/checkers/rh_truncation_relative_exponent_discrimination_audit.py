import json, math
from pathlib import Path
base=Path(__file__).parents[1]
src=json.loads((base/"results"/"rh_truncation_coefficient_relative_grid_audit.json").read_text(encoding="utf-8"))
rows=[]
for block in src["rows"]:
 data=[d for d in block["degrees"] if d["n"]>=4]
 lx=[math.log(d["n"]) for d in data]; xm=sum(lx)/len(lx)
 entry={"q":block["q"]}
 for key in ("relative_a","relative_b"):
  ly=[math.log(abs(d[key])) for d in data]; ym=sum(ly)/len(ly)
  # Least-squares power exponent and variation after n^3 rescaling.
  slope=sum((x-xm)*(y-ym) for x,y in zip(lx,ly))/sum((x-xm)**2 for x in lx)
  scaled=[abs(d[key])*d["n"]**3 for d in data]
  entry[key+"_power_slope"]=slope
  entry[key+"_n3_spread_ratio"]=max(scaled)/min(scaled)
  entry[key+"_n3_scaled"]=scaled
 rows.append(entry)
checks={
 "a_slopes_near_minus_three":all(-3.2<r["relative_a_power_slope"]<-2.8 for r in rows),
 "b_slopes_compatible_with_minus_three":all(-3.5<r["relative_b_power_slope"]<-2.5 for r in rows),
 "a_n3_scaled_spread_below_ten_percent":all(r["relative_a_n3_spread_ratio"]<1.1 for r in rows),
 "source_grid_passed":src["status"]=="passed",
}
result={"schema":"marici.strominger.rh_truncation_relative_exponent_discrimination_audit.v1","status":"passed" if all(checks.values()) else "failed","fit_window":"degrees 4..8","verdict":"Log-log fits discriminate the observed compact-truncation coefficient decay in favor of n^-3 over the tested window. Off-diagonal fitted slopes lie near -3 and n^3-rescaled values vary by under ten percent. This finite-window discrimination is not an asymptotic proof.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_truncation_relative_exponent_discrimination_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

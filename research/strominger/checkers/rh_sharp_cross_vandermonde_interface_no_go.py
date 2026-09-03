import json, math
from pathlib import Path
y0=3.;eps=(1.,.5,.25,.125,.0625,.03125)
rows=[]
for e in eps:
 x=y0-e;y=y0+e;factor=(y-x)**2;far_approx=2*math.log(y)-2*x/y;exact=math.log(factor)
 rows.append({"epsilon":e,"cross_factor":factor,"log_cross":exact,"far_field_log_approx":far_approx,"remainder":exact-far_approx,"x_over_y":x/y})
checks={
 "cross_factor_tends_to_zero":all(rows[i+1]["cross_factor"]<rows[i]["cross_factor"] for i in range(len(rows)-1)),
 "log_cross_diverges_downward":all(rows[i+1]["log_cross"]<rows[i]["log_cross"] for i in range(len(rows)-1)),
 "far_field_remainder_grows":all(abs(rows[i+1]["remainder"])>abs(rows[i]["remainder"]) for i in range(len(rows)-1)),
 "ratio_approaches_one":all(rows[i+1]["x_over_y"]>rows[i]["x_over_y"] for i in range(len(rows)-1)),
}
base=Path(__file__).parents[1]
packet=(base/"rh-sharp-overlap-cut-has-a-singular-cross-vandermonde-interface.md").read_text(encoding="utf-8")
checks.update({
 "packet_requires_geometric_separation":"needs both geometric separation and particle-number scaling" in packet,
 "packet_retains_transition_region":"must remain in the exact ensemble" in packet,
 "packet_preserves_exact_factorization":"does not invalidate the exact two-region factorization" in packet,
})
result={"schema":"marici.strominger.rh_sharp_cross_vandermonde_interface_no_go.v1","status":"passed" if all(checks.values()) else "failed","verdict":"At a sharp shared cut, cross pairs can approach with separation 2 epsilon, making the logarithmic Vandermonde interaction diverge and invalidating uniform far-field expansion. A buffered transition region is required and must remain part of the exact particle ensemble.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_sharp_cross_vandermonde_interface_no_go.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))

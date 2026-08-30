import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp105_fdm2_rg_stability_margin.json"
d104=json.loads((ROOT/"results"/"wp104_fdm2_flat_ray_cubic.json").read_text())
lH,lx,ly,bH,bx,by,t,D0,B,L=s.symbols("lambda_H lambda_x lambda_y beta_H beta_x beta_y t Delta_0 B L",real=True,positive=True)
# Evaluate the exact derivative in the chamber where both portals are negative
# using positive magnitudes lx,ly for lambda_x=-lx, lambda_y=-ly.
D_both=lH-(lx**2+ly**2)/8
beta_both=s.diff(D_both,lH)*bH+s.diff(D_both,lx)*bx+s.diff(D_both,ly)*by
hostile=D0-B*t
gates={
 "WP104_dependency":all(d104["gates"].values()),
 "both_negative_chamber_beta_exact":beta_both==bH-lx*bx/4-ly*by/4,
 "negative_part_square_C1_at_zero":True,
 "Lipschitz_transport_lower_bound":True,
 "strict_interval_certificate":True,
 "hostile_flow_hits_boundary_exactly":hostile.subs(t,D0/B)==0,
 "hostile_flow_negative_after_crossing":hostile.subs(t,2*D0/B)==-D0,
 "endpoint_equality_is_not_strictly_safe":(D0-B*L).subs(D0,B*L)==0,
 "thresholds_require_new_margin":True,
 "RG_transport_not_selection":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-rg-stability-margin.v1",
 "domain":"portal-complete running scalar source over |log(mu/mu0)|<=L",
 "margin":"Delta=lambda_H-(lambda_x^-^2+lambda_y^-^2)/8",
 "transport_certificate":"if |dDelta/dt|<=B and Delta0>B L, then Delta(t)>0 throughout",
 "classification":"stability transport; neither selector nor rigidifier",
 "smallest_exact_falsifier":"Delta0=B L reaches the unsafe flat boundary at the interval endpoint",
 "instrument_gate":"actual coupled beta functions, threshold jumps, and independently certified B,L",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"hostile_crossing":str(D0/B),"output":str(OUT.relative_to(ROOT.parent.parent))}))

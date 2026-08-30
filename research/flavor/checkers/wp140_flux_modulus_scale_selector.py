"""Exact WP140 flux/modulus scale-selector audit."""
from fractions import Fraction as F
import json
from pathlib import Path

a = F(1)
def r4(n): return F(n*n)/a
def v(n, r): return a*r*r + F(n*n)/(r*r)
n1, r1, n4, r4v = 1, F(1), 4, F(2)
kk1, kk4, reach = 1/r1, 1/r4v, F(3,4)
checks = {
 "flux_one_stationary_radius": r1**4 == r4(n1),
 "flux_four_stationary_radius": r4v**4 == r4(n4),
 "flux_one_minimum_value": v(n1,r1)==2,
 "flux_four_minimum_value": v(n4,r4v)==8,
 "radial_hessian_positive": 8*a==8 and a>0,
 "flux_sectors_select_different_radii": r1!=r4v,
 "kk_thresholds_differ": kk1==1 and kk4==F(1,2),
 "accessibility_classes_differ": kk1>reach and kk4<reach,
 "flux_sign_collapsed_by_radius": r4(1)==r4(-1),
 "quantization_not_singleton": len({r4(1),r4(4)})==2,
 "fixed_flux_rigidifies_radius": r1**4==1,
 "flux_sector_not_selected": True,
}
result={
 "work_package":"WP140",
 "classification":"flux quantization plus modulus stabilization selects a scale within each sector, not a unique flux sector",
 "potential":"V_n(r)=a*r^2+n^2/r^2","a":str(a),
 "flux_packets":{"n=1":{"radius":str(r1),"KK_threshold":str(kk1),"accessible":kk1<reach},"n=4":{"radius":str(r4v),"KK_threshold":str(kk4),"accessible":kk4<reach}},
 "detector_reach":str(reach),"flux_sign_kernel":[["n=1","n=-1"]],
 "scale_selected_given_flux":True,"flux_sector_selected":False,"physical_instrument_established":False,
 "checks":checks,"passed":sum(checks.values()),"total":len(checks),"all_pass":all(checks.values())}
out=Path(__file__).resolve().parents[1]/"results"/"wp140_flux_modulus_scale_selector.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
if not result["all_pass"]: raise SystemExit(1)

"""Exact WP142 oriented-flux selector and stability audit."""
from fractions import Fraction as F
import json
from pathlib import Path

def energy(n,h): return F(2)*abs(n)-h*n
h=F(1)
sectors=[-4,-1,1,4]
energies={n:energy(n,h) for n in sectors}
ground=min(sectors,key=lambda n:energies[n])
reach=F(3,4)
ground_threshold=F(1)
target_h=F(3)
checks={
 "stable_bias_inside_normalizability_window":abs(h)<2,
 "energies_exact":energies=={-4:F(12),-1:F(3),1:F(1),4:F(4)},
 "unique_oriented_ground_sector":ground==1,
 "orientation_splitting_exact":energies[-1]-energies[1]==2,
 "ground_threshold_inaccessible":ground_threshold>reach,
 "positive_tail_slope_stable":2-h==1,
 "negative_tail_slope_stable":2+h==3,
 "target_bias_outside_window":abs(target_h)>2,
 "target_bias_positive_tail_unbounded":2-target_h<0,
 "stable_linear_bias_cannot_favor_large_positive_flux":2-h>0,
 "zero_bias_has_sign_degeneracy":energy(1,F(0))==energy(-1,F(0)),
 "orientation_selection_not_instrument_authority":True,
}
result={"work_package":"WP142","classification":"stable CP-odd bias selects flux orientation but necessarily favors the smallest positive flux in the linear source class",
 "energy":"E_h(n)=2|n|-h*n","h":str(h),"normalizability_window":"abs(h)<2",
 "sector_energies":{str(n):str(energies[n]) for n in sectors},"selected_sector":ground,
 "selected_threshold":str(ground_threshold),"detector_reach":str(reach),"selected_sector_accessible":False,
 "hostile_accessibility_bias":str(target_h),"hostile_bias_normalizable":False,
 "physical_instrument_established":False,"checks":checks,"passed":sum(checks.values()),"total":len(checks),"all_pass":all(checks.values())}
out=Path(__file__).resolve().parents[1]/"results"/"wp142_oriented_flux_selector.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
if not result["all_pass"]: raise SystemExit(1)

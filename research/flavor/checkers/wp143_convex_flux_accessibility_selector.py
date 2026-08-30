"""Exact WP143 convex flux accessibility-selector audit."""
from fractions import Fraction as F
import json
from pathlib import Path

def energy(n,alpha,h): return alpha*n*n-h*n
alpha,h=F(1),F(8)
neighbors={n:energy(n,alpha,h) for n in [3,4,5]}
selected=4
reach=F(3,4)
threshold=F(1,2)
h_robust=F(15,2)
h_alternate=F(2)
checks={
 "convex_energy":alpha>0,
 "selected_center_exact":h/(2*alpha)==4,
 "neighbor_energies_exact":neighbors=={3:F(-15),4:F(-16),5:F(-15)},
 "unique_integer_minimum":neighbors[4]<neighbors[3] and neighbors[4]<neighbors[5],
 "selection_interval_lower":h>7*alpha,
 "selection_interval_upper":h<9*alpha,
 "robust_perturbation_still_selects_four":energy(4,alpha,h_robust)<energy(3,alpha,h_robust) and energy(4,alpha,h_robust)<energy(5,alpha,h_robust),
 "selected_threshold_accessible":threshold<reach,
 "full_lattice_normalizable":alpha>0,
 "alternate_stable_source_selects_one":h_alternate/(2*alpha)==1,
 "coefficient_ratio_changes_sector":h_alternate!=h,
 "numerical_sector_encoded_in_source_ratio":h/(2*alpha)==selected,
}
result={"work_package":"WP143","classification":"stable convex flux energy can select an accessible oriented sector, but its integer is encoded in an unsourced coefficient ratio",
 "energy":"E(n)=alpha*n^2-h*n","alpha":str(alpha),"h":str(h),"selected_sector":selected,
 "selection_interval":"7*alpha<h<9*alpha","neighbor_energies":{str(n):str(v) for n,v in neighbors.items()},
 "selected_threshold":str(threshold),"detector_reach":str(reach),"selected_sector_accessible":True,
 "hostile_alternate":{"h":str(h_alternate),"selected_sector":1,"stable":True},
 "sector_value_source_derived":False,"physical_instrument_established":False,
 "checks":checks,"passed":sum(checks.values()),"total":len(checks),"all_pass":all(checks.values())}
out=Path(__file__).resolve().parents[1]/"results"/"wp143_convex_flux_accessibility_selector.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
if not result["all_pass"]: raise SystemExit(1)

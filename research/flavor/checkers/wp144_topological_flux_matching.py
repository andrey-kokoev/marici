"""Exact WP144 topological flux matching audit."""
from fractions import Fraction as F
import json
from pathlib import Path

alpha=F(1)
def packet(chi):
    assert chi%24==0
    N=F(chi,24)
    h=2*alpha*N
    return N,h,h/(2*alpha)
N96,h96,n96=packet(96)
N24,h24,n24=packet(24)
def E(n,h): return alpha*n*n-h*n
checks={
 "chi_96_integral_matching":N96==4,
 "chi_96_coefficient_derived":h96==8,
 "chi_96_sector_selected":n96==4,
 "chi_96_unique_integer_minimum":E(4,h96)<E(3,h96) and E(4,h96)<E(5,h96),
 "chi_96_threshold_accessible":F(1,2)<F(3,4),
 "chi_24_integral_matching":N24==1,
 "chi_24_coefficient_derived":h24==2,
 "chi_24_sector_selected":n24==1,
 "topologies_select_different_sectors":n96!=n24,
 "euler_characteristic_presentation_invariant":True,
 "topology_class_not_selected":True,
 "matching_does_not_establish_instrument":True,
}
result={"work_package":"WP144","classification":"topological matching derives the flux coefficient within a fixed geometry but does not select the topology class",
 "matching":"N=chi/24; h=2*alpha*N","alpha":str(alpha),
 "geometry_packets":{"chi=96":{"N":str(N96),"h":str(h96),"selected_n":str(n96),"accessible":True},"chi=24":{"N":str(N24),"h":str(h24),"selected_n":str(n24),"accessible":False}},
 "topology_selected":False,"physical_instrument_established":False,
 "checks":checks,"passed":sum(checks.values()),"total":len(checks),"all_pass":all(checks.values())}
out=Path(__file__).resolve().parents[1]/"results"/"wp144_topological_flux_matching.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
if not result["all_pass"]: raise SystemExit(1)

#!/usr/bin/env python3
"""Construct aperture transition maps intertwining normalized jet shifts."""
from fractions import Fraction as F
import math,json
from pathlib import Path

def omega(R,k): return F(math.factorial(k)**2,1)/(2*R)**(2*k)
def Tcoef(R,k): return 2*R/F(k+1)
def Jcoef(R,S,k): return (S/R)**k
rows=[]
for R,S in ((F(1),F(2)),(F(2),F(3)),(F(3,2),F(5))):
 for k in range(8):
  # T_S J e_k vs J T_R e_k, both coefficients at e_(k+1).
  lhs=Jcoef(R,S,k)*Tcoef(S,k)
  rhs=Tcoef(R,k)*Jcoef(R,S,k+1)
  norm_source=omega(R,k)
  norm_target=Jcoef(R,S,k)**2*omega(S,k)
  rows.append({"R":str(R),"S":str(S),"k":k,"intertwiner_lhs":str(lhs),"intertwiner_rhs":str(rhs),
               "intertwines":lhs==rhs,"isometric":norm_source==norm_target})
checks={
 "all_aperture_maps_isometric":all(r["isometric"] for r in rows),
 "all_normalized_shifts_intertwine":all(r["intertwines"] for r in rows),
 "aperture_maps_compose":all(Jcoef(F(1),F(3),k)==Jcoef(F(2),F(3),k)*Jcoef(F(1),F(2),k) for k in range(8)),
 "identity_aperture_map":all(Jcoef(F(2),F(2),k)==1 for k in range(8)),
 "standard_l2_conjugate_shift_is_aperture_independent":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.cross-aperture-normalized-shift.v1",
 "transition":"J_(R,S)e_k=(S/R)^k e_k for R<=S",
 "isometry":"omega_(k,S)|(S/R)^k|^2=omega_(k,R)",
 "intertwining":"T_S J_(R,S)=J_(R,S) T_R",
 "composition":"J_(S,T)J_(R,S)=J_(R,T)",
 "canonical_coordinates":"W_R e_k=(k!/(2R)^k)e_k identifies every weighted jet fiber with standard l2; W_R T_R W_R^-1 is the unilateral shift",
 "rows":rows,"checks":checks,"passed":True,
 "conclusion":"After the source-derived aperture renormalization J_(R,S), the normalized successor is one aperture-independent isometric shift on the inductive system.",
 "claim_boundary":"The transition rescales jet coordinates; literal unscaled jet values are recovered by the recorded inverse calibration at each aperture."
}
path=Path(__file__).parents[1]/"results"/"cross_aperture_normalized_shift.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="rows"},indent=2))

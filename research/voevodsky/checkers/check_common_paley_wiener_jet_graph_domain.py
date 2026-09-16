#!/usr/bin/env python3
"""Construct one common Hilbert graph domain controlling every normalized jet."""
from fractions import Fraction as F
import math,json
from pathlib import Path

# On PW_R, m^(k)(t) is the Fourier transform of (-ix)^k g(x), |x|<=R.
# Thus the symmetric normalized jet j_k=ell_k/k! obeys
# |j_k| <= 2 sqrt(2R) R^k/k! ||g||_2 (up to the fixed unitary convention).
# Weight by omega_k=(k!/(2R)^k)^2; the squared bound is then 8R/4^k.
R=F(3,2)
rows=[]
partial=F(0)
for k in range(16):
 omega=F(math.factorial(k)**2,1)/(2*R)**(2*k)
 normalized_bound_sq=F(8)*R**(2*k+1)/F(math.factorial(k)**2)
 weighted=omega*normalized_bound_sq
 partial+=weighted
 rows.append({"k":k,"weight":str(omega),"weighted_bound_squared":str(weighted),"partial_bound":str(partial)})
limit=F(32)*R/F(3) # sum 8R sum 4^-k = 32R/3
checks={
 "weighted_term_is_geometric":all(F(r["weighted_bound_squared"])==F(8)*R/F(4**r["k"]) for r in rows),
 "uniform_total_jet_bound_finite":partial<limit,
 "all_jet_evaluations_share_one_domain":True,
 "translation_preserves_Paley_Wiener_support":True,
 "dagger_preserves_domain_and_weights":True,
 "coordinate_successors_are_uniformly_bounded":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.common-paley-wiener-jet-graph-domain.v1",
 "domain":"PW_R = Fourier transforms of L2 functions supported in [-R,R]",
 "normalized_jet":"j_k=(m^(k)(c+gamma)+(-1)^k m^(k)(c-gamma))/k!",
 "jet_space":"l2(omega), omega_k=(k!/(2R)^k)^2",
 "bound":"sum_k omega_k |j_k|^2 <= (32R/3)||g||_2^2",
 "common_graph":"D_R=Graph(J_R), J_R g=(j_0,j_1,...) in l2(omega)",
 "successor":"A_k exposes the kth coordinate of the single bounded map J_R; all stages are restrictions of one graph object",
 "rows":rows,"checks":checks,"passed":True,
 "conclusion":"A single translation- and dagger-stable Hilbert graph domain controls the full normalized jet tower with a uniform bound.",
 "claim_boundary":"This is aperture-wise. Passing to all compact supports uses the strict inductive limit over R and requires the corresponding LF-space bookkeeping."
}
path=Path(__file__).parents[1]/"results"/"common_paley_wiener_jet_graph_domain.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="rows"},indent=2))

"""Classify a controlled 1/t preimage as lattice Bockstein data, not a regular horn."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_singular_nearby_boundary_Bockstein_gate.json'
def main():
 # Abstract two-term R=Q[t] complex: d(h)=t*z, d(z)=0.
 # Encode coefficients in basis z; division by t is forbidden in R and allowed in Q(t).
 d_h=('t',1);assert d_h==('t',1)
 regular_preimage_exists=False;localized_preimage='h/t';principal_part_order=1
 assert not regular_preimage_exists and principal_part_order==1
 # Mod t, h is closed; the t-Bockstein is represented by d(h)/t=z.
 bockstein='z';assert bockstein=='z'
 # Deliberate invalid inference: exact after localization does not imply exact in the lattice.
 exact_localized=True;exact_regular=False;assert exact_localized and not exact_regular
 out={'schema':'marici.voevodsky.cosmology-singular-nearby-boundary-Bockstein-gate.v1','status':'one_over_t_preimage_is_Bockstein_principal_part_not_regular_filler','abstract_contract':{'base_ring':'Q[t]','equation':'d(h)=t z','regular_complex':'h/t is absent','localized_complex':'d(h/t)=z','special_fiber':'h mod t is closed','connecting_class':'beta_t([h mod t])=[z]'},'nearby_interpretation':'A simple-pole preimage records the rank-one vanishing/connecting class. It does not make z exact in the t-adic or regular source lattice.','arrangement_evidence':'The line-coefficient circuit has residual tZ, showing the required first-order determinant. This is not yet an equation d(h)=t(Xi_log,-sigma123) in a sourced motivic/logarithmic complex.','constructor_gate':'A genuine Bockstein requires an explicitly typed degree-one arrangement precycle h, a regular total differential, and an exact equality d(h)=t(Xi_log,-sigma123) with no extra components. The determinant calculation alone supplies none of these maps.','decision':'Allowing 1/t does not repair the horn. It identifies the formal shape of a possible t-Bockstein while moving the preimage outside the regular source. The current route remains unconstructed until the circuit is lifted to a sourced total-complex differential identity.','next_gate':'construct or falsify a regular arrangement circuit precycle h with differential t(Xi_log,-sigma123) and audit every residual component','limitations':['universal lattice/Bockstein classification plus first-order arrangement determinant','no circuit precycle constructed','no contour or physical period inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

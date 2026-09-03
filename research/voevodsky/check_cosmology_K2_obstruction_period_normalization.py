"""Normalize the torus period of dlog(u) wedge dlog(v) exactly."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_K2_obstruction_period_normalization.json'
def normalized_period(unit_order=(0,1),circle_orientation=(1,1)):
 permutation_sign=1 if unit_order==(0,1) else -1
 return permutation_sign*circle_orientation[0]*circle_orientation[1]
def main():
 assert normalized_period()==1
 assert normalized_period(circle_orientation=(-1,1))==-1
 assert normalized_period(circle_orientation=(1,-1))==-1
 assert normalized_period(circle_orientation=(-1,-1))==1
 assert normalized_period(unit_order=(1,0))==-1
 out={'schema':'marici.voevodsky.cosmology-K2-obstruction-period-normalization.v1','status':'primitive_torus_period_normalized_to_one','cycle':'T2={(u,v): |u|=|v|=1}, parameterized by u=exp(i theta), v=exp(i phi), with ordered orientation dtheta wedge dphi','integrand':'Xi_log=dlog(u) wedge dlog(v)','exact_period':'integral_T2 Xi_log=(2*pi*i)^2=-4*pi^2','normalized_period':'(2*pi*i)^(-2) integral_T2 Xi_log=1','orientation_rules':{'reverse_one_circle':-1,'reverse_both_circles':1,'swap_u_and_v':-1},'residue_comparison':'With the ordered units (u,v) and the corresponding positive circle orientations, the normalized period equals the primitive double residue and the oriented triangle coefficient: 1.','canonicity_boundary':'The value is canonical only after fixing the order (u,v) and both circle orientations. The unoriented torus determines the value only up to sign.','physical_boundary':'This is a mathematical Betti-de Rham period. No source-derived map from the cosmological carrier, contour prescription, state/effect pairing, or physical record map to this torus cycle has been established.','decision':'The obstruction has a primitive normalized mathematical period equal to one, consistent with its Parshin residue. This does not convert it into a horn or physical observable.','next_gate':'K2-period-physical-interface: search for and type any source-derived contour/readout map; otherwise prove the period remains purely mathematical','limitations':['complex algebraic torus period only','orientation-dependent sign','no physical-time or physical-readout interpretation'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

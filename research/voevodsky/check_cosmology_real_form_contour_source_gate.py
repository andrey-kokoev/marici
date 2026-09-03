"""Distinguish the split source real form from the compact torus contour."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_real_form_contour_source_gate.json'
def split_fixed(z):return z.conjugate()==z
def compact_fixed(z):return abs(z)!=0 and abs(z-1/z.conjugate())<1e-12
def main():
 samples=[2+0j,-3+0j,1j,-1j]
 assert split_fixed(samples[0]) and not compact_fixed(samples[0])
 assert compact_fixed(samples[2]) and not split_fixed(samples[2])
 # Their intersection on G_m is {+1,-1}, insufficient for an S1 cycle.
 intersection=[z for z in (1+0j,-1+0j,2+0j,1j) if split_fixed(z) and compact_fixed(z)];assert intersection==[1+0j,-1+0j]
 out={'schema':'marici.voevodsky.cosmology-real-form-contour-source-gate.v1','status':'compact_torus_not_selected_by_split_source_real_form','algebraic_source':'U=Spec Q[u^+/-1,v^+/-1] is the split two-torus inherited from exceptional coordinate ratios','split_real_structure':'ordinary conjugation fixes (R*)^2','period_contour':'|u|=|v|=1 is fixed by the compact involutions u -> 1/conjugate(u), v -> 1/conjugate(v)','mismatch':'For each factor the split and compact fixed loci intersect only at +1 and -1; the split real locus cannot supply the two-dimensional compact cycle.','twist_requirement':'A Cayley transform or compact real-form twist requires a choice of square root of -1, a boundary-point normalization, and orientations. No such choices arise from the rational DNC, IBP, K, q, exceptional-triangle, or Parshin source data.','temporal_boundary':'The deformation parameter and exceptional ratios have no physical-time meaning; no map to a physical-time or detector object has been declared.','decision':'The actual source coordinates do not select the unit-torus contour. The period cycle is a valid Betti generator chosen in the complexification, not the image of the available split real kinematics.','next_gate':'compact-real-form-twist: test whether any sourced boundary condition or Cayley transform canonically supplies the compact involution and its orientations','limitations':['audits the materialized rational/split source structure','does not exclude an external model with additional real-form data','no physical contour or record constructed'],'passed':True};OUT.write_text(json.dumps(out,indent=2,default=str)+'\n');print(json.dumps(out,indent=2,default=str))
if __name__=='__main__':main()

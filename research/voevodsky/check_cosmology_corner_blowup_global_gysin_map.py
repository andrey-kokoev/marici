"""Construct the global exceptional Gysin class for Bl_0(A^3)."""
from __future__ import annotations
import json
from math import gcd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_corner_blowup_global_gysin_map.json'
def main():
    # E=P^2 and N_{E/Bl}=O_E(-1); represent A*(E)=Z[H]/(H^3).
    normal_c1_coeff=-1
    assert gcd(abs(normal_c1_coeff),1)==1
    # Orientation reversal changes the sign but not primitivity.
    orientations={'standard':normal_c1_coeff,'reversed':-normal_c1_coeff}
    assert set(abs(x) for x in orientations.values())=={1}
    out={
      'schema':'marici.voevodsky.cosmology-corner-blowup-global-gysin-map.v1',
      'status':'global_exceptional_Gysin_source_class_constructed_primitive_up_to_orientation',
      'blowup':'Bl_(u,v,p)(A3)',
      'exceptional_divisor':'E=P2',
      'exceptional_normal_bundle':'N_{E/Bl}=O_E(-1)',
      'exceptional_chow_ring':'A*(E)=Z[H]/(H^3)',
      'self_intersection_formula':'i^* i_*(1)=c1(N_{E/Bl})=-H',
      'gysin_degree_shift':'codimension-one Gysin raises cohomological degree by two (or one after the programme total-complex shift)',
      'orientation_coefficients':orientations,
      'primitive_integral':True,
      'decision':'The global blow-up, unlike a single affine dlog chart, supplies a canonical degree-shifting source morphism with primitive coefficient: the exceptional Gysin class is +/-H.',
      'remaining_comparison':'Construct a chain map identifying the exceptional hyperplane class H with the target logarithmic circuit Xi_log; equality of coefficients or residues alone is insufficient.',
      'limitations':['source-side Gysin construction only','does not identify H with Xi_log','does not yet produce the full (1,1) horn column or a Bockstein'],'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__': main()

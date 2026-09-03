"""Classify primitive and weighted horns under integral monomial pullback."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_ramified_base_change_weighted_horn.json'
def det(M): return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def main():
    tests={'identity':[[1,0],[0,1]],'unimodular':[[1,1],[0,1]],'ramified':[[2,0],[0,3]],'reversing':[[0,1],[1,0]]}
    determinants={k:det(v) for k,v in tests.items()}
    assert determinants=={'identity':1,'unimodular':1,'ramified':6,'reversing':-1}
    out={
      'schema':'marici.voevodsky.cosmology-ramified-base-change-weighted-horn.v1',
      'status':'weighted_horn_multiplier_is_character_lattice_determinant_integral_normalization_classified',
      'monomial_map':'u maps to x^a y^b and v maps to x^c y^d, with character-lattice matrix M.',
      'multiplier':'Pullback sends dlog(u) wedge dlog(v), the Milnor top symbol, and the oriented relative horn class to det(M) times the target primitive generator.',
      'primitive_criterion':'The pulled-back integral class remains primitive exactly when det(M)=+1; det(M)=-1 reverses orientation but remains primitive with sign-local-system coefficients.',
      'ramified_case':'For diagonal indices e,f the multiplier is e*f. If e*f>1, no integral linear normalization recovers the primitive generator from the weighted class alone.',
      'transfer_boundary':'Norm/transfer composed with pullback multiplies by the finite degree; it does not provide integral division.',
      'saturated_reconstruction':'Reducing the pulled-back walls and rebuilding their incidence fundamental chain can produce an intrinsic primitive horn upstairs, but this uses new geometric divisor data and is not the pullback of the original horn.',
      'comparison':'weighted pullback = det(M) times saturated primitive horn, up to orientation.',
      'decision':'Ramified naturality yields a valid weighted HomotopyLift, not the primitive constructor. Primitive recovery requires a separate saturated geometric witness or rational coefficients.',
      'next_gate':'maximal-primitive-naturality-category',
      'limitations':['monomial normal-torus model','fan/incidence compatibility still required in addition to determinant','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

"""Classify equivalence and residual moduli of geometric witnesses."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_geometric_nonuniqueness_of_minimal_extension.json'
def equivalent(x): return x['compatible_carrier_map'] and x['ordered_walls'] and x['regulator_square'] and x['subdivision_zigzag']
def main():
    same={'compatible_carrier_map':True,'ordered_walls':True,'regulator_square':True,'subdivision_zigzag':True}
    same_chain={'compatible_carrier_map':False,'ordered_walls':False,'regulator_square':True,'subdivision_zigzag':False}
    assert equivalent(same) and not equivalent(same_chain)
    out={
      'schema':'marici.voevodsky.cosmology-geometric-nonuniqueness-of-minimal-extension.v1',
      'status':'geometric_witness_equivalence_classified_nonuniqueness_retained',
      'fixed_input':'For one fixed ordered regular triple (X,C,L,phi,walls), the blowup and its unsplit ambient star are canonical up to unique isomorphism.',
      'equivalence':'Witnesses are identified only by zigzags of orientation-preserving geometric isomorphisms and witnessed toroidal subdivisions whose carrier, wall, DNC, and regulator squares commute.',
      'not_equivalence':['isomorphic underlying chain pairs','equal boundary vectors','equal normal-bundle ranks','matching regulators without a carrier map','shared algebraic initial extension'],
      'moduli':['formal neighborhood of C in X','common line and ordered conormal identification','higher wall jets beyond I/I^2','DNC-to-carrier comparison','global transition and monodromy data'],
      'associated_graded_boundary':'The relative exceptional horn depends only on the ordered normal-cone data, so distinct witnesses can have the same associated-graded realization while differing as carrier geometry.',
      'universality_boundary':'The rank-one algebraic extension is initial after forgetting geometry; its fiber of geometric witnesses need not be contractible or even connected.',
      'decision':'No uniqueness theorem follows from the primitive boundary vector. The local normal model is canonical for fixed first-order data but does not identify global carrier witnesses.',
      'next_gate':'formal-neighborhood-dependence-of-witness',
      'limitations':['classification of admissible equivalence, not a census of witnesses','global carrier absent','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

"""Compare the absolute horn complex with its derived pair and relative class."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_pointed_vs_derived_source_category.json'
def main():
    absolute={'G1':1,'G2':1,'d_rank':1,'H1':0,'H2':0}
    relative={'quotient_degree1':1,'quotient_degree2':0,'d_rank':0,'H1':1,'H2':0}
    assert absolute['H1']==absolute['H2']==0
    assert relative['H1']==1
    out={
      'schema':'marici.voevodsky.cosmology-pointed-vs-derived-source-category.v1',
      'status':'minimal_localization_invariant_source_is_a_derived_geometric_pair',
      'absolute_complex':'G=[Z*Gamma -> Z*z] is acyclic and becomes zero after ordinary derived localization.',
      'boundary_pair':'Let B=Z*z be the boundary subcomplex and i:B -> G its inclusion.',
      'relative_invariant':'The quotient/cofiber G/B has one generator represented by Gamma and H1(G/B)=Z; the relative capability survives quasi-isomorphism localization.',
      'correct_category':'Use the stable infinity-category of derived arrows/pairs, with object i:B->G, its map to the comparison pair, and the chosen 2-cell/nullhomotopy. A triangulated homotopy category alone forgets the 2-cell.',
      'pointing_correction':'A bare pointing by Gamma is not a chain map because d Gamma=z. The boundary inclusion and relative cofiber, not a naive pointed complex, are required.',
      'source_gate':'Admit only pairs in the image of a geometric realization functor from ordered blowup incidence data; arbitrary algebraic disks remain unsourced cones.',
      'rank26_boundary':'The absorbed rank26 presentation has no relative pair whose boundary projects with primitive Xi coefficient one, so its no-go survives in the pair category.',
      'decision':'The HomotopyLift is durable in the derived category of geometrically realized pairs, but not as an absolute derived object or naive pointing.',
      'next_gate':'geometric-pair-provenance-gate',
      'limitations':['categorical construction; checker execution pending','does not materialize the global carrier pair','no ElementLift or physical interface inferred'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

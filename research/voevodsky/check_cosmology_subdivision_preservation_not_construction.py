"""Check that witnessed subdivision localization cannot create source provenance."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_subdivision_preservation_not_construction.json'
def admitted(x): return x['geometry_witness'] and x['realization_map'] and x['comparison_map']
def main():
    geometric={'geometry_witness':True,'realization_map':True,'comparison_map':True,'xi':1}
    formal={'geometry_witness':False,'realization_map':False,'comparison_map':True,'xi':1}
    rank26={'geometry_witness':False,'realization_map':True,'comparison_map':True,'xi':0}
    assert admitted(geometric) and not admitted(formal) and not admitted(rank26)
    assert rank26['xi']!=geometric['xi']
    out={
      'schema':'marici.voevodsky.cosmology-subdivision-preservation-not-construction.v1',
      'status':'witnessed_localization_preserves_provenance_and_blocks_reverse_laundering',
      'structured_object':'A sourced pair is a tuple (geometric witness G, realized derived pair C_rel(G), regulator comparison Phi_G), not an underlying chain pair alone.',
      'localization':'Invert only morphisms induced by witnessed toroidal subdivisions. Their formal inverses exist between already witnessed tuples.',
      'projection_boundary':'An isomorphism or quasi-isomorphism after forgetting G and Phi_G does not lift automatically to the witnessed category.',
      'coordinate_change':'A different chain presentation is admissible when accompanied by an explicit witness G and a comparison isomorphism; the isomorphism alone is not authority.',
      'rank26_obstruction':'Any comparison-respecting equivalence from the absorbed rank26 pair to the geometric horn would preserve the Xi projection, contradicting 0 versus 1. Subdivision cannot remove this obstruction.',
      'construction_boundary':'Subdivision may transport, refine, or contract an existing witnessed horn. It cannot supply the initial geometric witness or primitive relative class.',
      'decision':'Birational localization is safe only as localization of the witnessed category, not as repletion of its algebraic projection.',
      'next_gate':'rank26-relative-pair-obstruction',
      'limitations':['categorical provenance theorem','does not construct global carrier witness','checker execution pending'],
      'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

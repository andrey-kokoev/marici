#!/usr/bin/env python3
"""Test whether the p partial-fraction vector is an ordered Cech chain cell."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research'/'benincasa'/'results'/'cosmology_principal_wall_partial_fraction_cech_gate.json'
def mv(A,v):return [sum(a*x for a,x in zip(row,v)) for row in A]
def main():
 # Pair order (12,13,23); rows are vertices (1,2,3).
 edge_to_vertex=[[-1,-1,0],[1,0,-1],[0,1,1]]
 cech_face_boundary=[1,-1,1]
 partial_fraction=[1,-1,-1]
 assert mv(edge_to_vertex,cech_face_boundary)==[0,0,0]
 obstruction=mv(edge_to_vertex,partial_fraction);assert obstruction==[0,2,-2]
 prime_checks={}
 for p in (101,103):
  r=[x%p for x in obstruction];assert r!=[0,0,0];prime_checks[str(p)]={'obstruction_mod_prime':r,'d_squared_zero':False}
 out={'schema':'marici.benincasa.cosmology-principal-wall-partial-fraction-cech-gate.v1','pair_order':['12','13','23'],'edge_to_vertex_matrix':edge_to_vertex,'ordered_cech_face_boundary':cech_face_boundary,'p_partial_fraction_pair_vector':partial_fraction,'cech_boundary_obstruction':obstruction,'prime_checks':prime_checks,'partial_fraction_is_cech_cycle':False,'total_d_squared_zero':False,'orientation_rescaling_authorized':False,'coefficient_identity_remains_valid':True,'twisted_de_rham_chain_map_constructed':False,'interpretation':'the affine p identity is exact, but its induced pair-face coefficients are not the ordered Cech face boundary; treating it as the missing chain cell gives the nonzero vertex obstruction (0,2,-2)','next_gate':'a valid comparison requires additional source-derived vertex or bulk terms canceling (0,2,-2); coefficient-level partial fractions alone cannot supply tau_p','passed':True};OUT.parent.mkdir(exist_ok=True);OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

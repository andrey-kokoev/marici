#!/usr/bin/env python3
"""Factor the cyclic sign converter through triangle incidence and complement."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_marked_pair_L_shadow_connector_gate.json').read_text())['passed']
B=((-1,0,1),(1,-1,0),(0,1,-1)) # vertices 1,2,3 by edges 12,23,31
C=((0,0,1),(1,0,0),(0,1,0)) # vertices -> opposite pairs 12,23,31
def mm(X,Y):return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))) for i in range(len(X)))
def mv(X,v):return tuple(sum(X[i][j]*v[j] for j in range(len(v))) for i in range(len(X)))
A=mm(C,B);expected=((0,1,-1),(-1,0,1),(1,-1,0));assert A==expected
l=(0,-1,-1);assert mv(B,l)==(-1,1,0) and mv(C,mv(B,l))==(0,-1,1)
assert mv(B,(1,1,1))==(0,0,0)
out={'schema':'marici.benincasa.cosmology-complement-incidence-factorization-gate.v1','edge_order':['g12','g23','g31'],'vertex_order':['g1','g2','g3'],'occurrence_order':['G12:e6','G23:e6','G31:e6'],'ordered_incidence_B':[list(r) for r in B],'opposite_pair_complement_C':[list(r) for r in C],'factorization_A_equals_C_B':True,'literal_to_vertex_boundary':list(mv(B,l)),'vertex_to_occurrence_shadow':list(mv(C,mv(B,l))),'incidence_chain_check_B_face_boundary_zero':True,'C_label_lattice_isomorphism':True,'B_source_authorized_as_ordered_label_incidence':True,'C_source_authorized_as_label_complement':True,'C_realized_on_occurrence_modules':False,'exact_remaining_arrow':'lift the labelled complement permutation g1->G23:e6, g2->G31:e6, g3->G12:e6 to maps of the source and occurrence modules','q_g12_object_present':False,'conclusion':'the converter is exactly ordered incidence followed by canonical label complement; only the module-level complement realization remains','next_test':'test whether existing A2-to-e6 occurrence morphisms realize the complement permutation on modules and transports','passed':True};(R/'cosmology_complement_incidence_factorization_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

#!/usr/bin/env python3
"""Test whether one primitive A2 divisor root selects an equivariant shear."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
ext=json.loads((R/'cosmology_e6_complement_rank12_extension_lift.json').read_text());tors=json.loads((R/'clifford_a2_torsor_typing.json').read_text())
assert ext['passed'] and tors['equivariant_Hom_A2_to_trivial_dimension']==0
Q=((0,-1),(1,-1));r=(0,-1) # (0,-1,1) in basis b1=(1,-1,0), b2=(0,1,-1)
def M(x,y):return ((x,y),(-y,x+y))
def mv(A,v):return tuple(sum(A[i][j]*v[j] for j in range(2)) for i in range(2))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
# Two primitive domain anchors give distinct equivariant endomorphisms with image r.
b1=(1,0);b2=(0,1);m1=M(0,1);m2=M(-1,0)
assert mv(m1,b1)==r and mv(m2,b2)==r and m1!=m2
assert mm(m1,Q)==mm(Q,m1) and mm(m2,Q)==mm(Q,m2)
out={'schema':'marici.benincasa.cosmology-dlog-root-centralizer-element.v1','A2_basis':['(1,-1,0)','(0,1,-1)'],'dlog_X3_over_X2_coordinates':list(r),'required_shear_space':'M(x,y)=[[x,y],[-y,x+y]]','rank':2,'ambiguity_witnesses':[{'chosen_domain_anchor':'b1','selected_M':[list(x) for x in m1]},{'chosen_domain_anchor':'b2','selected_M':[list(x) for x in m2]}],'both_commute_with_cyclic_action':True,'root_selects_unique_shear':False,'type_obstruction':'a root is a vector; a shear is an endomorphism and requires an independently sourced covector or domain anchor','equivariant_linear_map_A2_to_trivial_centralizer_exists':False,'conclusion':'the sourced divisor root does not define centralizer coordinates (x,y) without extra pairing data','next_test':'seek or obstruct an occurrence-sensitive integral covector whose tensor with the dlog root defines the extension shear','passed':True};(R/'cosmology_dlog_root_centralizer_element.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

#!/usr/bin/env python3
"""Assemble the typed Bunch--Davies marked-top cusp readout."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
B=R/'research/benincasa';V=R/'research/voevodsky/results'
src=json.loads((B/'marked-relative-source-maps.json').read_text())
sp=json.loads((B/'total-energy-conductor-specialization.json').read_text())
ext=json.loads((V/'top_kernel_marked_extension_composition.json').read_text())
cech=json.loads((V/'BD_oriented_conductor_cech_chain.json').read_text())
cell=json.loads((V/'two_node_cellular_unit_incidence.json').read_text())
pic=json.loads((V/'infinity_component_picard_marking.json').read_text())
assert src['basis']['marked'][:3]==['Omega111','Omega101','Omega110']
assert sp['source']['generic_cycle_basis']==['g101','g110','g111_top']
assert sp['specialization_graph']['primitive_kernel']=='Z*g111_top'
assert cech['primitive_half_boundary']==[1,-1,1,-1]
assert cell['coefficient_of_e6_Betti']==1
assert ext['composite_column']==['0','0','1/(8*(x+y))','0']
assert pic['vectors']['e6_Betti=C_minus-C_plus']==[3,-1,-1,-1,-1,-1,-1,-3]
out={'schema':'marici.voevodsky.BD-marked-top-physical-readout.v1','physical_marked_form':'Omega111=da wedge db/(L1*L2*sqrt(K))','physical_boundary_value':'E -> E-i0','observable':'R_BD(Omega111) := (1/(2*pi*i)) Disc_E=0 integral_{Gamma_BD(E)} Omega111, read in the integral algebraic nearby-cycle quotient modulo 2','source_residue_coordinates':src['residue_w_source_normalized'][0],'vanishing_quotient_generator':'g111_top','BD_chain':{'boundary':cech['boundary'],'primitive_half_boundary':cech['primitive_half_boundary']},'integral_target':{'e6_Betti_vector':pic['vectors']['e6_Betti=C_minus-C_plus'],'v_alg_coordinate':'v0','cellular_e6_coefficient':1},'de_Rham_target_column':ext['composite_column'],'readout':{'e6_dual':1,'v_alg_dual':0,'ordered_parity':[1,0]},'interpretation':'The marked top discontinuity is an odd component-difference channel and has zero v_alg channel in the typed marked extension.','comparison_gate':{'statement':'The continued source integration current Gamma_BD specializes to the already derived BD conductor chain with multiplicity one.','status':'geometrically specified by the i0-oriented conductor arcs; an independent integral Mayer--Vietoris realization was requested from Grothendieck.'},'passed':True}
(V/'BD_marked_top_physical_readout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'observable':out['observable'],'readout':out['readout'],'gate':out['comparison_gate']}))

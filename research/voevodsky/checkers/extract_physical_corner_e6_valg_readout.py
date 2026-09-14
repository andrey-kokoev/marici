#!/usr/bin/env python3
"""Extract the sourced physical ET/Cut corner readout in the (e6,v_alg) plane."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
loc=json.loads((R/'research/benincasa/et-cut-nearby-normal-form.json').read_text())
nine=json.loads((R/'research/benincasa/total-energy-nine-master-residue.json').read_text())
vec=loc['exceptional_period_functional_e1_to_e9']
assert len(vec)==9
# e6 is coordinate six. v_alg(E=0) is supported entirely in e7,e8,e9.
e6=vec[5]; tail=vec[6:9]
checks={'physical_corner_selected':loc['physical_real_corner'].startswith('(a,b)=(y,x)'),'BD_interval_oriented':loc['canonical_leray_interval'].startswith('oriented interval'),'boundary_primitive':loc['canonical_boundary_vector']==[-1,1],'functional_exact':vec==[0,0,'y',0,'x',1,0,0,0],'e6_coefficient_unit':e6==1,'tail_zero':tail==[0,0,0],'v_alg_supported_in_tail':len(nine['gysin_kernel_check']['v_alg_at_E0_in_e7_e8_e9'])==3,'v_alg_projection_zero':tail==[0,0,0],'commutator_available':loc['full_nine_master_cut_nearby_commutator_computed']}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.physical-corner-e6-valg-readout.v1','observable':'source-normalized iterated total-energy/Cut nearby commutator at the physical real corner','physical_chain':'canonical BD Leray interval [pminus,pplus]','relative_boundary':loc['canonical_boundary_vector'],'algebraic_functional':{'basis':['e1','e2','e3','e4','e5','e6','e7','e8','e9'],'vector':vec,'expression':'y*e3 + x*e5 + e6'},'projection_to_final_algebraic_plane':{'basis':['e6','v_alg'],'coordinates':[1,0],'reason':'e6 has unit coefficient; v_alg(E=0) lies in span(e7,e8,e9), where the physical functional has zero tail'},'ordered_mod_two_readout':[1,0],'scope':'This is a sourced physical iterated ET/Cut corner observable. It is distinct from the plain total-energy marked-top discontinuity and from the four-mark global Cech chain.','checks':checks,'passed':True}
(R/'research/voevodsky/results/physical_corner_e6_valg_readout.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'observable':out['observable'],'functional':out['algebraic_functional']['expression'],'projection':out['projection_to_final_algebraic_plane'],'parity':out['ordered_mod_two_readout'],'scope':out['scope']}))

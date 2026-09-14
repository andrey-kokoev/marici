#!/usr/bin/env python3
"""Test C2 against the explicit local Betti/de Rham lattice comparison."""
import json
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parents[3]
loc=json.loads((R/'research/benincasa/et-cut-nearby-normal-form.json').read_text())
bet=json.loads((R/'research/benincasa/results/rank12-e6-local-betti-lattice.json').read_text())
cous=json.loads((R/'research/benincasa/results/rank12-e6-integral-cousin-comparison.json').read_text())
sat=json.loads((R/'research/benincasa/results/rank12-e6-global-integral-saturation.json').read_text())
vec=loc['exceptional_period_functional_e1_to_e9']; de_rham_e6_coeff=Fraction(vec[5]);rho_pair=Fraction(bet['first_rees_physical_pairing']);primitive_pair=Fraction(bet['primitive_pairing'])
index=primitive_pair/rho_pair
checks={'corner_deRham_e6_coefficient_one':de_rham_e6_coeff==1,'physical_boundary_primitive':bet['primitive_physical_boundary']==['-1','1'],'primitive_dual_pairing_one':primitive_pair==1,'source_e6_pairing_quarter':rho_pair==Fraction(1,4),'Betti_to_source_index_four':index==4,'local_saturation_Z4':bet['saturation_quotient']=='Z*rho_e6 / Z*eta = Z/4','global_saturation_index_four':sat['total_index']==4,'Betti_Cousin_boundary_unimodular':cous['occurrence_resolved_betti_smith']==[1],'quarter_frame_Smith_four':cous['quarter_enlarged_e6_smith']==[4]}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C2-corner-e6-Betti-primitivity-audit.v1','C2':'The coefficient 1 in y*e3+x*e5+e6 is a primitive integral Betti coefficient.','status':'rejected','deRham_corner_vector':vec,'local_integral_comparison':{'primitive_boundary':'d=e_minus-e_plus','primitive_dual':'eta=(-1/2,+1/2), eta(d)=1','source_first_Rees_e6':'rho_e6=(-1/8,+1/8)=(1/4)eta','rho_e6_pairing_with_d':'1/4','integral_lattice':'Z*eta=4Z*rho_e6','index':4},'Smith_checks':{'occurrence_resolved_Betti':1,'quarter_enlarged_source_frame':4},'consequence':'The displayed coefficient one is primitive in the frozen de Rham master coordinates and has Betti index four. Integral parity requires the comparison factor four before reduction.','effect_on_prior_readout':'The direct inference from de Rham coordinates [1,0] to integral parity [1,0] is withdrawn.','next':'Replay C1 in the primitive Betti basis eta and compute whether the complete sourced physical observable contributes rho_e6, 2*rho_e6, or 4*rho_e6 after every Leray and occurrence factor.','checks':checks,'passed':True}
(R/'research/voevodsky/results/C2_corner_e6_Betti_primitivity_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'audit_passed':True,'C2':out['status'],'index':4,'consequence':out['consequence'],'next':out['next']}))

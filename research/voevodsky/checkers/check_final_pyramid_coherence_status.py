#!/usr/bin/env python3
"""Final dependency-closed status certificate for the pyramid coherence objective."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
def load(n):return json.loads((ROOT/'research/voevodsky/results'/n).read_text())
names=['split_fiber_primitive_closure.json','normal_jet_e6_covector.json','one_wall_valg_covector.json','site_exchange_cross_pencil_equivariance.json','physical_chamber_full_smooth_return.json','joint_reflection_character_decomposition.json','common_pencil_alpha12_line.json','A2_pyramid_return_no_go.json','relative_Gysin_interface_synthesis.json','route_bit_thimble_obstruction_alignment.json']
d={n:load(n) for n in names};syn=d['relative_Gysin_interface_synthesis.json'];th=d['route_bit_thimble_obstruction_alignment.json']
checks={
 'dependency_closure_passes':all(v['passed'] for v in d.values()),
 'e6_axis_fixed':syn['absolute_domain']['e6_covector']==[-1,0,0],
 'route_plane_fixed':syn['absolute_domain']['route_plane']==['alpha13','alpha14'],
 'wall_valg_covector_fixed':syn['relative_domain']['v_alg_covector']==[-1,1],
 'wall_null_sum_fixed':syn['relative_domain']['null_route']==[1,1],
 'missing_interface_typed':syn['missing_interface']['symbol']=='J',
 'two_kernel_candidates':set(syn['fixed_kernel_candidates'])=={'alpha13+alpha14','alpha13-alpha14'},
 'same_thimble_constructor':th['same_missing_constructor'].startswith('source-normalized integral Picard-Lefschetz thimble'),
 'not_filesystem_derivable':th['filesystem_derivable_now'] is False,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.final-pyramid-coherence-status.v1','passed':True,'objective':'determine role and information-flow path of missing coherence comparison','objective_status':'complete','comparison':'J: relative two-wall lattice W -> absolute fixed-pencil route plane ker(q_e6)','known_rows':{'e6_on_alpha_frame':[-1,0,0],'v_alg_on_wall_frame':[-1,1]},'known_relative_kernel':'Z*(w101+w110)','fixed_pencil_kernel_candidates':['Z*(alpha13+alpha14)','Z*(alpha13-alpha14)'],'single_missing_value':'signed labelled Gysin column J(w110)','geometric_constructor':'integral Picard-Lefschetz thimble through primitive infinity-Gysin sequence','constructor_available':False,'checks':checks}
p=ROOT/'research/voevodsky/results/final_pyramid_coherence_status.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'objective_status':'complete','missing_value':out['single_missing_value']}))

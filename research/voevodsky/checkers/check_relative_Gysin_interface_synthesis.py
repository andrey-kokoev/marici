#!/usr/bin/env python3
"""Synthesize the typed relative-Gysin interface from exact prior packets."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
def load(name):return json.loads((ROOT/'research/voevodsky/results'/name).read_text())
lat=load('split_fiber_primitive_closure.json');e6=load('normal_jet_e6_covector.json');wall=load('one_wall_valg_covector.json');common=load('common_pencil_alpha12_line.json');ret=load('physical_chamber_full_smooth_return.json');bits=load('return_comparison_orientation_bit.json');typing=load('cross_pencil_wall_typing.json')
checks={
 'all_inputs_pass':all(d['passed'] for d in (lat,e6,wall,common,ret,bits,typing)),
 'absolute_rank_three':len(lat['primitive_gram'])==3,
 'e6_row':e6['covector_alpha_frame']==[-1,0,0],
 'absolute_route_rank_two':e6['kernel']==['alpha13','alpha14'],
 'relative_valg_row':wall['cleared_covector']==[-1,1],
 'relative_sum_kernel':wall['kernel_generator']==[1,1],
 'common_line_alpha12':common['common_rational_line']=='Q*alpha12',
 'absolute_return_identity':ret['split_Picard_return_matrix']==[[1,0,0],[0,1,0],[0,0,1]],
 'wall_routes_cross_pencil':typing['wall_routes']['w101'].startswith('b-pencil') and typing['wall_routes']['w110'].startswith('a-pencil'),
 'exactly_two_fixed_kernel_candidates':len(bits['unoriented_kernel_generators'])==2,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.relative-Gysin-interface-synthesis.v1','passed':True,'absolute_domain':{'lattice':'A1^3','frame':['alpha12','alpha13','alpha14'],'e6_covector':[-1,0,0],'route_plane':['alpha13','alpha14']},'relative_domain':{'frame':['w101','w110'],'v_alg_covector':[-1,1],'null_route':[1,1]},'absolute_chamber_transport':'identity','missing_interface':{'symbol':'J','type':'relative two-wall lattice W -> fixed-pencil absolute route plane','required_column':'J(w110) with signed alpha13/alpha14 coordinates'},'fixed_kernel_candidates':['alpha13+alpha14','alpha13-alpha14'],'decision':'the comparison role and information flow are determined; its final signed Gysin column is not constructed','checks':checks}
p=ROOT/'research/voevodsky/results/relative_Gysin_interface_synthesis.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'missing_arrow':'J: W -> L_b^route','remaining_candidates':2}))

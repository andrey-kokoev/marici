#!/usr/bin/env python3
"""Identify the common reflection-fixed pencil line in the b-pencil frame."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
joint=json.loads((ROOT/'research/voevodsky/results/joint_reflection_character_decomposition.json').read_text())
rb=json.loads((ROOT/'research/voevodsky/results/b_reflection_fixed_pencil_transport.json').read_text())
M=s.Matrix(rb['alpha_frame_action']);fixed=(M-s.eye(3)).nullspace();odd=(M+s.eye(3)).nullspace()
checks={
 'joint_packet':joint['passed'],
 'b_pencil_rank_three':M.shape==(3,3),
 'rb_fixed_line_alpha12':fixed==[s.Matrix([1,0,0])],
 'rb_odd_plane_alpha13_alpha14':odd==[s.Matrix([0,1,0]),s.Matrix([0,0,1])],
 'ambient_common_rank_one':joint['common_fixed_rank']==1,
 'plus_minus_joint_rank_two':joint['joint_characters']['+-']==2,
 'minus_plus_joint_rank_two':joint['joint_characters']['-+']==2,
}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.common-pencil-alpha12-line.v1','passed':True,'common_rational_line':'Q*alpha12','b_pencil_route_plane':'span(alpha13,alpha14), joint character (+,-)','a_pencil_route_plane':'rank-two joint character (-,+)','route_plane_intersection_rank':0,'missing_comparison_type':'integral off-character transport (-,+) -> (+,-)','checks':checks}
p=ROOT/'research/voevodsky/results/common_pencil_alpha12_line.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'common_line':'alpha12','route_character_sectors':['+-','-+']}))

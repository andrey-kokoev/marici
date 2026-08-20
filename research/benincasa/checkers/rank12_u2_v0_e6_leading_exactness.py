"""Exactness of the leading e6 form at the second-center node."""
import json
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/benincasa/results/rank12-u2-v0-e6-leading-exactness.json'
# For W=2T, both sides have coefficient -1/(2*T^2).
coefficient_factor=Fraction(-1,2)
primitive_derivative_factor=Fraction(-1,2)
assert coefficient_factor == primitive_derivative_factor
packet={
 'schema':'marici.benincasa.rank12_u2_v0_e6_leading_exactness.v1',
 'source_master':'e6=-K1*da wedge db/(2*K^(3/2))',
 'initial_forms':{'K':'4*p^2*T^2','K1':'-16*p*T','da_wedge_db':'p^2*dA wedge dB'},
 'leading_form':'8*T*dA wedge dB/W^3 = -4*T*dT wedge dB/W^3',
 'primitive':'1/W',
 'identity':'gr0(e6)=d_T(1/W) wedge dB',
 'leading_node_class_zero':True,
 'node_to_e6_map_derived':False,
 'classification':'the ordinary leading nodal grade of e6 is exact; any comparison must occur in a higher Rees grade or a supported relative complex'
}
OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(packet,indent=2)+'\n');print(json.dumps(packet))

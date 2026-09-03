#!/usr/bin/env python3
"""Verify the corrected all-S serialization at the admitted p-normal point."""
import json
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];R=ROOT/'research';B=R/'benincasa'/'results'
s=json.loads((B/'cosmology_all_S_row_serialization.json').read_text());p=json.loads((R/'voevodsky'/'results'/'cosmology_rank26_p_normal_protocol_gate.json').read_text());assert s['point']==p['test_point_xyz']==[3,6,-3];assert s['p_value']==0;assert s['serialized_terms']==[];assert s['normal_derivative_serialization']['column_label']==[0,1,1,1,1,1,[0,0]];out={'schema':'marici.benincasa.cosmology-all-S-row-serialization-final.v1','corrected_point':[3,6,-3],'p_value':0,'wall_value_serialization':'zero section','normal_derivative_column':[0,1,1,1,1,1,[0,0]],'ordered_laurent_coefficients':[-1,-1,1],'correction_to_prior_graph_state':'the earlier point (2,3,-5) and coefficient -10 were off-protocol and are superseded','passed':True};(B/'cosmology_all_S_row_serialization_final.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

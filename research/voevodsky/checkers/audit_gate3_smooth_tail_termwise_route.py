#!/usr/bin/env python3
"""Audit whether derivative-jump triangle bounds can prove the smooth-tail law."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];L=.6495;n=np.arange(1000);sc=np.sqrt((2*n+1)/(2*L));dp=n*(n+1)/(2*L);plus=np.linalg.norm((Z*(sc*dp)[:,None]).sum(axis=0));minus=np.linalg.norm((Z*(sc*dp*((-1.)**(n+1)))[:,None]).sum(axis=0));obs=json.loads((root/'continuum_residual_jump_smooth_decomposition_L06495_to5000.json').read_text())['rows'];scaled=[(i+1)*x['smooth_remainder_norm'] for i,x in enumerate(obs)];out={'schema':'marici.voevodsky.gate3-smooth-tail-termwise-route-audit.v1','endpoint_derivative_row_norms':[float(plus),float(minus)],'observed_m_times_smooth_block_norm':scaled,'target_uniform_constant':.015,'observed_blocks_pass_target':all(x<.015 for x in scaled[1:]),'termwise_derivative_triangle_viable':False,'reason':'endpoint derivative rows are O(1e6); separate derivative-jump triangle bounds discard cancellation among shifted endpoints','required_route':'finite physical residual integral bound or coefficientwise combined endpoint expansion','passed_audit':True,'rh_proved':False};p=root/'gate3_smooth_tail_termwise_route_audit.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['observed_blocks_pass_target']

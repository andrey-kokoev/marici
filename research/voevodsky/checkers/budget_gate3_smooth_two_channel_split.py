#!/usr/bin/env python3
"""Orthogonal two-channel budget for the Gate-3 smooth tail."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];L=.6495;n=np.arange(1000);sc=np.sqrt((2*n+1)/(2*L));fac=n*(n+1)/(2*L);plus=(Z*(sc*fac)[:,None]).sum(0);minus=(Z*(sc*fac*((-1.)**(n+1)))[:,None]).sum(0);Q=np.linalg.qr(np.array([plus,minus]).T)[0];P=Q@Q.T;rows=[]
for m in (5,6,7):
 S=np.load(root/f'continuum_residual_jump_smooth_L06495_{m}000_{m}999.npz')['smooth'];a=float(np.linalg.norm(S@P,2));b=float(np.linalg.norm(S@(np.eye(40)-P),2));rss=math.hypot(a,b);rows.append({'m':m,'endpoint_derivative_channel':a,'orthogonal_remainder':b,'rss_operator_upper':rss,'m_times_endpoint':m*a,'m_times_remainder':m*b,'m_times_rss_upper':m*rss,'actual_m_times_norm':m*float(np.linalg.norm(S,2))})
A=.023;B=.008;combined=math.hypot(A,B);out={'schema':'marici.voevodsky.gate3-smooth-two-channel-split.v1','rows':rows,'proposed_laws':{'endpoint_derivative_channel':f'{A}/m','orthogonal_remainder':f'{B}/m'},'combined_law_constant':combined,'target':.025,'budget_passes':combined<.025,'passed':False,'remaining':['directed coupled scalar-kernel bound for endpoint channel','directed higher-antiderivative bound for orthogonal remainder'],'rh_proved':False};p=root/'gate3_smooth_two_channel_split.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['budget_passes'] and all(x['m_times_endpoint']<A and x['m_times_remainder']<B for x in rows)

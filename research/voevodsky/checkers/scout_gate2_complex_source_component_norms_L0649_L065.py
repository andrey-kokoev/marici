#!/usr/bin/env python3
"""Component norm budget for the coarse Gate-2 E2 source bound."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';even=['L0649','L0649010','L0649038','L0649084','L0649146','L0649222','L0649309','L0649402','L06495','L0649598','L0649691','L0649778','L0649854','L0649916','L0649962','L0649990','L065'];odd=['L'+f'{(.6495+.0005*math.cos((32-j)*math.pi/32)):.10f}'.replace('.','') for j in range(1,32,2)];P=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['packet'];Q=np.linalg.qr(P,mode='complete')[0][:,40:];Fs=[];Bs=[]
for k in range(33):
 tag=even[k//2] if k%2==0 else odd[k//2];A=np.load(root/f'gamma_floor_{tag}_rank1000_midpoint.npz')['matrix'];Fs.append(P.T@A@P);Bs.append(P.T@A@Q)
t=np.cos(np.arange(32,-1,-1)*np.pi/32);CF=np.polynomial.chebyshev.chebfit(t,np.array(Fs).reshape(33,-1),16).reshape(17,40,40);CB=np.polynomial.chebyshev.chebfit(t,np.array(Bs).reshape(33,-1),16).reshape(17,40,960);CR=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'][:17];mf=mb=mr=0
for j in range(2048):
 th=2*math.pi*j/2048;z=(2*np.exp(1j*th)+.5*np.exp(-1j*th))/2;mf=max(mf,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,CF),2)));mb=max(mb,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,CB),2)));mr=max(mr,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,CR),2)))
tailfloor=.5341755858170448;alpha=1.067569476012246;schur=mf+mb*mb/tailfloor;complete=schur+mr/alpha;allow=6.465313495638705;out={'schema':'marici.voevodsky.gate2-complex-source-component-norms-L0649-L065.v1','sampled_F_norm':mf,'sampled_B_norm':mb,'covered_C_inverse_norm':1/tailfloor,'schur_triangle_bound':schur,'sampled_residual_gram_norm':mr,'complete_triangle_bound':complete,'admissible_full_source_norm':allow,'passed_scout':complete<allow,'passed':False,'remaining':'directed coefficient and post-degree16 remainder bounds for F, B, and residual Gram','rh_proved':False};p=root/'gate2_complex_source_component_norms_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']

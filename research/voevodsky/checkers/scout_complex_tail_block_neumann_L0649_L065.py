#!/usr/bin/env python3
"""Degree-32 source scout for a complex-ellipse tail-block Neumann argument."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';tags=[]
# Existing 17 tags in increasing-L Chebyshev order.
even=['L0649','L0649010','L0649038','L0649084','L0649146','L0649222','L0649309','L0649402','L06495','L0649598','L0649691','L0649778','L0649854','L0649916','L0649962','L0649990','L065']
odd=['L'+f'{(.6495+.0005*math.cos((32-j)*math.pi/32)):.10f}'.replace('.','') for j in range(1,32,2)]
for k in range(33):tags.append(even[k//2] if k%2==0 else odd[k//2])
P=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['packet'];Q=np.linalg.qr(P,mode='complete')[0][:,40:];Cs=[]
for tag in tags:
 A=np.load(root/f'gamma_floor_{tag}_rank1000_midpoint.npz')['matrix'];Cs.append(Q.T@A@Q)
Cs=np.array(Cs);t=np.cos(np.arange(32,-1,-1)*np.pi/32);coef=np.polynomial.chebyshev.chebfit(t,Cs.reshape(33,-1),32).reshape(33,960,960);norms=[float(np.linalg.norm(x,'fro')) for x in coef];rho=3.;# On E_rho, |T_k(z)| <= (rho^k+rho^-k)/2.
variation=sum(norms[k]*(rho**k+rho**(-k))/2 for k in range(1,33));C0=coef[0];floor=float(np.linalg.eigvalsh((C0+C0.T)/2)[0]);out={'schema':'marici.voevodsky.complex-tail-block-neumann-scout-L0649-L065.v1','bernstein_rho':rho,'constant_coefficient_floor':floor,'nonconstant_ellipse_norm_sum':variation,'neumann_margin':floor-variation,'coefficient_frobenius_norms':norms,'passed_scout':variation<floor,'passed':False,'reason_not_certificate':'source coefficient tail beyond degree 32 and floating coefficient norms remain open','rh_proved':False};p=root/'complex_tail_block_neumann_scout_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

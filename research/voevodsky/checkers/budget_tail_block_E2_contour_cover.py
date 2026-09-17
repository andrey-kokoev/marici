#!/usr/bin/env python3
"""Frobenius derivative budget for a directed E2 tail-block contour cover."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';# Reconstruct same degree-16 least-squares tail polynomial.
even=['L0649','L0649010','L0649038','L0649084','L0649146','L0649222','L0649309','L0649402','L06495','L0649598','L0649691','L0649778','L0649854','L0649916','L0649962','L0649990','L065'];odd=['L'+f'{(.6495+.0005*math.cos((32-j)*math.pi/32)):.10f}'.replace('.','') for j in range(1,32,2)];P=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['packet'];Q=np.linalg.qr(P,mode='complete')[0][:,40:];X=[]
for k in range(33):
 tag=even[k//2] if k%2==0 else odd[k//2];A=np.load(root/f'gamma_floor_{tag}_rank1000_midpoint.npz')['matrix'];X.append(Q.T@A@Q)
t=np.cos(np.arange(32,-1,-1)*np.pi/32);C=np.polynomial.chebyshev.chebfit(t,np.array(X).reshape(33,-1),16).reshape(17,960,960);rho=2.;den=rho-rho**-1;d_dz=sum(np.linalg.norm(C[k],'fro')*k*(rho**k-rho**(-k))/den for k in range(1,17));d_dtheta=d_dz*(rho+rho**-1)/2;sample_floor=1.0673377253416951;N=math.ceil(math.pi*d_dtheta/(sample_floor*.5));half_arc=math.pi/N;variation=d_dtheta*half_arc;out={'schema':'marici.voevodsky.tail-block-E2-contour-cover-budget.v1','frobenius_derivative_bound_dC_dz':float(d_dz),'frobenius_derivative_bound_dC_dtheta':float(d_dtheta),'sampled_floor_reference':sample_floor,'recommended_samples':N,'half_arc_variation_bound':float(variation),'conditional_singular_floor':float(sample_floor-variation),'passed_conditionally':bool(variation<sample_floor),'passed':False,'conditions':['directed coefficient Frobenius norms','directed singular lower bounds at recommended contour nodes','post-degree16 source tail included'],'rh_proved':False};p=root/'tail_block_E2_contour_cover_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']

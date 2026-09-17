#!/usr/bin/env python3
"""Sample complex singular values of the degree-16 tail-block polynomial on E2."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.linalg import svdvals
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.linalg import svdvals
root=Path(__file__).parents[1]/'results';# Rebuild coefficients from the 33-node source matrices.
d=np.load(root/'degree32_residual_gram_family_L0649_L065.npz') # existence guard
# Coefficients cached by the prior scout are not saved; repeat compactly from its source-node list.
even=['L0649','L0649010','L0649038','L0649084','L0649146','L0649222','L0649309','L0649402','L06495','L0649598','L0649691','L0649778','L0649854','L0649916','L0649962','L0649990','L065'];odd=['L'+f'{(.6495+.0005*math.cos((32-j)*math.pi/32)):.10f}'.replace('.','') for j in range(1,32,2)];P=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['packet'];Q=np.linalg.qr(P,mode='complete')[0][:,40:];X=[]
for k in range(33):
 tag=even[k//2] if k%2==0 else odd[k//2];A=np.load(root/f'gamma_floor_{tag}_rank1000_midpoint.npz')['matrix'];X.append(Q.T@A@Q)
t=np.cos(np.arange(32,-1,-1)*np.pi/32);C=np.polynomial.chebyshev.chebfit(t,np.array(X).reshape(33,-1),16).reshape(17,960,960);rows=[]
for j in range(8):
 th=2*math.pi*j/8;z=(2*np.exp(1j*th)+.5*np.exp(-1j*th))/2;M=np.polynomial.chebyshev.chebval(z,C);rows.append({'theta':th,'minimum_singular':float(svdvals(M)[-1]),'norm':float(svdvals(M)[0])})
out={'schema':'marici.voevodsky.tail-block-complex-E2-samples.v1','rows':rows,'minimum_sampled_singular':min(x['minimum_singular'] for x in rows),'passed_scout':min(x['minimum_singular'] for x in rows)>.5,'passed':False,'rh_proved':False};p=root/'tail_block_complex_E2_samples.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']

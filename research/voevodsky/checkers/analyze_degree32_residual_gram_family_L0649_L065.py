#!/usr/bin/env python3
"""Separate the physical residual-Gram family from the corrected lower forms."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';even=['L0649','L0649010','L0649038','L0649084','L0649146','L0649222','L0649309','L0649402','L06495','L0649598','L0649691','L0649778','L0649854','L0649916','L0649962','L0649990','L065'];oddnew=['L'+f'{(.6495+.0005*math.cos((32-j)*math.pi/32)):.10f}'.replace('.','') for j in range(1,32,2)];R=[]
for k in range(33):
 if k%2==0:
  tag=even[k//2];suffix='_degree16' if k%4==2 else ''
  # midpoint has both; ordinary corrected artifact is valid there.
  if tag=='L06495':suffix=''
  p=root/f'physical_regularized_residual_gram_{tag}{suffix}_refined_matrices.npz'
 else:
  tag=oddnew[k//2];p=root/f'physical_regularized_residual_gram_{tag}_degree32new_refined_matrices.npz'
 R.append(np.load(p)['residual_gram'])
R=np.array(R);t=np.cos(np.arange(32,-1,-1)*np.pi/32);C=np.polynomial.chebyshev.chebfit(t,R.reshape(33,-1),32).reshape(33,40,40);norms=[float(np.linalg.norm(x,2)) for x in C];rho=2.;mx=0
for j in range(2048):
 th=2*math.pi*j/2048;z=(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th))/2;D=np.polynomial.chebyshev.chebval(z,C[17:]) # wrong shifted basis diagnostic only
 # Evaluate actual high-degree sum.
 D=sum(C[k]*np.polynomial.chebyshev.chebval(z,[0]*k+[1]) for k in range(17,33));mx=max(mx,float(np.linalg.norm(D,2)))
out={'schema':'marici.voevodsky.degree32-residual-gram-family-L0649-L065.v1','coefficient_spectral_norms':norms,'degree17_32_l1':sum(norms[17:]),'sampled_E2_high_degree_sum_max':mx,'passed_scout':sum(norms[17:])<1e-10,'passed':False,'reason_not_certificate':'quadrature/source rounding and tail beyond degree32 are not enclosed','rh_proved':False};np.savez_compressed(root/'degree32_residual_gram_family_L0649_L065.npz',node_matrices=R,coefficients=C);p=root/'degree32_residual_gram_family_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']

#!/usr/bin/env python3
"""Finite regularized Schur scout using 90 concentration modes plus endpoint vectors."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import iv
root=Path(__file__).parents[1]/'results';A=np.load(root/'rank670_gamma_floor_midpoint.npz')['matrix'];d=json.loads((root/'two_prime_concentration_modes.json').read_text());C0=np.zeros((670,90));C0[:200]=np.array(d['coefficients']);L=.55;x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in range(670)]);am=ap*((-1.)**np.arange(670));X=np.column_stack((C0,ap,am));P,_=np.linalg.qr(X,mode='reduced');Q=np.linalg.qr(P,mode='complete')[0][:,P.shape[1]:];F=P.T@A@P;T=Q.T@A@Q;B=P.T@A@Q;te,U=np.linalg.eigh((T+T.T)/2);Y=U@((U.T@B.T)/te[:,None]);S=F-B@Y;S=(S+S.T)/2;Z=P-Q@Y;np.savez(root/'two_prime_regularized_rank670_vectors.npz',retained=P,tail_map=Q@Y,schur_vectors=Z,finite_schur=S);alpha=.5897761979384148
# A posteriori floor form using the exact finite solve has zero finite residual; report conditioning.
out={'schema':'marici.voevodsky.two-prime-regularized-schur-rank670-scout.v1','retained_dimension':P.shape[1],'finite_tail_dimension':Q.shape[1],'finite_tail_min':float(te[0]),'certified_infinite_tail_floor':alpha,'finite_schur_min':float(np.linalg.eigvalsh(S)[0]),'cross_norm':float(np.linalg.svd(B,compute_uv=False)[0]),'tail_inverse_norm':float(1/te[0]),'status':'floating finite Schur scout; residual beyond degree 669 not included','passed':float(te[0])>alpha and float(np.linalg.eigvalsh(S)[0])>0,'rh_proved':False};p=root/'two_prime_regularized_schur_rank670_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

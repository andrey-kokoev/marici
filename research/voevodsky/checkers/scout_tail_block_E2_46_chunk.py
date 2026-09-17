#!/usr/bin/env python3
"""Chunk of the 46-node E2 singular-value contour check."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.linalg import svd
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';a=int(sys.argv[1]);b=int(sys.argv[2]);C=np.load(root/'tail_block_degree16_polynomial_L0649_L065.npz')['coefficients'];rows=[]
for j in range(a,b):
 th=2*math.pi*j/46;z=(2*np.exp(1j*th)+.5*np.exp(-1j*th))/2;M=np.polynomial.chebyshev.chebval(z,C);U,s,Vh=svd(M,full_matrices=False);du=np.linalg.norm(U.conj().T@U-np.eye(960),'fro');dv=np.linalg.norm(Vh@Vh.conj().T-np.eye(960),'fro');rec=np.linalg.norm(M-(U*s)@Vh,'fro');u=2**-53;gam=2000*u/(1-2000*u);evalerr=gam*sum(np.linalg.norm(x,'fro') for x in C);low=s[-1]*math.sqrt(max(0,1-du))*math.sqrt(max(0,1-dv))-rec-evalerr;rows.append({'index':j,'theta':th,'minimum_singular':float(s[-1]),'norm':float(s[0]),'orthogonality_defects':[float(du),float(dv)],'reconstruction_error':float(rec),'evaluation_roundoff_bound':float(evalerr),'directed_style_lower':float(low)})
out={'schema':'marici.voevodsky.tail-block-E2-46-chunk.v1','range':[a,b],'rows':rows,'minimum':min(x['minimum_singular'] for x in rows),'passed_scout':min(x['minimum_singular'] for x in rows)>1.06,'passed':False,'rh_proved':False};p=root/f'tail_block_E2_46_chunk_{a}_{b}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));assert out['passed_scout']

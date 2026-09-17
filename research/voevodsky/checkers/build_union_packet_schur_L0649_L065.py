#!/usr/bin/env python3
"""Two-endpoint union-packet Schur continuation on [.649,.65]."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';names=['gamma_floor_L0649_rank1000_midpoint.npz','gamma_floor_L0649038_rank1000_midpoint.npz','gamma_floor_L0649146_rank1000_midpoint.npz','gamma_floor_L0649309_rank1000_midpoint.npz','gamma_floor_L06495_rank1000_midpoint.npz','gamma_floor_L0649691_rank1000_midpoint.npz','gamma_floor_L0649854_rank1000_midpoint.npz','gamma_floor_L0649962_rank1000_midpoint.npz','gamma_floor_L065_rank1000_midpoint.npz'];A0=np.load(root/names[0])['matrix'];A1=np.load(root/names[-1])['matrix'];e0,U0=np.linalg.eigh(A0);e1,U1=np.linalg.eigh(A1);U=np.linalg.qr(np.column_stack((U0[:,:20],U1[:,:20])))[0];# Put the two endpoint critical vectors last after orthogonalizing them against the other union directions.
C=np.column_stack((U0[:,0],U1[:,0]));R=np.linalg.qr(np.column_stack((U,C)))[0];# QR keeps U span first; instead use SVD union then classify 2 smallest endpoint aggregate directions by projected A0+A1.
H=U.T@(A0+A1)@U;eh,T=np.linalg.eigh(H);W=U@np.column_stack((T[:,2:],T[:,:2]));S=[];rob=[]
for n in names:
 M=W.T@np.load(root/n)['matrix']@W;F=M[:-2,:-2];B=M[:-2,-2:];S.append(M[-2:,-2:]-B.T@np.linalg.solve(F,B));rob.append(float(np.linalg.eigvalsh(F)[0]))
t=np.cos(np.arange(8,-1,-1)*np.pi/8);coef=np.polynomial.chebyshev.chebfit(t,np.array(S).reshape(9,-1),8).reshape(9,2,2);grid=np.linspace(-1,1,2001);mins=[]
for x in grid:
 M=np.polynomial.chebyshev.chebval(x,coef);mins.append(np.linalg.eigvalsh((M+M.T)/2)[0])
out={'schema':'marici.voevodsky.union-packet-schur-L0649-L065.v1','union_dimension':U.shape[1],'critical_schur_dimension':2,'robust_node_minima':rob,'schur_node_minima':[float(np.linalg.eigvalsh((x+x.T)/2)[0]) for x in S],'dense_degree8_min':float(min(mins)),'coefficient_norms':[float(np.linalg.norm(x,2)) for x in coef],'high_degree_norm_sum_5_to8':float(sum(np.linalg.norm(coef[k],2) for k in range(5,9))),'passed':bool(min(mins)>0 and min(rob)>0),'status':'floating union-packet continuation; directed leakage and analytic remainder open','rh_proved':False};p=root/'union_packet_schur_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

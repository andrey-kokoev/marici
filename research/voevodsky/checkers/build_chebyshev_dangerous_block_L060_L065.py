#!/usr/bin/env python3
"""Degree-4 Chebyshev continuation pilot for a fixed 20-mode dangerous packet."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';files=['gamma_floor_L060_rank1000_midpoint.npz','gamma_floor_L0607322_rank1000_midpoint.npz','gamma_floor_L0625_rank1000_midpoint.npz','gamma_floor_L0642678_rank1000_midpoint.npz','gamma_floor_L065_rank1000_midpoint.npz'];A=[np.load(root/f)['matrix'] for f in files];ev,V=np.linalg.eigh(A[-1]);V=V[:,:20];B=np.array([V.T@x@V for x in A]);# Values ordered at Lobatto t=-1,-sqrt(1/2),0,+sqrt(1/2),+1.
t=np.cos(np.arange(4,-1,-1)*np.pi/4);coef=np.polynomial.chebyshev.chebfit(t,B.reshape(5,-1),4).reshape(5,20,20);grid=np.linspace(-1,1,401);mins=[]
for x in grid:
 M=np.polynomial.chebyshev.chebval(x,coef);M=(M+M.T)/2;mins.append(np.linalg.eigvalsh(M)[0])
# Derivative norm provides a subdivision Lipschitz bound for the polynomial itself.
dcoef=np.polynomial.chebyshev.chebder(coef,axis=0);dn=max(np.linalg.norm(np.polynomial.chebyshev.chebval(x,dcoef),2) for x in grid);out={'schema':'marici.voevodsky.chebyshev-dangerous-block-L060-L065.v1','L_interval':[.6,.65],'degree':4,'packet_dimension':20,'lobatto_nodes':[.6,.6073223304703363,.625,.6426776695296637,.65],'node_minima':[float(np.linalg.eigvalsh((x+x.T)/2)[0]) for x in B],'dense_polynomial_min':float(min(mins)),'dense_min_L':float(.625+.025*grid[int(np.argmin(mins))]),'highest_coefficient_norm':float(np.linalg.norm(coef[-1],2)),'polynomial_t_derivative_norm_upper_sample':float(dn),'status':'floating continuation pilot; analytic matrix remainder and moving-packet leakage not yet enclosed','passed':bool(min(mins)>0),'rh_proved':False};p=root/'chebyshev_dangerous_block_L060_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'chebyshev_dangerous_block_L060_L065.npz',coefficients=coef,basis=V);print(json.dumps(out,indent=2))

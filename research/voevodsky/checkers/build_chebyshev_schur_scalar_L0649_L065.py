#!/usr/bin/env python3
"""Degree-4 scalar-Schur continuation on the endpoint slab [.649,.65]."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';names=['gamma_floor_L0649_rank1000_midpoint.npz','gamma_floor_L0649146_rank1000_midpoint.npz','gamma_floor_L06495_rank1000_midpoint.npz','gamma_floor_L0649854_rank1000_midpoint.npz','gamma_floor_L065_rank1000_midpoint.npz'];Aend=np.load(root/names[-1])['matrix'];ev,V=np.linalg.eigh(Aend);W=np.column_stack((V[:,1:20],V[:,0]));vals=[];rob=[]
for n in names:
 M=W.T@np.load(root/n)['matrix']@W;F=M[:19,:19];b=M[:19,19];vals.append(float(M[19,19]-b@np.linalg.solve(F,b)));rob.append(float(np.linalg.eigvalsh(F)[0]))
t=np.cos(np.arange(4,-1,-1)*np.pi/4);coef=np.polynomial.chebyshev.chebfit(t,np.array(vals),4);grid=np.linspace(-1,1,2001);sg=np.polynomial.chebyshev.chebval(grid,coef);out={'schema':'marici.voevodsky.chebyshev-schur-scalar-L0649-L065.v1','L_interval':[.649,.65],'node_schur_values':vals,'robust_block_minima':rob,'coefficients':[float(x) for x in coef],'highest_coefficient_absolute':float(abs(coef[-1])),'last_two_absolute_sum':float(np.sum(abs(coef[-2:]))),'dense_min':float(np.min(sg)),'dense_min_L':float(.6495+.0005*grid[int(np.argmin(sg))]),'passed':bool(np.min(sg)>0 and min(rob)>0),'status':'floating degree-4 endpoint slab; nested refinement needed for remainder','rh_proved':False};p=root/'chebyshev_schur_scalar_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

#!/usr/bin/env python3
"""Chebyshev continuation of the scalar Schur complement, not raw block entries."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';names=['gamma_floor_L0649_rank1000_midpoint.npz','gamma_floor_L0649038_rank1000_midpoint.npz','gamma_floor_L0649146_rank1000_midpoint.npz','gamma_floor_L0649309_rank1000_midpoint.npz','gamma_floor_L06495_rank1000_midpoint.npz','gamma_floor_L0649691_rank1000_midpoint.npz','gamma_floor_L0649854_rank1000_midpoint.npz','gamma_floor_L0649962_rank1000_midpoint.npz','gamma_floor_L065_rank1000_midpoint.npz'];Aend=np.load(root/names[-1])['matrix'];ev,V=np.linalg.eigh(Aend);# Put endpoint critical vector last, with next 19 modes as robust block.
W=np.column_stack((V[:,1:20],V[:,0]));vals=[];rob=[]
for n in names:
 M=W.T@np.load(root/n)['matrix']@W;F=M[:19,:19];b=M[:19,19];vals.append(float(M[19,19]-b@np.linalg.solve(F,b)));rob.append(float(np.linalg.eigvalsh(F)[0]))
t=np.cos(np.arange(8,-1,-1)*np.pi/8);coef=np.polynomial.chebyshev.chebfit(t,np.array(vals),8);grid=np.linspace(-1,1,2001);sg=np.polynomial.chebyshev.chebval(grid,coef);out={'schema':'marici.voevodsky.chebyshev-schur-scalar-L0649-L065.v1','node_schur_values':vals,'node_robust_block_minima':rob,'chebyshev_coefficients':[float(x) for x in coef],'high_degree_absolute_sum_5_to_8':float(np.sum(abs(coef[5:]))),'dense_schur_min':float(np.min(sg)),'dense_min_L':float(.6495+.0005*grid[int(np.argmin(sg))]),'status':'floating scalar Schur continuation; directed analytic remainder open','passed':float(np.min(sg))>0 and min(rob)>0,'rh_proved':False};p=root/'chebyshev_schur_scalar_L064_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

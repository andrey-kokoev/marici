#!/usr/bin/env python3
"""Reduce exact finite Schur matrices to a 2x2 moving critical block before interpolation."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';S=np.load(root/'regularized_union_tail_maps_L0649_L065.npz')['schur'];e,T=np.linalg.eigh(S[0]+S[-1]);W=np.column_stack((T[:,2:],T[:,:2]));R=[];flo=[]
for A in S:
 M=W.T@A@W;F=M[:38,:38];B=M[:38,38:];R.append(M[38:,38:]-B.T@np.linalg.solve(F,B));flo.append(float(np.linalg.eigvalsh(F)[0]))
t=np.cos(np.arange(8,-1,-1)*np.pi/8);coef=np.polynomial.chebyshev.chebfit(t,np.array(R).reshape(9,-1),8).reshape(9,2,2);cn=[float(np.linalg.norm(x,2)) for x in coef];grid=np.linspace(-1,1,2001);mins=[float(np.linalg.eigvalsh((np.polynomial.chebyshev.chebval(x,coef)+np.polynomial.chebyshev.chebval(x,coef).T)/2)[0]) for x in grid];out={'schema':'marici.voevodsky.regularized-reduced-schur-L0649-L065.v1','robust_floor_nodes':flo,'critical_node_minima':[float(np.linalg.eigvalsh(x)[0]) for x in R],'coefficient_norms':cn,'high_degree_sum_5_to8':sum(cn[5:]),'dense_min':min(mins),'passed':min(flo)>0 and min(mins)>0,'rh_proved':False};p=root/'regularized_reduced_schur_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

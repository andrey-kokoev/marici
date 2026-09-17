#!/usr/bin/env python3
"""Degree-8 refinement of the L=.64-.65 dangerous-block Chebyshev pilot."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';names=['gamma_floor_L064_rank1000_midpoint.npz','gamma_floor_L0640381_rank1000_midpoint.npz','gamma_floor_L0641464_rank1000_midpoint.npz','gamma_floor_L0643087_rank1000_midpoint.npz','gamma_floor_L0645_rank1000_midpoint.npz','gamma_floor_L0646913_rank1000_midpoint.npz','gamma_floor_L0648536_rank1000_midpoint.npz','gamma_floor_L0649619_rank1000_midpoint.npz','gamma_floor_L065_rank1000_midpoint.npz'];old=np.load(root/'chebyshev_dangerous_block_L064_L065.npz');V=old['basis'];B=np.array([V.T@np.load(root/n)['matrix']@V for n in names]);t=np.cos(np.arange(8,-1,-1)*np.pi/8);c8=np.polynomial.chebyshev.chebfit(t,B.reshape(9,-1),8).reshape(9,20,20);c4=old['coefficients'];grid=np.linspace(-1,1,801);mins=[];diff=[]
for x in grid:
 M8=np.polynomial.chebyshev.chebval(x,c8);M4=np.polynomial.chebyshev.chebval(x,c4);M8=(M8+M8.T)/2;mins.append(np.linalg.eigvalsh(M8)[0]);diff.append(np.linalg.norm(M8-M4,2))
tail=sum(np.linalg.norm(c8[k],2) for k in range(5,9));out={'schema':'marici.voevodsky.chebyshev-dangerous-block-L064-L065-degree8.v1','degree':8,'packet_dimension':20,'dense_polynomial_min':float(min(mins)),'dense_min_L':float(.645+.005*grid[int(np.argmin(mins))]),'degree8_coefficient_norms':[float(np.linalg.norm(x,2)) for x in c8],'sum_degree5_to8_coefficient_norms':float(tail),'max_degree8_minus_degree4_spectral':float(max(diff)),'positive_after_empirical_refinement_difference':float(min(mins)-max(diff))>0,'status':'floating nested refinement; analytic remainder and packet leakage not enclosed','passed':float(min(mins))>0,'rh_proved':False};p=root/'chebyshev_dangerous_block_L064_L065_degree8.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'chebyshev_dangerous_block_L064_L065_degree8.npz',coefficients=c8,basis=V);print(json.dumps(out,indent=2));assert out['passed']

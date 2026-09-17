#!/usr/bin/env python3
"""Chebyshev coefficient decay of regularized union tail maps and Schur matrices."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');D=d['tail_maps'];S=d['schur'];t=np.cos(np.arange(8,-1,-1)*np.pi/8);cD=np.polynomial.chebyshev.chebfit(t,D.reshape(9,-1),8).reshape(9,1000,40);cS=np.polynomial.chebyshev.chebfit(t,S.reshape(9,-1),8).reshape(9,40,40);dn=[float(np.linalg.norm(x,2)) for x in cD];sn=[float(np.linalg.norm(x,2)) for x in cS];out={'schema':'marici.voevodsky.regularized-tail-map-chebyshev-L0649-L065.v1','tail_map_coefficient_norms':dn,'schur_coefficient_norms':sn,'tail_map_high_degree_sum_5_to8':sum(dn[5:]),'schur_high_degree_sum_5_to8':sum(sn[5:]),'endpoint_schur_min':float(np.linalg.eigvalsh(S[-1])[0]),'status':'floating coefficient-decay scout','passed':sum(dn[5:])<1e-4 and sum(sn[5:])<1e-10,'rh_proved':False};p=root/'regularized_tail_map_chebyshev_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');np.savez(root/'regularized_tail_map_chebyshev_L0649_L065.npz',tail_map_coefficients=cD,schur_coefficients=cS);print(json.dumps(out,indent=2))

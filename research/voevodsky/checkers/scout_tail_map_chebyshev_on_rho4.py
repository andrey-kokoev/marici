#!/usr/bin/env python3
"""Evaluate the degree-8 tail-map interpolant on the rho=5 ellipse."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';c=np.load(root/'regularized_tail_map_chebyshev_L0649_L065.npz')['tail_map_coefficients'];rho=4.;rows=[]
for theta in np.linspace(0,2*np.pi,257)[:-1]:
 z=.5*(rho*np.exp(1j*theta)+rho**-1*np.exp(-1j*theta));Y=np.polynomial.chebyshev.chebval(z,c);rows.append(float(np.linalg.norm(Y,2)))
mx=max(rows);out={'schema':'marici.voevodsky.tail-map-chebyshev-rho4-scout.v1','rho':rho,'samples':len(rows),'maximum_interpolant_norm':mx,'target_true_tail_map_norm':1.0,'interpolant_below_target':mx<1.0,'status':'floating interpolant only; true analytic tail-map remainder is not bounded','passed':mx<1.0,'rh_proved':False};p=root/'tail_map_chebyshev_rho4_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

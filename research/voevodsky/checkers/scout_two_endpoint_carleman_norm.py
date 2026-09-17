#!/usr/bin/env python3
"""Nyström scout for the direct two-endpoint Carleman image kernel."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
from numpy.polynomial.legendre import leggauss
rows=[]
for n in (100,200,400,800):
 z,w=leggauss(n);x=(z+1)/2;w=w/2;X=x[:,None];K=1/(X+X.T)+1/(2-X-X.T);A=np.sqrt(w)[:,None]*K*np.sqrt(w)[None,:];ev=np.linalg.eigvalsh(A);rows.append({'nodes':n,'largest_eigenvalue':float(ev[-1]),'ratio_to_pi':float(ev[-1]/np.pi),'second_largest':float(ev[-2])})
out={'schema':'marici.voevodsky.two-endpoint-carleman-norm-scout.v1','kernel':'1/(x+y)+1/(2-x-y) on (0,1)','rows':rows,'interpretation':'The direct sum norm exceeds pi in finite sections and converges slowly; pi/2 per endpoint cannot simply be replaced by one shared pi/2 budget.','status':'floating scout only','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'two_endpoint_carleman_norm_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

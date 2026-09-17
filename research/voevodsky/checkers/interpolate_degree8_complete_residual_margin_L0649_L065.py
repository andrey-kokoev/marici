#!/usr/bin/env python3
"""Degree-8 Lobatto interpolation of complete-continuum lower margins."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';tags=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];vals=np.array([json.loads((root/f'physical_regularized_residual_gram_{x}_refined_scout.json').read_text())['a_posteriori_lower_form_min'] for x in tags]);t=np.cos(np.arange(8,-1,-1)*np.pi/8);coef=np.polynomial.chebyshev.chebfit(t,vals,8);grid=np.linspace(-1,1,4001);y=np.polynomial.chebyshev.chebval(grid,coef);out={'schema':'marici.voevodsky.degree8-complete-residual-margin-L0649-L065.v1','node_margins':[float(x) for x in vals],'coefficients':[float(x) for x in coef],'degree4_to_8_tail_l1':float(sum(abs(coef[5:]))),'last_coefficient_absolute':float(abs(coef[-1])),'dense_min':float(min(y)),'dense_min_L':float(.6495+.0005*grid[int(np.argmin(y))]),'passed':float(min(y))>0,'status':'floating scalar margin interpolation; eigenvalue analyticity and directed matrix enclosure open','rh_proved':False};p=root/'degree8_complete_residual_margin_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

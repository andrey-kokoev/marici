#!/usr/bin/env python3
"""Degree-4 Chebyshev interpolation of complete-continuum lower margins."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complete_residual_margin_across_L0649_L065.json').read_text());vals=np.array([x['lower_margin'] for x in d['rows']]);t=np.cos(np.arange(4,-1,-1)*np.pi/4);coef=np.polynomial.chebyshev.chebfit(t,vals,4);grid=np.linspace(-1,1,2001);y=np.polynomial.chebyshev.chebval(grid,coef);out={'schema':'marici.voevodsky.complete-residual-margin-chebyshev-L0649-L065.v1','coefficients':[float(x) for x in coef],'highest_coefficient_absolute':float(abs(coef[-1])),'last_two_absolute_sum':float(sum(abs(coef[-2:]))),'dense_min':float(min(y)),'dense_min_L':float(.6495+.0005*grid[int(np.argmin(y))]),'passed':float(min(y))>0,'status':'floating scalar-margin interpolation; matrix-valued directed continuation still required','rh_proved':False};p=root/'complete_residual_margin_chebyshev_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

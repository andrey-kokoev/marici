#!/usr/bin/env python3
"""Argument-principle scout for all recursive strong-block LDL pivots."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complex_schur_ellipse_L0649_L065_rho10_scout64.json').read_text());r=d['samples'];rows=[]
for k in range(18):
 z=np.array([complex(x['strong_ldl_pivot_real'][k],x['strong_ldl_pivot_imag'][k]) for x in r]);ph=np.unwrap(np.angle(np.r_[z,z[0]]));rows.append({'pivot':k,'minimum_sampled_abs':float(min(abs(z))),'winding':float((ph[-1]-ph[0])/(2*np.pi)),'maximum_phase_increment':float(max(abs(np.diff(ph))))})
out={'schema':'marici.voevodsky.rho10-recursive-ldl-pivot-windings.v1','rows':rows,'all_zero_winding':all(abs(x['winding'])<1e-12 for x in rows),'all_phase_increments_below_pi':all(x['maximum_phase_increment']<np.pi for x in rows),'passed':all(abs(x['winding'])<1e-12 and x['maximum_phase_increment']<np.pi for x in rows),'rh_proved':False};p=root/'rho10_recursive_ldl_pivot_windings.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

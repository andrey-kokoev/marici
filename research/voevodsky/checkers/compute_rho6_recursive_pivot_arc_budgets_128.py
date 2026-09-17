#!/usr/bin/env python3
"""Arc-cover budgets for reverse-ordered strong LDL pivots and robust scalar Schur."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=json.loads((root/'complex_schur_ellipse_L0649_L065_rho6_scout128.json').read_text());r=d['samples'];z=np.array([complex(x['L_real'],x['L_imag']) for x in r]);half=max(abs(z[(i+1)%len(z)]-z[i]) for i in range(len(z)))/2
def budget(vals,factor):
 der=max(abs((vals[(i+1)%len(vals)]-vals[i])/(z[(i+1)%len(z)]-z[i])) for i in range(len(z)));mn=min(abs(vals));var=factor*der*half;return {'minimum_sampled_abs':float(mn),'maximum_secant_derivative':float(der),'derivative_safety_factor':factor,'arc_variation_budget':float(var),'remaining_modulus':float(mn-var),'passes':bool(var<mn)}
piv=[]
for k in range(18):piv.append(budget(np.array([complex(x['strong_ldl_pivot_real'][k],x['strong_ldl_pivot_imag'][k]) for x in r]),4.0))
s=np.array([complex(x['robust_scalar_schur_real'],x['robust_scalar_schur_imag']) for x in r]);sb=budget(s,1.2);out={'schema':'marici.voevodsky.rho6-recursive-pivot-arc-budgets-128.v1','half_chord':float(half),'strong_pivots':piv,'robust_scalar_schur':sb,'all_conditional_arc_covers_pass':all(x['passes'] for x in piv) and sb['passes'],'conditions':'directed derivative bounds at the stated multiples of sampled secant bounds','passed':False,'rh_proved':False};p=root/'rho6_recursive_pivot_arc_budgets_128.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'half_chord':half,'minimum_strong_remaining':min(x['remaining_modulus'] for x in piv),'failed_strong_pivots':[i for i,x in enumerate(piv) if not x['passes']],'robust_scalar':sb,'all_conditional_arc_covers_pass':out['all_conditional_arc_covers_pass']},indent=2))

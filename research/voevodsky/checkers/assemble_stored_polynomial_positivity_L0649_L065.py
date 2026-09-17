#!/usr/bin/env python3
"""Assemble low-line inclusions and bulk min-max bound for stored polynomial."""
import json,sys,math
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';files=['corrected_moving_frame_polynomial_L0649_L065.npz','second_moving_line_corrected_L0649_L065.npz','third_moving_line_corrected_L0649_L065.npz'];mins=[1.9142969348170045e-11,6.690350306705608e-9,1.7538271572538422e-6];rows=[]
for f,mn in zip(files,mins):
 d=np.load(root/f);c=d['eigenvalue'];r=sum(np.linalg.norm(x) for x in d['residual']);nd=d['normalization_defect'];delta=sum(abs(nd)) if np.ndim(nd) else 1.8e-14;err=r/math.sqrt(1-delta);mx=float(c[0]+sum(abs(c[1:])));rows.append({'file':f,'branch_lower':mn,'branch_upper_triangle':mx,'residual_inclusion_radius':float(err),'eigenvalue_interval_lower':float(mn-err),'eigenvalue_interval_upper':float(mx+err)})
bulk=json.loads((root/'fourth_eigenvalue_directed_roundoff_L0649_L065.json').read_text())['global_fourth_eigenvalue_lower'];disjoint=rows[0]['eigenvalue_interval_upper']<rows[1]['eigenvalue_interval_lower'] and rows[1]['eigenvalue_interval_upper']<rows[2]['eigenvalue_interval_lower'] and rows[2]['eigenvalue_interval_upper']<bulk;lower=min(x['eigenvalue_interval_lower'] for x in rows);out={'schema':'marici.voevodsky.stored-polynomial-positivity-assembly-L0649-L065.v1','low_lines':rows,'bulk_fourth_eigenvalue_lower':bulk,'low_inclusion_intervals_disjoint_and_below_bulk':disjoint,'stored_polynomial_minimum_lower':lower,'theorem':'lambda_4 bulk bound gives at most three eigenvalues below bulk floor; three disjoint residual inclusion intervals each contain an eigenvalue, hence these are the three low eigenvalues and all are positive','passed_stored_polynomial':bool(disjoint and lower>0),'source_matrix_enclosed':False,'passed':False,'rh_proved':False};p=root/'stored_polynomial_positivity_assembly_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stored_polynomial']

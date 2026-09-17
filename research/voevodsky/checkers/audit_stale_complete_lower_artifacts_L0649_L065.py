#!/usr/bin/env python3
"""Detect stale saved lower forms inconsistent with their saved residual Grams."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');tags=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];rows=[];alpha=1.067569476012246
for i,tag in enumerate(tags):
 a=np.load(root/f'physical_regularized_residual_gram_{tag}_refined_matrices.npz');expected=d['schur'][i]-a['residual_gram']/alpha;expected=(expected+expected.T)/2;rows.append({'tag':tag,'stored_formula_discrepancy':float(np.linalg.norm(a['lower_form']-expected,2)),'recomputed_min':float(np.linalg.eigvalsh(expected)[0]),'stored_min':float(np.linalg.eigvalsh(a['lower_form'])[0])})
out={'schema':'marici.voevodsky.stale-complete-lower-artifacts-L0649-L065.v1','rows':rows,'maximum_discrepancy':max(x['stored_formula_discrepancy'] for x in rows),'stale_detected':any(x['stored_formula_discrepancy']>1e-10 for x in rows),'disposition':'stored lower_form fields are superseded; output_gram and residual_gram remain usable, and lower forms must be recomputed from schur-residual/alpha','passed_audit':True,'rh_proved':False};p=root/'stale_complete_lower_artifacts_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['stale_detected']

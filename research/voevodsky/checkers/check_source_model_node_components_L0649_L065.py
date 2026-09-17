#!/usr/bin/env python3
"""Range-compatible source/model discrepancies at the nine Lobatto source nodes."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';tags=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];C=np.load(root/'degree8_complete_lower_matrix_L0649_L065.npz')['coefficients'];P=np.load(root/'moving_frame_polynomial_L0649_L065.npz')['frame'];t=np.cos(np.arange(8,-1,-1)*np.pi/8);contract=json.loads((root/'source_to_moving_bundle_error_contract_L0649_L065.json').read_text());lim=contract['required_source_error_components'];rows=[]
for x,tag in zip(t,tags):
 H=np.load(root/f'physical_regularized_residual_gram_{tag}_refined_matrices.npz')['lower_form'];M=np.polynomial.chebyshev.chebval(x,C);p=np.polynomial.chebyshev.chebval(x,P);p=p/np.linalg.norm(p);E=(H-M);E=(E+E.T)/2;cross=E@p-p*(p@E@p);rob=np.linalg.norm((np.eye(40)-np.outer(p,p))@E@(np.eye(40)-np.outer(p,p)),2);rows.append({'tag':tag,'critical':abs(float(p@E@p)),'cross':float(np.linalg.norm(cross)),'robust':float(rob)})
mx={k:max(r[k] for r in rows) for k in ('critical','cross','robust')};out={'schema':'marici.voevodsky.source-model-node-components-L0649-L065.v1','rows':rows,'maxima':mx,'target_ratios':{'critical':mx['critical']/lim['critical_diagonal_max'],'cross':mx['cross']/lim['critical_robust_cross_max'],'robust':mx['robust']/lim['robust_block_max']},'all_nodes_within_targets':mx['critical']<lim['critical_diagonal_max'] and mx['cross']<lim['critical_robust_cross_max'] and mx['robust']<lim['robust_block_max'],'passed':False,'reason_not_certificate':'interpolation nodes only and floating source assembly; between-node directed remainder open','rh_proved':False};p=root/'source_model_node_components_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['all_nodes_within_targets']

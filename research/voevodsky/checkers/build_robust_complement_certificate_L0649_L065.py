#!/usr/bin/env python3
"""Range-compatible robust-complement budget for the [.649,.65] slab."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma
root=Path(__file__).parents[1]/'results';tags=['L0649','L0649038','L0649146','L0649309','L06495','L0649691','L0649854','L0649962','L065'];floors=[]
for x in tags:
 M=np.load(root/f'physical_regularized_residual_gram_{x}_refined_matrices.npz')['lower_form'];floors.append(float(np.linalg.eigvalsh((M+M.T)/2)[1]))
mov=json.loads((root/'moving_critical_line_complete_lower_L0649_L065.json').read_text());rnd=json.loads((root/'L06495_critical_robust_cross_roundoff_budget.json').read_text());src=json.loads((root/'source_matrix_refinement_range_components_L06495.json').read_text());# Recompute all 39 per-column bounds and use their Frobenius norm, rather than sqrt(39) times the worst column.
d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];md=np.load(root/'physical_regularized_residual_gram_L06495_refined2_matrices.npz');_,V=np.linalg.eigh((md['lower_form']+md['lower_form'].T)/2);Vr=V[:,1:];n=np.arange(1000);L=.6495;sc=np.sqrt((2*n+1)/(2*L));l1=np.sum(abs((Z@Vr)*sc[:,None]),axis=0);u=2**-53
def gamma(k):return k*u/(1-k*u)
qR=(digamma(.25+125j).real-math.log(math.pi))/2;prime=sum(math.log(p)/math.sqrt(p) for p in (2,3))/2;special=4096*u;column_errors=np.sqrt(2*L)*((abs(qR)+prime)*(gamma(6000)+special)*l1+(gamma(24000)+special)*10);robust_operator_error=float(np.linalg.norm(column_errors));roundoff=2*rnd['robust_output_operator_norm']*robust_operator_error+robust_operator_error**2;source=4*src['trial_robust_component'];interp=mov['robust_branch_tail_degree9_32_l1'];total=roundoff+source+interp;base=min(floors+[mov['minimum_robust_branch']]);lower=base-total;out={'schema':'marici.voevodsky.robust-complement-certificate-L0649-L065.v1','node_robust_floors':floors,'polynomial_dense_robust_floor':mov['minimum_robust_branch'],'base_floor':base,'modeled_errors':{'binary64_robust_column_error_range':[float(min(column_errors)),float(max(column_errors))],'binary64_robust_output_operator_error':robust_operator_error,'binary64_output_gram':roundoff,'source_assembly_4x_refinement':source,'moving_branch_interpolation_tail':interp},'total_modeled_error':total,'conditional_directed_lower':lower,'passed_conditionally':lower>0,'passed':False,'unclosed_conditions':['replace forward-error model by implementation-level directed arithmetic','directed complex-ellipse bound beyond the interpolating polynomial','repeat on every slab'],'rh_proved':False};p=root/'robust_complement_certificate_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

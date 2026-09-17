#!/usr/bin/env python3
"""Forward-error budget for physical Clenshaw evaluation and Gram accumulation."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,iv
root=Path(__file__).parents[1]/'results';Z=np.load(root/'two_prime_regularized_exact_span_midpoint.npz')['schur_vectors'];N=670;L=.55;k=np.arange(N);sc=np.sqrt((2*k+1)/(2*L));l1=float(np.max(np.sum(abs(Z*sc[:,None]),axis=0)));u=2**-53
def gamma(n):return n*u/(1-n*u)
clenshaw=gamma(6*N)*l1;qR=(digamma(.25+125j).real-math.log(math.pi))/2;prime=sum(math.log(p)/math.sqrt(p) for p in (2,3))/2;poly=(abs(qR)+prime)*clenshaw;x=L/2;ap=np.array([2*L*math.sqrt((2*n+1)/(2*L))*math.sqrt(math.pi/(2*x))*iv(n+.5,x) for n in k]);am=ap*((-1.)**k);dot_abs=max(float(np.max(np.sum(abs(ap[:,None]*Z),axis=0))),float(np.max(np.sum(abs(am[:,None]*Z),axis=0))));endpoint_dot=gamma(2*N)*dot_abs;endpoint=.5*(math.exp(L/2)+math.exp(L/2))*endpoint_dot+64*u*math.exp(L/2)*dot_abs;freq=json.loads((root/'residual_float_roundoff_budget.json').read_text())['pointwise_column_error'];point=poly+endpoint+freq;op=math.sqrt(2*L*92)*point;G=np.load(root/'physical_regularized_residual_gram_exact_span_matrices.npz')['output_gram'];an=math.sqrt(float(np.linalg.eigvalsh((G+G.T)/2)[-1]));output_pert=2*an*op+op*op;# Weighted Gram dot accumulation: sum absolute products <= output norm product; inflate by dimension for spectral norm.
gram_accum=92*gamma(2*4500)*(an+op)**2;total=output_pert+gram_accum;allow=json.loads((root/'exact_span_lower_form_error_budget.json').read_text())['allowable_residual_gram_operator_error_after_A_budget'];out={'schema':'marici.voevodsky.residual-physical-roundoff-budget.v1','maximum_scaled_coefficient_l1':l1,'clenshaw_gamma':gamma(6*N),'clenshaw_point_error':clenshaw,'polynomial_output_point_error':poly,'endpoint_point_error':endpoint,'frequency_point_error_included':freq,'total_pointwise_column_error':point,'output_operator_error':op,'output_gram_perturbation':output_pert,'gram_accumulation_error':gram_accum,'total_physical_roundoff_operator_error':total,'allowable_operator_error':allow,'reserve_factor':allow/total,'scope':'conditional on conservative six-rounding-per-degree Clenshaw model and 64-ulp elementary/special-function reserve','passed':bool(total<allow),'rh_proved':False};p=root/'residual_physical_roundoff_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

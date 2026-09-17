#!/usr/bin/env python3
"""Binary64 forward-error budget specialized to the refined critical direction."""
import json,math,sys
from pathlib import Path
try:
 import numpy as np
 from scipy.special import digamma,iv
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from scipy.special import digamma,iv
root=Path(__file__).parents[1]/'results';d=np.load(root/'regularized_union_tail_maps_L0649_L065.npz');Z=d['packet']-d['tail_maps'][4];md=np.load(root/'physical_regularized_residual_gram_L06495_refined2_matrices.npz');M=md['lower_form'];ev,V=np.linalg.eigh((M+M.T)/2);c=V[:,0];w=Z@c;L=.6495;N=1000;n=np.arange(N);sc=np.sqrt((2*n+1)/(2*L));l1=float(np.sum(abs(w*sc)));u=2**-53
def gamma(k):return k*u/(1-k*u)
cl=gamma(6*N)*l1;qR=(digamma(.25+125j).real-math.log(math.pi))/2;prime=sum(math.log(p)/math.sqrt(p) for p in (2,3))/2;point=(abs(qR)+prime)*cl;# Include frequency synthesis accumulation using prior 24000-operation scale and a broad absolute coefficient sum 10.
point+=gamma(24000)*10;op=math.sqrt(2*L)*point;output_norm=float(math.sqrt(max(0,c@md['output_gram']@c)));gram=2*output_norm*op+op*op;out={'schema':'marici.voevodsky.L06495-critical-roundoff-budget.v1','critical_margin':float(ev[0]),'critical_scaled_coefficient_l1':l1,'clenshaw_error':cl,'pointwise_error_budget':point,'L2_output_error_budget':op,'critical_output_norm':output_norm,'critical_gram_error_budget':gram,'budget_to_margin_ratio':gram/float(ev[0]),'passed':bool(gram<float(ev[0])),'scope':'conservative binary64 model; special-function directed values not included','rh_proved':False};p=root/'L06495_critical_roundoff_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

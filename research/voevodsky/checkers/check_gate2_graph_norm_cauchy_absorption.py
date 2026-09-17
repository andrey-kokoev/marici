#!/usr/bin/env python3
"""Graph-norm absorption budget for the Gate-2 source interpolation error."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree16_regularized_tail_map_L0649_L065.npz')['coefficients'];rho=2.;dm=0
for j in range(4096):
 th=2*math.pi*j/4096;z=(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th))/2;dm=max(dm,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,C),2)))
graph=1+dm*dm;raw=json.loads((root/'gate2_raw_source_operator_E2_budget.json').read_text());base=6.690324900504932e-9;operr=raw['conditional_interpolation_error'];formerr=graph*operr;lower=base-formerr;out={'schema':'marici.voevodsky.gate2-graph-norm-cauchy-absorption.v1','sampled_E2_tail_map_norm':dm,'graph_metric_upper_factor':graph,'raw_operator_interpolation_error':operr,'schur_coordinate_form_error':formerr,'stored_robust_lower':base,'conditional_true_source_robust_lower':lower,'theorem':'For Z=P-QD with orthogonal P,Q, Z*Z=I+D*D. Hence |Z* DeltaA Z| <= ||DeltaA|| (1+||D||^2) I. Weyl subtraction from the stored Schur robust floor gives the reported lower bound.','passed_conditionally':lower>0,'passed':False,'conditions':['directed E2 tail-map norm','directed raw-source analytic majorant','Cauchy interpolation error applies to the fixed ambient source operator family'],'rh_proved':False};p=root/'gate2_graph_norm_cauchy_absorption.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']

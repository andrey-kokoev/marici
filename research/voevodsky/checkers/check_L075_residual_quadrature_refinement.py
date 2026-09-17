#!/usr/bin/env python3
"""Q400/Q500 convergence of the degree-149 critical residual vector."""
import json,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:,-1];w=v.copy();w[150:]=0;A=np.load(root/'gamma_floor_L075_prime4_Q400_decomposition.npz')['total'];B=np.load(root/'gamma_floor_L075_prime4_Q500_decomposition.npz')['total'];rA=A@w;rA[:150]=0;rB=B@w;rB[:150]=0;diff=rB-rA;na=float(np.linalg.norm(rA));nb=float(np.linalg.norm(rB));nd=float(np.linalg.norm(diff));target=8.012133660773966e-9;out={'schema':'marici.voevodsky.L075-residual-quadrature-refinement.v1','Q400_residual_norm':na,'Q500_residual_norm':nb,'residual_vector_difference_norm':nd,'difference_to_target_reserve_ratio':nd/(target-nb),'Q500_plus_4x_difference':nb+4*nd,'target_upper':target,'passed_conditionally':nb+4*nd<target,'passed':False,'reason_not_directed':'two floating refinements do not enclose quadrature and rounding error','rh_proved':False};p=root/'L075_residual_quadrature_refinement.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']

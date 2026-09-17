#!/usr/bin/env python3
"""Cauchy budget specialized to the robust (second-eigenvalue) gap."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree32_complete_lower_L0649_L065.npz')['coefficients'];rho=2.;mx=0
for j in range(2048):
 th=2*math.pi*j/2048;z=(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th))/2;mx=max(mx,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,C),2)))
factor=4*rho**-33/(1-rho**-1);robust=6.690324900504932e-9;allocation=.9*robust;Mmax=allocation/factor;out={'schema':'marici.voevodsky.gate2-robust-source-cauchy-budget-L0649-L065.v1','rho':rho,'robust_polynomial_lower':robust,'allocated_source_interpolation_error':allocation,'safe_interpolation_tail_factor':factor,'maximum_admissible_full_source_ellipse_norm':Mmax,'sampled_degree32_ellipse_norm':mx,'sampled_reserve_factor':Mmax/mx,'conditional_robust_lower':robust-allocation,'passed_scout':mx<Mmax,'passed':False,'required_proof':'directed full-source norm bound on E2 below admissible maximum; unlike Gate 3 no cancellation against P16 is needed','rh_proved':False};p=root/'gate2_robust_source_cauchy_budget_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']

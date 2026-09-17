#!/usr/bin/env python3
"""Use E2.1 full residual-Gram norm instead of a shifted E2 cancellation bound."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';rho=2.1;factor=4*rho**-33/(1-rho**-1);critical=json.loads((root/'stored_polynomial_positivity_assembly_L0649_L065.json').read_text())['stored_polynomial_minimum_lower'];allocation=.9*critical;alpha=1.067569476012246;Mmax=allocation*alpha/factor;C=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'];mx=0
for j in range(2048):
 th=2*math.pi*j/2048;z=(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th))/2;mx=max(mx,float(np.linalg.norm(np.polynomial.chebyshev.chebval(z,C),2)))
out={'schema':'marici.voevodsky.gate3-residual-gram-E21-budget.v1','rho':rho,'safe_tail_factor':factor,'critical_error_allocation':allocation,'maximum_admissible_full_residual_gram_norm':Mmax,'sampled_degree32_residual_gram_norm':mx,'sampled_reserve_factor':Mmax/mx,'conditional_residual_tail':factor*Mmax/alpha,'remaining_critical_margin':critical-allocation,'passed_scout':mx<Mmax,'passed':False,'conditions':['holomorphic residual-Gram family through E2.1','directed full residual-Gram norm below admissible maximum','tail-map denominator zero-free through E2.1'],'rh_proved':False};p=root/'gate3_residual_gram_E21_budget.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']

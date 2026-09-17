#!/usr/bin/env python3
"""Complex-ellipse scout for H_32-H_16 and shifted Cauchy enclosure budget."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C16=np.load(root/'corrected_degree16_complete_lower_L0649_L065.npz')['coefficients'];C32=np.load(root/'degree32_complete_lower_L0649_L065.npz')['coefficients'];rho=2.;mx=0.;arg=0
for j in range(2048):
 th=2*math.pi*j/2048;z=(rho*np.exp(1j*th)+rho**-1*np.exp(-1j*th))/2;D=np.polynomial.chebyshev.chebval(z,C32)-np.polynomial.chebyshev.chebval(z,C16);q=float(np.linalg.norm(D,2))
 if q>mx:mx=q;arg=th
# For analytic R=H-P16 with ||R||<=M on E_rho, coefficients above 32
# are bounded by 2M rho^-k. Interpolation aliasing is safely charged twice.
factor=4*rho**-33/(1-rho**-1);target=5.00066667380444e-12;Mmax=target/factor;out={'schema':'marici.voevodsky.shifted-cauchy-remainder-scout-L0649-L065.v1','rho':rho,'sample_count':2048,'sampled_max_norm_H32_minus_H16':mx,'maximizing_theta':arg,'directed_source_error_target':target,'safe_interpolation_tail_factor':factor,'maximum_admissible_supremum_H_minus_P16':Mmax,'observed_to_admissible_ratio':mx/Mmax,'passed_scout':mx<Mmax/100,'passed':False,'required_proof':'directed bound ||H-P16|| on E_2 below the admissible supremum; sampled H32-P16 is not such a bound','rh_proved':False};p=root/'shifted_cauchy_remainder_scout_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_scout']

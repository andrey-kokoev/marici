#!/usr/bin/env python3
"""Conservative analytic E2.1 majorant for the finite rank-1000 gamma-floor source."""
import json,math
from pathlib import Path
rho=2.1;half=.0005;eta=half*(rho-rho**-1)/2;Lmin=.6495-half*(rho+rho**-1)/2;U=250.;N=1000;qR=1.841791592392184;mmax=4.527883302005017
# Complex Fourier rows acquire at most exp(U eta); use this twice in V^T m V.
gamma=qR+mmax*math.exp(2*U*eta)
# Conservative degree-N complex scaling deformation for each real translation contraction.
prime_real=math.log(2)/math.sqrt(2)+math.log(3)/math.sqrt(3);prime_factor=math.exp(2*(N-1)*eta/Lmin);prime=prime_real*prime_factor
# Entire endpoint moments have tiny deformation here; charge a deliberately coarse factor two.
endpoint=2*1.394;M=gamma+prime+endpoint;factor=4*rho**-33/(1-rho**-1)
# Real-slab graph map only: coefficient triangle on [-1,1].
import sys
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree16_regularized_tail_map_L0649_L065.npz')['coefficients'];dn=sum(float(np.linalg.norm(x,2)) for x in C);graph=1+dn*dn;base=6.690324900504932e-9;err=factor*M*graph;lower=base-err
out={'schema':'marici.voevodsky.gate2-raw-source-E21-majorant.v1','rho':rho,'imaginary_L_radius':eta,'minimum_real_L':Lmin,'gamma_majorant':gamma,'prime_complex_deformation_factor':prime_factor,'prime_majorant':prime,'endpoint_majorant':endpoint,'raw_source_majorant':M,'safe_interpolation_factor':factor,'real_tail_map_triangle_norm':dn,'graph_factor':graph,'source_form_error':err,'true_source_robust_lower':lower,'passed':lower>0,'scope':'finite rank-1000 gamma-floor source; uses elementary complex growth majorants before Cauchy interpolation','rh_proved':False};p=root/'gate2_raw_source_E21_majorant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

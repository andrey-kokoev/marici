#!/usr/bin/env python3
"""Coefficient-triangle norm of residual-Gram polynomial on theta-disk annulus."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'degree32_residual_gram_family_L0649_L065.npz')['coefficients'];rho=2.1*math.exp(.15);u=2**-53;gam=4000*u/(1-4000*u);rows=[];total=0
for k,A in enumerate(C):
 n=float(np.nextafter(np.linalg.norm(A,2)+gam*np.linalg.norm(A,'fro'),np.inf));w=(rho**k+rho**-k)/2;total+=n*w;rows.append({'degree':k,'norm_upper':n,'weight':w,'contribution':n*w})
out={'schema':'marici.voevodsky.gate3-residual-polynomial-annulus-norm.v1','outer_rho':rho,'rows':rows,'coefficient_triangle_norm':total,'full_annulus_target':1.0,'reserve':1-total,'passed_stored_polynomial':total<1,'passed':False,'remaining':'true physical-integral minus degree32 residual polynomial bound on annulus','rh_proved':False};p=root/'gate3_residual_polynomial_annulus_norm.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stored_polynomial']

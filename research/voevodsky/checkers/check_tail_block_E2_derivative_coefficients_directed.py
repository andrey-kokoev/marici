#!/usr/bin/env python3
"""Residual-checked spectral upper bounds for stored tail-block coefficients."""
import json,math,sys
from pathlib import Path
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
root=Path(__file__).parents[1]/'results';C=np.load(root/'tail_block_degree16_polynomial_L0649_L065.npz')['coefficients'];u=2**-53;gam=2000*u/(1-2000*u);rows=[]
for k,A in enumerate(C):
 A=(A+A.T)/2;e,V=np.linalg.eigh(A);orth=np.linalg.norm(V.T@V-np.eye(960),'fro');rec=np.linalg.norm(A-(V*e)@V.T,'fro');upper=max(abs(e))*max(1,1+orth)+rec+gam*np.linalg.norm(A,'fro');rows.append({'degree':k,'floating_spectral':float(max(abs(e))),'orthogonality_defect':float(orth),'reconstruction_error':float(rec),'directed_style_upper':float(np.nextafter(upper,np.inf))})
rho=2.;den=rho-rho**-1;dz=sum(x['directed_style_upper']*x['degree']*(rho**x['degree']-rho**(-x['degree']))/den for x in rows[1:]);dtheta=dz*(rho+rho**-1)/2;var=dtheta*math.pi/46;node=json.loads((root/'tail_block_E2_46_cover.json').read_text())['minimum_directed_style_node_lower'];out={'schema':'marici.voevodsky.tail-block-E2-derivative-coefficients-directed.v1','arithmetic_model':'binary64 residual reconstruction with gamma_n inflation and outward nextafter','rows':rows,'directed_style_dC_dz_upper':dz,'directed_style_dC_dtheta_upper':dtheta,'half_arc_variation':var,'node_singular_lower':node,'covered_singular_lower':node-var,'passed_stored_polynomial':bool(node>var),'passed':False,'remaining':'true-source coefficient/remainder enclosure','rh_proved':False};p=root/'tail_block_E2_derivative_coefficients_directed.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_stored_polynomial']

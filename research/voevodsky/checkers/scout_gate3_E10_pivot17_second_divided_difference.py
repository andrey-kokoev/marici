#!/usr/bin/env python3
"""Second-divided-difference targets for a direct E10 derivative enclosure."""
import json
from pathlib import Path
root=Path(__file__).parents[1]/'results';a=json.loads((root/'complex_schur_ellipse_L0649_L065_rho10_scout64.json').read_text());b=json.loads((root/'complex_schur_ellipse_L0649_L065_rho10_scout128odd.json').read_text());r=sorted(a['samples']+b['samples'],key=lambda x:x['theta']);z=[complex(x['L_real'],x['L_imag']) for x in r];f=[complex(x['strong_ldl_pivot_real'][17],x['strong_ldl_pivot_imag'][17]) for x in r];n=len(r);sec=[(f[(i+1)%n]-f[i])/(z[(i+1)%n]-z[i]) for i in range(n)];# Difference of adjacent secants divided by midpoint separation estimates f''.
curv=[]
for i in range(n):
 m0=(z[i]+z[(i+1)%n])/2;m1=(z[(i+1)%n]+z[(i+2)%n])/2;curv.append(abs((sec[(i+1)%n]-sec[i])/(m1-m0)))
maxsec=max(abs(x) for x in sec);maxcurv=max(curv);chord=max(abs(z[(i+1)%n]-z[i]) for i in range(n));target_der=.04188;adopt_curv=4*maxcurv;covered=maxsec+adopt_curv*chord/2;out={'schema':'marici.voevodsky.gate3-E10-pivot17-second-divided-difference.v1','nodes':n,'maximum_secant_derivative':maxsec,'maximum_second_divided_difference':maxcurv,'adopted_second_derivative_target':adopt_curv,'maximum_chord':chord,'conditional_derivative_cover':covered,'required_derivative_bound':target_der,'passed_conditionally':covered<target_der,'passed':False,'remaining':'direct interval second-derivative bound at adopted target','rh_proved':False};p=root/'gate3_E10_pivot17_second_divided_difference.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_conditionally']

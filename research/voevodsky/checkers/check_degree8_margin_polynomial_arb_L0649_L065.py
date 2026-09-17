#!/usr/bin/env python3
"""Directed Arb positivity of the stored scalar degree-8 margin interpolant."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';d=json.loads((root/'degree8_complete_residual_margin_L0649_L065.json').read_text());c=[arb(repr(x)) for x in d['coefficients']]
def val(x,coef):
 b1=arb(0);b2=arb(0)
 for a in reversed(coef[1:]):b0=a+2*x*b1-b2;b2,b1=b1,b0
 return coef[0]+x*b1-b2
# derivative coefficients in Chebyshev basis, exact recurrence.
n=len(c)-1;dc=[arb(0)]*n
if n:dc[n-1]=2*n*c[n]
if n>1:dc[n-2]=2*(n-1)*c[n-1]
for k in range(n-3,-1,-1):dc[k]=dc[k+2]+2*(k+1)*c[k+1]
if n:dc[0]/=2
mins=[];dmins=[];N=4096
for j in range(N):
 lo=-1+2*j/N;hi=-1+2*(j+1)/N;x=arb(repr((lo+hi)/2),arb(repr((hi-lo)/2)));y=val(x,c);z=val(x,dc);mins.append(float(y.lower()));dmins.append(float(z.lower()))
out={'schema':'marici.voevodsky.degree8-margin-polynomial-arb-L0649-L065.v1','precision_bits':flint.ctx.prec,'interval_count':N,'minimum_interval_lower':min(mins),'minimum_derivative_interval_lower':min(dmins),'positive':min(mins)>0,'monotone_increasing':min(dmins)>0,'scope':'directed certificate for the stored scalar interpolating polynomial only; does not enclose matrix assembly or interpolation remainder','passed':min(mins)>0 and min(dmins)>0,'rh_proved':False};p=root/'degree8_margin_polynomial_arb_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

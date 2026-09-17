#!/usr/bin/env python3
"""Weighted second-variation scout for jump-subtracted prime residual output."""
import json,sys,math
from pathlib import Path
try:
 import numpy as np
 from numpy.polynomial.legendre import legval,legder
 from scipy.special import roots_legendre
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
 from numpy.polynomial.legendre import legval,legder
 from scipy.special import roots_legendre
root=Path(__file__).parents[1]/'results';v=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];v[1::2]=0;L=.75;n=np.arange(150);coef=v*np.sqrt((2*n+1)/(2*L));d1=legder(coef);d2=legder(d1);z,w=roots_legendre(400);ac=0.;dj=0.;rows=[]
for nn,lam in ((2,math.log(2)),(3,math.log(3)),(4,math.log(2))):
 a=math.log(nn);shift=a/L;c=lam/math.sqrt(nn)/2;# y intervals for w(y+shift) and w(y-shift)
 val=0.
 for lo,hi,sgn in [(-1,1-shift,shift),(-1+shift,1,-shift)]:
  yy=(lo+hi)/2+(hi-lo)*z/2;arg=yy+sgn;hpp=c*np.abs(legval(arg,d2));weight=(1-yy*yy)**(-.25);val+=(hi-lo)/2*np.dot(w,weight*hpp)
 jump=2*c*abs(legval(1,d1));ac+=val;dj+=jump;rows.append({'prime_power':nn,'weighted_absolute_second_derivative':float(val),'weighted_derivative_jumps':float(jump)})
total=ac+dj;tol=json.loads((root/'L075_second_variation_tolerance.json').read_text())['maximum_weighted_second_variation'];out={'schema':'marici.voevodsky.L075-prime-second-variation-scout.v1','rows':rows,'absolute_continuous_part':float(ac),'derivative_jump_part':float(dj),'prime_weighted_second_variation':float(total),'full_tolerance':tol,'prime_fraction_of_tolerance':total/tol,'passed_scout':bool(total<tol),'passed':False,'remaining':'absolute second-variation route fails; extract derivative-jump coefficients and use higher-order piecewise-polynomial cancellation instead','rh_proved':False};p=root/'L075_prime_second_variation_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

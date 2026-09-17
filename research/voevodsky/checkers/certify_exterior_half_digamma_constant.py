#!/usr/bin/env python3
"""Binet N=1 exterior bound for the half-normalized digamma deficit."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=256;u=arb(10);a=arb(1)/4;b=u/2;rho2=a*a+b*b
# For u>=10: each displayed positive majorant decreases. Bound |Re z^-2| by |z|^-2.
logratio=((1+u)/rho2.sqrt()).log();half_inv=a/(2*rho2);twelfth_abs=1/(12*rho2)
# N=1 vertical-line remainder: Gamma(4) zeta(4)/( (2pi)^4 a b |z|^2 ) = 1/(240 a b |z|^2).
rem=1/(240*a*b*rho2)
C=(logratio+arb.pi().log()+half_inv+twelfth_abs+rem)/2
out={'schema':'marici.voevodsky.exterior-half-digamma-constant.v1','exterior_frequency_floor':10,'terms':{'log_ratio_upper':str(logratio),'half_inverse_upper':str(half_inv),'twelfth_inverse_square_upper':str(twelfth_abs),'binet_remainder_upper':str(rem)},'certified_exterior_constant':str(C),'certified_exterior_upper':float(C.upper()),'monotonicity':'all positive majorants decrease for u>=10','passed':float(C.upper())<1.02,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'exterior_half_digamma_constant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

#!/usr/bin/env python3
"""Directed constants for the x>=60 Xi and Hilbert-kernel envelopes."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,acb
flint.ctx.prec=192;X=arb(60);t=acb.zeta_zero(1).imag
# Euler-Maclaurin with N=ceil(x): sum + pole + half term + periodic-B1 remainder
# is bounded by 4*sqrt(x+1) for x>=60.
zeta_constant=arb(4)
# First-term complex Stirling remainder: |R| <= 1/(12|z|cos(arg(z)/2)^2)
# <=1/(3x) for z=1/4+ix/2 and x>=60.
R=1/(arb(3)*X)
# Ratio after factoring x^(9/2) exp(-pi*x/2) from |xi|^2.
ratio=arb(8)*arb.pi().sqrt()*arb(2).sqrt()*(1+1/(arb(4)*X*X))**2*(1+1/X)*(arb(2)*R).exp()
# 2t/(x^2-t^2) <= K/x^2; ratio increases with t and decreases with x.
kernel_constant=2*t/(1-(t/X)**2)
out={'schema':'marici.voevodsky.evans-tail-envelope-constants.v1','precision_bits':flint.ctx.prec,'range_start':60,'zeta_bound':'|zeta(1/2+ix)| <= 4*sqrt(x+1)','stirling_remainder_bound_at_60':str(R),'xi_squared_constant_upper':str(ratio),'adopted_xi_squared_constant':25,'kernel_constant_upper':str(kernel_constant),'adopted_kernel_constant':31,'checks':{'xi_constant':bool(ratio<25),'kernel_constant':bool(kernel_constant<31)},'passed':bool(ratio<25 and kernel_constant<31),'rh_proved':False};p=Path(__file__).parents[1]/'results'/'evans_tail_envelope_constants.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

#!/usr/bin/env python3
"""Directed upper bound for .5[log(1+u)-Re psi(1/4+iu/2)+log pi]."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,acb
flint.ctx.prec=128;N=32768;U=arb(10);best=arb(0);arg=0
for k in range(N):
 u=arb(k*10/N,(10/N)/2);u+=arb(5/N) # cell midpoint +/- halfwidth
 q=((1+u).log()-acb(arb('.25'),u/2).digamma().real+arb.pi().log())/2
 if q.upper()>best.upper():best=q;arg=k
tail=((arb('2.2')).log()+arb('1.5')+arb.pi().log())/2
upper=max(float(best.upper()),float(tail.upper()));out={'schema':'marici.voevodsky.sharp-half-normalized-digamma-constant.v1','core':[0,10],'cells':N,'core_upper':float(best.upper()),'maximizing_cell':[arg*10/N,(arg+1)*10/N],'tail_upper_from_global_bound':float(tail.upper()),'certified_global_upper':upper,'passed':upper<2.695,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'sharp_half_normalized_digamma_constant.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

#!/usr/bin/env python3
"""Directed positivity of stored third eigenbranch polynomial."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
try: import numpy as np
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import numpy as np
flint.ctx.prec=256;root=Path(__file__).parents[1]/'results';cc=np.load(root/'third_moving_line_corrected_L0649_L065.npz')['eigenvalue'];c=[arb(repr(float(x))) for x in cc]
def val(x):
 b1=arb(0);b2=arb(0)
 for a in reversed(c[1:]):b0=a+2*x*b1-b2;b2,b1=b1,b0
 return c[0]+x*b1-b2
N=65536;low=arb('1e100')
for j in range(N):
 a=-1+2*j/N;b=-1+2*(j+1)/N;y=val(arb(repr((a+b)/2),arb(repr((b-a)/2))));
 if y.lower()<low:low=y.lower()
out={'schema':'marici.voevodsky.third-branch-polynomial-arb-L0649-L065.v1','interval_count':N,'minimum_interval_lower':str(low),'passed_polynomial':low>0,'passed':False,'source_remainder_open':True,'rh_proved':False};p=root/'third_branch_polynomial_arb_L0649_L065.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed_polynomial']

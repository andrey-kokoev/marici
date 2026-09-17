#!/usr/bin/env python3
"""Verify the normalized leading spherical-Bessel phases by parity."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
x=s.symbols('x',real=True);checks={}
for n in range(16):
 lead=s.expand_trig((-1)**(n//2)*s.sin(x-s.pi*n/2))
 target=s.sin(x) if n%2==0 else -s.cos(x)
 checks[str(n)]=s.simplify(lead-target)==0
assert all(checks.values())
out={'schema':'marici.voevodsky.legendre-gamma-tail-parity.v1','orders_checked':list(range(16)),'checks':checks,'conclusion':'all normalized even modes share leading sin phase and all normalized odd modes share leading minus-cos phase','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'legendre_gamma_tail_parity.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

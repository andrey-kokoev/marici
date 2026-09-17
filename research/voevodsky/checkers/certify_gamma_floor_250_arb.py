#!/usr/bin/env python3
"""Directed value of the monotone gamma floor at frequency 250."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb,acb
flint.ctx.prec=256;R=arb(250);q=(acb(arb(1)/4,R/2).digamma().real-arb.pi().log())/2
out={'schema':'marici.voevodsky.gamma-floor-250-arb.v1','precision_bits':flint.ctx.prec,'R':250,'q_R':str(q),'q_R_lower':float(q.lower()),'monotonicity_proof':'q prime = -Im trigamma(1/4+iu/2)/4 > 0 by the termwise trigamma series','operator_consequence':'Gamma_[R,infinity] >= q(R)(I-K_R)','passed':float(q.lower())>1.84,'rh_proved':False};p=Path(__file__).parents[1]/'results'/'gamma_floor_250_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

#!/usr/bin/env python3
"""Directed Arb certificate for the two-prime overlap-graph norm and threshold."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
flint.ctx.prec=256;L=arb('0.55');a=arb(2).log();b=arb(3).log();delta=b-a;u=a/(2*arb(2).sqrt());v=b/(2*arb(3).sqrt())
# Exact geometry inequalities with directed signs.
gaps={'a_minus_L':a-L,'b_minus_L':b-L,'translated_b_domain_left_gap':delta,'second_delta_exit_gap':(-L+2*delta)-(L-a)}
# The translated b-domain right endpoint equals L-a identically after delta=b-a.
geom=all(float(x.lower())>0 for x in gaps.values());norm=(u*u+v*v/2+v*(v*v+4*u*u).sqrt()/2).sqrt();cg=arb('2.6947343670010686');cb=arb.pi()/arb(3).sqrt()+arb(2).log()-arb(3)/8;C=cg+cb+norm
# Search with upper C; verify lower logarithmic reserve.
import math
Cu=float(C.upper());Lf=.55;M=math.floor((2*Lf/math.pi)*(math.exp(2*Cu)-1))+1;reserve=(arb(1)+arb.pi()*M/(2*L)).log()/2-C
out={'schema':'marici.voevodsky.exact-two-shift-prime-norm-arb.v1','precision_bits':flint.ctx.prec,'geometry_gaps':{k:str(x) for k,x in gaps.items()},'translated_b_domain_right_endpoint_identity':'L-b+(b-a)=L-a','geometry_certified':geom,'prime_norm_ball':str(norm),'prime_norm_upper':float(norm.upper()),'total_constant_ball':str(C),'sufficient_dirichlet_mode':M,'margin_ball':str(reserve),'passed':geom and float(reserve.lower())>0,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'exact_two_shift_prime_norm_arb.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert out['passed']

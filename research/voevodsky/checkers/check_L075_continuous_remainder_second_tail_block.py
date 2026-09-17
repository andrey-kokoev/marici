#!/usr/bin/env python3
"""Subtract directed jump coefficients from residual modes 1000..1098."""
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
flint.ctx.prec=512;root=Path(__file__).parents[1]/'results';d=json.loads((root/'L075_residual_cached_chunk_1100_1200.json').read_text());vv=np.load(root/'normalized_prime_codefect_L075_modes.npz')['vectors'][:150,-1];vv[1::2]=0;v=[arb(repr(float(x))) for x in vv];L=arb('.75')
def peval(y):
 p0=arb(1);s=v[0]*(1/(2*L)).sqrt();p1=y
 for n in range(1,149):p2=((2*n+1)*y*p1-n*p0)/(n+1);s+=v[n+1]*((2*(n+1)+1)/(2*L)).sqrt()*p2;p0,p1=p1,p2
 return s
we=peval(arb(1));dwe=sum((v[n]*((2*n+1)/(2*L)).sqrt()*arb(n*(n+1))/2 for n in range(0,150,2)),arb(0));jumps=[];djumps=[]
for nn,lam in ((2,arb(2).log()),(3,arb(3).log()),(4,arb(2).log())):
 y=(L-arb(nn).log())/L;c=lam/arb(nn).sqrt()/2;J=c*we;K=c*dwe;jumps += [(y,J),(-y,-J)];djumps += [(y,K),(-y,K)]
sq=arb(0);jsq=arb(0);dsq=arb(0)
for n,rs in zip(d['indices'],d['components']):
 jc=arb(0)
 for y,J in jumps:jc+=J*((2*n+1)/(2*L)).sqrt()*L*(y.legendre_p(n-1)-y.legendre_p(n+1))/(2*n+1)
 dc=arb(0);A=(L*(2*n+1)/2).sqrt()/(2*n+1)
 for y,K in djumps:
  R=(y.legendre_p(n+2)-y.legendre_p(n))/(2*n+3)-(y.legendre_p(n)-y.legendre_p(n-2))/(2*n-1);dc+=A*K*R
 rem=arb(rs)-jc-dc;sq+=rem*rem;jsq+=jc*jc;dsq+=dc*dc
out={'schema':'marici.voevodsky.L075-continuous-remainder-second-tail-block.v1','degree_range':[1100,1200],'jump_block_norm':str(jsq.sqrt()),'derivative_jump_block_norm':str(dsq.sqrt()),'twice_continuous_remainder_block_norm':str(sq.sqrt()),'full_block_norm':str(arb(d['squared_norm']).sqrt()),'passed_scout':sq.sqrt().upper()<arb('1e-9'),'passed':False,'reason_not_certificate':'one directed block only; infinite continuous remainder needs a second-variation tail bound','rh_proved':False};p=root/'L075_continuous_remainder_second_tail_block.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

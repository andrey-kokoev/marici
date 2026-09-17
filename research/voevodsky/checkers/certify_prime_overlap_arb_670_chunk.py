#!/usr/bin/env python3
"""Directed exact-Gauss prime-overlap rows for the rank-670 Legendre matrix."""
import argparse,json,sys,time
from pathlib import Path
try:
 import flint
 from flint import arb
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb
ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,required=True);ap.add_argument('--count',type=int,default=10);z=ap.parse_args();flint.ctx.prec=4096;N=670;Q=670;L=arb('0.55');stop=min(N,z.start+z.count);M=[[arb(0) for _ in range(N)] for _ in range(stop-z.start)];t0=time.time()
def legs(x):
 out=[arb(1),x]
 for n in range(1,N-1):out.append(((2*n+1)*x*out[n]-n*out[n-1])/(n+1))
 return out
norm=[((2*n+1)/(2*L)).sqrt() for n in range(N)]
for prime in (2,3):
 a=arb(prime).log();lo=-L;hi=L-a;coef=a/arb(prime).sqrt()
 for k in range(Q):
  root,w=arb.legendre_p_root(Q,k,weight=True);tt=(lo+hi)/2+(hi-lo)*root/2;ww=(hi-lo)*w/2;px=legs(tt/L);py=legs((tt+a)/L)
  bx=[norm[n]*px[n] for n in range(N)];by=[norm[n]*py[n] for n in range(N)]
  for ii,i in enumerate(range(z.start,stop)):
   for j in range(N):M[ii][j]-=coef*ww*(bx[i]*by[j]+by[i]*bx[j])/2
maxrad=max(v.rad() for row in M for v in row);out={'schema':'marici.voevodsky.prime-overlap-arb-670-chunk.v1','precision_bits':flint.ctx.prec,'dimension':N,'gauss_order':Q,'row_range':[z.start,stop-1],'polynomial_degree_exactness':2*Q-1,'maximum_entry_radius':str(maxrad),'elapsed_seconds':time.time()-t0,'rows':{str(i):[str(v) for v in M[i-z.start]] for i in range(z.start,stop)},'passed':maxrad<arb('1e-20'),'rh_proved':False};p=Path(__file__).parents[1]/'results'/f'prime_overlap_arb_670_rows_{z.start}_{stop-1}.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('row_range','maximum_entry_radius','elapsed_seconds','passed')},indent=2));assert out['passed']

#!/usr/bin/env python3
"""Directed rank-670 gamma integral on a resumable set of unit panels."""
import argparse,json,sys,time
from pathlib import Path
try:
 import flint
 from flint import arb,acb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import flint
 from flint import arb,acb,arb_mat
ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,required=True);ap.add_argument('--stop',type=int,required=True);z=ap.parse_args();flint.ctx.prec=512;Q=64;N=670;L=arb('.55');logpi=arb.pi().log();rows=[[],[]];srows=[[],[]];t=time.time()
def sj(n,x):return (arb.pi()/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('.5'))
for left in range(z.start,z.stop):
 a=arb(left);b=arb(left+1)
 for k in range(Q):
  r,w=arb.legendre_p_root(Q,k,weight=True);u=(a+b)/2+(b-a)*r/2;fac=(b-a)*w/2*(acb(arb('.25'),u/2).digamma().real-logpi)/(2*arb.pi());vals=[2*L*((2*n+1)/(2*L)).sqrt()*((-1)**(n//2))*sj(n,L*u) for n in range(N)]
  for p in (0,1):v=vals[p::2];rows[p].append(v);srows[p].append([fac*x for x in v])
blocks=[arb_mat(rows[p]).transpose()*arb_mat(srows[p]) for p in (0,1)];maxrad=max(blocks[p][i,j].rad() for p in (0,1) for i in range(335) for j in range(335));out={'schema':'marici.voevodsky.gamma-arb-670-unit-chunk.v1','precision_bits':flint.ctx.prec,'start':z.start,'stop':z.stop,'gauss_order':Q,'maximum_ball_radius':str(maxrad),'elapsed_seconds':time.time()-t,'quadrature_error_status':'separate Bernstein enclosure required','blocks':[[[str(blocks[p][i,j]) for j in range(335)] for i in range(335)] for p in (0,1)],'passed':maxrad<arb('1e-30'),'rh_proved':False};path=Path(__file__).parents[1]/'results'/f'gamma_arb_670_{z.start}_{z.stop}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('start','stop','maximum_ball_radius','elapsed_seconds','quadrature_error_status','passed')},indent=2));assert out['passed']

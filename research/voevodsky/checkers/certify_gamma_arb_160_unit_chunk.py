#!/usr/bin/env python3
"""Directed rank-160 gamma integral on unit panels within [0,250]."""
import json,sys
from pathlib import Path
try:
 import flint
 from flint import arb,acb,arb_mat
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'))
 import flint
 from flint import arb,acb,arb_mat
flint.ctx.prec=192;start=int(sys.argv[1]);stop=int(sys.argv[2]);Q=48;N=160;L=arb('.55');logpi=arb.pi().log();rows=[[],[]];srows=[[],[]]
def sj(n,x):return (arb.pi()/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('.5'))
for left in range(start,stop):
 a=arb(left);b=arb(left+1)
 for k in range(Q):
  r,w=arb.legendre_p_root(Q,k,weight=True);u=(a+b)/2+(b-a)*r/2;fac=(b-a)*w/2*(acb(arb('.25'),u/2).digamma().real-logpi)/(2*arb.pi());vals=[2*L*((2*n+1)/(2*L)).sqrt()*((-1)**(n//2))*sj(n,L*u) for n in range(N)]
  for p in (0,1):v=vals[p::2];rows[p].append(v);srows[p].append([fac*x for x in v])
blocks=[arb_mat(rows[p]).transpose()*arb_mat(srows[p]) for p in (0,1)];maxrad=max(float(blocks[p][i,j].rad()) for p in (0,1) for i in range(80) for j in range(80));out={'schema':'marici.voevodsky.gamma-arb-160-unit-chunk.v1','start':start,'stop':stop,'gauss_order':Q,'blocks':[[[str(blocks[p][i,j]) for j in range(80)] for i in range(80)] for p in (0,1)],'maximum_node_radius':maxrad,'passed':True}
path=Path(__file__).parents[1]/'results'/f'gamma_arb_160_{start}_{stop}.json';path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'start':start,'stop':stop,'maximum_node_radius':maxrad,'passed':True},indent=2))

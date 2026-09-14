#!/usr/bin/env python3
"""Exact hostile to factoring Hardy boundary work through the scalar section line."""
import argparse,json
from pathlib import Path

def add(z,w):return (z[0]+w[0],z[1]+w[1])
def conj(z):return (z[0],-z[1])
def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cross(a,b):return -2*mul(conj(a),b)[1]
def show(z):return f'{z[0]}{z[1]:+d}i'
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_scalar_line_boundary_readout_hostile_certificate_20260908.json');args=p.parse_args();checks=0
 pairs=[((1,0),(0,0)),((1,1),(0,-1))]
 sums=[add(a,b) for a,b in pairs];works=[cross(a,b) for a,b in pairs]
 assert sums[0]==sums[1]==(1,0);checks+=1
 assert works[0]==0 and works[1]==2;checks+=2
 # On the scalar-zero fibre b=-a, the same cross work vanishes identically.
 zero_samples=[]
 for a in ((1,0),(1,2),(-3,1),(0,4)):
  b=(-a[0],-a[1]);assert add(a,b)==(0,0) and cross(a,b)==0;checks+=2
  zero_samples.append({'a':show(a),'b':show(b),'work':0})
 out={'schema':'marici.rh.scalar-line-boundary-readout-hostile.v1','status':'scalar_factorization_falsified','checks':checks,'equal_scalar_examples':[{'a':show(a),'b':show(b),'scalar':show(add(a,b)),'hardy_cross_work':cross(a,b)} for a,b in pairs],'zero_fibre_examples':zero_samples,'claim':'Hardy cross work does not factor through the aggregate scalar line a+b, although it vanishes on that scalar zero fibre','consequence':'no function rho of the scalar theta value alone can reproduce this boundary work on the full two-channel state','surviving_constructor':'define the readout on the full four-channel relative theta state, then prove its descent only on a source-restricted quotient if that quotient is faithful'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'same_scalar':show(sums[0]),'work_values':works}))
if __name__=='__main__':main()

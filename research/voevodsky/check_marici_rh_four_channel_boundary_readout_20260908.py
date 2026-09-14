#!/usr/bin/env python3
"""Exact four-channel Hardy boundary readout and scalar-null hostile."""
import argparse,json
from pathlib import Path

def add(*zs):return (sum(z[0] for z in zs),sum(z[1] for z in zs))
def conj(z):return (z[0],-z[1])
def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def neg(z):return (-z[0],-z[1])
def work(state):
 a,b,_,_=state;return -2*mul(conj(a),b)[1]
def scalar(state):return add(*state)
def reciprocal(state):
 a,b,p0,p1=state;return (b,a,p1,p0)
def show(z):return f'{z[0]}{z[1]:+d}i'
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_four_channel_boundary_readout_certificate_20260908.json');args=p.parse_args();checks=0
 samples=[((1,2),(3,-1),(-2,0),(0,1)),((2,-1),(-1,4),(0,-2),(5,0))]
 rows=[]
 for state in samples:
  reflected=reciprocal(state)
  assert scalar(reflected)==scalar(state);checks+=1
  assert work(reflected)==-work(state);checks+=1
  rows.append({'state':[show(z) for z in state],'scalar':show(scalar(state)),'work':work(state),'reciprocal_work':work(reflected)})
 # Full scalar cancellation can be absorbed by the polar channels while the
 # relative phase of the two bulk channels retains nonzero boundary work.
 hostile=((1,1),(0,-1),(-1,0),(0,0))
 assert scalar(hostile)==(0,0);checks+=1
 assert work(hostile)==2;checks+=1
 # Stronger bulk pairwise nullity b=-a does kill the cross work independently
 # of the polar cancellation.
 a=(2,3);controlled=(a,neg(a),(4,-1),(-4,1))
 assert scalar(controlled)==(0,0) and work(controlled)==0;checks+=2
 out={'schema':'marici.rh.four-channel-boundary-readout.v1','status':'relative_readout_typed_scalar_promotion_falsified','checks':checks,'readout':'rho_rel(a,b,p0,p1)=-2 Im(conj(a)b)','reciprocity':'rho_rel(b,a,p1,p0)=-rho_rel(a,b,p0,p1)','rows':rows,'scalar_zero_hostile':{'state':[show(z) for z in hostile],'scalar':'0+0i','work':work(hostile)},'claim':'the four-channel relative state supports an orientation-sensitive boundary readout, but total scalar nullity does not force its vanishing','required_extra_incidence':'bulk pairwise nullity b=-a, or another source-derived relation retaining the bulk/polar split'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'hostile_work':work(hostile)}))
if __name__=='__main__':main()

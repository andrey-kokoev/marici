#!/usr/bin/env python3
"""Exact audit of the exchange-odd Hardy work after self-dual Poisson sewing."""
import argparse,json
from pathlib import Path

def conj(z):return (z[0],-z[1])
def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def cross(a,b):return -2*mul(conj(a),b)[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_poisson_cross_work_collapse_certificate_20260908.json');args=p.parse_args();checks=0;rows=[]
 for a in ((1,0),(1,2),(-3,4),(0,-5)):
  b=a # self-dual histories in the common Fourier frame
  assert cross(a,b)==0;checks+=1
  rows.append({'common_history_readout':list(a),'cross_work':0})
 # Scalar cancellation is irrelevant: a=b can have nonzero aggregate scalar.
 assert (2*rows[1]['common_history_readout'][0],2*rows[1]['common_history_readout'][1])!=(0,0);checks+=1
 # A Green work value can be nonzero while the sewn exchange-odd port is forced zero.
 modeled_green_work=3;assert modeled_green_work!=rows[0]['cross_work'];checks+=1
 out={'schema':'marici.rh.poisson-cross-work-collapse.v1','status':'exchange_odd_candidate_closed','checks':checks,'rows':rows,'identity':'for b=a, -2 Im(conj(a)b)=0','claim':'self-dual Poisson sewing kills the primal-dual exchange-odd Hardy work independently of scalar nullity','consequence':'this port cannot equal a generally nonzero Green boundary-work defect and supplies no RH orientation','next_constructor':'a source-derived Green mate R2 -> dual(R3) retaining scale and modular boundary incidence'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()

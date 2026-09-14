#!/usr/bin/env python3
"""Exact positive-weight threshold factorization of the summed theta Green image."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_theta_green_weighted_threshold_certificate_20260908.json');args=p.parse_args();checks=0;rows=[]
 for count in (1,2,3,5):
  X=s.symbols('X0:'+str(count),positive=True)
  weights=[4*x*s.exp(-x) for x in X]
  W=sum(weights,s.Integer(0));mu=sum((weights[i]*X[i] for i in range(count)),s.Integer(0))/W
  direct=sum(((4*x*x-6*x)*s.exp(-x) for x in X),s.Integer(0))
  numerator=sum((weights[i]*X[i] for i in range(count)),s.Integer(0))
  factored=numerator-s.Rational(3,2)*W
  assert s.expand(direct-factored)==0;checks+=1
  rows.append({'labels':count,'residual':'0','weight_sum':str(W),'weighted_mean':str(mu)})
 out={'schema':'marici.rh.theta-green-weighted-threshold.v1','status':'aggregate_threshold_factorization_exact','checks':checks,'rows':rows,'identity':'sum_i (4X_i^2-6X_i)e^-X_i = W(mu-3/2)','weights':'w_i=4X_i e^-X_i >0','mean':'mu=sum_i w_i X_i/W','claim':'all finite label cancellation in the centered theta Green image reduces to one positive weighted-mean threshold mu=3/2','boundary':'does not prove monotonicity or uniqueness of the threshold under scale change, reciprocal modular sewing, or equality with D_bw'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'threshold':'3/2'}))
if __name__=='__main__':main()

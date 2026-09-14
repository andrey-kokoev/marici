#!/usr/bin/env python3
"""Exact reduction of theta threshold monotonicity to log-scale concavity."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_theta_threshold_log_concavity_certificate_20260908.json');args=p.parse_args();y=s.symbols('y',positive=True);checks=0
 S1=s.Function('S1')(y);mu=1-y*s.diff(S1,y)/S1
 dmu=s.simplify(y*s.diff(mu,y));log_curvature=s.simplify((y*s.diff(y*s.diff(s.log(S1),y),y)))
 assert s.simplify(dmu+log_curvature)==0;checks+=1
 # If T(y)=sum exp(-pi n^2 y), then S1=-y T'(y).
 T=s.Function('T')(y);sub=s.simplify(mu.subs(S1,-y*s.diff(T,y)).doit())
 expected=s.simplify(-y*s.diff(s.log(-s.diff(T,y)),y))
 assert s.simplify(sub-expected)==0;checks+=1
 out={'schema':'marici.rh.theta-threshold-log-concavity.v1','status':'monotonicity_retyped','checks':checks,'definitions':'T(y)=sum_n exp(-pi n^2 y), S1(y)=-y T_prime(y), mu=1-d log(S1)/d log(y)','identity':'d mu/d log(y) = -d^2 log(S1)/d(log y)^2','equivalent_identity':'mu=-d log(-T_prime(y))/d log(y)','claim':'strict increase of the Green threshold is exactly strict log-concavity of the first theta heat moment on logarithmic scale','consequence':'Poisson modularity can now be applied to one scalar heat-moment curvature instead of an ad hoc weighted variance','boundary':'the checker proves the reduction, not the required strict log-concavity theorem'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'target':'strict log-concavity of S1 in log y'}))
if __name__=='__main__':main()

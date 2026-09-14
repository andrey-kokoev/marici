#!/usr/bin/env python3
"""Exact boundary-pole audit for the geometric determinant-three normalization."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_det3_geometric_boundary_pole_certificate_20260908.json');a=p.parse_args();q=s.symbols('q')
 ginf=1/(1-q);u3=s.exp(-2*q-q*q)*ginf**2
 scaled=s.simplify((1-q)**2*u3);limit=s.limit(scaled,q,1,dir='-');checks=0
 assert s.simplify(limit-s.exp(-3))==0;checks+=1
 assert limit!=0;checks+=1
 first=s.limit((1-q)*u3,q,1,dir='-')
 assert first in (s.oo,-s.oo) or first.has(s.oo);checks+=1
 # The regularizing exponential is itself a nowhere-zero unit at the boundary,
 # so it cannot cancel the order-two pole of the geometric limit.
 exp_at_boundary=s.limit(s.exp(-2*q-q*q),q,1,dir='-')
 assert s.simplify(exp_at_boundary-s.exp(-3))==0;checks+=1
 out={'schema':'marici.rh.det3-geometric-boundary-pole.v1','status':'order_two_boundary_pole_retained','checks':checks,'carrier':'u3(q)=exp(-2q-q^2)/(1-q)^2','scaled_boundary_limit':'exp(-3)','pole_order':2,'claim':'subtracting primitive and square logarithmic terms leaves a unit multiplier and does not remove the geometric boundary pole','disposition':'do not use the geometric det3 normalization as an H2 seam completion','boundary':'this refutes only the geometric one-variable presentation, not the source-labelled Schatten-three prime operator on its own chart'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'pole_order':2}))
if __name__=='__main__':main()

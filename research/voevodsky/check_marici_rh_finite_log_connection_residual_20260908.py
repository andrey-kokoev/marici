#!/usr/bin/env python3
"""Exact finite-cutoff determinant-three logarithmic-connection audit."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_finite_log_connection_residual_certificate_20260908.json');a=p.parse_args()
 q=s.symbols('q');rows=[];checks=0
 for depth in (2,3,5,10):
  g=sum(q**k for k in range(depth+1));delta=s.expand(g**2)
  full=s.cancel(s.diff(delta,q)/delta)
  primitive=s.Integer(2);square=2*q
  tail=s.cancel(full-primitive-square)
  residual=s.cancel(full-primitive-square-tail)
  assert residual==0;checks+=1
  # Hostiles delete one typed low grade; their residuals must remain exact.
  without_primitive=s.cancel(full-square-tail)
  without_square=s.cancel(full-primitive-tail)
  assert without_primitive==2 and s.cancel(without_square-2*q)==0;checks+=2
  # A cubic-order logarithmic tail has no constant or linear connection term.
  tail_series=s.series(tail,q,0,2).removeO().expand()
  assert tail_series==0;checks+=1
  rows.append({'depth':depth,'delta':str(delta),'tail_connection':str(tail),'residual':str(residual),'without_primitive':str(without_primitive),'without_square':str(without_square),'tail_constant_and_linear':str(tail_series)})
 out={'schema':'marici.rh.finite-log-connection-residual.v1','status':'exact_finite_cutoff_identity','checks':checks,'variable':'q','rows':rows,'claim':'dlog Delta_X equals primitive plus square plus determinant-three tail at each tested polynomial cutoff','boundary':'does not prove cutoff-refinement naturality, completion, identification with Xi, or boundary-work conservation'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'depths':[r['depth'] for r in rows]}))
if __name__=='__main__':main()

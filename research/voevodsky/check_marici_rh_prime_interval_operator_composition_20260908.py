#!/usr/bin/env python3
"""Exact finite composition law for labelled prime interval operators."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_prime_interval_operator_composition_certificate_20260908.json');a=p.parse_args();rows=[];checks=0
 for count in (1,2,3,5):
  x=s.symbols('x0:'+str(count));y=s.symbols('y0:'+str(count));I=s.eye(count)
  A=s.diag(*[u-1 for u in x]);B=s.diag(*[u-1 for u in y]);AB=A+B+A*B
  composed=s.diag(*[x[i]*y[i]-1 for i in range(count)])
  assert (AB-composed).applyfunc(s.expand)==s.zeros(count);checks+=1
  primitive_residual=s.expand(s.trace(AB)-sum((x[i]*y[i]-1 for i in range(count)),s.Integer(0)))
  square_residual=s.expand(s.trace(AB*AB)/2-sum(((x[i]*y[i]-1)**2/2 for i in range(count)),s.Integer(0)))
  assert primitive_residual==0 and square_residual==0;checks+=2
  # Additive composition omits the transported interaction A B.
  hostile=s.simplify(composed-(A+B));assert hostile!=s.zeros(count);checks+=1
  rows.append({'prime_channels':count,'star_composition_residual':'zero matrix','primitive_trace_residual':str(primitive_residual),'square_trace_residual':str(square_residual),'additive_only_residual_diagonal':[str(s.expand(x[i]*y[i]-x[i]-y[i]+1)) for i in range(count)]})
 out={'schema':'marici.rh.prime-interval-operator-composition.v1','status':'finite_interval_star_law_verified','checks':checks,'rows':rows,'construction':'A_a=diag(chi_p(a)-1); A_a star A_b=A_a+A_b+A_a A_b=A_(a+b)','character_law':'chi_p(a+b)=chi_p(a)chi_p(b)','claim':'the same finite labelled operator supports interval concatenation and its primitive and square traces','boundary':'identifying chi_p and these traces with the independently derived endpoint cocycle, then completing its anomaly lines with seam and archimedean data, remains open'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'max_channels':rows[-1]['prime_channels']}))
if __name__=='__main__':main()

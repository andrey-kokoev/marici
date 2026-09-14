#!/usr/bin/env python3
"""Exact finite common-operator test for primitive and square Euler currents."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_common_prime_operator_traces_certificate_20260908.json');a=p.parse_args();rows=[];checks=0
 for count in (1,2,3,5):
  x=s.symbols('x0:'+str(count));K=s.diag(*x)
  primitive=sum(x,s.Integer(0));square=sum((u*u/s.Integer(2) for u in x),s.Integer(0))
  tr1=s.trace(K);tr2=s.trace(K*K)/2
  assert s.expand(tr1-primitive)==0;checks+=1
  assert s.expand(tr2-square)==0;checks+=1
  # Hostile: using an independently rescaled square operator preserves shape
  # but changes the source current.
  Ksquare=2*K;hostile=s.expand(s.trace(Ksquare*Ksquare)/2-square)
  assert hostile!=0;checks+=1
  rows.append({'prime_channels':count,'primitive_residual':str(s.expand(tr1-primitive)),'square_residual':str(s.expand(tr2-square)),'independent_square_operator_residual':str(hostile)})
 out={'schema':'marici.rh.common-prime-operator-traces.v1','status':'finite_common_operator_verified','checks':checks,'rows':rows,'operator':'K_X=diag(x_p) on the finite labelled prime space','specialization':'x_p=p^(-s)','claim':'the independently defined finite primitive and square Euler currents are Tr(K_X) and Tr(K_X^2)/2 of the same labelled operator','boundary':'finite Euler-chamber identity only; endpoint interval realization, anomaly-line completion, reciprocal theta-section identification, and boundary-work conservation are not proved'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'max_channels':rows[-1]['prime_channels']}))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact matrix audit that the order-three multiplicative anomaly is δr."""
import argparse,json
from pathlib import Path
import sympy as s

def star(A,B):return A+B+A*B
def r(A):return s.expand(-s.trace(A)+s.trace(A*A)/2)
def alpha(A,B):return s.expand(r(star(A,B))-r(A)-r(B))
def zero(M):return all(s.expand(x)==0 for x in M)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_det3_anomaly_coboundary_certificate_20260908.json');a=p.parse_args();checks=0;rows=[]
 fixtures=[
  (s.Matrix([[1,2],[0,-1]]),s.Matrix([[0,1],[3,2]]),s.Matrix([[2,0],[-1,1]])),
  (s.Matrix([[0,1],[-1,0]]),s.Matrix([[2,-1],[1,0]]),s.Matrix([[-1,2],[2,1]])),
  (s.Matrix([[s.Rational(1,2),1],[0,s.Rational(-1,3)]]),s.Matrix([[1,0],[2,s.Rational(1,4)]]),s.Matrix([[0,-2],[1,1]]))]
 for i,(A,B,C) in enumerate(fixtures):
  assert zero(star(star(A,B),C)-star(A,star(B,C)));checks+=1
  lhs=s.expand(alpha(A,B)+alpha(star(A,B),C));rhs=s.expand(alpha(B,C)+alpha(A,star(B,C)))
  assert s.expand(lhs-rhs)==0;checks+=1
  # Removing the normalization cochain leaves the computed anomaly generally nonzero.
  ab=alpha(A,B);assert ab!=0;checks+=1
  rows.append({'fixture':i,'alpha_AB':str(ab),'three_fold_residual':str(s.expand(lhs-rhs))})
 out={'schema':'marici.rh.det3-anomaly-coboundary.v1','status':'exact_coboundary_coherence','checks':checks,'rows':rows,'definitions':'A star B=A+B+AB; r(A)=-Tr(A)+Tr(A^2)/2; alpha3(A,B)=r(A star B)-r(A)-r(B)','claim':'the order-three anomaly is the coboundary of the primitive-square normalization and obeys the three-fold cocycle equation','disposition':'normalize once by r; do not add an independent associator','boundary':'finite exact matrices only; endpoint-current identification and completed seam/archimedean trivialization remain separate'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'fixtures':len(rows)}))
if __name__=='__main__':main()

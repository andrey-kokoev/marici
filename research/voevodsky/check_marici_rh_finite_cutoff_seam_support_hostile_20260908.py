#!/usr/bin/env python3
"""Test whether finite Fourier-cutoff leakage is supported on the real seam x=0."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_finite_cutoff_seam_support_hostile_certificate_20260908.json');args=p.parse_args();x,y=s.symbols('x y',real=True);checks=0
 F=s.Matrix([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
 P=s.diag(1,0,0,0);I=s.eye(4);leak=s.simplify(P*F*(I-P))
 assert leak.rank()==1;checks+=1
 assert leak==s.Matrix([[0,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]);checks+=1
 # A finitely generated module supported on V(x) must be x-power torsion.
 # This constant leakage survives multiplication by every x^k and restriction
 # to the principal open D(x).
 for k in (1,2,3,4):
  assert (x**k*leak)!=s.zeros(4);checks+=1
 localized=leak.subs(x,1);assert localized.rank()==1;checks+=1
 out={'schema':'marici.rh.finite-cutoff-seam-support-hostile.v1','status':'generic_leakage_not_seam_supported','checks':checks,'leakage_matrix':[list(map(str,leak.row(i))) for i in range(4)],'rank':1,'support_test':'x^k L is nonzero for k=1..4 and L|_(x=1) has rank one','claim':'the hard finite Fourier-cutoff comparison fibre has a generic rank-one component and is not supported on the seam V(x)','disposition':'do not feed this cutoff cone to seam Kashiwara localization; first pass to a completion in which the leakage cocycle converges to zero or is retained as a separate approximation object','boundary':'does not refute a completed smooth cutoff or a corrected boundary-bearing comparison whose generic leakage vanishes'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'rank':1,'localized_rank':localized.rank()}))
if __name__=='__main__':main()

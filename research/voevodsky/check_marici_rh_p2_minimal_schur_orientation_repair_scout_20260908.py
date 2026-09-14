#!/usr/bin/env python3
"""Scout feasibility of a rank-one Schur return supplying the p=2 orientation residual."""
import argparse,json,math
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_p2_minimal_schur_orientation_repair_scout_20260908.json');args=p.parse_args();r,q1,q2,D1,D2=s.symbols('r q1 q2 D1 D2',positive=True);I=s.I;checks=0
 Q=s.Matrix([[q1,-I*r],[I*r,q2]]);E=s.diag(D1,D2)-Q
 assert s.expand(Q.det())==q1*q2-r*r;checks+=1
 assert s.expand(E.det())==D1*D2-D1*q2-D2*q1+q1*q2-r*r;checks+=1
 # Rank-one Q has q1*q2=r^2, leaving det(E)=D1D2-D1q2-D2q1.
 # AM-GM minimizes the cost at q1=r sqrt(D1/D2), q2=r sqrt(D2/D1).
 q1opt=r*s.sqrt(D1/D2);q2opt=r*s.sqrt(D2/D1)
 detopt=s.simplify(E.det().subs({q1:q1opt,q2:q2opt}))
 assert s.simplify(detopt-(D1*D2-2*r*s.sqrt(D1*D2)))==0;checks+=1
 a=0.637405002217635112636240829881;b=0.973571176349066980268480987606
 hgeom=2*(b-a)/(a+b);heuler=math.log(2)*2**-.5/(1-2**-.5);repair=heuler-hgeom;d1=2*b;d2=2*a
 threshold=math.sqrt(d1*d2)/2;best_det=d1*d2-2*repair*math.sqrt(d1*d2)
 assert repair>threshold and best_det<0;checks+=1
 balanced_det=(d1-repair)*(d2-repair)-repair**2;assert balanced_det<0;checks+=1
 out={'schema':'marici.rh.p2-minimal-schur-orientation-repair-scout.v2','status':'superseded_noninvariant_residual_model','checks':checks,'orientation_residual':repair,'p2_pauli_diagonal':[d1,d2],'necessary_and_sufficient_rank_one_threshold':'r <= sqrt(D1 D2)/2','threshold_value':threshold,'optimal_remaining_determinant':best_det,'balanced_remaining_determinant':balanced_det,'claim':'conditional on the now-rejected Euler-minus-Pauli residual split, no positive rank-one subtraction fits the p=2 Pauli block','consequence':'do not use this subtraction model: the alleged Pauli orientation is rephasing-dependent, so the residual has no invariant source meaning','boundary':'retained as a hostile calculation for the superseded split; it is not a constraint on the correctly typed full Stokes/Fourier orientation sector'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'repair':repair,'threshold':threshold,'best_det':best_det}))
if __name__=='__main__':main()

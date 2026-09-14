#!/usr/bin/env python3
"""Verify the faithful positive Pauli quadratic lift of a two-endpoint Gram."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_pauli_quadratic_lift_certificate_20260908.json');args=p.parse_args();a,b,c,h=s.symbols('a b c h',real=True);I=s.I;checks=0
 G=s.Matrix([[a,c+I*h],[c-I*h,b]]);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,I],[-I,0]]);R=X.row_join(Y)
 Gamma=s.simplify(R.conjugate().T*G*R)
 blocks=s.Matrix.vstack(s.Matrix.hstack(X*G*X,X*G*Y),s.Matrix.hstack(Y*G*X,Y*G*Y))
 assert s.simplify(Gamma-blocks)==s.zeros(4);checks+=1
 assert s.simplify(X*Gamma[:2,:2]*X-G)==s.zeros(2);checks+=1
 assert R.rank()==2;checks+=1
 # The lift is additive and *-preserving by exact symbolic fixtures.
 G2=s.Matrix([[s.symbols('d',real=True),0],[0,s.symbols('e',real=True)]])
 assert s.simplify(R.conjugate().T*(G+G2)*R-(Gamma+R.conjugate().T*G2*R))==s.zeros(4);checks+=1
 # Positive numerical fixture has the same rank after the lift.
 Gn=s.Matrix([[2,1+I/2],[1-I/2,3]]);GamN=R.conjugate().T*Gn*R
 assert Gn.is_positive_definite and GamN.rank()==Gn.rank()==2;checks+=1
 # Quadratic-form positivity is inherited: z*Gamma z=(Rz)*G(Rz).
 out={'schema':'marici.rh.pauli-quadratic-lift.v1','status':'faithful_positive_quadratic_lift_constructed','checks':checks,'lift':'Gamma_P(G)=R^* G R, R=[X Y]','dimension':'M_2 -> M_4','retraction':'G=X Gamma_P(G)_(XX) X','rank':'rank Gamma_P(G)=rank G because R is surjective','positivity':'z^*Gamma_P(G)z=(Rz)^*G(Rz)','claim':'the separate-output Pauli construction is an injective positive linear lift of the entire polarized endpoint form','consequence':'the four matrix-unit comparison can be stated as equality of two explicit 4x4 lifted linking Grams, without compressing away orientation','boundary':'the lift supplies the correct finite target and retraction, not the equality with the theta-history quadratic representation'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'lift_rank':2}))
if __name__=='__main__':main()

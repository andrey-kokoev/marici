#!/usr/bin/env python3
"""Reject conflating target-frame stabilization with Pauli-domain Gram congruence."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_identity_frame_congruence_no_go_certificate_20260908.json');args=p.parse_args();a,b,h=s.symbols('a b h',real=True);I=s.I;checks=0
 w=s.Matrix([s.Rational(1,2),s.Rational(1,2)]);j=s.Matrix([s.Rational(1,4),-s.Rational(1,4)]);F=s.Matrix.hstack(w,j)
 t11,t12,t21,t22=s.symbols('t11 t12 t21 t22');T=s.Matrix([[t11,t12],[t21,t22]])
 solT=s.solve(list(T*w-w)+list(T*j-j),[t11,t12,t21,t22],dict=True)
 assert solT==[{t11:1,t12:0,t21:0,t22:1}];checks+=1
 H=s.Matrix([[2,I*h],[-I*h,2]]);D=s.diag(2*b,2*a)
 diff=H-D
 assert diff==s.Matrix([[2-2*b,I*h],[-I*h,2-2*a]]);checks+=1
 sol=s.solve(list(diff),[a,b,h],dict=True)
 assert sol==[{a:1,b:1,h:0}];checks+=1
 out={'schema':'marici.rh.identity-frame-congruence-no-go.v1','status':'domain_target_frame_conflation_rejected','checks':checks,'claim':'if one map fixes both theta target columns, it is the identity; it can also satisfy T^* H_h T=D_p only in the special case a_p=b_p=1 and h_p=0','consequence':'because the RH odd coordinate has h_p>0, the Pauli source columns cannot be identified with the theta wall/odd columns before constructing their source-derived correspondence','first_missing_data':'the two Pauli-domain vectors whose images are w_theta and j_theta under the linear Adams constructor','boundary':'does not reject a nonidentity prime-dependent congruence once its domain vectors are typed'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'exception':'a=b=1,h=0'}))
if __name__=='__main__':main()

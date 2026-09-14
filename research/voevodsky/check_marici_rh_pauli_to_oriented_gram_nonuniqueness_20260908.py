#!/usr/bin/env python3
"""Show Gram congruence does not choose the Pauli-to-oriented comparison map."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_pauli_to_oriented_gram_nonuniqueness_certificate_20260908.json');args=p.parse_args();I=s.I;checks=0
 H=s.Matrix([[2,I],[-I,2]]) # h=1, eigenvalues 1,3
 Id=s.eye(2);P1=(3*Id-H)/2;P3=(H-Id)/2
 assert P1*P1==P1 and P3*P3==P3 and P1*P3==s.zeros(2);checks+=1
 Hm=P1+P3/s.sqrt(3)
 assert s.simplify(Hm*H*Hm-Id)==s.zeros(2);checks+=1
 D=2*Id;sqrtD=s.sqrt(2)*Id
 U0=Id;U1=s.diag(1,-1)
 T0=s.simplify(Hm*U0*sqrtD);T1=s.simplify(Hm*U1*sqrtD)
 assert s.simplify(T0.conjugate().T*H*T0-D)==s.zeros(2);checks+=1
 assert s.simplify(T1.conjugate().T*H*T1-D)==s.zeros(2);checks+=1
 assert T0!=T1;checks+=1
 # Relative map is the nontrivial unitary U1; Gram data cannot distinguish it.
 rel=s.simplify(T0.inv()*T1);assert rel==U1;checks+=1
 out={'schema':'marici.rh.pauli-to-oriented-gram-nonuniqueness.v1','status':'gram_congruence_has_unitary_ambiguity','checks':checks,'fixture':'D=2I, H=[[2,i],[-i,2]]','solutions':['T0=H^-1/2 sqrt(D)','T1=H^-1/2 diag(1,-1) sqrt(D)'],'relative_unitary':'diag(1,-1)','general_family':'T_U=H^-1/2 U D^1/2 for arbitrary unitary U','claim':'even exact positive Gram matching does not canonically determine the comparison arrow','consequence':'the Fourier quarter-turn and reciprocal orientation must select the unitary part before the crystal Hermitian realization is source-authorized','boundary':'this is a finite structural hostile; it does not deny existence of a source-selected comparison map'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'relative_unitary':'diag(1,-1)'}))
if __name__=='__main__':main()

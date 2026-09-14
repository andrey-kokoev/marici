#!/usr/bin/env python3
"""Construct the canonical positive congruence from the Pauli Gram to H_h."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_prime_dependent_pauli_oriented_candidate_certificate_20260908.json');args=p.parse_args();a,b,h=s.symbols('a b h',positive=True);I=s.I;checks=0
 H=s.Matrix([[2,I*h],[-I*h,2]]);Id=s.eye(2)
 # Spectral projectors for eigenvalues 2-h and 2+h.
 Pm=((2+h)*Id-H)/(2*h);Pp=(H-(2-h)*Id)/(2*h)
 assert s.simplify(Pm*Pm-Pm)==s.zeros(2) and s.simplify(Pp*Pp-Pp)==s.zeros(2);checks+=1
 Hm=Pm/s.sqrt(2-h)+Pp/s.sqrt(2+h)
 assert s.simplify(Hm*H*Hm-Id)==s.zeros(2);checks+=1
 K=s.sqrt(2)*Hm
 assert s.simplify(K*H*K-2*Id)==s.zeros(2);checks+=1
 A=s.diag(s.sqrt(b),s.sqrt(a));D=s.diag(2*b,2*a);T=s.simplify(K*A)
 assert s.simplify(A*(2*Id)*A-D)==s.zeros(2);checks+=1
 assert s.simplify(A*K*H*K*A-D)==s.zeros(2);checks+=1
 out={'schema':'marici.rh.prime-dependent-pauli-oriented-candidate.v1','status':'canonical_positive_congruence_constructed','checks':checks,'source_pauli_gram':'D_p=diag(2b_p,2a_p)','normalizer':'A_p=diag(sqrt(b_p),sqrt(a_p))','oriented_metric':'H_h=[[2,ih],[-ih,2]]','orientation_map':'K_h=sqrt(2) H_h^-1/2','candidate':'T_p=K_h A_p','identity':'T_p^* H_h T_p=D_p','claim':'positive endpoint energies and the oriented Euler coordinate define a canonical positive congruence candidate after Pauli dilation','boundary':'positive square roots select the metric part only; source functoriality must still prove that T_p agrees with the fixed wall/odd/quarter-turn constructor and is natural in prime cutoff and completion'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'candidate':'T_p=sqrt(2) H_h^-1/2 diag(sqrt(b_p),sqrt(a_p))'}))
if __name__=='__main__':main()

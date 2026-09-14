#!/usr/bin/env python3
"""Verify the canonical sum/difference decomposition of resolved output ports."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_resolved_output_hadamard_decomposition_certificate_20260908.json');a=p.parse_args()
 x11,x12,x21,x22,M=s.symbols('x11 x12 x21 x22 M',real=True)
 B=s.Matrix([[x11,x12+s.I*x21],[x12-s.I*x21,x22]])
 I=s.eye(2);star=lambda X:X.conjugate().T
 P=star(B+M*I)*(B+M*I);N=star(B-M*I)*(B-M*I)
 Gres=(1+M**2)*I+star(B)*B;Ghist=I+P
 checks=0
 assert s.simplify(Gres-(I+(P+N)/2))==s.zeros(2);checks+=1
 assert s.simplify(Ghist-Gres-(P-N)/2)==s.zeros(2);checks+=1
 H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
 assert s.simplify(star(H)*H-I)==s.zeros(2);checks+=1
 # Hadamard sends resolved amplitudes (t,o) to normalized sum/difference.
 t1,t2,o1,o2=s.symbols('t1 t2 o1 o2');v=s.Matrix([[t1,t2],[o1,o2]])
 hv=s.simplify(H*v)
 assert hv[0,0]==s.sqrt(2)*(o1+t1)/2 and hv[1,0]==s.sqrt(2)*(-o1+t1)/2;checks+=1
 out={'schema':'marici.rh.resolved-output-hadamard-decomposition.v1','status':'exact_decomposition_constructed','checks':checks,
 'identity':'G_res=I+1/2 G_+ +1/2 G_-, where G_+=(B+M)^*(B+M), G_-=(B-M)^*(B-M)',
 'oriented_identity':'G_hist-G_res=1/2(G_+-G_-)=M(B+B^*)',
 'constructor':'canonical unitary Hadamard transform on retained tail/output-wall ports',
 'consequence':'the missing ordered bulk polarization is exactly the norm imbalance between codiagonal and anti-codiagonal resolved outputs',
 'boundary':'the algebra does not authorize discarding the anti-codiagonal port or prove the theta/Pauli source comparison'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()

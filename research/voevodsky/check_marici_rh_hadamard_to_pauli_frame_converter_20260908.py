#!/usr/bin/env python3
"""Construct the fixed converter from Hadamard blocks to the Pauli lift."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_hadamard_to_pauli_frame_converter_certificate_20260908.json');a=p.parse_args()
 a0,b,c,h=s.symbols('a b c h',real=True);I=s.I
 G=s.Matrix([[a0,c+I*h],[c-I*h,b]])
 X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,I],[-I,0]]);R=X.row_join(Y)
 H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);L=s.simplify(H*G*H);S=s.simplify(H*R)
 Gamma=s.simplify(R.conjugate().T*G*R);checks=0
 assert s.simplify(G-H*L*H)==s.zeros(2);checks+=1
 assert s.simplify(Gamma-S.conjugate().T*L*S)==s.zeros(4);checks+=1
 assert S.rank()==2 and s.simplify(S*S.conjugate().T-2*s.eye(2))==s.zeros(2);checks+=1
 # Retraction from the tight frame S: L=(1/4) S Gamma S*.
 assert s.simplify(S*Gamma*S.conjugate().T/4-L)==s.zeros(2);checks+=1
 U=s.simplify(X*Y)
 assert s.simplify(Y-X*U)==s.zeros(2);checks+=1
 out={'schema':'marici.rh.hadamard-to-pauli-frame-converter.v1','status':'fixed_faithful_converter_constructed','checks':checks,
 'converter':'Gamma_P(G)=S^* L S with L=H G H and S=H[X Y]',
 'retraction':'L=(1/4) S Gamma_P(G) S^*','tight_frame':'S S^*=2I','phase':'Y=XU, U=XY=diag(-i,i)',
 'consequence':'equality of the four Hadamard blocks is equivalent to equality of the full Pauli lift; no separate sixteen-entry theorem is needed',
 'boundary':'the fixed converter does not prove equality of the source-derived theta Hadamard Gram and the Stieltjes endpoint Gram'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()

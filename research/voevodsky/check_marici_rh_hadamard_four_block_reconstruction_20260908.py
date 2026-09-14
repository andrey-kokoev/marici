#!/usr/bin/env python3
"""Verify that four Hadamard linking blocks reconstruct ordered polarization."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_hadamard_four_block_reconstruction_certificate_20260908.json');a=p.parse_args()
 # General scalar Hermitian two-port Gram; the identities are block-polynomial.
 T,O,cr,ci=s.symbols('T O cr ci',real=True);C=cr+s.I*ci
 K=s.Matrix([[T,C],[s.conjugate(C),O]])
 H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);L=s.simplify(H*K*H)
 P,Q,R,N=L[0,0],L[0,1],L[1,0],L[1,1];checks=0
 assert s.simplify(P-N-(C+s.conjugate(C)))==0;checks+=1
 assert s.simplify(Q-R-(s.conjugate(C)-C))==0;checks+=1
 assert s.simplify((P+N+Q+R)/2-T)==0;checks+=1
 assert s.simplify((P+N-Q-R)/2-O)==0;checks+=1
 assert s.simplify((P-N-Q+R)/2-C)==0;checks+=1
 assert s.simplify(H*L*H-K)==s.zeros(2);checks+=1
 out={'schema':'marici.rh.hadamard-four-block-reconstruction.v1','status':'full_ordered_polarization_reconstructed','checks':checks,
 'hadamard_blocks':{'P':'(T+O+C+C*)/2','N':'(T+O-C-C*)/2','Q':'(T-O-C+C*)/2','R':'(T-O+C-C*)/2'},
 'cross_reconstruction':'C=(P-N-Q+R)/2','hermitian_cross':'C+C*=P-N','skew_cross':'C*-C=Q-R',
 'consequence':'the diagonal Hadamard energies recover only the Hermitian cross term; both off-diagonal linking blocks are necessary for reciprocal orientation',
 'next_test':'compare the four theta Hadamard blocks P,Q,R,N with the faithful Pauli linking blocks before summation'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks}))
if __name__=='__main__':main()

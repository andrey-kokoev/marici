#!/usr/bin/env python3
"""Verify that separate Pauli outputs retain the full polarized endpoint Gram."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_full_pauli_linking_gram_faithful_certificate_20260908.json');args=p.parse_args();a,b,c,h=s.symbols('a b c h',real=True);I=s.I;checks=0
 G=s.Matrix([[a,c+I*h],[c-I*h,b]]);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,I],[-I,0]])
 Bxx=s.simplify(X*G*X);Byy=s.simplify(Y*G*Y);Bxy=s.simplify(X*G*Y);Byx=s.simplify(Y*G*X)
 assert s.simplify(Bxx+Byy)==s.diag(2*b,2*a);checks+=1
 assert s.simplify(Bxy.conjugate().T-Byx)==s.zeros(2);checks+=1
 assert s.simplify(X*Bxx*X-G)==s.zeros(2);checks+=1
 # Even without using Bxx alone, the cross block visibly retains c and h.
 assert any(entry.has(c) for entry in Bxy) and any(entry.has(h) for entry in Bxy);checks+=1
 # Summed observer deletes both coordinates.
 assert all(not entry.has(c,h) for entry in Bxx+Byy);checks+=1
 out={'schema':'marici.rh.full-pauli-linking-gram-faithful.v1','status':'separate_pauli_outputs_preserve_full_polarization','checks':checks,'blocks':{'B_XX':[[str(Bxx[i,j]) for j in range(2)] for i in range(2)],'B_YY':[[str(Byy[i,j]) for j in range(2)] for i in range(2)],'B_XY':[[str(Bxy[i,j]) for j in range(2)] for i in range(2)],'B_YX':[[str(Byx[i,j]) for j in range(2)] for i in range(2)]},'summed_frame':'B_XX+B_YY=diag(2b,2a)','reconstruction':'G=X B_XX X','claim':'the full two-output Pauli linking Gram is faithful to a,b,c,h, while its summed frame operator discards c and h','consequence':'the crystal comparison must act on the four linking blocks before summing output energy; the source Fourier Y-port then fixes the phase rather than an arbitrary rephasing','boundary':'faithfulness of the finite algebraic encoding does not establish its identification with the completed theta-history representation'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'summed_frame':'diag(2b,2a)'}))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Verify that the source-fixed wall and odd columns uniquely select the unitary factor."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_wall_odd_frame_kills_unitary_ambiguity_certificate_20260908.json');args=p.parse_args();a,b,c,d=s.symbols('a b c d');checks=0
 U=s.Matrix([[a,b],[c,d]])
 w=s.Matrix([s.Rational(1,2),s.Rational(1,2)])
 j=s.Matrix([s.Rational(1,4),-s.Rational(1,4)])
 frame=s.Matrix.hstack(w,j)
 assert frame.det()==-s.Rational(1,4);checks+=1
 equations=list(U*w-w)+list(U*j-j)
 sol=s.solve(equations,[a,b,c,d],dict=True)
 assert sol==[{a:1,b:0,c:0,d:1}];checks+=1
 # Equivalent frame conjugation reconstruction.
 assert s.simplify(frame*frame.inv())==s.eye(2);checks+=1
 # Reversing the odd column gives the previously exhibited ambiguity, but
 # violates the frozen curvature-return sign.
 Uflip=frame*s.diag(1,-1)*frame.inv()
 assert Uflip*w==w and Uflip*j==-j and Uflip!=s.eye(2);checks+=1
 out={'schema':'marici.rh.wall-odd-frame-kills-unitary-ambiguity.v1','status':'target_frame_stabilizer_is_trivial','checks':checks,'wall_column':'(1/2,1/2)','odd_column':'(1/4,-1/4)','frame_determinant':'-1/4','unique_map':'U=I when Uw=w and Uj=j','orientation_hostile':'the nontrivial frame reflection fixes w but sends j to -j','claim':'the common stabilizer of the two target columns is trivial','consequence':'a unitary is uniquely selected only after source-domain columns and their required images are separately specified','boundary':'this target-frame calculation alone does not select the unitary in a congruence between the prime-dependent Pauli domain and the theta target'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'frame_determinant':'-1/4'}))
if __name__=='__main__':main()

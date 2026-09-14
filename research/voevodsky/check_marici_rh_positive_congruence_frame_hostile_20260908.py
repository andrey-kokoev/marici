#!/usr/bin/env python3
"""Test the positive congruence against the fixed wall/odd endpoint frame."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_positive_congruence_frame_hostile_certificate_20260908.json');args=p.parse_args();h=s.symbols('h',positive=True);I=s.I;checks=0
 H=s.Matrix([[2,I*h],[-I*h,2]]);Id=s.eye(2);Pm=((2+h)*Id-H)/(2*h);Pp=(H-(2-h)*Id)/(2*h);K=s.sqrt(2)*(Pm/s.sqrt(2-h)+Pp/s.sqrt(2+h))
 w=s.Matrix([s.Rational(1,2),s.Rational(1,2)]);j=s.Matrix([s.Rational(1,4),-s.Rational(1,4)])
 Kw=s.simplify(K*w);Kj=s.simplify(K*j)
 # At h=1, exact mismatch with both fixed columns.
 Kw1=s.simplify(Kw.subs(h,1));Kj1=s.simplify(Kj.subs(h,1))
 assert Kw1!=w and Kj1!=j;checks+=2
 assert s.simplify(K.subs(h,1)*H.subs(h,1)*K.subs(h,1)-2*Id)==s.zeros(2);checks+=1
 # The mismatch disappears only at the unoriented limit h=0; verify by series limit.
 assert s.simplify(K.limit(h,0)-Id)==s.zeros(2);checks+=1
 out={'schema':'marici.rh.positive-congruence-frame-hostile.v1','status':'positive_square_root_does_not_preserve_source_frame','checks':checks,'fixture':'h=1','K_w':[str(x) for x in Kw1],'K_j':[str(x) for x in Kj1],'claim':'the canonical positive metric congruence is not the source-fixed wall/odd constructor when the orientation coordinate is nonzero','consequence':'a source-selected unitary factor is still required between H^-1/2 and the Pauli endpoint scaling; positive square roots alone do not define the Adams arrow','boundary':'the hostile tests the U=I positive congruence, not every unitary-corrected congruence'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'fixture':'h=1'}))
if __name__=='__main__':main()

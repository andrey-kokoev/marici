#!/usr/bin/env python3
"""Exhibit the orientation parameter omitted by the real three-port Green form."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_three_port_oriented_hermitian_extension_certificate_20260908.json');args=p.parse_args();h=s.symbols('h',real=True);I=s.I;checks=0
 Pi=s.Matrix([[1,0,-1],[0,1,-1]]);S=s.Matrix([[0,1,0],[1,0,0],[0,0,1]]);r=s.Matrix([1,1,1])
 H=s.Matrix([[2,I*h],[-I*h,2]])
 G=s.simplify(Pi.T.conjugate()*H*Pi)
 assert G*r==s.zeros(3,1);checks+=1
 assert s.simplify(S.T*G.conjugate()*S-G)==s.zeros(3);checks+=1
 assert G.subs(h,0)==s.Matrix([[2,0,-2],[0,2,-2],[-2,-2,4]]);checks+=1
 e1=s.Matrix([1,0,0]);e2=s.Matrix([0,1,0])
 assert s.im((e1.T.conjugate()*G*e2)[0])==h;checks+=1
 # Positivity of the quotient metric H is equivalent to |h|<=2.
 assert s.simplify(H.det()-(4-h**2))==0;checks+=1
 # Diagonal endpoint energies are insensitive to h.
 assert G[0,0]==2 and G[1,1]==2;checks+=1
 out={'schema':'marici.rh.three-port-oriented-hermitian-extension.v1','status':'one_orientation_parameter_remains','checks':checks,'quotient_metric':[['2','i h'],['-i h','2']],'three_port_matrix':[[str(G[i,j]) for j in range(3)] for i in range(3)],'overlap_radical':'span(1,1,1)','reciprocity':'G=S^T conjugate(G) S','positivity':'|h|<=2','claim':'the previously normalized real matrix is only the h=0 reciprocal-even part; endpoint norms and overlap conservation do not determine the oriented imaginary polarization','next_gate':'derive h from the source odd seam current and test its sign under endpoint reversal'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'positivity':'|h|<=2'}))
if __name__=='__main__':main()

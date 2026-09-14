#!/usr/bin/env python3
"""Assemble the grade-K and completed oriented relative Green matrices."""
import argparse,json,math
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_completed_three_port_green_family_certificate_20260908.json');args=p.parse_args();h=s.symbols('h',real=True);I=s.I;checks=0
 Pi=s.Matrix([[1,0,-1],[0,1,-1]]);H=s.Matrix([[2,I*h],[-I*h,2]]);G=s.expand(Pi.T.conjugate()*H*Pi);rvec=s.Matrix([1,1,1]);S=s.Matrix([[0,1,0],[1,0,0],[0,0,1]])
 assert G*rvec==s.zeros(3,1);checks+=1
 assert s.simplify(S.T*G.conjugate()*S-G)==s.zeros(3);checks+=1
 assert H.eigenvals()=={2-h:1,h+2:1};checks+=1
 assert s.simplify(H.det()-(4-h*h))==0;checks+=1
 rows=[]
 for prime in (2,3,5,11,101):
  rr=prime**-.5;L=math.log(prime);hinf=L*rr/(1-rr)
  margins=[]
  prev=0
  for K in (1,2,3,5,10):
   hk=L*sum(rr**k for k in range(1,K+1));assert prev<hk<hinf;checks+=1;prev=hk;margins.append({'K':K,'h_K':hk,'determinant_margin':4-hk*hk})
  assert 4-hinf*hinf>0;checks+=1
  rows.append({'p':prime,'h_infinity':hinf,'completed_determinant_margin':4-hinf*hinf,'grades':margins})
 out={'schema':'marici.rh.completed-three-port-green-family.v1','status':'finite_and_completed_green_family_positive','checks':checks,'grade_K_coordinate':'h_p,K=log(p) sum_{k=1}^K p^(-k/2)','completed_coordinate':'h_p,inf=log(p)p^-1/2/(1-p^-1/2)','quotient_matrix':'[[2,i h],[-i h,2]]','three_port_matrix':[[str(G[i,j]) for j in range(3)] for i in range(3)],'quotient_eigenvalues':['2-h','2+h'],'determinant_margin':'4-h^2','claim':'every finite-grade oriented form and its all-grade limit remain in the positive reciprocal cone, with the overlap direction radical','consequence':'the oriented auxiliary/Schur target is explicit at each grade and compatible with connected-tail completion','boundary':'this matrix cannot directly equal the general prime-dependent Stieltjes endpoint Gram; comparison must pass through the separately typed Pauli outputs or another source-derived embedding','samples':rows}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'smallest_sample_completed_margin':min(q['completed_determinant_margin'] for q in rows)}))
if __name__=='__main__':main()
